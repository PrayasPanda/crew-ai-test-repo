from crewai import Agent
from tools.crew_tools import (
    get_repo_details_tool,
    get_file_content_tool,
    review_code_snippet_tool
)

review_agent = Agent(
    role="Code Reviewer",
    goal="Review and analyze GitHub repos",
    backstory="You are a senior AI developer who reviews open-source projects.",
    tools=[
        get_repo_details_tool,
        get_file_content_tool,
        review_code_snippet_tool
    ],
    verbose=True
)

crew = [review_agent]
