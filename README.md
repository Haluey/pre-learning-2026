# pre-learning-2026
IoT개발자 과정 사전학습 리포지토리

## 1일차
과정소개

학습 리포지토리 생성

- 마크다운 문법
   1. 제목
     ```markdown
     # 제목1
     ## 제목2
     ### 제목3
     #### 제목4
     ##### 제목5 (기본글자랑 비슷)
     ###### 제목6 (잘 사용 안함)
     <!-- 주석(HTML주석 동일) -->
     ```
  
   2. 목록
     ```markdown
     - 목록
     * 목록
     1. 숫자목록
     2. 숫자목록
     ```
   3. 링크, 이미지
     ```markdown
     [네이버](https://naver.com)

     ![이미지](이미지URL)

     ## 사이즈 조절 이미지
     src : 이미지URL
     width : 이미지넓이 픽셀단위 지정
     <img src="이미지URL" width="500">
     ```
     - [네이버](https://naver.com)
      
     - ![이미지](https://upload.wikimedia.org/wikipedia/commons/9/99/Welsh_Pembroke_Corgi.jpg)
     - 이미지와 링크의 차이는 !로 시작하는지 밖에 없음
       
     - <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Welsh_Pembroke_Corgi.jpg" width ="400">
 
     - <img width="275" height="183" alt="image" src="https://github.com/user-attachments/assets/0b664f40-62ff-4483-96bc-751001bb6d17" />
     - 이미지 링크 복사가 아닌 이미지 복사로 그냥 붙여넣기하면 위와 같이 나타나짐

   4. 가로줄
     ```markdown
     ---
     ```
     ---
   5. 코드블럭
     - 소스코드를 작성할 때 코드하이라이팅, 영역표시 때 사용
     - 백틱(`)을 세번 후 표시언어를 입력 또는 한번(인라인 코드블럭)
     ```python
     print('Hello, Python!')
     ```
     - 일반적인 문장에서 한 단어를 강조하고 싶을 때 `인라인 코드블럭`을 사용
       
   6. 강조 및 밑줄
     ```markdown
     **, ~~, __, html의 u 태그 사용, i 이탤릭
     ```
     - 문장을 작성할 시 **강조**, ~~취소선~~, __강조2__, <u>밑줄</u>, <i>이탤릭</i>을 사용할 수 있습니다.
  
