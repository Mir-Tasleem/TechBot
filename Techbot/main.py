import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
import streamlit as st


st.title("TechBot Transformers")
with st.sidebar:
    aikey=st.text_input("Enter key",placeholder="openai_api_key",type="password")

def qa_model(query,key):
    # Load, chunk and index the contents of the blog.
    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/","https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/","https://lilianweng.github.io/posts/2023-01-10-inference-optimization/",),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    OPENAI_API_KEY=key
    embeddings=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    # Retrieve and generate using the relevant snippets of the blog.
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125",openai_api_key=OPENAI_API_KEY)
    retriever = vectorstore.as_retriever()
    prompt = hub.pull("rlm/rag-prompt")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    answer=rag_chain.invoke(query)
    return answer


with st.form("ASK"):
    query=st.text_input("Enter Your Query?",placeholder="What are transformers")
    x=st.form_submit_button("submit")
if x:
    if aikey==False:
        with st.warning():
            st.write("Please Enter AI Key to Proceed!")
    else:
        result=qa_model(query,aikey)
        st.write(result)


