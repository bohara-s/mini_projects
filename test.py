# class person :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")
# class student(person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id


# obj = student("John", 20, "S12345")
# obj.display()


# def person():
#     print("person class")

# person()    

# def student():
#     print("student class")
# student()



# class Bankaccount:
#     def __init__(self,owner , blance =  0):
#         self.owner  = owner
#         self.blance = blance

#     def deposit(self, amount):
#         if amount > 0:
#             self. balane += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Invalid deposit amount")

# a ={}

# def c(name,phone):
#     name=input("enter the name of the contact  ")
#     phone = input("enter the phone number  ")

#     a[name] = phone
#     print(a)


# def view_contacts():
#     for name,phone in a.items():
#         print(f"Name: {name}, Phone: {phone}")

# c(name="name", phone="phone")
# view_contacts()


# A simple dictionary
fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}


for a,b in fruits.items():
    print(f"fruit: {a}, color: {b}")