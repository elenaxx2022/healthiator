
# Here we demonstrate how an agent can respond to plain text questions with data from an AI model and convert it into a machine readable format.
# Note: the AI model used here is not actually able to verify its information and is not guaranteed to be correct. The purpose of this example is to show how to interact with such a model.
#
# In this example we will use:
# - 'agent': this is your instance of the 'Agent' class that we will give an 'on_interval' task
# - 'ctx': this is the agent's 'Context', which gives you access to all the agent's important functions
# - 'requests': this is a module that allows you to make HTTP requests
#
# To use this example, you will need to provide an API key for OPEN AI: https://platform.openai.com/account/api-keys
# You can define your OPENAI_API_KEY value in the .env file
#if OPENAI_API_KEY == "YOUR_OPENAI_API_KEY":
#    raise Exception("You need to provide an API key for OPEN AI to use this example")

# Configuration for making requests to OPEN AI 

from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType

OPENAI_URL = "https://api.together.xyz/v1/chat/completions"
MODEL_ENGINE = "meta-llama/Llama-2-70b-chat-hf"
HEADERS = {
    "Authorization": f"Bearer 4fbc78f4cae052bc8b2b358646e3ffad231f7241da976fa649b06168141e15b3"
}


class Request(Model):
    text: str


class Error(Model):
    text: str


class Data(Model):
    name: str
    explanation: str
    CDM: str
    HCPCS: str

class ListModel(Model):
    procs_list: List[Data]

class Response(Model):
    text: str

medical_condition_protocol = Protocol("Medical_Condition")

# Send a prompt and context to the AI model and return the content of the completion
def get_completion(context: str, prompt: str):
    data = 'data'

    try:
        response = requests.post('https://api.together.xyz/v1/chat/completions', json={
    "model": "meta-llama/Llama-2-70b-chat-hf",
    "messages": [
        {
            "role": "system",
            "content": context
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.1,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1,
    "stop": [
        "[/INST]",
        "</s>"
    ],
    "repetitive_penalty": 1
}, headers={
    "Authorization": "Bearer 4fbc78f4cae052bc8b2b358646e3ffad231f7241da976fa649b06168141e15b3",
})

        messages = response.json()['choices']

        message = messages[0]['message']['content']

    except Exception as ex:
        return None

    #print("Got response from AI model: " + message)
    return message


# Instruct the AI model to retrieve data and context for the data and return it in machine readable JSON format
def get_data(ctx: Context, request: str):
    context = """A patient is describing their symptoms. Based on that, give the best prediction of the medical condition in up to 3 words. Don't say anything more than that. Only give your best guess and no other explanation. Keep it at 3 words or less."""

    response = get_completion(context, request)

    try:
        print(response)
        return Response(text=response)
    except Exception as ex:
        ctx.logger.exception(f"An error occurred retrieving data from the AI model: {ex}")
        return Error(text="Sorry, I wasn't able to answer your request this time. Feel free to try again.")

# Message handler for data requests sent to this agent
#@agent.on_message(model=Request)
#async def handle_request(ctx: Context, sender: str, request: Request):
#    ctx.logger.info(f"Got request from {sender}: {request.text}")
#    response = get_data(ctx, request.text)
#    print("After data, about to send")
#    await ctx.send(sender, response)
#    print("After sent")
    

@medical_condition_protocol.on_message(model=Request, replies={UAgentResponse})
async def send_llm_request(ctx: Context, sender: str, msg: Request):
    condition = await get_data(ctx, msg.text)
    print("Condition is found:")
    print(condition)
    await ctx.send(
        sender, UAgentResponse(message=condition.text, type=UAgentResponseType.FINAL)
    )
agent.include(medical_condition_protocol, publish_manifest=True)