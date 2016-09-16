import abc


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
    def __init__(self):
        super(NYCPizzaStore, self).__init__()
        self.ingredient_factory = NYPizzaIngredientFactory

    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            pizza = CheesePizza(self.ingredient_factory)
            pizza.name = "NY Style Pizza"
            return pizza
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


class Pizza(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._type = ''
        self._name = str()
        self.dough = Dough()
        self.sauce = Sauce()
        self.veggies = Veggies()
        self.cheese = Cheese()
        self.clams = Clam()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, pizza_type):
        self._type = pizza_type

    @abc.abstractmethod
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


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        super(CheesePizza, self).__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing {}".format(self.name))
        self.dough = self.ingredient_factory.create_dough(self.ingredient_factory())
        self.sauce = self.ingredient_factory.create_sauce(self.ingredient_factory())
        self.cheese = self.ingredient_factory.create_cheese(self.ingredient_factory())


class PizzaIngredientFactory(object):
    def create_dough(self):
        pass

    def create_cheese(self):
        pass

    def create_sauce(self):
        pass

    def create_veggies(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        pass


class NYPizzaIngredientFactory(object):
    def create_dough(self):
        return ThinCrustDough()

    def create_cheese(self):
        return ReggianoCheese()

    def create_sauce(self):
        return MarinaraSauce()

    def create_veggies(self):
        veggie_list = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggie_list

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class Dough(object):
    def __call__(self):
        return "Plain Dough"


class ThinCrustDough(Dough):
    def __call__(self):
        return "Thin Crust Dough"


class Cheese(object):
    def __call__(self):
        return "Plain Cheese"


class ReggianoCheese(Cheese):
    def __call__(self):
        return "Reggiano Cheese"


class Sauce(object):
    def __call__(self):
        return "Plain Sauce"


class MarinaraSauce(Sauce):
    def __call__(self):
        return "Marinara sauce"



class Veggie(object):
    def __call_(self):
        return "Avocado"


class Veggies(object):
    def __call__(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

class Garlic(Veggie):
    def __call_(self):
        return "Garlic"


class Onion(Veggie):
    def __call_(self):
        return "Onion"


class Mushroom(Veggie):
    def __call_(self):
        return "Mushroom"


class RedPepper(Veggie):
    def __call_(self):
        return "Red Pepper"


class Garlic(Veggie):
    def __call_(self):
        return "Stank breath"


class Clam(object):
    def __call__(self):
        return "Normal Clam"


class FreshClams(Clam):
    def __call__(self):
        return "Fresh Clams"


if __name__ == "__main__":
    ginos_pizza_shop = NYCPizzaStore()
    ginos_sample = ginos_pizza_shop.order_pizza("cheese")
    print(ginos_sample.name)
    print("#" * 15)
