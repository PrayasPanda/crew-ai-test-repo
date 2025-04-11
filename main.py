from agents.crew_agents import crew

def run():
    task = "Analyze https://github.com/PrayasPanda/crew-ai-test-repo and review code"
    result = crew[0].execute(task)
    print(result)

if __name__ == "__main__":
    run()
