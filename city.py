class City:
   def __init__(self, name, city, citizens):
         self.name = name
         self.country = city
         self.citizens = citizens

   def data_input(self):
       print(f"Name of the city: {self.name}")
       print((f"Name of the country: {self.country}"))
       print((f"Number of citizens: {self.citizens}"))

c1 = City(input(""), input(""), input(""))

c1.data_input()