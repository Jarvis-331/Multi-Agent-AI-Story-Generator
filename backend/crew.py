from crewai import Crew
from .tasks import create_tasks

def run_story_crew(prompt: str) -> str:
    tasks = create_tasks(prompt)

    crew = Crew(
        tasks=tasks,
        process="sequential",
        verbose=True
    )

    result = crew.kickoff()
    return result
