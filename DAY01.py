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