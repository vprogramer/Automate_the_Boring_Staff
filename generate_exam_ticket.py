import random
import time


class Question(object):
    def __init__(self, number):
        self.number = number
        self.capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                         'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford',
                         'Delaware': 'Dover',
                         'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                         'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                         'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
                         'Maryland': 'Annapolis',
                         'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
                         'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
                         'Nebraska': 'Lincoln',
                         'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                         'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                         'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
                         'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                         'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
                         'Utah': 'Salt Lake City',
                         'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                         'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
        self.generate()

    def generate(self):
        states = list(self.capitals.keys())
        random.shuffle(states)
        self.correct_state = states[self.number]
        # self.correct_state = states[random.randint(0, number_of_questions-1)]
        self.correct_capital = self.capitals[self.correct_state]

        wrong_answers = list(self.capitals.values())
        wrong_answers.remove(self.capitals.get(self.correct_state))
        self.all_variants = [self.correct_capital] + random.sample(wrong_answers, 3)

    def get_cor_state(self):
        return self.correct_state

    def get_cor_capital(self):
        return self.correct_capital

    def get_all_variants(self):
        return self.all_variants


class Ticket(object):
    def __init__(self, number):
        self.number = number
        self.correct_answers = list()
        self.answers = list()
        self.position_right_answer = list()
        self.create()

    def create(self):
        for question_number in range(number_of_questions):
            quest = Question(question_number)
            self.correct_answers.append((quest.get_cor_state(), quest.get_cor_capital()))
            temporal_all_variants = quest.get_all_variants()
            random.shuffle(quest.get_all_variants())
            self.position_right_answer.append(temporal_all_variants.index(quest.get_cor_capital()))
            self.answers.append(temporal_all_variants)

    def get_correct_answers(self):
        return self.correct_answers

    def get_all_answers(self):
        return self.answers

    def get_correct_position(self):
        return self.position_right_answer


class FileTicket(Ticket):
    def __init__(self, number):
        Ticket.__init__(self, number)
        self.variants = 'ABCD'

    def write_all_questions(self):
        filename = 'quiz_files/capitals_quiz{}.txt'.format(self.number + 1)
        with open(filename, 'a') as f:
            for question in range(number_of_questions):
                f.write('{0}) What is the capital of {1}?'.format(question + 1, self.get_correct_answers()[question][0]))
                f.write('\n')
                for var in range(len(self.variants)):
                    f.write('{0}: {1}'.format(self.variants[var], self.get_all_answers()[question][var]))
                    f.write('\n')
                f.write('\n\n')
            f.close()

    def write_head(self):
        filename = 'quiz_files/capitals_quiz{}.txt'.format(self.number + 1)
        with open(filename, 'w') as f:
            f.write('Name:\n\nDate:\n\nPeriod:\n\n')
            f.write((' ' * 20) + 'State Capitals Quiz (Form {0})'.format(self.number + 1))
            f.write('\n\n')
            f.close()


class AnswerFileTicket(FileTicket):
    def __init__(self, number):
        self.number = number
        super(AnswerFileTicket, self).__init__(number)

    def write_answer(self):
        filename = 'quiz_files/capitals_quiz_answer{}.txt'.format(self.number + 1)
        with open(filename, 'w') as f:
            f.write('Answers:')
            f.write('\n')
            for num_quest in range(number_of_questions):
                f.write('{0}: {1} ({2})'.format(num_quest + 1, self.variants[self.get_correct_position()[num_quest]], self.get_correct_answers()[num_quest][1] ))
                f.write('\n')
            f.write('\n')
            f.close()


class Test(object):
    def __init__(self):
        self.number_ticket = None

    def choose_ticket(self):
        self.number_ticket = 32 #random.randint(1, number_tickets)

    def show_ticket(self):
        filename = 'quiz_files/capitals_quiz{}.txt'.format(self.number_ticket)
        with open(filename, 'r') as f:
            print(f.read())


class AnswerTest(Test):
    def __init__(self):
        Test.__init__(self)
        self.all_ans = list()
    def answer_the_question(self):
        for ans in range(1, number_of_questions+1):
            self.all_ans.append(input('Введите ответ (одну из букв A,B,C,D) на вопрос №{}: \n'.format(ans)).upper())
    def get_ans(self):
        return self.all_ans


class ResultTest(AnswerTest):
    def __init__(self):
        AnswerTest.__init__(self)
        self.right_ans_from_file = list()
        self.result = 0
    def result_of_test(self):
        filename = 'quiz_files/capitals_quiz_answer{}.txt'.format(self.number_ticket)
        with open(filename, 'r') as f:
            i = 0
            for j in range(number_of_questions):
                for line in f:
                    if i > 0 and i < 51:
                        right_ans = line.split(' ')[1]
                        time.sleep(2)
                        corr_ans = self.get_ans()[j]
                        if right_ans == corr_ans:
                            self.result += 1
                    i += 1
            f.close()

        return self.result*10 / number_of_questions


if __name__ == '__main__':
    number_of_questions = 50
    number_tickets = 35
    test = ResultTest()
    test.choose_ticket()
    test.show_ticket()
    test.answer_the_question()
    print(test.result_of_test())
    # for i in range(number_of_questions):
    #     ticket = AnswerFileTicket(i)
    #     ticket.write_answer()
    #     ticket.write_head()
    #     ticket.write_all_questions()
