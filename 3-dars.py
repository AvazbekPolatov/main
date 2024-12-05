# numbers=[1,2,3,4,5]

# min_num=min(numbers)
# print(min_num)

# max_num=max(numbers)

# print(max_num)

# sum_numbers=sum(numbers)

# print(sum_numbers)

# print(abs(-5))

# num=127.15554
# print(round(num,1))

# print(pow(2,3))

# print(pow(2,3,5)) # 2^3 % 5 = 8 % 5 = 3


# num=4**2

# print(num)

# num=2**(1/2)

# print(num)

# import math

# import math  # Matematik operatsiyalar uchun kerak bo'lgan modul

# num = math.pow(2, 3)  
# print(num)  # 2 ning 3-darajasini hisoblaydi (2^3 = 8.0).

# print(math.sqrt(4))  
# # 4 ning kvadrat ildizini hisoblaydi (√4 = 2.0).

# print(math.pow(27, 1/3))  
# # 27 ning kub ildizini hisoblaydi (27^(1/3) ≈ 3.0).

# print(math.pi)  
# # π ning qiymatini chiqaradi (3.141592653589793).

# print(math.sin(math.radians(90)))  
# # 90° burchakning sinusini hisoblaydi (1.0).

# print(math.cos(math.radians(60)))  
# # 60° burchakning kosinusini hisoblaydi (0.5).

# print(math.tan(math.radians(45)))  
# # 45° burchakning tangensini hisoblaydi (1.0).

# print(math.log(4, 2))  
# # 4 ning 2 ga bo'lgan logarifmini hisoblaydi (log_2(4) = 2.0).

# print(math.exp(1))  
# # e ning eksponentini hisoblaydi (e = 2.718281828459045).

# print(math.factorial(5))  
# # 5 ning faktorialini hisoblaydi (5! = 120).

# print(math.log(100, 10))  
# # 100 ning 10 asosidagi logarifmini hisoblaydi (log10(100) = 2.0).

# print(math.log10(100))  
# # 100 ning 10 asosidagi logarifmini yana hisoblaydi (log10(100) = 2.0).

# print(math.exp(1))  
# # e ning birinchi darajasini hisoblaydi (e^1 ≈ 2.718281828459045).

# print(math.factorial(5))  
# # 5! (5 faktoriyal) ni hisoblaydi (5! = 5 × 4 × 3 × 2 × 1 = 120).

# print(math.gcd(24, 36))  
# # 24 va 36 ning eng katta umumiy bo'luvchisini (GCD) topadi (12).

# print(math.isqrt(25))  
# # 25 ning butun kvadrat ildizini hisoblaydi (5).

# print(math.comb(10, 3))  
# # 10 elementdan 3 ta tanlashning kombinatsiyalar sonini hisoblaydi (C(10, 3) = 120).

# print(math.perm(10, 3))  
# # 10 elementdan 3 ta tanlashning tartibli usullarini hisoblaydi (P(10, 3) = 720).

# print(math.prod([1, 2, 3, 4, 5]))  
# # Ro'yxatdagi barcha sonlarning ko'paytmasini hisoblaydi (1 × 2 × 3 × 4 × 5 = 120).

# print(math.hypot(3, 4))  
# # Pifagor teoremasi yordamida 3 va 4 katetli to'g'ri burchakli uchburchakning gipotenuzasini hisoblaydi (√(3² + 4²) = 5.0).

# print(math.degrees(math.atan2(4, 3)))  
# # Arktangensni radianlardan gradusga o'zgartiradi (atan2(4, 3) ≈ 53.13010235415599°).

# print(math.radians(45))  
# # 45 gradusni radianlarga aylantiradi (45° = π/4 ≈ 0.7853981633974483 radian).

# print(math.fabs(-5))  
# # -5 ning mutlaq qiymatini hisoblaydi (|-5| = 5.0).

# print(math.floor(4.9))  
# # 4.9 sonini pastga yaqin butun songa aylantiradi (4).

# print(math.ceil(4.9))  
# # 4.9 sonini yuqoriga yaqin butun songa aylantiradi (5).

# print(math.trunc(4.9))  
# # 4.9 sonining butun qismini ajratib oladi (4).

