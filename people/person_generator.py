import json
import random

from typing import Optional, TYPE_CHECKING, Tuple
from people.person import Person

people_file = "data/people_data.json"

class PersonGenerator():
    def __init__(self):
        with open(people_file) as json_file:
            data = json.load(json_file)
            self.firstnames = data["firstnames"]
            self.lastnames = data["lastnames"]
            self.constituencies = data["constituencies"]
            random.shuffle(self.constituencies)
    
    def GeneratePerson(self, politicalPower : int):
        return Person(id=0, 
            name=self.firstnames[random.randrange(0, len(self.firstnames))][0] + " " +  self.lastnames[random.randrange(0, len(self.lastnames))][0],
            title="",
            constituency=self.constituencies.pop()[1],
            politicalPower=politicalPower)
            