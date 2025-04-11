from crewai import Tool

def get_repo_details_fn(repo_path: str) -> str:
    """Returns a list of all files in the repo."""
    import os
    files = []
    for root, _, filenames in os.walk(repo_path):
        for f in filenames:
            files.append(os.path.relpath(os.path.join(root, f), repo_path))
    return f"Repo contains {len(files)} files:\n" + "\n".join(files)

def get_file_content_fn(file_path: str) -> str:
    """Reads and returns content of a given file."""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def review_code_snippet_fn(code: str) -> str:
    """Provides a basic review of the given code snippet."""
    return f"Review of code:\n{code[:300]}...\n(This is a simulated review.)"

# Wrap the functions with CrewAI Tool
get_repo_details = Tool(
    name="Get Repo Details",
    description="Get list of all files in a given repo path",
    func=get_repo_details_fn
)

get_file_content = Tool(
    name="Get File Content",
    description="Read and return the content of a file by path",
    func=get_file_content_fn
)

review_code_snippet = Tool(
    name="Review Code Snippet",
    description="Simulates code review based on passed Python code",
    func=review_code_snippet_fn
)
