# functions.py
# def 함수명([매개변수]):
#       함수 내 코드
# 매개변수 == 파라미터(parameter) == 아규먼트(argument)

# 내장함수 사용
print()
print('Hello Python')
print(str(10))

# 함수 정의(매개변수 없는 것)
def sayHello1():
    # pass  # 코드 오류 방지 기능(일하는 tip)
    print('Hello Everyone~')
    # return None 이 숨어있는 형태

# 매개변수 사용
def sayHello2(name):
    #  "" ''
    # print('Hello~ Im ' + name )
    print("Hello~ I'm " + name )

# 매개변수 사용 + 반환(리턴)
def add(x, y):
    result = x + y
    return result

# 매개변수 없이 반환하는 함수
def process():
    result = 'Done'
    return result

def get_user_info(id):
    # DB에서 개인정보를 가져옴
    info = None
    return info

# 커스텀함수 사용(호출)
sayHello1()

# 함수 호출(매개변수 사용)
sayHello2('민주')
sayHello2('애슐리')

sum = add(10,5)
# sum = 15
print(sum)

print(process())  # print('Done') 와 동일
