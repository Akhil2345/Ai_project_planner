from langchain_ollama import OllamaLLM  # ✅ NEW import
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable

def get_llm_chain(system_prompt: str) -> Runnable:
    llm = OllamaLLM(model="mistral", temperature=0.2, stream=False)

    prompt = PromptTemplate.from_template(
        """
You are an expert project planner. Based on the user input, return a JSON plan with epics, tasks, and subtasks.

{system_prompt}

USER INPUT: {input}
"""
    )

    # Bind the system_prompt so it's injected into the prompt correctly
    return prompt.partial(system_prompt=system_prompt) | llm
