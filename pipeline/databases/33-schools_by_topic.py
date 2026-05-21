#!/usr/bin/env python3
"""Create a function to list all schools for a specific topic"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns a list of schools having a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
