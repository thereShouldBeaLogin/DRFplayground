

class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def gether_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gether_attrs())


if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()      # Make two instances
    print(X)                         # Show all instance attrs
    print(Y)                         # Show lowest class name


class ListInstance:

    def __str__(self):

        return '<Instanse of %s, address %s:\n%s>' % (
            self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):

        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


class ListTree:

    def __str__(self):

        self.__visited = {}
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__, id(self), self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):

        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}Class {1}:, address {2}: (see above)>\n'.format(
                dots, aClass.__name__, id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent +4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots, aClass.__name__, id(aClass), self.__attrnames(aClass, indent),
                ''.join(genabove), dots)

    def __attrnames(self, obj, indent):

        spaces = ' ' * (indent +4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


def factory(aClass, *args, **kwargs):

    return aClass(*args, **kwargs)


class MyList(list):

    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset -1)


class Set(list):

    def __init__(self, value = []):
        list.__init__([])
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + list.__repr__(self)


class traser:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)


def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall


def decorator(cls):

    class Proxy:

        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    return Proxy


class FormatError(Exception):

    logfile = 'logfile.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at: ', self.file, self.line, file=log)
