import os
from google import genai
from dotenv import load_dotenv
import json
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

userprompt = input("Enter your prompt:")
with open("prompt.txt", "r") as f:
    instructions = f.read()
with open("Leetcode_topics.txt","r") as f:
    topics_name = f.read().splitlines()
final_prompt = instructions +"\n".join(topics_name) + "\n" + userprompt 
responses = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=final_prompt
)
topics_listed=[]
with open("response.txt", "w") as f:
    f.write(responses.text)
with open("response.txt", "r") as f:
  r=json.loads(f.read())
for item in r['topics']:
    topics_listed.append(item)
# topic_mapping = {
#     "Arrays": "Array",
#     "Hash Tables": "Hash Table",
#     "Linked Lists": "Linked List"
# }
