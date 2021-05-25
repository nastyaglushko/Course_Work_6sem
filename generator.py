from marks import Marks
import names
import datetime
import random


class Generator:

    start_subjects = ['Mathematics', 'English', 'German', 'Music', 'Art', 'Literature',
                      'Ukrainian', 'Health']
    mid_subjects = ['English', 'Algebra', 'Geometry', 'Geography', 'History',
                    'German', 'Music', 'Art', 'Ethic', 'Literature',
                    'Computer studies', 'Ukrainian', 'Health']
    top_subjects = ['English', 'Algebra', 'Geometry', 'Physic', 'Geography', 'History',
                    'German', 'Biology', 'Chemistry', 'Literature', 'Computer studies', 'Ukrainian', 'Economic']
    specialty = ['Linguistic', 'Math', 'Humanitarian', 'Natural science', 'Art', 'Economic']

    @staticmethod
    def get_all_subjects():
        subjects_list = Generator.start_subjects
        for subject in Generator.mid_subjects:
            if subjects_list.count(subject) == 0:
                subjects_list.append(subject)
        for subject in Generator.top_subjects:
            if subjects_list.count(subject) == 0:
                subjects_list.append(subject)
        return subjects_list

    @staticmethod
    def get_subjects_by_grade(grade):
        if grade <= 4:
            return Generator.start_subjects
        elif grade <= 9:
            return Generator.mid_subjects
        else:
            return Generator.top_subjects

    @staticmethod
    def generate_doc():
        student_name = names.get_full_name()
        subject = ''
        grade = random.randint(1, 11)
        if grade <= 4:
            subject = random.choice(Generator.start_subjects)
        elif grade <= 9:
            subject = random.choice(Generator.mid_subjects)
        else:
            subject = random.choice(Generator.top_subjects)
        max_mark = 12
        mark = 0
        if random.randint(0, 3) < 3:
            mark = random.randint(7, 10)
        elif random.randint(0, 2) > 0:
            mark = random.randint(11, 12)
        else:
            mark = random.randint(1, 6)

        specialty = random.choice(Generator.specialty)

        d1 = datetime.datetime(2020, 1, 1, 0, 0, 0, 0)
        d2 = datetime.datetime.now()
        delta = d2 - d1
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        date = d1 + datetime.timedelta(seconds=random_second)

        marks = Marks(subject, student_name, mark, max_mark, grade, specialty, date)
        return marks

    @staticmethod
    def generate_marks(count):
        marks_list = list()
        for i in range(count):
            mark = Generator.generate_doc()
            marks_list.append(mark)
        return marks_list

