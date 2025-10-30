from openai import OpenAI
import os
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    OpenAI_api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)