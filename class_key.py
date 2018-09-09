import functools

def class_key(key='__key__'):
    def wrapper(cls):
        nonlocal key

        if not callable(key):
            key_str = str(key)
            key = lambda self: getattr(self, key_str)

        def lt(self, other):
            return key(self) < key(other)

        def le(self, other):
            return key(self) <= key(other)

        def eq(self, other):
            return key(self) == key(other)

        def ne(self, other):
            return key(self) != key(other)

        def gt(self, other):
            return key(self) > key(other)

        def ge(self, other):
            return key(self) >= key(other)

        def hash_(self):
            return hash(key(self))

        methods_map = {
            '__lt__': lt,
            '__le__': le,
            '__eq__': eq,
            '__ne__': ne,
            '__gt__': gt,
            '__ge__': ge,
            '__hash__': hash_
        }
        for method_name, method in methods_map.items():
            if getattr(cls, method_name, None) is getattr(object, method_name, None):
                method.__name__ = method_name
                setattr(cls, method_name, method)
        return cls

    return wrapper
