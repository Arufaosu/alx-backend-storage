#!/usr/bin/env python3
"""12-log_stats.py"""
from pymongo import MongoClient

def nginx_logs_stats():
    """script that provides some stats about Nginx logs"""
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    status_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_logs_stats()
