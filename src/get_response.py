from phoenix.otel import register

tracer_provider = register(
    project_name="my-llm-app",
    auto_instrument=True,
)

tracer = tracer_provider.get_tracer(__name__)

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add OpenAI API Key
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.environ.get("API_KEY"),
)

chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(chat_completion.choices[0].message.content)