from langchain_core.tools import tool

@tool
def get_repo_details(repo_path: str) -> str:
    """Returns a list of all files in the repository."""
    import os
    files = []
    for root, dirs, filenames in os.walk(repo_path):
        for f in filenames:
            files.append(os.path.relpath(os.path.join(root, f), repo_path))
    return f"Repo contains {len(files)} files:\n" + "\n".join(files)

@tool
def get_file_content(file_path: str) -> str:
    """Reads and returns the content of a file given its path."""
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@tool
def review_code_snippet(code: str) -> str:
    """Provides a basic review of the given code snippet."""
    return f"Review of code:\n{code[:300]}...\n(This is a simulated review by CrewAI.)"
