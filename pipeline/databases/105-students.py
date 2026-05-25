#!/usr/bin/env python3
"""return students sorted by average score"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """function returning all students"""
    top = list(mongo_collection.find())
    student_list = []
    for student in top:
        #  print(f"student: {student}")
        avg_score = 0
        total_score = 0
        student_topics = student['topics']
        #  print(f"student_topics: {student_topics}")
        i = 0  # counting records
        for rec in student_topics:  # iterate to become total score
            i += 1
            #  print(f"rec : {rec}")
            score = rec['score']
            #  print(f"score : {score}")
            total_score += rec['score']
        #  print(f"total_score: {total_score}")
        avg_score = total_score / i
        #  print(f"average_score: {avg_score}")
        student['averageScore'] = avg_score
        student_list.append(student)
    return sorted(student_list, key=lambda x: x['averageScore'], reverse=True)
