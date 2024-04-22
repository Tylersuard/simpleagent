import simpleagent
from simpleagent.utils import SendToGroq, MODELS

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

groq = SendToGroq(endpoint=None, api_key=GROQ_API_KEY, model=MODELS.MIXTRAL_8X_7B)

agent = simpleagent.Agent(instructions="Write a poem about what a butterfly feels emerging from its coccoon.",
                          client=groq)

agent_swarm = simpleagent.Swarm(instructions="Write lyrics for a song called 'Dandelion Haze'.",
                                client=groq,
                                number_of_agents=10)
