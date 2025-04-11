from agents.crew_agents import crew

if __name__ == "__main__":
    with open("main.py", "r") as f:
        main_code = f.read()

    result = crew.kickoff(inputs={
        "repo_path": ".", 
        "file_path": "main.py", 
        "code": main_code
    })

    print(result)
