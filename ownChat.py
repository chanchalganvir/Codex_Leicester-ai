import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv

# load the Environment Variables. 
load_dotenv()
st.set_page_config(page_title="Codex Leicester Chat App")

# Sidebar contents
with st.sidebar:
    st.title('Your personal AI')
    st.markdown('''
    
    ## Be educated, be organised, and be agitated
    - [LAION-AI](https://laion.ai/)
    The LLM of Codex Leicester was trained by LAION-AI.
    
    ''')
    add_vertical_space(3)
    st.markdown('<p style="font-family:monospace; color: White;">Made by Chanchal C. Ganvir</p>', unsafe_allow_html=True)

st.markdown('<p style="font-family:larg-cursive;font-size:40px; color:Green;text-shadow: 14 14 20px black;">Codex Leicester</p>', unsafe_allow_html=True)

def main():
    # Generate empty lists for generated and user.
    st.session_state.setdefault('generated', ["Hey there, great to meet you. Iâm Codex Leicester, your personal AI. My goal is to be useful, friendly and providing information. Ask me for advice, for answers, or letâs talk about whateverâs on your mind. "])
    st.session_state.setdefault('user', ['Hi!'])

    # get user input
    input_text = st.text_input("Search ", "", key="input")

    # load LLM only when needed
    if input_text:
        llm_chain = chain_setup()
        response = generate_response(input_text, llm_chain)
        st.session_state.user.append(input_text)
        st.session_state.generated.append(response)

    # main loop
    if st.session_state['generated']:
        for i, (user, generated) in enumerate(zip(st.session_state['user'], st.session_state["generated"])):
            message(user, is_user=True, key=f"{i}_user")
            message(generated, key=str(i))

if __name__ == '__main__':
    main()