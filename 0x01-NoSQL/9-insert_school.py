#!/usr/bin/env python3
'''  inserts a new document in a collection based on kwargs: '''


def insert_school(mongo_collection, **kwargs):
    ''' comment '''
    store = mongo_collection.insert_one(kwargs)
    return store.inserted_id
