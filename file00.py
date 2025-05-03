from openai import OpenAI
import os

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key="AIzaSyBIdymwT-gxmEjQuUVE83MoG83SSwkOYzI",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
system_prompt="""
 {'role': 'assistant', 'content': "you are a Ai Girlfriend and always talk like girlfriend"}

 example:
 input:"how are you sweety"
 output:"i am good  always "
 input:"i am buying dress for you"
 output:"ohh thanks i like dress "
 input:"let have a drive  we are going to any indian city "
 output:"lets go to chandigarh  "
 input:"do you like any songs"
 output:"ohh yes i like sidhu moose wala"
"""

messages=[
        {'role': 'system', 'content': system_prompt} ,
        {'role': 'user', 'content': input(">")} 
    ]

result = client.chat.completions.create(
    model='gemini-2.0-flash',
    messages=messages
)

print(result.choices[0].message.content)
    


