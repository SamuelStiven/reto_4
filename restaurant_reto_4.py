class Restaurant:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self._phone = phone

class Order:
    def __init__(self):
        self.items = []
        self.discount_rules = [self.quantity_discount, self.Entrees_discount, self.drinks_discount]
    
    def add_item(self, item: 'MenuItem', quantity: int):
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        self.items.append((item, quantity))
    
    def quantity_discount(self, current_total: float):
        
        discount = 0.0
        for item, qty in self.items:
            if qty >= 3:
                discount += item.price * qty * 0.10
        return current_total - discount
    
    def Entrees_discount(self, current_total: float):
        has_entree = any(isinstance(item, Entrees) for item, quantity in self.items)
        if has_entree:
            return current_total * 0.90
        return current_total
    
    def drinks_discount(self, current_total: float):
        has_drink = any(isinstance(item, Drinks) for item, quantity in self.items)
        if has_drink:
            return current_total * 0.95
        return current_total
    
    def total_cost(self, discount_rules: list = None):
        subtotal = sum(item.total_price(quantity) for item, quantity in self.items)
        total = subtotal 
        rules = discount_rules if discount_rules is not None else self.discount_rules
        total = subtotal 
        for rule in rules:
            total = rule(total)
        return total



class MenuItem:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.__price = price
        self.description = description
        
    @property
    def price(self):
        return self.__price
    
    def total_price(self, quantity: float):
        return self.__price * quantity
    
    
class Entrees(MenuItem):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.category = "Entree"
    
    
class BeefPatacones(Entrees):
    def __init__(self):
        super().__init__("Beef Patacones", 12.000, "Fried plantain slices topped with seasoned beef, cheese, and a drizzle of sour cream.")

class CreolePotatoes(Entrees):
    def __init__(self):
        super().__init__("Creole Potatoes", 9.990, "Roasted potatoes with a blend of creole spices, served with a side of garlic aioli.")

class ChessFingers(Entrees):
    def __init__(self):
        super().__init__("Chess Fingers", 8.990, "Crispy breaded cheese sticks served with marinara sauce for dipping.")
 
class MainCourses(MenuItem):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.category = "Main Course"

class Barbacue(MainCourses):
    def __init__(self):
        super().__init__("Barbacue", 24.990, "Grilled barbacue ribs served with coleslaw and fries.")


class RoastSteak(MainCourses):
    def __init__(self):
        super().__init__("Roast Steak", 22.990, "Juicy roast steak cooked to perfection, served with mashed potatoes and steamed vegetables.")


class ChickenBreast(MainCourses):
    def __init__(self):
        super().__init__("Chicken Breast", 18.990, "Grilled chicken breast served with quinoa salad and a lemon vinaigrette.")


class Drinks(MenuItem):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.category = "Drink"

class Juice(Drinks):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.category = "Juice"

class OrangeJuice(Juice):
    def __init__(self):
        super().__init__("Orange Juice", 4.990, "Freshly squeezed orange juice.")

class LuloJuice(Juice):
    def __init__(self):
        super().__init__("Lulo Juice", 5.490, "Refreshing lulo juice made from ripe lulo fruit.")


class BlackBerryJuice(Juice):
    def __init__(self):
        super().__init__("Blackberry Juice", 5.990, "Delicious blackberry juice made from fresh blackberries.")
    
class Soda(Drinks):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.category = "Soda"

class CocaCola(Soda):
    def __init__(self):
        super().__init__("Coca-Cola", 3.990, "Classic Coca-Cola soda.")

class Postobon(Soda):
    def __init__(self):
        super().__init__("Postobon", 3.990, "Popular Colombian soda with a unique flavor.")
        
class Desserts(MenuItem):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.category = "Dessert"

class TresLeches(Desserts):
    def __init__(self):
        super().__init__("Tres Leches", 6.990, "Classic tres leches cake soaked in three types of milk, topped with whipped cream and fresh fruit.")


class Brownie(Desserts):
    def __init__(self):
        super().__init__("Brownie", 5.990, "Warm chocolate brownie served with vanilla ice cream and chocolate sauce.")

  
class Flan(Desserts):
    def __init__(self):
        super().__init__("Flan", 4.990, "Creamy caramel flan topped with whipped cream.")

if __name__ == "__main__":
    restaurant = Restaurant("Los Patrones", "Chapinero Central, calle 78", "789023324")
    
    order = Order()
    order.add_item(BeefPatacones(), 2)
    order.add_item(CreolePotatoes(), 1)
    order.add_item(ChessFingers(), 3)
    order.add_item(Barbacue(), 1)
    order.add_item(OrangeJuice(), 2)
    order.add_item(TresLeches(), 1)
    
    total = order.total_cost()
    print(f"Total cost of the order: {total}")
