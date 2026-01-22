# file_write.py - 파일 쓰기

# open('파일경로', '모드')
# 모드 : w(쓰기), r(읽기), a(추가)

# 파일 오픈
file = open('./day03/my_first_file.txt', 'w', encoding = 'utf-8')

# 파일 쓰기
file.write('Hello, Python!\n')  # 엔터키 입력 필요
file.write('How are you?\n')
file.write('I\'m a student')

# 파일 닫기
file.close()

# 문자열을 여러개 담은 리스트(배열)
lines = ['안녕하세요\n', '반갑습니다\n', '안녕히가세요\n']

# encoding 글자 체계, utf-8 전세계 언어 표현하는 인코딩 방식 
file2 = open('./day03/second_file.txt', 'w', encoding = 'utf-8')
file2.writelines(lines)
file2.close()

print('파일쓰기 완료')