import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv

# Load the Environment Variables.
load_dotenv()
st.set_page_config(page_title="Codex Leicester Chat App")

# Sidebar contents
with st.sidebar:
    st.title('Your personal AI')
    st.markdown('''
    
    ## Be educated, be organized, and be agitated
    - [LAION-AI](https://laion.ai/)
    The LLM of Codex Leicester was trained by LAION-AI.
    
    ''')
    add_vertical_space(3)
    st.markdown('<p style="font-family:monospace; color: White;">Made by Chanchal C. Ganvir</p>', unsafe_allow_html=True)

st.markdown('<p style="font-family:larg-cursive;font-size:40px; color:Green;text-shadow: 14 14 20px black;">Codex Leicester</p>', unsafe_allow_html=True)

def main():
    st.session_state.setdefault('generated', ["Hey there, great to meet you. Iâm Codex Leicester, your personal AI. My goal is to be useful, friendly, and provide information. Ask me for advice, for answers, or letâs talk about whateverâs on your mind. "])
    st.session_state.setdefault('user', ['Hi!'])

    input_text = st.text_input("Search ", "", key="input")

    # Initialize LLM directly in the main function
    template = """{question}
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])

    try:
        llm = HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens": 1200})
        llm_chain = LLMChain(llm=llm, prompt=prompt)
    except Exception as e:
        st.error(f"Error initializing LLM: {e}")
        return

    if input_text:
        try:
            response = llm_chain.run(input_text)
            st.session_state.user.append(input_text)
            st.session_state.generated.append(response)
        except Exception as e:
            st.error(f"Error generating response: {e}")
            return

    if st.session_state['generated']:
        for i, (user, generated) in enumerate(zip(st.session_state['user'], st.session_state["generated"])):
            message(user, is_user=True, key=f"{i}_user")
            message(generated, key=str(i))

if __name__ == '__main__':
    main()