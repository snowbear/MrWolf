import json


class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    @staticmethod
    def from_dict(dict):
        return Test(dict['input'], dict['output'])

    @staticmethod
    def from_json_str(js_str):
        return [Test.from_dict(o) for o in json.loads(js_str)]
        
    def __eq__(self, other):
        return (
            self.input == other.input and
            self.output == other.output
        )


class SubmissionResult:
    def __init__(self, successful, output):
        self.successful = successful
        self.output = output
