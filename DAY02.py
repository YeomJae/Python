# 변수 정의(에러코드_Dictionary 사용)
code = {"inform01":"연봉은 모두 숫자로 기입하십시오.",
        "inform02":"시간(HH)분(MM) 형태의 4자리수로 기입하세요. 24시간제로 표기하십시오.",
        "inform03":"정규 근무시간이 지났습니다.",
        "error01":"에러 발생"}
# 변수 정의
sales = input("1. 연봉을 입력하세요: ")
try: # 연봉이 숫자가 아닌 경우 에러코드 출력: try~except 문법은 ChatGPT의 도움을 받음
  salesi = int(sales)
except ValueError:
  print(code["inform01"])
  salesi = None
# 나머지 변수 정의
if salesi is not None:
  sales_ratio = [1.3, 1.1, 0.85]
  status = ["출근", "출근인정", "지각"]
  name = input("2. 이름을 입력하세요: ")
  time = input("3. 출근시간을 입력하세요(HHMM): ")
  hour = int(time[:2]) # 출근시간의 시간(HH)
  min = int(time[2:]) # 출근시간의 분(MM)
  hour_to_min = hour * 60 # 시간을 분으로 환산

# 비즈니스 로직
  if(len(time) != 4):
    print(code["inform02"])
    status = None #에러 발생 시 status를 None으로 설정
  elif(hour_to_min + min >= 1050): # 17:30을 분으로 환산: "17.5시간 * 60분/시간 = 1,050분"
    print(code["inform03"])
    status = None # 에러 발생 시 status를 None으로 설정
  else:
    if(hour_to_min + min <= 540): # 09:00를 분으로 환산: "9시간 * 60분/시간 = 540분"
      sales = salesi * sales_ratio[0]
      status = status[0]
    elif(hour_to_min + min <= 545): # 09:05을 분으로 환산: "540분 + 5분 = 545분"
      sales = salesi * sales_ratio[1]
      status = status[1]
    elif(hour_to_min + min >= 550):
      sales = salesi * sales_ratio[2]
      status = status[2]
    else:
      print(code["error01"])
      status = None #에러 발생 시 status를 None으로 설정

# 출력
  if status is not None: #status가 None이 아닌 경우에만 출력
    print(f"{name}님의 출근시간은 {hour}시 {min}분입니다. <근태기록: {status}> - 당신의 연봉은 {"{:,}".format(int(sales))}원입니다.")