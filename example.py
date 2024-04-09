import simpleagent
from utils import SendToGroq, SendToOpenai
from groq import Groq

groq = SendToGroq(endpoint=None, api_key="YOUR_GROQ_API_KEY")

agent = simpleagent.Agent(instructions = "Write a poem about what a butterfly feels emerging from its coccoon.", client=groq)

agent_swarm = simpleagent.Swarm(instructions = "Write lyrics for a song called 'Dandelion Haze'.", 
                                client=groq, 
                                number_of_agents = 10)
