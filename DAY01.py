sales = 100,000,000
name = input(“이름: ”)
time = input(“출근시간(HHMM): ”)
if(int(time) <= 900)
  sales = int(sales) * 1.3
  print(str(name) + “님 ” + str(time)+ “ 출근 ” + “- ” + str(sales))
elif(int(time) <= 905)
  sales = int(sales) * 1.1
  print(str(name) + “님 ” + str(time)+ “ 출근인정” + “- ” + str(sales))
else(int(time) > 905)
  sales = int(sales) * 0.85
  print(str(name) + “님 ” + str(time) + “ 지각” + “- ” + str(sales))
