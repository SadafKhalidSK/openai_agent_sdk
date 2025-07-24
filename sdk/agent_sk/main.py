from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ✅ Correct argument: openai_client, not client
model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash"
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="Frontend",
    instructions="You are a frontend developer,"
)

result = Runner.run_sync(
    agent,
    input="Hello",
    run_config=config  # ✅ fixed typo
)

print(result.final_output)

