
# Multi-Agent AI Story Generator

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)

A web application that takes a story prompt from the user and generates a creative short story (100-200 words) using a **multi-agent AI system** powered by **CrewAI** and **OpenAI**.

---

## ✨ Features

- Simple and beautiful Streamlit frontend
- Multi-agent collaboration (Idea Brainstormer → Writer → Editor)
- FastAPI backend with proper error handling
- Clean separation of concerns (agents, tasks, crew)
- Ready for local development and easy deployment

---

## 🛠 Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Backend    | FastAPI + Uvicorn           |
| AI Agents  | CrewAI + LangChain + OpenAI |
| Frontend   | Streamlit                   |
| Environment| python-dotenv               |

---

## 📁 Project Structure

```
ASSIGNMENT/
├── backend/
│   ├── main.py          # FastAPI app
│   ├── crew.py          # CrewAI orchestration
│   ├── agents.py        # AI agent definitions
│   ├── tasks.py         # Agent tasks
│   ├── schemas.py       # Pydantic models
│   ├── config.py        # Configuration
│   └── __init__.py
├── frontend/
│   └── app.py           # Streamlit UI
├── requirements.txt
├── .env                 # Add your OPENAI_API_KEY here
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Jarvis-331/ASSIGNMENT.git
cd ASSIGNMENT
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root:
```env
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### 5. Run the Application

**Terminal 1** – Start Backend:
```bash
cd backend
uvicorn main:app --reload --port 8000
```

**Terminal 2** – Start Frontend:
```bash
cd frontend
streamlit run app.py
```

Open your browser → `http://localhost:8501`

---

## 📝 How to Use

1. Enter a story prompt (e.g., "A dragon in a modern city...")
2. Click **Generate Story**
3. Watch the agents work (spinner shown)
4. Enjoy your AI-generated short story!

---

## 🎯 Assignment Requirements Fulfilled

- ✅ User inputs story prompt
- ✅ Multi-agent system (3 agents collaborating)
- ✅ FastAPI backend with `/generate` endpoint
- ✅ Streamlit frontend with loading indicator
- ✅ Clean, modular, and well-structured code
- ✅ Error handling for empty prompts

---

## 🔧 Future Improvements

- Add story length selector
- Add genre/style options
- Save generated stories
- Deploy on Streamlit Cloud + Render / Railway
- Add authentication
- Switch to Groq / Anthropic for faster & cheaper generation

---

## 📄 License

This project was created as part of an academic assignment. Feel free to use and modify for learning purposes.

---

**Made with ❤️ using CrewAI + FastAPI + Streamlit**



It looks professional, explains everything clearly, and matches exactly what your code does.

Let me know if you want any changes (e.g., add screenshots, change title, or make it more assignment-focused)!
