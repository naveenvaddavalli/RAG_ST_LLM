
from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader("static").load_data()

from llama_index.core.node_parser.text import SentenceSplitter
text_parser = SentenceSplitter(
 chunk_size=1024,
)

text_chunks = []
doc_idxs = []
for doc_idx, doc in enumerate(documents):
    cur_text_chunks = text_parser.split_text(doc.text)
    text_chunks.extend(cur_text_chunks)
    doc_idxs.extend([doc_idx] * len(cur_text_chunks))
    
    
from llama_index.core.schema import TextNode
nodes = []
for idx, text_chunk in enumerate(text_chunks):
    node = TextNode(
    text=text_chunk,
    )
    src_doc = documents[doc_idxs[idx]]
    node.metadata = src_doc.metadata
    nodes.append(node)
    
from llama_index.core.embeddings import HuggingFaceEmbedding
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")
for node in nodes:
    node_embedding = embed_model.get_text_embedding(
    node.get_content(metadata_mode="all")
    )
    node.embedding = node_embedding
    
from llama_index.llms import LlamaCPP
model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_0.gguf"
llm = LlamaCPP(
 model_url=model_url,
 model_path=None,
 temperature=0.1,
 max_new_tokens=256,
 context_window=3900,
 generate_kwargs={},
 model_kwargs={"n_gpu_layers": 1},
 verbose=True,
)


from llama_index import ServiceContext
service_context = ServiceContext.from_defaults(
 llm=llm, embed_model=embed_model
)

import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore
client = qdrant_client.QdrantClient(location=":memory:")
from llama_index.storage.storage_context import StorageContext
from llama_index import (
 VectorStoreIndex,
 ServiceContext,
 SimpleDirectoryReader,
)
vector_store = QdrantVectorStore(client=client, collection_name="my_collection")
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
 documents, storage_context=storage_context, service_context=service_context
)


vector_store.add(nodes)

query_str = "Can you tell me about the key concepts for safety finetuning"
query_embedding = embed_model.get_query_embedding(query_str)


from llama_index.vector_stores import VectorStoreQuery
query_mode = "default"
# query_mode = "sparse"
# query_mode = "hybrid"
vector_store_query = VectorStoreQuery(
 query_embedding=query_embedding, similarity_top_k=2, mode=query_mode
)
query_result = vector_store.query(vector_store_query)
print(query_result.nodes[0].get_content())