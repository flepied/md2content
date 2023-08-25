"""Second brain web interface

Take a question from the user and call the LLM for an answer using the
closest documents stored in the vector database as context.
"""

import streamlit as st
from dotenv import load_dotenv

from htmlTemplates import css, user_template
from lib import Agent


def handle_userinput(user_question):
    "Handle the input from the user as a question to the LLM"
    response = st.session_state.agent.html_question(user_question)
    st.write(
        user_template.replace("{{MSG}}", response),
        unsafe_allow_html=True,
    )


def clear_input_box():
    "Empty the input box"
    handle_userinput(st.session_state["question"])
    st.session_state["question"] = ""


def main():
    "Entry point"
    load_dotenv()
    st.set_page_config(
        page_title="Ask questions to your Second Brain", page_icon=":brain:"
    )
    st.write(css, unsafe_allow_html=True)
    st.header("Ask a question to your Second Brain :brain:")

    if "agent" not in st.session_state:
        st.session_state.agent = Agent()

    st.text_input(
        "Ask a question to your second brain:",
        key="question",
        on_change=clear_input_box,
    )

    st.components.v1.html(
        """
<script>
var input = window.parent.document.querySelectorAll("input[type=text]");

        for (var i = 0; i < input.length; ++i) {{
            input[i].focus();
        }}
</script>
""",
        height=150,
    )


if __name__ == "__main__":
    main()
