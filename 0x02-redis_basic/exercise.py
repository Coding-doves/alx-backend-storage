#!/usr/bin/env python
''' Create a Cache class '''
import redis
from typing import Union
import uuid


class Cache():
    ''' comment '''
    def __init__(self):
        '''initializing '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)


    def store(self,
              data: Union[str, bytes, int, float]
              ) -> str:
        ''' 
        generate a random key 
        (e.g. using uuid)
        '''
        stored_key = str(uuid.uuid4())
        self._redis.set(stored_key, data)
        return stored_key


    def get(self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        '''comment'''
        self._redis.get(key)
        if fn is not None:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        '''
        correct conversion function
        '''

    def get_int(self,):
        '''
        correct conversion function
        '''
