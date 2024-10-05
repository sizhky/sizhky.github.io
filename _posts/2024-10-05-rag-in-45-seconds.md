---
layout: post
title:  "RAG in 45 seconds"
date:   2024-10-05 14:35 +0530
categories: posts
---

If you want to know about what is RAG and how it's used, read the following pseudo(ish) code

<!--more-->

```python
from rag import RAG, Document
from typing import Literal
from pydantic import BaseModel

# Where do you want to store your vectors?
hub = 'hub://international-school-of-engineering/biotechnology/'
# How do you want to create the vectors?
vector_model = 'https://my-vector-embedder/'
rag = RAG(hub_url=hub, model=vector_model)

# Whare are your documents?
source = 'quizzes/batch-2024/2024-10-05/'
exam_papers = Document.fetch_all_documents_from_source(f'filestore://{source}')

rag_store = f'{hub}/{source}/'
# Inject the documents in the location given by rag_store
# i.e., hub://international-school-of-engineering/biotechnology/quizzes/batch-2024/2024-10-05/
rag.inject_documents(exam_papers, store=rag_store, chunk_size=1000)

# Specify the desired response format
class Response(BaseModel):
    name: str
    response_source: str
    response_summary: str
    response_type: Literal['correct','incorrect','missing']


llm = 'https://my-llm/'
query = 'Give me the list of all students who could not identify what is the powerhouse of the cell and summarize what was answered for the question'

# Fetch your universe of documents, the LLM needs to know context for
vectors = rag.fetch_vectors(store=rag_store)
# Correlate the query with all the exam papers and fetch the responses from an LLM in the desired format
responses = rag.query(query, llm=llm, vectors=vectors, response_class=Response)

for response in responses:
    print(response)

"""
Response(
    name="Matt",
    response_source="quizzes/batch-2024/2024-10-05/Matt.pdf:::page-2::lines-3:5",
    response_summary="Nucleus is the power house of the cell where the necessary proteins are made that help in the functioning of the cell"
    response_type="incorrect"
)

Response(
    name="John",
    response_source="quizzes/batch-2024/2024-10-05/John.txt:::page-3::lines-11:12",
    response_summary="Cell is too small to hold a powerhouse"
    response_type="incorrect"
)

Response(
    name="Sarah",
    response_source="quizzes/batch-2024/2024-10-05/Sarah.docx",
    response_summary="Skipped the question altogether"
    response_type="missing"
)

Response(
    name="Alice",
    response_source="quizzes/batch-2024/2024-10-05/Alice.txt:::page-12::lines-12:15,17:18:::page-13::lines-1:2",
    response_summary="DNA is the powerhouse of the cell with the help of RNA"
    response_type="incorrect"
)
"""

# Alternatively, you can suggest the vector store directly
# to get results from evey document that you have in hand.
responses = rag.query(
    query, llm=llm, 
    rag_store='hub://international-school-of-engineering/biotechnology/', 
    response_class=Response
)
```

Post was inspired from the first chapter of *[RAG-Driven Generative AI](https://www.packtpub.com/en-at/product/rag-driven-generative-ai-9781836200918)*