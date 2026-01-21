# if_statement.py - 제어문 if문
# 제어문 중 최초로 만들어진 것
# if 조건:  # 참인 조건
#       처리할 문장
# else:
#       처리할 문장

age = 16

print('담배주세요')

if age > 19:  # 항상 참인 조건(논리적으로)
    print('담배를 산다')
else:  # 거짓인 조건
    print('민증주세요')

print()
blood = 'AB'  # A, B, AB, O

if blood == 'A':
    print('소심하네요')
elif blood == 'B':
    print('돌아이네요')
elif blood == 'AB':
    print('괴팍하네요')
elif blood == 'O':
    print('온화하네요')
else:
    print('외계인이세요?')

print()

is_adult = True
gender = 'Female'

# 이중 if문으로 분기
if is_adult == True:
    print('대인입니다. 20000원입니다.')  # 실행
    if gender == 'Male':
        print('남탕으로 가세요')
    else:
        print('여탕으로 가세요')  # 실행
else:
    print('소인입니다. 12000원입니다.')
    if gender == 'Male':
        print('남탕으로 가세요')
    else:
        print('여탕으로 가세요')

# 논리 연산자 and로 분기
is_adult = False
gender = 'Male'

if is_adult == True and gender == 'Male':
    print('대인, 남자입니다. 20000원')
elif is_adult == True and gender == 'Female':
    print('대인, 여자입니다. 20000원')
elif is_adult == False and gender == 'Male':
    print('소인, 남자입니다. 12000원')  # 실행
elif is_adult == False and gender == 'Female':
    print('소인, 여자입니다. 12000원')

# and, or, not
print(not is_adult)
