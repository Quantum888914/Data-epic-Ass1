# Task 1: Identify and print the type of different values using type()
print(type(10))
print(type(10.5))   
print(type("Hello")) 
print(type(True))    
print(type([1, 2, 3]))

# Task 2: Perform basic arithmetic operations using int and float
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Task 3: Convert between different numeric types using int() and float()
num = 5.7
print("Float to Int:", int(num))
num2 = 10
print("Int to Float:", float(num2))

# Task 4: Use string methods to manipulate text
text = "  Python Programming  "
print(text.strip())      
print(text.lower())      
print(text.upper())       
print(text.replace("Python", "Java"))

# Task 5: Format strings in different ways
name = "Rasheed"
age = 20
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# Task 6: Create a list, access elements using indexing and slicing, and perform list operations
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0]) 
print("Last two elements:", numbers[-2:]) 

numbers.append(60)  
numbers.remove(30)   
popped = numbers.pop()  
numbers.sort()       
numbers.reverse()  
print("Modified list:", numbers)

# Task 7: Create a tuple, access elements, and demonstrate tuple immutability
my_tuple = (1, 2, 3, 4, 5)
print("First element of tuple:", my_tuple[0])
# my_tuple[0] = 10  # Uncommenting this line will raise an error because tuples are immutable
