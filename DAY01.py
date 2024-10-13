# First
"""
sales = 100000000
name = input("1. 이름을 입력하세요: ")
time = input("2. 출근시간을 입력하세요(HHMM): ")
if(int(time) <= 900):
  sales = int(sales) * 1.3
  print(str(name) + "님 " + str(time)+ " 출근 - ", end="")
  print("{:,}".format(int(sales)))
elif(int(time) <= 905):
  sales = int(sales) * 1.1
  print(str(name) + "님 " + str(time)+ " 출근인정 - ", end="")
  print("{:,}".format(int(sales)))
else:
  sales = int(sales) * 0.85
  print(str(name) + "님 " + str(time) + " 지각 - ", end="")
  print("{:,}".format(int(sales)))
  """

# Second
sales = 100000000
name = input("1. 이름을 입력하세요: ")
time = input("2. 출근시간을 입력하세요(HHMM): ")
hour = int(time[:2])
min = int(time[2:])
hour_to_min = hour * 60

if(hour_to_min + min <= 540):
  print(f"{name}님 {time} 출근 - {"{:,}".format(int(sales * 1.3))}")
elif(hour_to_min + min <= 545):
  print(f"{name}님 {time} 출근인정 - {"{:,}".format(int(sales * 1.1))}")
else:
  print(f"{name}님 {time} 지각 - {"{:,}".format(int(sales * 0.85))}")