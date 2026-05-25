#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def log_stats():
    """Connects to MongoDB logs database and prints structural stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Total logs count
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Methods stats block
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Specific status check query (method=GET, path=/status)
    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_checks} status check")

    # 4. Print IPs
    print("IPs:")

    # 5. Aggregate IPs
    pipeline = [
        # Stage 1: Group and count
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},

        # Stage 2: Independent dictionary, quotes added, sorting by count
        {"$sort": {"count": -1}},

        # Stage 3: Independent dictionary, quotes added
        {"$limit": 10}
    ]

    ip_count = nginx_collection.aggregate(pipeline)

    for item in ip_count:
        print(f"\t{item.get('_id')}: {item.get('count')}")


if __name__ == "__main__":
    log_stats()
