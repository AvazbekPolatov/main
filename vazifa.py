# 1-masala
# class MyValueError(Exception):
#     def __init__(self, message="Qiymat noto'g'ri. Age musbat butun son bo'lishi kerak."):
#         self.message = message
#         super().__init__(self.message)


# class Age:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         if isinstance(value, int) and value > 0:
#             instance.__dict__[self.name] = value
#         else:
#             raise MyValueError("Age musbat butun son bo'lishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class User:
#     age = Age()

#     def __init__(self, age):
#         self.age = age



# user = User(25)
# print(f"User age: {user.age}")
# user.age = 30
# print(f"Updated age: {user.age}")
# user.age = -5


# 2-masala
# class MyInvalidPhoneNumberError(Exception):
#     def __init__(self, message="Telefon raqami noto'g'ri formatda."):
#         self.message = message
#         super().__init__(self.message)


# class PhoneNumber:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         if isinstance(value, str) and value.isdigit() and len(value) in (9, 12):
#             instance.__dict__[self.name] = value
#         else:
#             raise MyInvalidPhoneNumberError("Telefon raqami faqat raqamlardan iborat bo'lib, uzunligi 9 yoki 12 ta bo'lishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class User:
#     phone_number = PhoneNumber()

#     def __init__(self, phone_number):
#         self.phone_number = phone_number



# user = User("998901234567")
# print(f"User phone number: {user.phone_number}")
# user.phone_number = "12a3456789"



# 3-masala
# import re

# class MyWeakPasswordError(Exception):
#     def __init__(self, message="Parol juda zaif."):
#         self.message = message
#         super().__init__(self.message)


# class Password:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         if (isinstance(value, str) and len(value) >= 8 and
#             any(char.isupper() for char in value) and
#             re.search(r"[!@#$%^&*(),.?\":{}|<>]", value)):
#             instance.__dict__[self.name] = value
#         else:
#             raise MyWeakPasswordError("Parol uzunligi kamida 8 ta belgidan iborat bo'lishi, kamida bitta katta harf va bitta maxsus belgi bo'lishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class User:
#     password = Password()

#     def __init__(self, password):
#         self.password = password



# user = User("Ozod123@#")
# print(f"User password: {user.password}")
# user.password = "Avazbek123"


# 4-masala
# class MyInvalidEmailError(Exception):
#     def __init__(self, message="Email manzili noto'g'ri formatda."):
#         self.message = message
#         super().__init__(self.message)


# class Email:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         if isinstance(value, str) and "@" in value and "." in value.split("@")[-1]:
#             instance.__dict__[self.name] = value
#         else:
#             raise MyInvalidEmailError("Email manzilida @ va . belgilar mavjud bo'lishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class User:
#     email = Email()

#     def __init__(self, email):
#         self.email = email



# user = User("avazbek@gmail.com")
# print(f"User email: {user.email}")
# user.email = "ozodbek@.test"


# # 5-masala
# from datetime import datetime

# class MyUnderageError(Exception):
#     def __init__(self, message="Foydalanuvchi 16 yoshdan kichik bo'lishi mumkin emas."):
#         self.message = message
#         super().__init__(self.message)


# class EmploymentYears:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         current_year = datetime.now().year
#         if isinstance(value, int) and current_year - value >= 16:
#             instance.__dict__[self.name] = value
#         else:
#             raise MyUnderageError("Foydalanuvchining tug'ilgan yili shunday bo'lishi kerakki, yoshi kamida 16 bo'lsin.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class User:
#     employment_years = EmploymentYears()

#     def __init__(self, employment_years):
#         self.employment_years = employment_years



# user = User(2000)
# print(f"Employment years: {user.employment_years}")
# user.employment_years = 2022

# 6-masala
# class MyNegativePriceError(Exception):
#     def __init__(self, message="Narx manfiy bo'lishi mumkin emas."):
#         self.message = message
#         super().__init__(self.message)


# class Price:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         if isinstance(value, (int, float)) and value >= 0:
#             instance.__dict__[self.name] = value
#         else:
#             raise MyNegativePriceError("Narx musbat yoki 0 bo'lishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class Product:
#     price = Price()

#     def __init__(self, price):
#         self.price = price


# product = Product(100.50)
# print(f"Product price: {product.price}")
# product.price = -20

# 7-masala
# class MyInvalidGradeError(Exception):
#     def __init__(self, message="Bosqich faqat 1 dan 12 gacha bo'lishi kerak."):
#         self.message = message
#         super().__init__(self.message)


# class Grade:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         if isinstance(value, int) and 1 <= value <= 12:
#             instance.__dict__[self.name] = value
#         else:
#             raise MyInvalidGradeError("Bosqich faqat 1 dan 12 gacha bo'lishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class Student:
#     grade = Grade()

#     def __init__(self, grade):
#         self.grade = grade



# student = Student(5)
# print(f"Student grade: {student.grade}")
# student.grade = 13

# 8-masala
# import re

# class MyInvalidDateError(Exception):
#     def __init__(self, message="Sana noto'g'ri formatda. YYYY-MM-DD formatida bo'lishi kerak."):
#         self.message = message
#         super().__init__(self.message)


# class Date:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value):
#         if isinstance(value, str) and re.match(r"\d{4}-\d{2}-\d{2}", value):
#             instance.__dict__[self.name] = value
#         else:
#             raise MyInvalidDateError("Sana faqat YYYY-MM-DD formatida kiritilishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class Event:
#     date = Date()

#     def __init__(self, date):
#         self.date = date



# event = Event("2024-11-29")
# print(f"Event date: {event.date}")
# event.date = "29-11-2024"

# 9-masala

