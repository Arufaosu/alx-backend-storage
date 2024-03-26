#!/usr/bin/env python3
"""12-log_stats.py"""

if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(nginx.count_documents({}), 'logs')

    print('Methods:')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:
        method_count = nginx.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, method_count))

    status_check_count = nginx.count_documents({'method': 'GET',
                                                'path': '/status'})
    print('{} status check'.format(status_check_count))
