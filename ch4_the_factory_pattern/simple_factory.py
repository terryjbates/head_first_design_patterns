import abc


class Pizza(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._type = ''

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, pizza_type):
        self._type = pizza_type


class CheesePizza(Pizza):
    def __init__(self):
        super(CheesePizza, self).__init__()
        self.type = "Cheese"


class PepperoniPizza(Pizza):
    def __init__(self):
        super(PepperoniPizza, self).__init__()
        self.type = "Pepperoni"


class SimplePizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()
        return pizza


class PizzaStore(object):
    def __init__(self, factory_type=SimplePizzaFactory):
        self.factory = factory_type

    def order_pizza(self, pizza_type):
        pizza = self.factory.create_pizza(pizza_type)
        # pizza.prepare()
        # pizza.bake()
        # pizza.box()
        return pizza


if __name__ == "__main__":
    new_store = PizzaStore()
    new_pizza = new_store.order_pizza("pepperoni")
    print(new_pizza.type)

    cheese_pizza = new_store.order_pizza("cheese")
    print(cheese_pizza.type)