import random
import json

from typing import Optional, TYPE_CHECKING, Tuple
from people.person import Person
from people.person_generator import PersonGenerator

people_file = "data/people.json"

class PersonManager:
    def __init__(self):
        self.people = list()
        self.import_people()
        self.personGenerator = PersonGenerator()

    def import_people(self):
        with open(people_file) as json_file:
            data = json.load(json_file)
            for p in data['people']:
                self.people.append(Person(id=p[0], name=p[1], constituency=p[2], politicalPower=p[3], title=""))

        random.shuffle(self.people)

    def get_next_person(self):
        self.currentPerson = self.personGenerator.GeneratePerson(100)
        return self.currentPerson