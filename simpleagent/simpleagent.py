from random import randint
from typing import Optional

from agent_names import agent_firstnames, agent_lastnames
from constants import PROMPT_GENERATION_PREFIX
from utils import SendToLLM


class Agent:
    def __init__(self, instructions, client: SendToLLM, number_of_turns=5):
        self.instructions = instructions
        self.client = client
        self.prompt = self.generate_prompt_from_instructions(instructions)
        self.agent_name = self.generate_random_agent_name()
        if number_of_turns > 0:
            self.start_project(number_of_turns)

    def generate_random_agent_name(self):
        firstname = agent_firstnames[randint(0, len(agent_firstnames) - 1)]
        lastname = agent_lastnames[randint(0, len(agent_lastnames) - 1)]
        return f"{firstname} {lastname}"

    def generate_prompt_from_instructions(self, instructions):
        prompt = self.client.send(message=instructions, system=PROMPT_GENERATION_PREFIX)
        return prompt

    def generate_system_instructions(self, is_initial_prompt: bool) -> str:
        """Generate instructions for the AI assistant.

        Args:
            is_initial_prompt (bool): True if it's the initial prompt, False otherwise.

        Returns:
            str: The system instructions for the AI assistant.
        """
        if is_initial_prompt:
            return "You are a helpful assistant."
        return (
            "BEGINNING OF NEW PROMPT, DO NOT CONTINUE ANSWERING THE LAST PROMPT:"
            " This is a conversation between multiple AI assistants "
            f"discussing the original prompt: {self.prompt}."
            " The assistant should politely correct each other if one provides incorrect information."
            " Finally, the assistant should then give the final corrected response to the original prompt,"
            " and clearly indicate it using 'FINAL RESPONSE:'."
        )

    def start_project(self, number_of_turns: int = 5, history: Optional[str] = None):
        """Start the project and generate responses.

        Args:
            number_of_turns (int): The number of turns to generate responses for.
            history (Optional[str]): The initial conversation history.

        Returns:
            str: The final conversation history, including the generated responses.
        """
        self.history = history
        print("Project started for agent: ", self.agent_name)
        print("Instructions: ", self.instructions)

        message_to_llm = self.history if bool(self.history) else self.prompt
        agent_responses = []
        is_initial_prompt = not bool(self.history)

        for _ in range(number_of_turns):
            response = self.client.send(
                message=message_to_llm,
                system=self.generate_system_instructions(
                    is_initial_prompt=is_initial_prompt
                ),
            )
            is_initial_prompt = False
            print(
                "\n\n---------------------------------------------- \n\n"
                f"Response from agent {self.agent_name}: \n\n{response}\n\n"
            )
            if message_to_llm == self.prompt:
                message_to_llm = ""
            message_to_llm += f"\nResponse from agent {self.agent_name}: \n{response}"
            agent_responses.append(response)

        return agent_responses[-1]


class Swarm:
    def __init__(self, instructions, client, number_of_agents, number_of_turns=5):
        self.agents_list = []
        for _ in range(number_of_agents):
            self.agents_list.append(Agent(instructions, client, 0))
        self.start_project(number_of_turns)

    # Each agent has its own name and ai-generated instructions, told to work with n-1 number of other agents.
    def start_project(self, number_of_turns=5):
        chat_history = []
        for _ in range(number_of_turns):
            for agent in self.agents_list:
                agent_response = agent.start_project(
                    number_of_turns=1, history="\n".join(chat_history)
                )
                chat_history.append(
                    f"\nResponse from agent {agent.agent_name}: \n {agent_response}"
                )
                # print(f"Response from {agent.agent_name}: \n {agent_response}")


# Something is wrong, it will have each agent talk 5 times before moving on to the next agent.
