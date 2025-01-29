from typing import Any

# Dummy module to invoke 'main' function dynamically
class GenericScorer:
    def __init__(self):
        pass

class Score:
    name : str
    score : float
    def __init__(self, name, score):
        self.name = name
        self.score = score

# handler function - Start
import spacy
nlp = spacy.load("en_core_web_sm")

def handler(input: Any, output: Any, expected: Any) -> Any:
    output_ents = {ent.text for ent in nlp(output).ents}
    expected_ents = {ent.text for ent in nlp(expected).ents}
    common_ents = output_ents.intersection(expected_ents)
    score = len(common_ents) / len(expected_ents) if expected_ents else 0
    return Score(name="ner_scorer", score=score)
# handler function - End

def main(input: Any, output: Any, expected: Any) -> Any:
    return handler(input, output, expected)

