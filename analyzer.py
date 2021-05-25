import numpy as np


class Analyzer:

    @staticmethod
    def average_mark(marks):
        count = 0
        _sum = 0
        for mark in marks:
            count += 1
            _sum += mark.get('mark')
        if count == 0:
            return 0
        return round(_sum / count)

    @staticmethod
    def correlation_coef(x, y):
        r = np.corrcoef(x, y)
        return r[0, 1]

    @staticmethod
    def correlation_coef_marks_and_grades(marks):
        x = []
        y = []
        for mark in marks:
            x.append(mark.get('grade'))
            y.append(mark.get('mark'))
        return Analyzer.correlation_coef(x, y)

