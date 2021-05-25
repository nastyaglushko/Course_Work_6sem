import numpy as np
import matplotlib.pyplot as plt
from analyzer import Analyzer
from generator import Generator


class GraphicsBuilder:

    PLOT_LABEL_FONT_SIZE = 8

    @staticmethod
    def get_colors(n):
        colors = []
        cm = plt.cm.get_cmap('hsv', n)
        for i in np.arange(n):
            colors.append(cm(i))
        return colors

    @staticmethod
    def dict_sort(_keys, _values):
        keys = []
        values = []
        my_dict = dict.fromkeys(_keys, _values)
        my_dict = sorted(my_dict.items(), key=lambda x: x[1])
        for k, v in my_dict:
            keys.append(k)
            values.append(v)
        return keys, values

    def create_graph(self, all_marks, keys, key_name, x_title, title):
        values = []
        for key in keys:
            marks = [mark for mark in all_marks if mark.get(key_name) == key]
            values.append(Analyzer.average_mark(marks))
        top_keys = len(keys)
        plt.title(title, fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.bar(np.arange(top_keys), values, color=self.get_colors(top_keys))
        plt.xticks(np.arange(top_keys), keys, rotation=90, fontsize=8)
        plt.yticks(np.arange(1, 12), fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.ylabel('Бал', fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.xlabel(x_title, fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.show()

    def average_mark_graph(self, db, date1, date2):
        GraphicsBuilder.create_graph(self, list(db.get_by_dates(date1, date2)),
                                     Generator.get_all_subjects(),
                                     'subject',
                                     'Предмет',
                                     'Середній бал з предметів за період з ' + str(date1) + ' по ' + str(date2))

    def average_mark_by_grade_graph(self, db, date1, date2, grade):
        GraphicsBuilder.create_graph(self, list(db.get_by_grade_and_dates(grade, date1, date2)),
                                     Generator.get_subjects_by_grade(grade),
                                     'subject',
                                     'Предмет',
                                     'Середній бал з предметів учнів ' + str(grade)
                                     + ' класу за період з ' + str(date1) + ' по ' + str(date2))

    def average_mark_by_specialty_graph(self, db, date1, date2, specialty):
        GraphicsBuilder.create_graph(self, list(db.get_by_specialty_and_dates(specialty, date1, date2)),
                                     Generator.get_all_subjects(),
                                     'subject',
                                     'Предмет',
                                     'Середній бал з предметів учнів за спеціальністю ' + specialty
                                     + ' за період з ' + str(date1) + ' по ' + str(date2))

    def average_mark_by_subject_order_by_specialty_graph(self, db, date1, date2, subject):
        GraphicsBuilder.create_graph(self, list(db.get_by_subject_and_dates(subject, date1, date2)),
                                     Generator.specialty,
                                     'specialty',
                                     'Спеціалізація',
                                     'Середній бал з предмету ' + subject + ' за різними спеціальностями за період з '
                                     + str(date1) + ' по ' + str(date2))

    def average_mark_by_subject_order_by_grade_graph(self, db, date1, date2, subject):
        GraphicsBuilder.create_graph(self, list(db.get_by_subject_and_dates(subject, date1, date2)),
                                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                                     'grade',
                                     'Клас',
                                     'Середній бал з предмету ' + subject + ' у різних класах за період з '
                                     + str(date1) + ' по ' + str(date2))

    def correlation_mark_for_subject_and_specialty_graph(self, db, date1, date2, subject):
        all_marks = list(db.get_by_subject_and_dates(subject, date1, date2))
        specialities = Generator.specialty
        keys = []
        values = []
        for mark in all_marks:
            keys.append(specialities.index(mark.get('specialty')))
            values.append(mark.get('mark'))
        plt.title('Кореляція балів з предмету ' + subject + ' за різними спеціальностями: '
                  + str(Analyzer.correlation_coef(keys, values))
                  + '\nза період з ' + str(date1) + ' по ' + str(date2),
                  fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.scatter(keys, values)
        plt.xticks(np.arange(len(specialities)), specialities, rotation=90, fontsize=8)
        plt.yticks(np.arange(1, 12), fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.ylabel('Бал', fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.show()

    def regression_mark_for_subject_and_grade_graph(self, db, date1, date2, subject):
        all_marks = list(db.get_by_subject_and_dates(subject, date1, date2))
        keys = []
        values = []
        for mark in all_marks:
            keys.append(mark.get('grade'))
            values.append(mark.get('mark'))
        plt.title('Регресія балів з предмету ' + subject + ' у різних класах\nsза період з '
                  + str(date1) + ' по ' + str(date2), fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.scatter(keys, values)
        x = np.array(keys)
        y = np.array(values)
        k, b = np.polyfit(x, y, 1)
        plt.plot(x, k * x + b)
        plt.xticks(np.arange(1, 11), rotation=90, fontsize=8)
        plt.yticks(np.arange(1, 12), fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.ylabel('Бал', fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.xlabel('Клас', fontsize=self.PLOT_LABEL_FONT_SIZE)
        plt.show()
