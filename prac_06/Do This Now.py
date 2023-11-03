# 1.
# products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
# on_sale_products = [product for product in products if product[2]]
# print(on_sale_products)

# 2.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"{self.name} ({self.age})"
#
#
# p1 = Person("Jane", 19)
# print(p1)
# people = [Person("Alexa", 21), Person("Siri", 25), Person("James", 20)]
# print(people)

# 3.
# monsters = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]
# monsters_with_16_teeth = [monster[0] for monster in monsters if monster[1] > 16]
# print(monsters_with_16_teeth)

# 4.
# class Monster:
#     def __init__(self, name, number_of_teeth, colour, is_scary):
#         self.name = name
#         self.number_of_teeth = number_of_teeth
#         self.colour = colour
#         self.is_scary = is_scary
#
#     def __repr__(self):
#         return f"{self.name} {self.number_of_teeth} {self.colour} {self.is_scary}"
#
#     def is_scary(self, is_scary):
#         if self.number_of_teeth > 16 or self.colour == "red":
#             is_scary = "Scary"
#         else:
#             is_scary = "Not Scary"
#         return is_scary


# monsters = [Monster("Mike", 0, "Red", {is_scary}), Monster("Sully", 1, "Blue"), Monster("James", 2, "Green")]
# print(monsters)
#

# class Monster:
#     """Represent a monster."""
#
#     def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
#         """Construct a monster object."""
#         self.name = name
#         self.number_of_teeth = number_of_teeth
#         self.colour = colour
#
#     def __repr__(self):
#         return f"{vars(self)}"
#
#     def is_scary(self):
#         """Determine if monster is scary based on teeth and colour."""
#         return self.number_of_teeth > 16 or self.colour == "red"
#
#
# def return_scary_monsters():
#     monsters = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]
#     monsters_with_16_teeth = [monster[0] for monster in monsters if monster.number_of_teeth > 16]
#     print(monsters_with_16_teeth)
#
#
# def run_test():
#     """Test the Monster class."""
#     # Test default values
#     # m1 = Monster()
#     # print(m1)
# assert m1.name == "Mike"
# assert not m1.is_scary()
# m2 = Monster("Larry", 17, "Orange")
# print(m2)
# print(m2.is_scary())
# assert m2.is_scary()
# m2.number_of_teeth //= 2
# print(m2.is_scary())
# print(m1.return_scary_monsters())


# run_test()


# 4.
# class Plant:
#     def __init__(self, name="", height=0.0, growth_rate=0.1):
#         self.name = name
#         self.height = height
#         self.growth_rate = growth_rate
#
#     def feed(self, water):
#         self.height += water * self.growth_rate
