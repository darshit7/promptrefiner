from unittest.mock import patch
from promptrefiner.strategies import (
    Persona,
    FewShot,
    ChainofThought,
    SelfConsistency,
    RecursiceCritiqueRefinement,
)


@patch("promptrefiner.base.get_llm_client")
def test_persona(mock_get_llm_client):
    st = Persona(api_key="custom_key", model="custom_model", temperature=0.9)
    prompt = st.get_system_prompt()
    assert isinstance(prompt, str)
    assert prompt


@patch("promptrefiner.base.get_llm_client")
def test_fewshot(mock_get_llm_client):
    st = FewShot(api_key="custom_key", model="custom_model", temperature=0.9)
    prompt = st.get_system_prompt()
    assert isinstance(prompt, str)
    assert prompt


@patch("promptrefiner.base.get_llm_client")
def test_cot(mock_get_llm_client):
    st = ChainofThought(api_key="custom_key", model="custom_model", temperature=0.9)
    prompt = st.get_system_prompt()
    assert isinstance(prompt, str)
    assert prompt


@patch("promptrefiner.base.get_llm_client")
def test_sc(mock_get_llm_client):
    st = SelfConsistency(api_key="custom_key", model="custom_model", temperature=0.9)
    prompt = st.get_system_prompt()
    assert isinstance(prompt, str)
    assert prompt


@patch("promptrefiner.base.get_llm_client")
def test_rcr(mock_get_llm_client):
    st = RecursiceCritiqueRefinement(
        api_key="custom_key", model="custom_model", temperature=0.9
    )
    prompt = st.get_system_prompt()
    assert isinstance(prompt, str)
    assert prompt
