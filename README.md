## 1. 프로젝트 개요
![image](https://github.com/Hseongha/football_site.zip/assets/145640813/9e5436ab-cc68-4341-b127-c70106908d83)

  프로젝트명 : Football 중계사이트 모음 zip.
  
 프로젝트기간 : 8/16 ~ 8/25
 
DB - FLASK - VUE 연동을 통해 축구 중계 site 를 제작하였고,
기존의 Football 중계사이트보다 더 편리하고 빠르게 축구 경기를 볼 수 있도록
만드는 것을 목표로 하였습니다.
 - 사용한 주요 기술
Oracle db, sql,plsql, Flask, Vue, axios, css

## 2. DB 설계

<img width="500" alt="barker" src="https://github.com/Hseongha/football_site.zip/assets/145640813/3a6828ab-f1fc-495f-86fd-44f2df20bd77">
<img width="500" alt="modelling" src="https://github.com/Hseongha/football_site.zip/assets/145640813/b1fed284-83ef-4d62-87be-6ed25fe6cd3d">

  - PL/SQL 작업 : 각 테이블마다 CRUD PACKAGE 생성.

## 3. Flask 작업
  dbconnection.py 에 Oracle db 와 연동될 수 있도록 app.py 로 데이터를 전송.
  Flask 서버 내에 app.py 를 main으로 @app.route 로 vue 와 연동될 수 있는 route 를 설정하였고 return 
jsonify 를 사용하여 웹페이지로 데이터를 보낼 수 있도록 하였습니다. 

app.py 안에는 코드를 dao module 을 사용하여 6 개의 테이블 각각마다 .py 파일로 분류하였고 JOIN 된 테이블 데이터와
static 폴더를 만들어 그 안에 이미지 데이터를 route 로 불러올 수 있도록 개발하였습니다.


## 4. Vue.js
  axios를 활용하여 Flask-Vue.js 연동을 하여 Json형태로 데이터 전송할 수 있음.


## 5. 발표 영상
https://youtu.be/AgiVkd0FCWE?si=NVFgjfIf3u_Mf601
