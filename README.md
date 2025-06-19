# 🧠 AI Project Manager – Your Local Jira Replacement

**Offline. Private. Agent-powered.**  
A fully local, LangChain + Mistral-based **Multi-Agent AI system** that automates project planning — from idea to execution.  

> 🔧 Built for devs & PMs who are tired of Jira, and want to run their own AI project manager on their machine.  

---

## ✨ What It Does

✅ Breaks down project ideas into structured task trees  
✅ Automatically adds priorities & time estimates  
✅ Plans projects like a product manager would  
✅ Exports clean project plans (PDF, Notion, Telegram)  
✅ Runs 100% offline using [Ollama](https://ollama.com/) + [Mistral](https://mistral.ai/)

---

## 🔁 Example Workflow

1. 🧠 You enter a project idea  
2. 🤖 Agent 1 breaks it into tasks  
3. 🔢 Agent 2 assigns priority & hours  
4. 📄 Agent 3 generates a report  
5. 💌 Agent 4 syncs it to Notion / Telegram

---

## 🧱 Tech Stack

- 🛠 [LangChain](https://www.langchain.com/)  
- 🧠 Mistral LLM via [Ollama](https://ollama.com/)  
- 🐍 Python  
- 🎨 Streamlit / Gradio (optional frontend)

---

## ⚙️ Setup

```bash
# 1. Clone this repo
git clone https://github.com/Akhil2345/Ai_project_planner.git
cd Ai_project_planner

# 2. Create & activate environment
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Make sure Mistral is running
ollama run mistral

# 5. Run the planner
python main.py
