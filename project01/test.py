# FString
# 기존 문법
name = '홍길동'
age = '30'

hello = '제 이름은 ' + name + '이구요, 나이는 ' + age + '살 입니다.'
print(hello)

# FString을 이용한 문법
name = '우투리'
age = '3'

hello = f'제 이름은 {name} 이구요, 나이는 {age}살 입니다'
print(hello)

##########################################################

from datetime import datetime

today = datetime.now()
mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
print(mytime)
