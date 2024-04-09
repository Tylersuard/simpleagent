# simpleagent
A simple framework for building agents and agent swarms.  Get started in 2 lines of code.

Example:
```
import simpleagent
from utils import SendToOpenai

oai = SendToOpenai(endpoint=None, api_key="YOUR_OPENAI_API_KEY")

agent = simpleagent.Agent(instructions = "Write a poem about what a butterfly feels emerging from its coccoon.", client=oai)

agent_swarm = simpleagent.Swarm(instructions = "Write lyrics for a song called 'Dandelion Haze'.", 
                                client=groq, 
                                number_of_agents = 10)
```
