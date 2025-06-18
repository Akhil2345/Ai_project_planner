from utils.llm import get_llm_chain

def decompose_project(project_description: str) -> dict:
    system_prompt = """
You are a project decomposition expert. Your job is to take a high-level project idea and break it into:

- 3 to 5 Epics (broad themes or modules)
- Under each Epic, list 2–4 detailed Tasks
- For each Task, break into 2–3 Subtasks

Return everything in structured JSON format like this:

{
  "epics": [
    {
      "name": "Epic 1 name",
      "tasks": [
        {
          "name": "Task 1 name",
          "subtasks": ["Subtask A", "Subtask B"]
        },
        ...
      ]
    },
    ...
  ]
}
Be concise and actionable in naming each item.
"""

    chain = get_llm_chain(system_prompt)
    response = chain.invoke({"input": project_description}).strip()

    
    # Try parsing response as JSON
    try:
        import json
        return json.loads(response)
    except Exception:
        return {"error": "Failed to parse JSON", "raw": response}
