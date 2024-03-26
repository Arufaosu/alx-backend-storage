#!/usr/bin/env python3
"""9-insert_school.py"""

def insert_school(mongo_collection, **kwargs):
    """ inserts a document into a MongoDB collection"""
    new_document_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_document_id
