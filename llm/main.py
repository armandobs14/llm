from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama import OllamaEmbeddings, OllamaLLM as Ollama

output_parser = StrOutputParser()
embeddings = OllamaEmbeddings(base_url="http://localhost:11434", model="llama3.2:3b")

llm = Ollama(base_url="http://localhost:11434", model="llama3.2:3b")

# Creating a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}"),
    ]
)

# creating chain
chain = prompt | llm | output_parser

# chain invocation
llm_answer = chain.invoke({"input": "how can langsmith help with testing?"})

print(llm_answer)
