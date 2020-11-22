# a = int(input("Введите число >>>"))
# h = a // 3600
# m = (a // 60) % 60
# s = a % 60
# if m < 10:
#     j = 0
# else:
#     j = ''
# if s < 10:
#     t = 0
# else:
#     t = ''
# print(str(h) + ':' + str(j) + str(m) + ':' + str(t) + str(s))#

time = int(input("Введите время в секундах >>> "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")