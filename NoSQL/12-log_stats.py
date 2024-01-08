#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


def log_stats():
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Counting total logs
    total_logs = collection.count_documents({})

    # Counting methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method})
                     for method in methods}

    # Counting status check
    status_check = collection.count_documents({"method": "GET",
                                               "path": "/status"})

    # Displaying stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
