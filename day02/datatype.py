# datatype.py - 자료형 확인

# 정수형
int_val = 10
# 실수형
pi = 3.141592
# 문자열형
# 파이썬에서 문자열은 '," 둘 다 사용
name = 'Hugo'  # "Hugo"와 동일
# C, C++, C#, JAVA 등은 홑따옴표, 쌍따옴표가 다르게 동작
# 불형
is_student = False  # True
# False는 0과 동일, Ture 0 이외(보통 1을 씀)

print(int_val)
print("Hello" + name)
print(name + str(int_val))  # int_val은 숫자형이므로 문자열로 합치고자 하면 문자열형으로 바꿔야 함

print(pi)
print(is_student)

name = '김민주'  # 문자열형
age = 24  # 정수형
height = 168.2  # 실수형

print('이름 : ' + name + ', 나이 : ' + str(age) + ', 키 : ' + str(height))