from games.classmethods.class_employees import PizzaRobot, Server, Processor


class Customer:

    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for item too', server)


class Oven:

    def bake(self):
        print('oven bakes')


class PizzaShop:

    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


class Uppercase(Processor):

    def converter(self, data):
        return data.upper()


if __name__ == "__main__":
    # make the composite
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
