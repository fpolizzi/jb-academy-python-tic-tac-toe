class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # define your methods here
    def __iadd__(self, height):
        self.height += height
        return self

    def __isub__(self, height):
        self.height -= height
        return self
