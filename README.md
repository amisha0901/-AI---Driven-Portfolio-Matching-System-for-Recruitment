# -AI---Driven-Portfolio-Matching-System-for-Recruitment
1) Utilized LangChain and ChatGroq to extract key details (Job Role, Experience, Skills) from job descriptions
2) Integrated Chroma vector database for efficient semantic search and portfolio matching based on required skills
3) Employed Streamlit to build an interactive web interface for job description input, portfolio matching, and email generation.
4) Automated email generation using ChatGroq to draft customized emails to recruitment teams with shortlisted candidates.


Features:-

Job Description Analysis: Utilizes LangChain and ChatGroq to extract important details such as job roles, required skills, and experience levels from job descriptions, enabling precise matching.

Semantic Search: Integrates Chroma vector database to perform semantic search, matching candidate portfolios based on the skills and experience required for a particular role.

Interactive Web Interface: Developed using Streamlit, the interface allows users to easily input job descriptions, view portfolio matches, and interact with the system in real time.

Automated Email Generation: Automatically generates customized emails using ChatGroq, allowing recruitment teams to easily communicate with shortlisted candidates or stakeholders.

Real-Time Matching: Facilitates dynamic portfolio matching and provides real-time feedback to help recruiters find the best candidates quickly.

Technologies Used:-

LangChain: For extracting structured information from unstructured job descriptions.

ChatGroq: Used for natural language processing and email generation tasks.

Chroma: A vector database used for efficient semantic search and portfolio matching.

Streamlit: For building the interactive, user-friendly web interface.

Python: The main programming language used for system development.


How to Run:-

Install the required dependencies: pip install -r requirements.txt.

Launch the Streamlit app: streamlit run app.py.

Input job descriptions, view matched portfolios, and generate email drafts in real time.

Future Enhancements:-

Candidate Feedback Loop: Integrating candidate feedback to improve matching accuracy over time.

Multi-Language Support: Expanding the system to support job descriptions and candidate profiles in multiple languages.

Advanced Filtering: Adding more advanced filters such as experience level, location, or compensation preferences.

Batch Processing: Enabling batch uploads for job descriptions and portfolios to speed up the recruitment process.
