#!/usr/bin/env python3
"""10-update_topics.py"""

def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    mongo_collection.update_many(filter_query, update_query)
