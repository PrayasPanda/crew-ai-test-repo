from crewai import Agent, Task, Crew
from tools.crew_tools import get_repo_details, get_file_content, review_code_snippet

# Define Agent
review_agent = Agent(
    role="Senior GitHub Analyst",
    goal="Analyze and review GitHub repositories",
    backstory="An expert in Python and open-source repo analysis.",
    tools=[get_repo_details, get_file_content, review_code_snippet],
    verbose=True
)

# Define Task
task = Task(
    description="Analyze the repo structure and review main.py.",
    expected_output="Repo overview and code review of main.py",
    agent=review_agent
)

# Create Crew
crew = Crew(
    agents=[review_agent],
    tasks=[task],
    verbose=True
)
