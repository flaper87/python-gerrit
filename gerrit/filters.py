class Items(list):
    key = None

    def add_items(self, key, value):

        if not isinstance(value, (list, tuple)):
            value = [str(value)]

        self.extend(["%s:%s" % (key, val) for val in value])
        return self

    def __repr__(self):
        subs_repr = [str(i) for i in self]

        base = '(%s)'
        key = self.key

        if not key:
            key, base = ' ', '%s'

        return base % key.join(subs_repr)


class OrFilter(Items):
    key = ' OR '


class AndFilter(Items):
    key = ' AND '
