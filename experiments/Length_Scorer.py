# Example 1:
# Objective:
#  - To validate the length of the model response. Model response length = 50 

# Input parameters
#  - Expected_outcome -> define this in the function
#  - Response (LLM Output) -> length is applied on this response

# Design
#  - Python len() to get the length
#  - Compare against the Expected_outcome
#  - Return logic

# calling function dynamically in python
# https://www.danielmorell.com/blog/dynamically-calling-functions-in-python-safely
# https://stackoverflow.com/questions/7719466/i-have-a-string-whose-content-is-a-function-name-how-to-refer-to-the-correspond
# https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/exec/python-exec/
# ** https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string **
# ** ACE Editor - https://discuss.streamlit.io/t/how-to-add-a-streamlit-editable-code-editor-with-python-syntax-highlighting/54473
# Auto generate requirements.txt - https://stackoverflow.com/questions/46419607/how-to-automatically-install-required-packages-from-a-python-script-as-necessary
# Code editor: https://discuss.streamlit.io/t/new-component-streamlit-code-editor-a-react-ace-code-editor-customized-to-fit-with-streamlit-with-some-extra-goodies-added-on-top/42868

def length_scorer(response, expected_outcome):
    if len(response) >= expected_outcome:
        return True
    else:
        return False

def execute(callback, response, expected_outcome):
    return callback(response, expected_outcome)

if __name__ == "__main__":
    response = "This is a test response"
    expected_outcome = 3
    print(execute(length_scorer, response, expected_outcome))

    response = "This is a test response"
    expected_outcome = 50
    print(execute(length_scorer, response, expected_outcome))  

