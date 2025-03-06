"""
Provides interface for command line execution of `promptrefiner`.
"""

import sys
import openai
import textwrap
from io import StringIO
import rich_click as click
from rich.table import Table
from rich.console import Console
from promptrefiner.refiner import PromptRefiner
from promptrefiner.strategies import STRATEGY_MAP

console = Console()


def parse_strategy(ctx, param, value):
    """Splits the comma-separated strategies into a list."""
    if not value:
        return []
    strategies = []
    for item in value:
        strategies.extend(item.split(","))
    return strategies


class CustomHelp(click.RichCommand):
    def format_help(self, ctx, formatter):
        # Capture default help message
        help_buffer = StringIO()
        default_formatter = click.rich_help_formatter.RichHelpFormatter()
        super().format_help(ctx, default_formatter)
        help_buffer.write(default_formatter.getvalue())

        self.display_strategy_table()

    def display_strategy_table(self):
        """Displays a formatted table of available strategies."""
        table = Table(
            title="Available Strategies",
            show_header=True,
            header_style="bold cyan",
        )
        table.add_column("Strategy", style="bold yellow")
        table.add_column("Alias", style="cyan")
        table.add_column("Description", style="green")

        for full_name, data in STRATEGY_MAP.items():
            aliases = ", ".join(data["aliases"]) if data["aliases"] else "-"
            table.add_row(full_name, aliases, data["class_"].__doc__.strip())

        console.print(table)


@click.command(cls=CustomHelp)
@click.argument("prompt", type=str)
@click.option(
    "--strategy",
    "-s",
    multiple=True,
    required=True,
    callback=parse_strategy,
    help="Strategies to apply (can be used multiple times, e.g., -s verbose, os)",
)
def main(prompt: str, strategy: list):
    """ """
    selected_strategies = []
    for s in strategy:
        normalized_name = next(
            (
                name
                for name, data in STRATEGY_MAP.items()
                if s.lower() in [name] + data["aliases"]
            ),
            None,
        )
        if normalized_name not in STRATEGY_MAP:
            console.print(
                f"[red]❌ Error: Unknown strategy '{s}'[/red]", style="bold red"
            )
            sys.exit(1)
        selected_strategies.append(normalized_name)  # Convert short name if exists

    console.print("\n[bold cyan] Initializing PromptRefiner...[/bold cyan]")
    try:
        # Initialize selected strategies
        strategies = [STRATEGY_MAP[name]["class_"]() for name in selected_strategies]

        # Initialize PromptRefiner
        refiner = PromptRefiner(strategies)

        ppromt = (
            textwrap.shorten(prompt, width=250, placeholder="...")
            if len(prompt) > 250
            else prompt
        )
        console.print(f"[yellow]📝 Input Prompt:[/yellow] {ppromt}")

        console.print("\n[bold cyan]🔍 Refining Prompt...[/bold cyan]")
        console.print(
            f"[green]🚀 Strategies Applied:[/green] {', '.join(selected_strategies)}\n"
        )
        refined_prompt = refiner.refine(prompt)

        console.print("\n[bold blue]✨ Refined Prompt:[/bold blue]")
        console.print(f"[bold green]{refined_prompt}[/bold green]")
    except openai.OpenAIError as err:
        console.print(f"[red]❌ Error: {err} ")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
