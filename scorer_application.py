# pip install streamlit_code_editor - https://discuss.streamlit.io/t/new-component-streamlit-code-editor-a-react-ace-code-editor-customized-to-fit-with-streamlit-with-some-extra-goodies-added-on-top/42868/10
# pip install CodeEditor - https://pypi.org/project/CodeEditor/
# pip install streamlit

import os
import streamlit as st
from pathlib import Path
from score import Score
from module_loader import Module_Loader
from code_editor import code_editor
import datetime

# code editor config variables
height = [10, 22]
language="python"
theme="default"
shortcuts="vscode"
focus=False
wrap=True
editor_btns = [{
    "name": "Run",
    "feather": "Play",
    "primary": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "style": {"bottom": "0.44rem", "right": "0.4rem"}
  }]

# if 'clicked' not in st.session_state:
#     st.session_state.clicked = False

# def click_button():
#     st.session_state.clicked = True

funcname = st.text_input("Name")
st.radio('Type', ['Python', 'LLM as Judge'])
code = '''def handler(input: Any, output: Any, expected: Any) -> Any:
    return Score(name="scorer_name", score=0.0)'''
python_code = code_editor(code,  
                            height = height, 
                            lang=language, 
                            theme=theme, 
                            shortcuts=shortcuts, 
                            focus=focus, 
                            buttons=editor_btns, 
                            options={"wrap": wrap})
input = st.text_input("Input")
output = st.text_input("Output")
expected = st.text_input("Expected")
# st.button("Run", on_click=click_button)

# if st.session_state.clicked:
if len(python_code['id']) != 0 and (python_code['type'] == "selection" or python_code['type'] == "submit" ):
    # Capture the text part
    code_text = python_code['text']
    # Read in the file
    filedata = None
    filename = 'Run_Scorer_' + str(datetime.datetime.now()).replace('.', '_') + '.py'
    with open('generic_scorer_template.py', 'r') as file:
        filedata = file.read()
        # Replace the target string from template file with user function
        filedata = filedata.replace('# Add your scorer function here', code_text)
        file.close()
        # Create the executable runtime python file with replaced user function
        with open(filename, 'w') as file:
            file.write(filedata)
            file.close()
            # Load module from created runtime python file to execute the user function
            rs = Module_Loader.import_source_file(Path(filename), "GenericScorer")
            st.write("Program Response:")
            # Execute module function with input, output and expected values - Approach 1
            score_ouput = rs.main(input="prompt query", output=output, expected=expected)
            st.text_area("Results - Approach_1", score_ouput.name + " : " + str(round(score_ouput.score, 2)))
            # Execute module function with input, output and expected values - Approach 2
            score_ouput = eval("rs.main")("prompt query", output, expected)
            st.text_area("Results - Approach_2", score_ouput.name + " : " + str(round(score_ouput.score, 2)))
            # Remove the runtime python file
            os.remove(filename)
    # st.session_state.clicked = False
    