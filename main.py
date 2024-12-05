# # descriptors

# class Person:
#     def __init__(self, ism,familiya):
#         self.ism = ism
#         self.familiya = familiya
        
#     @property
#     def fullname(self):
#         return f"{self.ism} {self.familiya}"
#     @ism.setter
#     def ism(self,new_ism):
#         if type (new_ism) is str:
#             self._ism = new_ism
#         else:
#             raise ValueError("harf kiriting")
        
#     @ism.deleter
#     def ism(self):
#         del self.ism
        
#     @property
#     def familiya(self):
#         return self._familiya
#     @familiya.setter
#     def familiya(self, new_familiya):
#         if type(new_familiya) is str:
#             self._familiya = new_familiya
#         else:
#             raise ValueError("harf kiriting")
        
#     @familiya.deleter
#     def familiya(self):
#         del self.familiya
        
    
# class NameString:
#     def __set_name__(self, owner, name):
#        self.name='_'+name
            
            
#     def __set__(self, instance, value:str):
#         if type(value)is str:
#             if value.isalpha():
#                 instance.__dict__[self.name] = value
#             else:
#                 print ("harf kiriting")
#         else:
#             print ("harf kiriting")
            

#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
    
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
        
        
# class Person:
#     ism = NameString()
#     familiya = NameString()
    
#     def __init__(self, ism, familiya):
#         self.ism = ism
#         self.familiya = familiya
    
    
# p1=Person("ali","valiyev")
# p1.ism="Avazbek"
# print(p1.ism)
# p1.familiya="Polatov"
# print(p1 .familiya)
# print(p1.__dict__)



# class NameString:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
            
#     def __set__(self, instance, value: str):
#         if isinstance(value, str) and value.isalpha():
#             instance.__dict__[self.name] = value
#         else:
#             print("Faqat harflardan iborat bo'lgan so'z kiriting.")
            
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
    
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class Age:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
            
#     def __set__(self, instance, value: int):
#         if isinstance(value, int) and 0 <= value <= 100:
#             instance.__dict__[self.name] = value
#         else:
#             print("Yosh 0 dan 120 gacha bo'lishi kerak.")
            
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
    
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class PhoneNumber:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __set__(self, instance, value: str):
#         value = str(value)
#         if isinstance(value, str) and value.isdigit() and len(value) == 12:
#             instance.__dict__[self.name] = value
#         else:
#             print("Telefon raqami faqat 12 ta raqamdan iborat bo'lishi kerak.")

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)

#     def __delete__(self, instance):
#         del instance.__dict__[self.name]

# class Email:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
            
#     def __set__(self, instance, value: str):
#         if isinstance(value, str) and "@" in value and "." in value.split("@")[-1]:
#             instance.__dict__[self.name] = value
#         else:
#             print("Email noto'g'ri formatda.")
            
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
    
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]


# class Person:
#     ism = NameString()
#     familiya = NameString()
#     age = Age()
#     phone_number = PhoneNumber()
#     email = Email()
    
#     def __init__(self, ism, familiya, age, phone_number, email):
#         self.ism = ism
#         self.familiya = familiya
#         self.age = age
#         self.phone_number = phone_number
#         self.email = email



# p1 = Person("Avazbek", "Poltov", 25, "9989012345", "avazbekpoltov@gmail.com")
# print(p1.phone_number)
# p1.age = 25
# p1.phone_number = 998887651804
# p1.email = "avazbek@gmail.com"
# print(p1.__dict__)


    
        
# class Person:
#     ism = NameString()
#     familiya = NameString()
#     age = Age()
#     phone_number = PhoneNumber()
#     email = Email()
    
#     def __init__(self, ism, familiya, age, phone_number, email):
#         self.ism = ism
#         self.familiya = familiya
#         self.age = age
#         self.phone_number = phone_number
#         self.email = email

# p1 = Person("Avazbek", "Poltov", 25, "9989012345", "avazbekpoltov@gmail.com")
# print(p1.email)