from decimal import Decimal
# # 1-masala
# num1 = Decimal(input("Birinchi o'nlik sonni kiriting: "))
# num2 = Decimal(input("Ikkinchi o'nlik sonni kiriting: "))
# print("Yig'indisi:", num1 + num2)
# -----------------------------------------------------

# # 2-masala
# price = Decimal(input("Mahsulot narxini kiriting: "))
# discount = Decimal(input("Chegirma foizini kiriting: "))
# discount_amount = price * (discount / Decimal(100))
# print("Chegirma miqdori:", discount_amount)
# # ---------------------------------------------------------------------

# # 3-masala
# num = Decimal(input("Sonni kiriting: "))
# rounded_num = round(num, 2)
# print("Yaxlitlangan son:", rounded_num)
# # -----------------------------------------------------------------

# # 4-masala
# num1 = Decimal(input("Birinchi sonni kiriting: "))
# num2 = Decimal(input("Ikkinchi sonni kiriting: "))
# print("Kattasi:", max(num1, num2))
# # ----- ------------------------------------------------------------

# # 5-masala
# num1 = Decimal(input("Birinchi sonni kiriting: "))
# num2 = Decimal(input("Ikkinchi sonni kiriting: "))
# num3 = Decimal(input("Uchinchi sonni kiriting: "))
# print("Yig'indisi:", num1 + num2 + num3)
# print("Ayirmasi:", num1 - num2 - num3)
# print("Bo'linmasi:", num1 / num2 / num3)
# # ----------------------------------------------------------------

# # 6-masala
# amount = Decimal(input("Summani kiriting: "))
# formatted_amount = f"${amount:,.2f}"
# print("Valyuta formatida:", formatted_amount)
# # -----------------------------------------------------------------

# # 7-masala
# price = Decimal(input("Mahsulot narxini kiriting: "))
# doubled_price = price * 2
# print("Narx ikki barobar oshirilganda:", doubled_price)

# # ------------------------------------------------------------------

# # 8-masala
# num = Decimal(input("Sonni kiriting: "))
# fraction_part = num % 1
# print("Kasr qismi:", fraction_part)
# # ----------------------------------------------------------------

# # 9-masala
# num = Decimal(input("Sonni kiriting: "))
# cube = num ** 3
# print("Kub:", cube)
# # ----------------------------------------------------------------

# # 10-masala
# value = Decimal(input("Qiymatni kiriting: "))
# percentage = value * Decimal(0.15)
# print("15% qismi:", percentage)
# ----------------------------------------------------------------

# Random bilan ishlangan misollar

# 1-masala
import random,string

# random_number = random.randint(1, 1000)
# print("Tasodifiy raqam:", random_number)

# -------------------------------------------------------------

# 2-masala
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choices(characters, k=12))
# print("Tasodifiy parol:", password)
# -----------------------------------------------------------------

# 3-masala
# toss_result = random.choice(["Oq", "Gerb"])
# print("Tanga natijasi:", toss_result)

# ---------------------------------------------------------------

# 4-masala
# lottery_numbers = random.sample(range(1, 50), 6)
# print("Lotereya sonlari:", lottery_numbers)

# ----------------------------------------------------------------

# 5-masala
# numbers = [random.randint(1, 1000) for _ in range(1000)]
# average = sum(numbers) / len(numbers)
# print("O'rtacha qiymat:", average)

# ----------------------------------------------------------------

# 6-masala
# rgb_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# print("Tasodifiy RGB rang:", rgb_color)

# ---------------------------------------------------------------------

# 7-masala
# items = ["Olma", "Banan", "Gilos", "Anor", "Apelsin"]
# random_item = random.choice(items)
# print("Tasodifiy tanlov:", random_item)

# -------------------------------------------------------------------

# 8-masala
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print("Aralashtirilgan ro'yxat:", my_list)

# -----------------------------------------------------

# Math bilan ishlash uchun 6 ta vazifa
import math
# 1-masala

# num = float(input("Sonni kiriting: "))
# sqrt_value = math.sqrt(num)
# print(f"{num} sonining kvadrat ildizi: {sqrt_value}")

# -----------------------------------------------------

# 2-masala
# angle = float(input("Burchakni kiriting (gradusda): "))
# angle_radians = math.radians(angle)  # Gradusni radianga o'tkazish
# sin_value = math.sin(angle_radians)
# cos_value = math.cos(angle_radians)
# print(f"{angle}° sinusi: {sin_value}")
# print(f"{angle}° kosinusi: {cos_value}")

# # -------------------------------------------------------------

# # 3-masala
# value = float(input("Qiymatni kiriting: "))
# base = float(input("Asosni kiriting: "))
# log_value = math.log(value, base)
# print(f"log{base}({value}) = {log_value}")

# # --------------------------------------------------------------------

# # 4-masala
# num = int(input("Butun sonni kiriting: "))
# factorial = math.factorial(num)
# print(f"{num} sonining faktoriali: {factorial}")

# # ----------------------------------------------------------------------

# # 5-masala
# radii = [float(input(f"{i+1}-radiusni kiriting: ")) for i in range(3)]
# circumferences = [2 * math.pi * r for r in radii]
# for i, c in enumerate(circumferences, 1):
#     print(f"{i}-radius uchun aylananing uzunligi: {c}")

# # ----------------------------------------------------------------------

# # 6-masala
# base = float(input("Asosni kiriting: "))
# exponent = float(input("Darajani kiriting: "))
# power = math.pow(base, exponent)
# print(f"{base} ning {exponent}-darajasi: {power}")

