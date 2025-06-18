from agents.task_decomposer import decompose_project
import json

def main():
    print("\n🚀 Welcome to AI Project Planner!")
    project_idea = input("📌 What project do you want to plan? \n> ")

    print("\n🧠 Decomposing your project into epics, tasks and subtasks...\n")
    plan = decompose_project(project_idea)

    if "error" in plan:
        print("❌ Error:", plan["error"])
        print("📄 Raw Response:", plan["raw"])
    else:
        for epic in plan["epics"]:
            print(f"\n📁 Epic: {epic['name']}")
            for task in epic["tasks"]:
                print(f"  📝 Task: {task['name']}")
                for sub in task["subtasks"]:
                    print(f"     - {sub}")
        
        # Save the JSON result
        with open("outputs/project_plan.json", "w") as f:
            json.dump(plan, f, indent=2)
            print("\n✅ Saved project_plan.json to /outputs")

if __name__ == "__main__":
    main()
