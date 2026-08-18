class State:

    def __init__(self):

        self.data = {

            "user_prompt": "",

            "execution_plan": [],

            "results": {},

            "logs": []
        }

    def set(self, key, value):

        self.data[key] = value

    def get(self, key):

        return self.data.get(key)

    def add_result(self, agent, value):

        self.data["results"][agent] = value