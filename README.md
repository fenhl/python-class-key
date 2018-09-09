This Python 3 module provides the `class_key` function, which returns a class decorator that implements comparison methods and `__hash__` using a given key.

# Example

Create a class for calendar events with start and end times. Comparison of events should use start time, then end time, then event name. This example works because the default attribute used as a key is `__key__`.

```python
import class_key
import datetime

@class_key.class_key()
class Event:
    def __init__(self, name, start, end=None):
        self.name = name
        self.start = start
        if end is None:
            self.end = start + datetime.timedelta(hours=1)
        else:
            self.end = end

    @property
    def __key__(self):
        return self.start, self.end, self.name

events = [
    Event('test now', datetime.datetime.utcnow()),
    Event('test past', datetime.datetime.utcnow() - datetime.timedelta(hours=3)),
    Event('test future', datetime.datetime.utcnow() + datetime.timedelta(hours=7))
]
assert sorted(events) == [events[1], events[0], events[2]]
```
