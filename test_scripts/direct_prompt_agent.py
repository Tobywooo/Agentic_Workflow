# Test script for DirectPromptAgent class
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from workflow_agents.base_agents import DirectPromptAgent # TODO: 1 - Import the DirectPromptAgent class from BaseAgents
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
print(f"{openai_api_key[:3]}...{openai_api_key[-3:]}" if openai_api_key else "Not found")

prompt = "What is the Capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key)
# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(f"Prompt Used: {prompt}")
print(f"Reponse: {direct_agent_response}")

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("Response generated using the model's pre-trained knowledge (no external data source).")
