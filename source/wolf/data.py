import json

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def from_dict(dict):
        return Test(dict['input'], dict['output'])
        
    def from_json_str(jsStr):
        return [ Test.from_dict(o) for o in json.loads(jsStr) ]
        
    def __eq__(self, other):
        return (
            self.input == other.input and
            self.output == other.output
        )

class SubmissionResult:
    def __init__(self, successful, output):
        self.successful = successful
        self.output = output
