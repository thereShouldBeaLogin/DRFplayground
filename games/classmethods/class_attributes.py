

class Name:
    """
    example of descriptor
    """
    def __get__(self, instance, owner):
        print('fetch name: ')
        return instance._name

    def __set__(*args):
        raise AttributeError('Is not permitted to set')

    def __delete__(self, instance):
        print('remove ')
        del instance._name


class Person:

    def __init__(self, name):
        self._name = name

    name = Name()


class Profile:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # setter can dynamically check conditions
        self._name = value + ' krosaucheg'

    @name.deleter
    def name(self):
        # before deletion of profile model
        # we could check child\parent relations
        # and make cases for both variants
        del self._name


class DescState:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescrState get')
        return self.value * 10

    def __set__(self, instance, value):
        print('DescrState set')
        self.value = value


# client Class
class CalcAttrs:

    X = DescState(2)
    Y = 3

    def __init__(self):
        self.Z = 4


class InstState:

    def __get__(self, instance, owner):
        print('Instance get')
        return instance._X * 10

    def __set__(self, instance, value):
        print('Instance set')
        instance._X = value


class NextCalc:

    X = InstState()
    Y = 3

    def __init__(self):
        self._X = 2
        self.Z = 4


class DescBoth:

    def __init__(self, data):
        self.data = data

    def __get__(self, instance, owner):
        return '%s, %s' % (self.data, instance.data)

    def __set__(self, instance, value):
        instance.data = value


class Client:

    def __init__(self, data):
        self.data = data

    managed = DescBoth('spam')

