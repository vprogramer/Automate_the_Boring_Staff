import os
import sys
import random


class Question(object):
    def __init__(self, number):
        self.number = number
        self.capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
                    'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
                    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
                    'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
                    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
                    'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
                    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
        # self.answer = ['A', 'B', 'C', 'D']
    def generate(self):
        states = self.capitals.keys()
        type(states)
        random.shuffle(states)

        self.correct_answer = self.capitals[states[random.randint(0,50)]]
        wrong_answers = self.capitals.values()
        del wrong_answers[self.capitals.index(self.correct_answer)]
        self.variants = [self.correct_answer] + random.sample(wrong_answers, 3)
        return self.correct_answer, self.variants


class Ticket(object):
    def __init__(self, number):
        self.number = number
    def create(self):
        for question_number in range(50):
            quest = Question(question_number)
            correct, variants = quest.generate()
            print(correct, variants)


ticket = Ticket(1)
ticket.create()




