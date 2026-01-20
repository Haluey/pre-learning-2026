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

  
 - 깃허브 로컬 리포지토리 생성
   1. git for windows 설치
     - https://git-scm.com/ 에서 `Install for Windows` 버튼 클릭
     - Git for Windows/x64 Setup 클릭
     - Git 설치 옵션은 기본 그대로 사용 가능(변경하지 말것)
     - cmd 또는 powershell 에서 `git --version` 또는 `git -v`로 확인 
   2. Github Desktop 설치
     - https://desktop.github.com/download/ 에서 다운로드 클릭 후 설치
     - 계정 브라우저 연동
   3. 리포지토리 클론
     - Github Desktop File 메뉴 Clone Repository 클릭
     - Github.com 탭에서 저장소 검색, 선택
     - Local Path 지정 후 `클론` 버튼 클릭


 - Visual Studio Code 설치
   1. https://code.visualstudio.com/ 에서 Download for Windows 버튼 클릭
   2. 설치 `C:\DEV\IDE\Microsoft VS Code`에 설치
   3. Extensions > Korean Pack for Visual Studio Code 설치 후 재시작
  

 - 추가 설치 프로그램
   1. Notepad++ 에디터
      - https://notepad-plus-plus.org/downloads/v8.9/ 에서 `Download Notepad++ v8.9: security enhancements` 버튼 클릭 후 설치
   2. 픽픽 - https://picpick.net/ 에서 메뉴의 다운로드 눌러서 beta버전 설치


 - **파이썬** 개발환경 설정
   1. https://www.python.org/ 에서 Downloads의 `Python 3.14.2` 버튼 클릭
   2. Add python.exe to PATH 체크 활성화 후
   3. Installer > Customize installation 클릭
   4. Documents 체크 해제, for all users 체크 활성화 다음
   5. Advanced Options 에서 Install Python 3.14 for all users 체크
   6. 경로 변경 후 설치
        <img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/42fd5ac5-75cf-4526-be07-638d766d36f5" />
        
   7. Setup was succesful 에서 Disable path length limit 클릭(필수!)
         <img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/a4db3424-2ec4-43a1-aeb1-56eb96d48167" />

   8. cmd 또는 powershell 오픈, `python --version` 확인

   9. VS Code, Extensions(확장)에서 Python을 검색 후 설치

   10. VS Code를 재오픈 후 폴더 생성(day01)

   11. main.py파일 생성 오른쪽 밑에 상태표시줄 보면 python과 버전까지 같이 보임 그럼 준비 완료

   12. 파일에 입력 후 `print('Hello Python 3.14.2')` Ctrl+F5하고 python debugger 선택

 - 프로그램 개발 개념
