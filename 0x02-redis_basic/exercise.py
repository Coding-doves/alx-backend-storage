#!/usr/bin/env python
''' Create a Cache class '''
import redis
from typing import Union, Any, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
    count how many times methods
    of the Cache class are called.
    '''
    @wraps(method)
    def increments_count(self, *args, **kwargs) -> Any:
        ''' increments the count'''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)

        return method(self, *args, **kwargs)

    return increments_count


def call_history(method: Callable) -> Callable:
    '''comment '''
    @wraps(method)
    def increments_count(self, *args, **kwargs) -> Any:
        ''' increments the count'''

        inpt = "{}:inputs".format(method.__qualname__)
        outpt = "{}:outputs".format(method.__qualname__)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(inpt, str(args))

        got = method(self, *args, **kwargs)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(outpt, got)

        return got

    return increments_count


class Cache():
    ''' comment '''
    def __init__(self):
        '''initializing '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
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
        return self.get(key, fn=lambda x: x.decode('uft-8'))

    def get_int(self, key: str) -> int:
        '''
        correct conversion function
        '''
        return self.get(key, fn=lambda x: int(x))
