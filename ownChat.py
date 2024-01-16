import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv

def initialize_session_state():
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hey there, great to meet you. I’m Codex Leicester, your personal AI. My goal is to be useful, friendly and providing information. Ask me for advice, for answers, or let’s talk about whatever’s on your mind."]

    if 'user' not in st.session_state:
        st.session_state['user'] = ['Hi!']

def get_user_input():
    return st.text_input("Search ", "", key="input")

def setup_llm_chain():
    template = """{question}"""
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens": 1200})
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    return llm_chain

def generate_response(user_input, llm_chain):
    response = llm_chain.run(user_input)
    return response

def display_messages():
    response_container = st.container()
    with response_container:
        if st.session_state['generated']:
            for i, (user_msg, generated_msg) in enumerate(zip(st.session_state['user'], st.session_state['generated'])):
                message(user_msg, is_user=True, key=f"{i}_user")
                message(generated_msg, key=str(i))

def main():
    load_dotenv()
    st.set_page_config(page_title="Codex Leicester Chat App")

    initialize_session_state()

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

    user_input = get_user_input()
    llm_chain = setup_llm_chain()

    with st.container():
        if user_input:
            response = generate_response(user_input, llm_chain)
            st.session_state.user.append(user_input)
            st.session_state.generated.append(response)

        display_messages()

if __name__ == '__main__':
    main()
