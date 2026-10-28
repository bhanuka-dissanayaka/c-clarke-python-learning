class Agent:
    num_of_agents: int = 0

    def __init__(self, agent_id: str):
        self.id: str= agent_id
        self.task: str = "Default task"
        Agent.num_of_agents += 1
    def add_sub_agent_id(self,sub_agent_id):
        self.sub_agent_id = sub_agent_id
        print("Added the sub agent id successfully.")

agent1 = Agent(agent_id="001")
print(f"No fo agents {agent1.num_of_agents}")

agent1.add_sub_agent_id(sub_agent_id="111")
print(f"Sub agent id: {agent1.sub_agent_id}")

print(agent1.__dict__)
if 'sub_agent_id' in agent1.__dict__:  # __dict__ Dunder method give us the attributes of a object as a dictionary
    print(agent1.sub_agent_id)

if hasattr(agent1,'sub_agent_id'):  # above same thing can be done using hasattr method. it is more clean
    print(agent1.sub_agent_id)

agent2 = Agent(agent_id="002")
print(f"No fo agents {agent2.num_of_agents}")
print(f"No fo agents {Agent.num_of_agents}") # Accessing the class variable without an object