# print(math.copysign(10, -5))  
# # 10 sonining ishorasini -5 bilan bir xil qiladi (-10).

# print(math.frexp(10))  
# # 10 sonini mantissa va 2 asosidagi daraja shaklida qaytaradi ((0.625, 4)).

# print(math.modf(10))  
# # 10 sonini butun va kasr qismlariga ajratadi ((0.0, 10.0)).

# print(math.ldexp(0.5, 3))  
# # 0.5 sonini 2 ning 3-darajasi bilan ko'paytiradi (0.5 × 2^3 = 4.0).

# print(math.expm1(1))  
# # e^1 - 1 ni hisoblaydi (≈ 1.718281828459045).

# print(math.log1p(1))  
# # log(1 + 1) ni hisoblaydi (log(2) ≈ 0.6931471805599453).

# print(math.log2(1024))  
# # 1024 ning 2 asosidagi logarifmini hisoblaydi (log2(1024) = 10.0).

# print(math.log10(100))  
# # 100 ning 10 asosidagi logarifmini hisoblaydi (log10(100) = 2.0).

# print(math.sinh(math.radians(30)))  
# # 30 gradusni radianlarga aylantirib, shu qiymatning giperbolik sinusini hisoblaydi (sinh(30° ≈ 0.523599) ≈ 0.5478534738880397).

# ----------------------------------------------------------------------------------------------

# from decimal import Decimal

# print(0.1 + 0.2 == 0.3)  
# # False, qayta ishlatish uchun
# print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))


# num= Decimal('0.1')
# num=num+2

# print(num)

# num=num*3

# print(num)

# --------------------------------------------------------------------------------

# from decimal import Decimal,ROUND_HALF_EVEN

# num=Decimal('123.2555')
# num=num.quantize(Decimal('1.00'))
# print(num)

# num=Decimal('2.6')
# num=num.quantize(Decimal('0'), rounding=ROUND_HALF_EVEN)
# print(num)

# ------------------------------------------------------------------------------------

# from decimal import Decimal,ROUND_HALF_UP

# num=Decimal('123.2555')
# num=num.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
# print(num)

# -------------------------------------------------------------------------------------


# from decimal import Decimal,ROUND_HALF_DOWN

# num=Decimal('1.5')
# num=num.quantize(Decimal('0'), rounding=ROUND_HALF_DOWN)
# print(num)

# --------------------------------------------------------------------------------------
# import random  # Tasodifiy qiymatlar yaratish uchun kerak bo'lgan modul

# print(random.randint(1, 10))  
# # 1 va 10 (ikkalasi ham kiritilgan) orasidagi tasodifiy butun sonni chiqaradi.

# print(random.random())  
# # 0.0 va 1.0 orasida tasodifiy o'nlik sonni chiqaradi.

# print(random.uniform(1, 10))  
# # 1 va 10 orasida tasodifiy o'nlik sonni chiqaradi.

# print(random.randrange(1, 10))  
# # 1 va 10 orasidagi tasodifiy butun sonni chiqaradi, lekin 10 kiritilmagan (range(1, 10)).

# print(random.choice([1, 2, 3, 4, 5]))  
# # Berilgan ro'yxatdan (`[1, 2, 3, 4, 5]`) tasodifiy bir qiymatni tanlaydi.



# import string,random

# def green():
#     return "\033[32m"

# # print(string.ascii_letters)

# # print(string.digits)

# # print(string.punctuation)

# # print(string.whitespace)

# # print(string.printable)

# # print(string.hexdigits)

# ascii_letters = string.ascii_letters
# ascii_uppercase = string.ascii_uppercase
# digits = string.digits
# punctuation = string.punctuation

# while True:
#     length_pasword=int(input("Parol uzunligini kiriting: "))
#     password=""
#     for i in range(length_pasword):
#         password+=random.choice(ascii_letters+ascii_uppercase+digits+punctuation)
#     print(green(),password)
#     repeat=input("Boshqa parol yaratishni istaysizmi? (yes/no): ")
#     if repeat.lower()!="yes":
#         break
#     print("\033[0m")
    
    