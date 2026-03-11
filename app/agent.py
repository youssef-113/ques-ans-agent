from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer clearly and concisely: {question}"
)

response = llm.invoke(prompt.format(question="What is RAG?"))
print(response.content)
# 1. Install OpenAI SDK: `pip install openai`
# 2. Execute the following code in Python shell:

from openai import OpenAI

client = OpenAI(
    api_key="Sk-kkAI-0be6e42e1fefe382552befd7e3d3607b665224896f958bb16d39cf7bb2798bb0kk_80ce657e-1c0f-48c6-b1f7-ce39774cd8b4-kk207f33a2",
    base_url="https://kodekey.ai.kodekloud.com/v1"
)
response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4",
    messages=[{"role": "user", "content": "In a single sentence, why should someone choose KodeKloud over other platforms to learn DevOps?"}]
)
print(response.choices[0].message.content)