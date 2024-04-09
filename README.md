# SimpleAgent

## Overview

SimpleAgent is an intuitive and lightweight framework designed to simplify the development and management of agents and agent swarms. With just a couple of lines of code, you can bootstrap a powerful agent or an entire swarm of agents for various automated tasks. Whether you're crafting poetry or generating song lyrics, SimpleAgent offers a flexible solution to integrate artificial intelligence into your projects.

## Getting Started

To get started with SimpleAgent, you only need to import the package and set it up with your OpenAI API key. Below is a quick example on how to create a single agent that writes a poem about the experience of a butterfly emerging from its cocoon.

```python
import simpleagent
from utils import SendToOpenai

# Initialize the OpenAI client with your API key
oai = SendToOpenai(endpoint=None, api_key="YOUR_OPENAI_API_KEY")

# Create an agent with a specific task
agent = simpleagent.Agent(instructions="Write a poem about what a butterfly feels emerging from its cocoon.", client=oai)
```

## Working with Agent Swarms

SimpleAgent also allows you to manage multiple agents simultaneously through the Swarm feature. This is particularly useful for tasks that require parallel processing or diversity in output. Here's how you can create a swarm of agents tasked with writing lyrics for a song named 'Dandelion Haze'.

```python
from utils import SendToGroq
agent_swarm = simpleagent.Swarm(instructions="Write lyrics for a song called 'Dandelion Haze'.", 
                                client=groq, 
                                number_of_agents=10)
```

# Features
- Easy to Use: SimpleAgent's API is designed for simplicity, making it accessible for developers of all skill levels.
- Flexible: Tailor your agents or swarms to perform a wide range of tasks, from creative writing to data analysis.
- Scalable: Easily scale up your agent-based solutions by managing multiple agents as a cohesive swarm.

# Requirements
Python 3.6+
OpenAI (or Groq) API key for utilizing GPT-powered agents

# Contributions
Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to submit a pull request or open an issue.
