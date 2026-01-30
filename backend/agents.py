from crewai import Agent
from langchain_openai import ChatOpenAI
from .config import OPENAI_API_KEY

llm = ChatOpenAI(
    temperature=0.8,
    model="gpt-4",
    openai_api_key=OPENAI_API_KEY
)

plot_agent = Agent(
    role="Plot Planner",
    goal="Create a compelling outline for a short story",
    backstory="Expert storyteller who designs engaging plots.",
    llm=llm,
    verbose=True
)

writer_agent = Agent(
    role="Story Writer",
    goal="Write a vivid short story based on an outline",
    backstory="Creative writer with strong narrative skills.",
    llm=llm,
    verbose=True
)

editor_agent = Agent(
    role="Story Editor",
    goal="Refine and polish the story for clarity and creativity",
    backstory="Professional editor who improves storytelling flow.",
    llm=llm,
    verbose=True
)
