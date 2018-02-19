# django_simpleblog_noCSS
> Work In Process (CSS 더 쉽게 적용할 수 있도록 수정중)

## 개요  
장고로 심플 블로그 만들기 강의의 전체 코드입니다.     
블로그 강의: [링크](https://blog.naver.com/godori91/221197956351)    
유튜브 강의: [링크](https://youtu.be/xe1cufuUNGw)    
이메일: <skyepodium@gmail.com>     

## 목표
심플 블로그 제작.
`Django` 를 사용하여 블로그를 만들며 누구나 쉽게  장고 및 웹 서버에 대해 이해할 수 있도록 돕습니다.
이 리포지토리는 강의를 통해 함께 만든 장고 블로그에 `CSS`로 반응형 디자인을 입혔습니다.        

이를 통해 웹 어플리케이션을 만드는 튜토리얼입니다.    

## 사용 버전
- Python: 3.6.0
- Django: 2.0.1     


## 설치

1. [python3.6](https://www.python.org/downloads/) 이상이 설치되어 있어야합니다.
2. 가상환경 생성 및 활성화
```
$ python3 -m venv venv
$ source venv/bin/activate
```

3. requirements 설치
```
$ pip3 install -r requirements.txt
```
4. 실행   
```
$ python3 manage.py runserver 0.0.0.0:8000
```
5. 샘플
반응형 완료
![Alt Text](https://github.com/skyepodium/django_simpleblog_withCSS/raw/master/blog/media/blog_final.gif)
