# -AI---Driven-Portfolio-Matching-System-for-Recruitment
1) Utilized LangChain and ChatGroq to extract key details (Job Role, Experience, Skills) from job descriptions
2) Integrated Chroma vector database for efficient semantic search and portfolio matching based on required skills
3) Employed Streamlit to build an interactive web interface for job description input, portfolio matching, and email generation.
4) Automated email generation using ChatGroq to draft customized emails to recruitment teams with shortlisted candidates.


Features:-

1)Job Description Analysis: Utilizes LangChain and ChatGroq to extract important details such as job roles, required skills, and experience levels from job descriptions, enabling precise matching.

2)Semantic Search: Integrates Chroma vector database to perform semantic search, matching candidate portfolios based on the skills and experience required for a particular role.

3)Interactive Web Interface: Developed using Streamlit, the interface allows users to easily input job descriptions, view portfolio matches, and interact with the system in real time.

4)Automated Email Generation: Automatically generates customized emails using ChatGroq, allowing recruitment teams to easily communicate with shortlisted candidates or stakeholders.

5)Real-Time Matching: Facilitates dynamic portfolio matching and provides real-time feedback to help recruiters find the best candidates quickly.

Technologies Used:-


1)LangChain: For extracting structured information from unstructured job descriptions.

2)ChatGroq: Used for natural language processing and email generation tasks.

3)Chroma: A vector database used for efficient semantic search and portfolio matching.

4)Streamlit: For building the interactive, user-friendly web interface.

5)Python: The main programming language used for system development.


How to Run:-

1)Install the required dependencies: pip install -r requirements.txt.

2)Launch the Streamlit app: streamlit run app.py.

3)Input job descriptions, view matched portfolios, and generate email drafts in real time.

Future Enhancements:-

1)Candidate Feedback Loop: Integrating candidate feedback to improve matching accuracy over time.

2)Multi-Language Support: Expanding the system to support job descriptions and candidate profiles in multiple languages.

3)Advanced Filtering: Adding more advanced filters such as experience level, location, or compensation preferences.

4)Batch Processing: Enabling batch uploads for job descriptions and portfolios to speed up the recruitment process.
