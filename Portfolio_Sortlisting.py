import streamlit as st
from langchain_groq import ChatGroq
import chromadb
import json


llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key='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'
)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

    

collection.add(
    documents=[
        "My Name is Amisha having experience of 2 years in python ML,DL,LLM, Generative AI",
        "My Name is Eva,Experties in Python,numpy,pandas, ML, DL",
        "My Name is Priyanka , I have 10 years of experience in java ,python",
        "My Name is Kranti,I have 1 years of experience in Java,SQL,Javascript"
    ],
    ids=["id1", "id2", "id3", "id4"]
)

st.set_page_config(page_title='Portfolio Sorting', layout='wide')
st.title('Portfolio Sorting')

job_post = st.text_area("Enter Job Description", height=200)


if job_post:

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You have to extract following details from provided job post. Extract JOB_ROLE, EXPERIENCE, SKILLS in JSON format. Don't provide preamble information"
            ),
            ("human", "{input}"),
        ]
    )

  
    chain = prompt | llm
    result = chain.invoke(
        {"input": job_post},
    )

    details = json.loads(result.content.strip("`\n"))

    
    st.subheader("Extracted Job Details:")
    st.write(details)

    skills = ' '.join(details['SKILLS'])
    st.subheader("Required Skills:")
    st.write(skills)

    
    results = collection.query(
        query_texts=[skills],  # Chroma will embed this for you
        n_results=2  # Number of matching results
    )

    
    st.subheader("Matching Portfolios:")
    for idx, doc in enumerate(results['documents']):
        st.markdown(f"**Portfolio {idx + 1}:**")
        st.write(doc)

    
    portfolios = " ".join(results['documents'])
    email_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                '''We are working as a placement officer in placement consultancy Codespyder.
                   We have shortlisted candidates portfolio as per the requirement of TCS job post.
                   Create an email to the recruitment team of TCS mentioning that we have best suitable candidates for your job.
                   Do not provide any preamble''',
            ),
            ("human", "{input}"),
        ]
    )

    email_chain = email_prompt | llm
    email_result = email_chain.invoke({"input": portfolios})

    # Display generated email
    st.subheader("Generated Email for TCS Recruitment Team:")
    st.markdown(email_result.content)

# Optionally, add a loading spinner when AI is processing
if not job_post:
    st.info("Submit.")