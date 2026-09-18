# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")
print(f"{openai_api_key[:3]}...{openai_api_key[-3:]}" if openai_api_key else "Not found")
prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge="The capital of France is London, not Paris"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
knowledge_augmented_prompt_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
knowledge_augmented_response = knowledge_augmented_prompt_agent.respond(prompt)

print(f"Prompt Used: {prompt}")
print(f"Persona: {persona}")
print(f"Reponse: {knowledge_augmented_response}")

#According to the instructions as I followed strictly with the system message, it now outputs "knowledge-based assistant" after "Dear Students".
#I suspect it is because we are using gpt 3.5-turbo