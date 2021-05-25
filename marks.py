class Marks:
    def __init__(self, subject, student_name, mark, max_mark, grade, specialty, date):
        self.subject = subject
        self.student_name = student_name
        self.mark = mark
        self.max_mark = max_mark
        self.grade = grade
        self.specialty = specialty
        self.date = date

    def print(self):
        print("subject: " + self.subject)
        print("name of student: " + self.student_name)
        print("mark: " + str(self.mark) + "/" + str(self.max_mark))
        print("grade: " + self.grade)
        print("specialty: " + self.specialty)
        print("date: " + str(self.date))
