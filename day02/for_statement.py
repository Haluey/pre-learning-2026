# for_statement.py - for 반복문
# for 변수 in 범위:
#   반복할 구문

print(range(5))
print(list(range(5)))

for i in range(5):  # range(0, 5) => 0, 1, 2, 3, 4 까지
    print(i, end = ' ')

print()

for i in range(1, 6):  # range(1, 6) => 1, 2, 3, 4, 5 까지
    print(i, end = ' ')

print()

for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print(i, end = ' ')

print()
print('구구단')

for x in range(2, 10):  # 2부터 9까지
    print(str(x) + '단 시작')
    
    for y in range(1, 10):  # 1부터 9까지
        print(str(x) + ' x ' + str(y) + ' = ' + str(x*y), end = ' ')
    
    print()


# 성적 판별
score = int(input('정수를 입력하세요 > '))  # 키보드 입력은 무조건 문자열(str)이므로 숫자형으로 형변환해야 함

if score >= 90:
    print('A학점')
elif score >= 80:
    print('B학점')
elif score >= 70:
    print('C학점')
else:
    print('F학점')
