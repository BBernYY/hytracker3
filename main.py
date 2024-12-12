from requests import get
from time import sleep
from copy import copy


class Request:
    def __init__(self, url, **kwargs):
        self.url = url
        self.kwargs = kwargs
    def call(self):
        return get(self.url, **self.kwargs)
    def wait_for_update(self, first_value, delay=1, comparison=lambda x, y: x == y):
        if first_value is not None:
            t0 = first_value.json()
        else:
            t0 = None
        r = self.call()
        t1 = r.json()
        while comparison(t0, t1):
            sleep(delay)
            r = self.call()
            t0 = copy(t1)
            t1 = r.json()
        return r





