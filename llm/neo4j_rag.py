from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_community.llms import Ollama


from utils import get_graph

# Credentials
# NEO4J_URI = "bolt://localhost:7687"
NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "12345678"

## Running query

# print(graph.query("MATCH (t:Task {status:'Open'}) RETURN count(*)"))

# GraphCypherQAChain
# graph = get_graph(url, username, password)
# graph.refresh_schema()

# # Give the hability to read neo4j
# cypher_chain = GraphCypherQAChain.from_llm(
#     cypher_llm=Ollama(temperature=0),
#     qa_llm=Ollama(temperature=0),
#     graph=graph,
#     verbose=True,
# )

# cypher_answer = cypher_chain.invoke("How many OPEN tickets there are?") # 5 minutos
# print(cypher_answer["result"])

#-------------------------------------------------------------------------------------

from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_neo4j import Neo4jVector
from langchain_ollama.llms import OllamaLLM
from langchain_community.embeddings import OllamaEmbeddings

graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD)
chain = GraphCypherQAChain.from_llm(
    OllamaLLM(model="llama3.2:3b"),
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True
)

chain.run("How many OPEN tickets there are?")