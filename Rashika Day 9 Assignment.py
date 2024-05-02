#1. Write a Python method in Oop called "calculate_area" that takes the radius of a circle as input and returns the area of the circle, write program using Oop.


class Circle:
    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return 3.14 * self.radius ** 2


radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
area = circle.calculate_area()
print("The area of the circle is:", area)




#2.  Write a Python method in Oop called "calculate_discount" that calculates the final price of an item after applying a discount percentage. The function should take the original price and the discount percentage as inputs.


class Item:
    def __init__(self, original_price):
        self.original_price = original_price


    def calculate_discount(self, discount_percentage):
        discount_amount = self.original_price * (discount_percentage / 100)
        final_price = self.original_price - discount_amount
        return final_price


original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
item = Item(original_price)
final_price = item.calculate_discount(discount_percentage)
print("The final price after discount is:", final_price)


 
 #3. Write a method in Oop named "count_vowels" that takes a string as input and returns the count of vowels (both uppercase and lowercase) in the string


class VowelCounter:
    def __init__(self, string):
        self.string = string


    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in self.string:
            if char in vowels:
                count += 1
        return count


input_string = input("Enter a string: ")
counter = VowelCounter(input_string)
vowel_count = counter.count_vowels()
print("The number of vowels in the string is:", vowel_count)







