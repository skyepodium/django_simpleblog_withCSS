# django_simpleblog_withCSS
> Work In Process (CSS를 더 쉽게 적용할 수 있도록 수정중)

## 개요  
장고로 심플 블로그 만들기 강의의 전체 코드입니다. 또한, CSS를 포함하고 있습니다.       

블로그 강의: [링크](https://blog.naver.com/godori91/221197956351)    
유튜브 강의: [링크](https://youtu.be/xe1cufuUNGw)    
이메일: <skyepodium@gmail.com>     

## 목표
심플 블로그 제작.

`Django` 를 사용하여 블로그를 만들며 누구나 쉽게  장고 및 웹 서버에 대해 이해할 수 있도록 돕는 튜토리얼 입니다.
이 리포지토리는 강의를 통해 함께 만든 장고 블로그에 `CSS`로 반응형 디자인을 입힌 것입니다.     

**장고가 2.0 으로 버전 업** 이 되면서 많은 부분이 바뀌었는데 **장고 2.0** 이상 버전으로 만들어졌습니다.   

## 사용 버전
- Python: 3.6.0
- Django: 2.0.2     


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
`http://localhost:8000/`에 들어가면 블로그 앱을 볼 수 있습니다.        
```
$ python3 manage.py runserver 0.0.0.0:8000
```
5. 샘플     
반응형 완료

![Alt Text](./readme_image/blog_final.gif)
