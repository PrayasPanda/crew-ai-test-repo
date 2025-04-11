from crewai import Tool

def get_repo_details(repo_url: str):
    """Fetches basic info about a GitHub repo."""
    return f"Simulating fetching details from {repo_url}"

def get_file_content(file_path: str):
    """Gets file contents from a path."""
    return f"Simulated contents of {file_path}"

def review_code_snippet(code: str):
    """Analyzes the quality of a code snippet."""
    return f"Simulated review: Code looks clean!"

get_repo_details_tool = Tool(
    name="Get Repo Details",
    description="Fetch basic repo details",
    func=get_repo_details
)

get_file_content_tool = Tool(
    name="Get File Content",
    description="Fetch file content from repo",
    func=get_file_content
)

review_code_snippet_tool = Tool(
    name="Review Code Snippet",
    description="Review code for quality and structure",
    func=review_code_snippet
)
