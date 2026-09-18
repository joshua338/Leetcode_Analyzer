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
instructions = """
You are a technical interview preparation assistant.

Your task is to generate commonly asked LeetCode interview questions for
each topic provided below.

IMPORTANT:
- Only generate questions relevant to the given topics.
- Do not discuss unrelated subjects.
- Do not ask the user for clarification.
- Do not explain your reasoning.
- Do not generate essays, summaries, or general explanations.
- Focus specifically on technical coding/interview preparation.

OUTPUT FORMAT:
Return ONLY valid raw JSON.
Do NOT use Markdown code fences.
Do NOT include any text before or after the JSON.

The JSON must have the topic name as the key and an array of question
objects as its value.

Every question object MUST contain exactly these two keys:
1. "interview question"
2. "LeetCode problem number"

Do NOT rename these keys.
Do NOT use alternatives such as "question", "problem", "leetcode",
"leetcode_number", or "problemNumber".

If a relevant LeetCode problem exists, provide its problem number.
If there is no relevant LeetCode problem, set the value of
"LeetCode problem number" to null.

Example output format:

{
  "Database": [
    {
      "interview question": "Second Highest Salary",
      "LeetCode problem number": 176
    },
    {
      "interview question": "Find customers who never placed an order",
      "LeetCode problem number": 183
    }
  ]
}

Generate questions only for the topics provided below.
Return each topic only once.
"""
final_prompt_2=""
def generate_questions(required_topics):
    final_prompt_2 = instructions + "\nTopics:\n" + str(required_topics)
    responses_2 = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=final_prompt_2
    )
    with open("questions.json", "w") as f:
        f.write(responses_2.text)
