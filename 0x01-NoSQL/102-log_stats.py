#!/usr/bin/env python3
"""102-log_stats.py"""
from pymongo import MongoClient

def get_logs_count(collection):
    return collection.count_documents({})

def count_methods(collection):
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]
    methods = list(collection.aggregate(pipeline))
    return methods

def top_10_ips(collection):
    """Improve 12-log_stats.py"""
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    
    logs_count = get_logs_count(nginx_collection)
    print(f"{logs_count} logs")

    # Count the occurrence of each method
    methods = count_methods(nginx_collection)
    print("Methods:")
    for method in methods:
        print(f"    method {method['_id']}: {method['count']}")

    # Get the top 10 most present IPs
    top_ips = top_10_ips(nginx_collection)
    print("IPs:")
    for ip_data in top_ips:
        print(f"    {ip_data['_id']}: {ip_data['count']}")
