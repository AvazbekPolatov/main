# text="Hello world"
# print(id(text))
# print(hex(id(text)))
# print(oct(id(text)))
# print(bin(id(text)))
# print(type(text))
# print(text)
# -------------------------------------------------------------------
# import gc
# print(gc.get_threshold())
# gc.set_threshold(100,5,5)
# print(gc.get_threshold())


# gc.disable()
# gc.enable()
# print(gc.isenabled())
# -------------------------------------------------------

# import time

# current_time = time.time()
# h="%H:%M:%S"
# now=time.strftime(h, time.localtime(current_time))

# print("Current time:", now)
# -----------------------------------------------

# start=time.time()
# for i in range(10):
#     time.sleep(0.5)
# end=time.time()
# print(end-start)

# ------------------------------------------------------------------


# import datetime

# current_date = datetime.date.today()
# print(current_date.day)
# print(current_date.month)
# print(current_date.year)
# print(current_date.strftime("%d-%m-%Y"))

# -------------------------------------------------------------------

from datetime import datetime

current_time = datetime.now()
print(current_time)
print(current_time.strftime("%H:%M:%S"))

# -------------------------------------------------------------------

from datetime import timedelta

delta = timedelta(days=10)
new_date = current_time + delta
print(new_date)
