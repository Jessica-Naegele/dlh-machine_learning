#!/usr/bin/env python3
from pymongo import MongoClient

if __name__ == "__main__":
    # 1. Connect to your local database
    client = MongoClient('mongodb://127.0.0.1:27017')
    test_collection = client.logs.nginx

    # 2. Clear out any previous junk test data
    test_collection.delete_many({})

    # 3. Create a tiny mock layout of logs to test your logic!
    mock_logs = [
        {"ip": "1.1.1.1", "method": "GET", "path": "/status"},
        {"ip": "1.1.1.1", "method": "GET", "path": "/home"},
        {"ip": "2.2.2.2", "method": "POST", "path": "/login"},
        {"ip": "1.1.1.1", "method": "GET", "path": "/status"},
        {"ip": "3.3.3.3", "method": "DELETE", "path": "/data"},
    ]
    
    # 4. Insert them into your local test collection
    test_collection.insert_many(mock_logs)

    # 5. Now fire your function! It will run against your fake logs.
    log_stats()