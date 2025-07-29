# from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
# from dotenv import load_dotenv
# import os
# import chainlit as cl

# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# # ✅ Correct argument: openai_client, not client
# model = OpenAIChatCompletionsModel(
#     openai_client=external_client,
#     model="gemini-2.0-flash"
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# agent = Agent(
#     name="Frontend",
#     instructions="You are a frontend developer,"
# )


# @cl.on_message
# async def handle_message(message:cl.Message):
#     result=await Runner.run(
#         agent,
#         input=message.content,
#         run_config=config
#     )
#     await cl.Message(content=result.final_output).send()
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
from dotenv import load_dotenv
import os
import chainlit as cl

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

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
    instructions="You are a frontend developer."
)
@cl.on_chat_start
async def handle_start():
    cl.user_session.set("history",[])
    await cl.Message(content="👏Helllo from SK ,do u need any help?").send()
@cl.on_message
async def handle_message(message: cl.Message):

    history=cl.user_session.get("history")
    history.append({"role":"user","content":message.content})


    result = await Runner.run(
        agent,
        input=history,
        run_config=config
    )
    history.append({"role":"assistant","content":result.final_output})
    cl.user_session.set("history",history)
    await cl.Message(content=result.final_output).send()
