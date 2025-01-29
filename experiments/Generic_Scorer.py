from typing import Any

class Score:
    name : str
    score : float
    def __init__(self, name, score):
        self.name = name
        self.score = score

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
def handler(input: Any, output: Any, expected: Any) -> Any:
    if len(output) >= expected:
        return True
    else:
        return False

# # We need one standard function "scorer" with return type as "Score"
# def scorer(input: Any, output: Any, expected: Any) -> Any:
#     return Score(name="abc", score=number)

# Example 2
def banana_scorer(input: Any, output: Any, expected: Any) -> Any:
    return Score(name="banana_scorer", score=1 if "banana" in output else 0)

# Example 3
def politeness_scorer(input: Any, output: Any, expected: Any) -> Any:
    polite_words = ["please", "thank you", "sorry"]
    score = sum(1 for word in polite_words if word in output.lower()) / len(polite_words)
    return Score(name="politeness_scorer", score=score)

# Example 4
import spacy
nlp = spacy.load("en_core_web_sm")

def ner_scorer(input: Any, output: Any, expected: Any) -> Any:
    output_ents = {ent.text for ent in nlp(output).ents}
    expected_ents = {ent.text for ent in nlp(expected).ents}
    common_ents = output_ents.intersection(expected_ents)
    score = len(common_ents) / len(expected_ents) if expected_ents else 0
    return Score(name="ner_scorer", score=score)

# Example 5
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

def grammar_spelling_scorer(input: Any, output: Any, expected: Any) -> Any:
    matches = tool.check(output)
    score = 1.0 - (len(matches) / max(1, len(output.split())))
    return Score(name="grammar_spelling_scorer", score=score)

# Example 6
from textblob import TextBlob
def sentiment_scorer(input: Any, output: Any, expected: Any) -> Any:
    output_sentiment = TextBlob(output).sentiment.polarity
    expected_sentiment = TextBlob(expected).sentiment.polarity
    score = 1.0 if (output_sentiment > 0 and expected_sentiment > 0) or \
               (output_sentiment < 0 and expected_sentiment < 0) else 0
    return Score(name="sentiment_scorer", score=score)


class GenericScorer:
    def __init__(self):
        pass

    def execute(self, callback, input, output, expected):
        return callback(input, output, expected)

if __name__ == "__main__":
    # For all, get the response from LLM for a given prompt

    # Example 1
    gen_scorer_obj = GenericScorer()
    # String
    input = "prompt query"
    output = "This is a test response"
    expected = 3
    print(gen_scorer_obj.execute(handler, input, output, expected))

    # String
    output = "This is a test response"
    expected = 50
    print(gen_scorer_obj.execute(handler, input, output, expected))

    # List
    output = [1, 2, 3, 4, 5]
    expected = 3
    print(gen_scorer_obj.execute(handler, input, output, expected))  

    # Map
    output = {1: "one", 2: "two", 3: "three"}
    expected = 5
    print(gen_scorer_obj.execute(handler, input, output, expected))

    # Tuple
    output = (("1", "one"), ("2", "two"), ("3", "three"))
    expected = 2
    print(gen_scorer_obj.execute(handler, input,  output, expected))

    # ----------------------------------------------------------
    # Example 2
    input = "What is 1 banana + 2 bananas?"
    output = "3"
    expected = "3 bananas"
    banana_scorer_obj = gen_scorer_obj.execute(banana_scorer, input,  output, expected)
    print("Name = ", banana_scorer_obj.name, "and score = ", round(banana_scorer_obj.score))

    # Example 3
    input = "Can you explain how to reboot the server?"
    output = "Please reboot the server by following the instructions. Thank you!"
    expected = "Follow the instructions to reboot the server."
    politeness_scorer_obj = gen_scorer_obj.execute(politeness_scorer, input,  output, expected)
    print("Name = ", politeness_scorer_obj.name, "and score = ", round(politeness_scorer_obj.score, 2))

    # Example 4
    input = "Who was the first man on the moon?"
    output = "Neil Armstrong was the first man on the moon."
    expected = "Neil Armstrong was the first man on the moon."
    ner_scorer_obj = gen_scorer_obj.execute(ner_scorer, input,  output, expected)
    print("Name = ", ner_scorer_obj.name, "and score = ", round(ner_scorer_obj.score, 2))  

    # Example 5
    input = "Describe your favorite book."
    output = "I loves reading books. My favorite is The Hobbit."
    expected = "I love reading books. My favorite is The Hobbit."
    grammar_spelling_scorer_obj = gen_scorer_obj.execute(grammar_spelling_scorer, input,  output, expected)
    print("Name = ", grammar_spelling_scorer_obj.name, "and score = ", round(grammar_spelling_scorer_obj.score, 2))

    # Example 6
    input = "How do you feel about the new policy?"
    output = "I love the new policy; it's great!"
    expected = "I am very happy with the new policy."
    sentiment_scorer_obj = gen_scorer_obj.execute(sentiment_scorer, input,  output, expected)
    print("Name = ", sentiment_scorer_obj.name, "and score = ", round(sentiment_scorer_obj.score))

        
