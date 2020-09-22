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
        states = list(self.capitals.keys())
        random.shuffle(states)

        self.correct_state = states[random.randint(0, 50)]
        self.correct_answer = self.capitals[self.correct_state]

        wrong_answers = list(self.capitals.values())
        del wrong_answers[self.capitals.index(self.correct_answer)]
        self.variants = [self.correct_answer] + random.sample(wrong_answers, 3)
        return self.correct_state, self.correct_answer, self.variants


class Ticket(object):
    def __init__(self, number):
        self.number = number
    def create(self):
        for question_number in range(50):
            quest = Question(question_number)
            answers = list()
            answers.append((quest.generate()))
            print(answers)
            # correct, variants = quest.generate()
        return answers


class FileTicket(Ticket):
    def __init__(self, number):
        Ticket.__init__(self, number)
        self.variants = ['A', 'B', 'C', 'D']
        self.answer = Ticket.create()
    def write_all_questions(self):
        filename = 'capitals_quiz{}.txt'.format(self.number + 1)
        with open(filename, 'w') as f:
            for i in range(0, 50):
                f.write('{0}) What is the capital of {1}'.format(i + 1, self.answer[i][0]))

    def write_head(self):
        filename = 'capitals_quiz{}.txt'.format(self.number + 1)
        with open(filename, 'w') as f:
            f.write('Name:\n\nDate:\n\nPeriod:\n\n')
            f.write((' ' * 20) + 'State Capitals Quiz (Form {0})'.format(self.number + 1))
            f.write('\n\n')


class AnswerFileTicket(FileTicket):
    def __init__(self, number):
        super(AnswerFileTicket, self).__init__(number)
    def write_answer(self, number):
        filename = 'capitals_quiz_answer{}.txt'.format(number + 1)
        with open(filename, 'w') as f:
            f.write('')


ticket = FileTicket(1)
ticket.write_head()




