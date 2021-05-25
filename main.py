from colorama import init
from database import Database
from generator import Generator
from analyzer import Analyzer
from graphics_bilder import GraphicsBuilder


db = Database()
init(autoreset=True)


def generate_data():
    count = int(input("> Enter count of marks to generate: "))
    marks_list = Generator.generate_marks(count)
    db.insert_list(marks_list)


def remove_mark():
    _id = str(input("> Enter ID of mark to delete: "))
    db.delete(_id)


def clear_db():
    db.delete_all()


def analyze_data():
    print(" Choose graphic to show:")
    print(" 1. Average mark for subject of certain specialty")
    print(" 2. Average mark for subject of certain grade")
    print(" 3. Correlation of marks for subject and grades")
    _choice = int(input("> Enter your choice [1-3]: "))
    subject = str(input("> Enter subject: "))
    if _choice == 1:
        specialty = str(input("> Enter specialty: "))
        av = Analyzer.average_mark(db.get_by_subject_and_specialty(subject, specialty))
        print("Average mark for " + subject + " of " + specialty + " specialty is: " + str(av))
    elif _choice == 2:
        grade = int(input("> Enter grade: "))
        av = Analyzer.average_mark(db.get_by_subject_and_grade(subject, grade))
        print("Average mark for " + subject + " in " + str(grade) + " grades is: " + str(av))
    elif _choice == 3:
        cor = Analyzer.correlation_coef_marks_and_grades(db.get_by_subject(subject))
        print("Correlation of marks for subject " + subject + " depends on grades is: " + str(cor))
    else:
        print("  Wrong option")


def find_marks():
    print(" Choose search parameter:")
    print(" 1. ID")
    print(" 2. Subject")
    print(" 3. Grade")
    print(" 4. Dates")
    _choice = int(input("> Enter your choice [1-4]: "))
    if _choice == 1:
        _id = str(input("> Enter ID of mark: "))
        print_marks(db.get_by_id(_id))
    elif _choice == 2:
        subject = str(input("> Enter subject: "))
        print_marks(db.get_by_subject(subject))
    elif _choice == 3:
        grade = int(input("> Enter grade: "))
        print_marks(db.get_by_grade(grade))
    elif _choice == 4:
        date1 = str(input("> Enter start date:  "))
        date2 = str(input("> Enter end date: "))
        print_marks(db.get_by_dates(date1, date2))
    else:
        print("  Wrong option")


def print_graphics():
    gb = GraphicsBuilder()
    print(" Choose graphic to show:")
    print(" 1. Average marks")
    print(" 2. Average marks by grade")
    print(" 3. Average marks by specialty")
    print(" 4. Average marks by subject ordered by specialty")
    print(" 5. Average marks by subject ordered by grade")
    print(" 6. Correlation of marks for subject and specialties")
    print(" 7. Regression of marks for subject and grades")
    _choice = int(input("> Enter your choice [1-7]: "))
    date1 = str(input("> Enter start date:  "))
    date2 = str(input("> Enter end date: "))
    if _choice == 1:
        gb.average_mark_graph(db, date1, date2)
    elif _choice == 2:
        grade = int(input("> Enter grade: "))
        gb.average_mark_by_grade_graph(db, date1, date2, grade)
    elif _choice == 3:
        specialty = str(input("> Enter specialty: "))
        gb.average_mark_by_specialty_graph(db, date1, date2, specialty)
    elif _choice == 4:
        subject = str(input("> Enter subject: "))
        gb.average_mark_by_subject_order_by_specialty_graph(db, date1, date2, subject)
    elif _choice == 5:
        subject = str(input("> Enter subject: "))
        gb.average_mark_by_subject_order_by_grade_graph(db, date1, date2, subject)
    elif _choice == 6:
        subject = str(input("> Enter subject: "))
        gb.correlation_mark_for_subject_and_specialty_graph(db, date1, date2, subject)
    elif _choice == 7:
        subject = str(input("> Enter subject: "))
        gb.regression_mark_for_subject_and_grade_graph(db, date1, date2, subject)
    else:
        print("  Wrong option")


def print_marks(marks_list):
    for mark in marks_list:
        print('ID:         ' + str(mark.get('_id')))
        print('SUBJECT:    ' + str(mark.get('subject')).strip())
        print('STUDENT:    ' + str(mark.get('student_name')).strip())
        print('MARk:       ' + str(mark.get('mark')) + '/' + str(mark.get('max_mark')))
        print('GRADE:      ' + str(mark.get('grade')))
        print('SPECIALITY: ' + str(mark.get('specialty')).strip())
        print('DATE:       ' + str(mark.get('date').strftime('%Y-%m-%d')).strip())
        print(74 * '-')


def print_menu():
    print(30 * "*", "MENU", 30 * "*")
    print("1. Add generated data")
    print("2. Get all marks")
    print("3. Find marks")
    print("4. Delete mark")
    print("5. Analyze data")
    print("6. Print graphics")
    print("7. Clear db")
    print("8. Exit")
    print(66 * "-")


while True:
    print_menu()
    try:
        choice = int(input("> Enter option [1-8]: "))
    except ValueError:
        print("Wrong option")
        continue
    if choice == 1:
        generate_data()
    elif choice == 2:
        print_marks(db.get_all())
        input(" Press Enter to return...")
    elif choice == 3:
        find_marks()
        input(" Press Enter to return...")
    elif choice == 4:
        remove_mark()
    elif choice == 5:
        analyze_data()
        input(" Press Enter to return...")
    elif choice == 6:
        print_graphics()
    elif choice == 7:
        clear_db()
    elif choice == 8:
        break
    else:
        print("Wrong option")
