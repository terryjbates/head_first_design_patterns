import abc


class Pizza(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._type = ''
        self._name = str()
        self.dough = str()
        self.sauce = str()
        self.toppings = list()

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, pizza_type):
        self._type = pizza_type

    def prepare(self):
        print("Preparing {}".format(self.name))
        print("Tossing dough....")
        print("Adding sauce...")
        print("Adding toppings: ")
        print("{}".format([topping for topping in self.toppings]))

    def bake(self):
        print("Bake for 25 minutes at 350 degrees")

    def cut(self):
        print("Cutting Pizza into diagonal slices")

    def box(self):
        print("Place pizza in offical PizzaStore box")


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self._name = "NY Style Sauce and Cheese Pizza"
        self.toppings.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super(ChicagoStyleCheesePizza, self).__init__()
        self.dough = "Extra Thick Crust"
        self.sauce = "Plum Tomato Sauce"
        self._name = "Chicago Style Deep Dish Cheese Pizza"
        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting into square slices")


class PizzaStore(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.box()
        return pizza

    @abc.abstractmethod
    def create_pizza(self, type):
        raise NotImplementedError


class NYCPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return NYCPepperoniPizza()
        return None


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        return None


if __name__ == "__main__":
    ginos_pizza_shop = NYCPizzaStore()
    ginos_sample = ginos_pizza_shop.order_pizza("cheese")
    print(ginos_sample.name)
    print("#" * 15)
    tonys_pizza_shop = ChicagoPizzaStore()
    tonys_sample = tonys_pizza_shop.order_pizza("cheese")
    print(tonys_sample.name)