class Person():
    def __init__(self, id : int, name : str, title : str, constituency : str, politicalPower : int):
        self.id = id
        self.name = name
        self.constituency = constituency
        self.politicalPower = politicalPower
        self.title = ""

    def print(self):
        print(self.name + ", " + self.constituency)