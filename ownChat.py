import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
st.set_page_config(page_title="Codex Leicester Chat App")

# Sidebar contents
with st.sidebar:
    st.title('Your personal AI')
    st.markdown('''
    
   ## Be educated, be organised, and be agitated
- [LAION-AI](https://laion.ai/)
    The LLM for Codex Leicester is trained using LAION-AI.
    
    ''')
    add_vertical_space(3)
    st.markdown('<p style="font-family:monospace; color: Teal;">Made by Chanchal C. Ganvir</p>', unsafe_allow_html=True)

# Main app title
st.markdown('<p style="font-family:larg-cursive;font-size:40px; color:Green;text-shadow: 14 14 20px black;">Codex Leicester</p>', unsafe_allow_html=True)

def main():
    # Initialize or retrieve session state
    generated_responses = st.session_state.get('generated', ["Hey there, great to meet you. I’m Codex Leicester, your personal AI. My goal is to be useful, friendly and providing information. Ask me for advice, for answers, or let’s talk about whatever’s on your mind."])
    user_inputs = st.session_state.get('user', ['Hi!'])

    # Layout of input/response containers
    response_container = st.container()
    colored_header(label='', description='', color_name='blue-70')
    input_container = st.container()

    # Get user input
    with input_container:
        user_input = st.text_input("You: ", "", key="input")

    # Chain setup for language model
    llm_chain = st.session_state.get('llm_chain')
    if llm_chain is None:
        template = """{question}"""
        prompt = PromptTemplate(template=template, input_variables=["question"])
        llm = HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens": 1200})
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        st.session_state['llm_chain'] = llm_chain

    # Generate response
    with response_container:
        if user_input:
            response = llm_chain.run(user_input)
            user_inputs.append(user_input)
            generated_responses.append(response)

        for i, (user, generated) in enumerate(zip(user_inputs, generated_responses)):
            message(user, is_user=True, key=f"{i}_user")
            message(generated, key=str(i))

if __name__ == '__main__':
    main()
