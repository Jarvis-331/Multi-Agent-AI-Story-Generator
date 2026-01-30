from crewai import Task
from .agents import plot_agent, writer_agent, editor_agent

def create_tasks(prompt: str):

    plot_task = Task(
        description=f"Create a short outline for a story based on: {prompt}",
        agent=plot_agent,
        expected_output="A concise story outline with key plot points."
    )

    writing_task = Task(
        description="Write a 100-200 word story using the outline.",
        agent=writer_agent,
        expected_output="A complete short story draft."
    )

    editing_task = Task(
        description="Refine the story to improve coherence and creativity.",
        agent=editor_agent,
        expected_output="A polished final story."
    )

    return [plot_task, writing_task, editing_task]
