#!/usr/bin/env python3
''' returns the list of school having a specific topic '''


def schools_by_topic(mongo_collection, topic):
    ''' comment '''
    query = mongo_collection.find({"topic": topic})

    return [lit for school in query]
