from crewai import Agent, Task, Crew
from tools.crew_tools import get_repo_details, get_file_content, review_code_snippet

# Define the agent
review_agent = Agent(
    role="Senior GitHub Analyst",
    goal="Analyze and review GitHub repositories",
    backstory="An expert in reviewing Python projects and static analysis.",
    tools=[get_repo_details, get_file_content, review_code_snippet],
    verbose=True
)

# Define the task
task = Task(
    description="Analyze the repo structure and review main.py.",
    expected_output="Repo overview and quality review of main.py",
    agent=review_agent
)

# Initialize the crew
crew = Crew(
    agents=[review_agent],
    tasks=[task],
    verbose=True
)
