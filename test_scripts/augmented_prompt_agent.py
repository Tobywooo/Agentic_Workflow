# TODO: 1 - Import the AugmentedPromptAgent class
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from workflow_agents.base_agents import AugmentedPromptAgent
# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
print(f"{openai_api_key[:3]}...{openai_api_key[-3:]}" if openai_api_key else "Not found")
prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_prompt_agent = AugmentedPromptAgent(openai_api_key, persona)
# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = augmented_prompt_agent.respond(prompt)
# Print the agent's response
print(f"Prompt Used: {prompt}")
print(f"Persona: {persona}")
print(f"Reponse: {augmented_agent_response}")

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.
# The agent is using no additional knowledge outside of it's own training to answer the question. 
# The system prompt is instructing the agent to act as a college professor and to respond starting with "deat students", however, 
# since we are using GPT-3.5 Turbo and the temperature is set to 0, it chooses the most probable token which is just a direct answer
# The role instructions had to be set more strictly for it to use the persona. 