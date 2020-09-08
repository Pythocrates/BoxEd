''' This module contains the main base class.
'''

from contextlib import contextmanager


class BoxEd:
    @contextmanager
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        yield None
