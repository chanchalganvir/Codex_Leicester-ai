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
        The LLM for Codex Leicester is trained using LAION-AI.
    ''')

    add_vertical_space(3)
    st.markdown('<p style="font-family:monospace; color: Red;">Made by Chanchal C. Ganvir</p>', unsafe_allow_html=True)

# Main title
st.markdown('<p style="font-family:larg-cursive;font-size:40px; color:Green;text-shadow: 14 14 20px black;">Codex Leicester</p>',
            unsafe_allow_html=True)

def main():
    # Generate empty lists for generated and user.
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hey there, great to meet you. I’m Codex Leicester, your personal AI. My goal is to be useful, friendly and providing information. Ask me for advice, for answers, or let’s talk about whatever’s on your mind. "]

    if 'user' not in st.session_state:
        st.session_state['user'] = ['Hi!']

    # Layout of input/response containers
    response_container = st.container()
    colored_header(label='', description='', color_name='blue-70')
    input_container = st.container()

    # Get user input
    def get_text():
        input_text = st.text_input("You: ", "", key="input")
        return input_text

    # Applying the user input box
    with input_container:
        user_input = get_text()

    # Chain setup
    def chain_setup():
        template = """{question}"""

        prompt = PromptTemplate(template=template, input_variables=["question"])

        llm = HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens": 1200})

        llm_chain = LLMChain(llm=llm, prompt=prompt)
        return llm_chain

    # Generate response
    def generate_response(question, llm_chain):
        try:
            response = llm_chain.run(question)
            return response
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

    # Load LLM
    llm_chain = chain_setup()

    # Main loop
    with response_container:
        if user_input:
            response = generate_response(user_input, llm_chain)
            st.session_state.user.append(user_input)
            st.session_state.generated.append(response)

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['user'][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))

if __name__ == '__main__':
    main()
