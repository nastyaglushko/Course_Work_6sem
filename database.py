from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime


class Database:
    def __init__(self):
        # self.client = MongoClient('localhost', 27017)
        self.client = MongoClient('localhost', 27100)
        self.db = self.client['marks_db']
        self.collection = self.db['marks']

    def insert(self, marks):
        self.collection.insert_one({'subject': marks.subject, 'student_name': marks.student_name, 'mark': marks.mark,
                                    'max_mark': marks.max_mark, 'grade': marks.grade, 'specialty': marks.specialty,
                                    'date': marks.date})

    def insert_list(self, marks_list):
        for mark in marks_list:
            self.insert(mark)

    def get_all(self):
        return self.collection.find()

    def get_by_grade(self, grade):
        return self.collection.find({'grade': grade})

    def get_by_dates(self, date1, date2):
        return self.collection.find({'date': {'$gte': datetime.datetime.strptime(date1, '%Y-%m-%d'),
                                              '$lt': datetime.datetime.strptime(date2, '%Y-%m-%d')}})

    def get_by_subject(self, subject):
        return self.collection.find({'subject': subject})

    def get_by_id(self, _id):
        return self.collection.find({'_id': ObjectId(_id)})

    def delete(self, _id):
        return self.collection.delete_one({'_id': ObjectId(_id)})

    def delete_all(self):
        return self.collection.delete_many({})

    def get_by_subject_and_dates(self, subject, date1, date2):
        return self.collection.find({'subject': subject,
                                     'date': {'$gte': datetime.datetime.strptime(date1, '%Y-%m-%d'),
                                              '$lt': datetime.datetime.strptime(date2, '%Y-%m-%d')}})

    def get_by_grade_and_dates(self, grade, date1, date2):
        return self.collection.find({'grade': grade,
                                     'date': {'$gte': datetime.datetime.strptime(date1, '%Y-%m-%d'),
                                              '$lt': datetime.datetime.strptime(date2, '%Y-%m-%d')}})

    def get_by_specialty_and_dates(self, specialty, date1, date2):
        return self.collection.find({'specialty': specialty,
                                     'date': {'$gte': datetime.datetime.strptime(date1, '%Y-%m-%d'),
                                              '$lt': datetime.datetime.strptime(date2, '%Y-%m-%d')}})

    def get_by_subject_and_specialty(self, subject, specialty):
        return self.collection.find({'subject': subject,
                                     'specialty': specialty})

    def get_by_subject_and_grade(self, subject, grade):
        return self.collection.find({'subject': subject,
                                     'grade': grade})

    def get_unique_subjects(self):
        mark_list = self.collection.find()
        subjects_list = list()
        for mark in mark_list:
            if subjects_list.count(mark.get('subject')) == 0:
                subjects_list.append(mark.get('subject'))
        return subjects_list
