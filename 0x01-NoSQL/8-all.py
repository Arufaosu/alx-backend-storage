#!/usr/bin/env python3
"""Write a Python function that lists all documents"""

def list_all(mongo_collection):
    """will return a list of all documents"""
    all_documents = []
    for document in mongo_collection.find({}):
        all_documents.append(document)
    return all_documents
