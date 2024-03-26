#!/usr/bin/env python3
"""11-schools_by_topic.py"""

def schools_by_topic(mongo_collection, topic):
    """returns the list of school"""
    result = mongo_collection.find({'topic': topic})
    
    return list(result)
