class AIAgent:
    def __init__(self):
        self.memory = []

    def think(self, task):
        return f"Planning task: {task}"

    def act(self, task):
        result = f"Completed: {task}"
        self.memory.append(result)
        return result

if __name__ == "__main__":
    agent = AIAgent()
    task = "Research AI trends"
    print(agent.think(task))
    print(agent.act(task))
