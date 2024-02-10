import streamlit
from langchain_community.document_loaders import PyPDFLoader
import qdrant_client
from sentence_transformers import SentenceTransformer


def foo(): pass

streamlit.header("Open University Tutor")
streamlit.write("This platform is for uploading course materials relavant to the courses we are enrolled")

subjects:list=['EEX4456','EEX3373']

streamlit.session_state['selected_subject']:streamlit.session_state=streamlit.selectbox(label='Select the course relavant to the material',options=subjects)

streamlit.file_uploader(label='Choose files for upload')

if streamlit.button('Upload'):
    foo()

embedding_model:SentenceTransformer=SentenceTransformer('all-MiniLM-L6-v2')

