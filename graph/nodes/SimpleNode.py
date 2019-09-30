class SimpleNode():
    value = None

    def __init__(self, value):
        self.value = value

    def change_value(self, new_value):
        self.value = new_value