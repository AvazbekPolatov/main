# 1-masala
# from datetime import datetime


# datetime_object = datetime.now()
# print("Bugungi sana: ", datetime_object.strftime("%Y-%m-%d"))

# ------------------------------------------------------------------

# 2-misol
# import time

# current_time = time.time()
# h="%H:%M:%S"
# now=time.strftime(h, time.localtime(current_time))

# print("Current time:", now)

# --------------------------------------------------------------

# 3-masala
# from datetime import datetime

# data_and_time = datetime.now()
# print(data_and_time.strftime("%Y-%m-%d %H:%M:%S"))

# ----------------------------------------------------------------

# 4-masala
# from datetime import datetime

# entered_date = input("Enter a date (YYYY-MM-DD): ")

# data=datetime.strptime(entered_date, "%Y-%m-%d")

# day_of_week = data.weekday()

# week_days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(f"Entered date: {entered_date}, Day of the week: {week_days[day_of_week]}")

# ----------------------------------------------------------------

# 5-masala

# import time

# secunds=int(input("Enter the number of seconds: "))

# print(f"Kuting... {secunds} second")

# time.sleep(secunds)

# print("vaqt tugadi")

# ------------------------------------------------------------------

# 6-masala
# from datetime import datetime

# tugulgan_kun=input("Tugulgan kuningizni kiriting: (YYYY-MM-DD) ")

# tugulgan_sana=datetime.strptime(str(tugulgan_kun), "%Y-%m-%d")

# hozirgi_sana=datetime.now()

# farq=hozirgi_sana-tugulgan_sana

# print(f"Tug'ulgan kuningizdan boshlab {farq.days} kun o'tdi.")

# -------------------------------------------------------------------

# 7-masala
# from datetime import datetime

# bugungi_sana=datetime.now()

# print(f"Bugungi sana: {bugungi_sana.strftime('%Y-%m-%d')}")

# --------------------------------------------------------------------

# 8-masala

# from datetime import datetime

# kiritilgan_sana=input("Sana kiriting (YYYY-MM-DD): ")

# sana=datetime.strptime(kiritilgan_sana, "%Y-%m-%d")

# hafta_kuni=sana.weekday()

# if hafta_kuni in [5,6]:
#     print(f"Kiritilgan sana: {kiritilgan_sana}, Hafta oxiri.")
    
# else:
#     print(f"Kiritilgan sana: {kiritilgan_sana}, Hafta o'rtasi.")
    

# ----------------------------------------------------------------

# 9-masala

# from datetime import datetime,timedelta

# bugungi_sana=input("Birinchi sanani kiriting (YYYY-MM-DD): ")

# ikkinci_sana=input("Ikkinchi sanani kiriting (YYYY-MM-DD): ")

# def ish_kunlari_farqi(start_date, end_date):
#     ish_kunlari=0
#     current_date = start_date
    
#     while current_date <= end_date:
#         if current_date.weekday() < 5:
#             ish_kunlari += 1
#         current_date += timedelta(days=1)
        
#     return ish_kunlari

# birinchi_sana=datetime.strptime(bugungi_sana, "%Y-%m-%d")
# ikkinci_sana=datetime.strptime(ikkinci_sana, "%Y-%m-%d")

# if birinchi_sana > ikkinci_sana:
#     birinchi_sana, ikkinci_sana=ikkinci_sana, birinchi_sana
    
# farq=ish_kunlari_farqi(birinchi_sana, ikkinci_sana)

# print(f"Ikki sana orasidagi ish kunlari farqi: {farq} kun.")

# -----------------------------------------------------------------------

# 10-masala

from datetime import datetime

datetime_obj=datetime.now()

date_string=datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

print("Converted datatime object to string:", date_string)

date_string_new="2024-11-30 14:30:00"

datetime_new=datetime.strptime(date_string_new, "%Y-%m-%d %H:%M:%S")

print("Converted string to datetime object:", datetime_new)

# ----------------------------------------------------------------------------

# 11-masala

# from datetime import datetime

# kiritilgan_sana=input("Sana kiriting (YYYY-MM-DD): ")

# def faslni_aniqlash(sana):
#     oy=sana.month
#     if oy in(12,1,2):
#         return"Qish"
#     elif oy in(3,4,5):
#         return "Bahor"
#     elif oy in(6,7,8):
#         return"Yoz"
#     elif oy in(9,10,11):
#         return "Kuz"
#     else:
#         return None

# sana=datetime.strptime(kiritilgan_sana, "%Y-%m-%d")

# if sana.year % 4 == 0 and (sana.year % 100!= 0 or sana.year % 400 == 0):
#     print(f"Kiritilgan sana: {kiritilgan_sana}, Oy: {sana.strftime('%B')}, Fasli: {faslni_aniqlash(sana)}")
# else:
#     print(f"Kiritilgan sana: {kiritilgan_sana}, Fasli: Yo'q")

# -----------------------------------------------------------------------

# 12masala

# from datetime import datetime

# bugungi_sana=datetime.now()

# yangi_yil_sanasi=datetime(year=bugungi_sana.year+1, month=1, day=1)

# qolgan_vaqt=yangi_yil_sanasi-bugungi_sana

# print(f"Yangi yilgacha {qolgan_vaqt.days} kun va {qolgan_vaqt.seconds//3600}soat,{(qolgan_vaqt.seconds%3600)//60} daqiqa va {qolgan_vaqt.seconds%60} soniya qoldi.")

# --------------------------------------------------------------------------------------------------------------------------------

# 13-masala

# import time 

# kutish_vaqti=int(input("Kutish uchun soniyalrni kiriting: "))

# print(f"Kod {kutish_vaqti} soniyaga toxtatildi...")

# time.sleep(kutish_vaqti)

# print("Vaqt tugadi!")

# -----------------------------------------------------------------------

# 14-masala

# import time 

# interval=int(input("Enter the interval (in seconds)between repetitions:"))

# repetitions=int(input("Enter how many times to repeat the action:"))

# for i in range (1 , repetitions + 1):
#     print(f"{i}-repetition: Current time : {time.strftime('%Y-%m-%d %H:%M:%S')}")
#     time.sleep(interval)
    
# print("Repetitions are complete!")


# 15-masal

