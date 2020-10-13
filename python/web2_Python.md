#### 등장 배경
- 웹이등장하고 html로도 행복했다.
- 그러나 사람이 직접 html을 타이핑하고 수정해야했다..
- 방문자에게 마음대로 웹페이지를 수정하도록 할 수도 업었다.
- 성장이 한계에 직면
- 귀찮고 반복적인 작업을 기계에게 시키고자 한다.

#### common gateway interface (CGI) 가등장
- 이 기술을 이용하면 Python, PHP, JSP, ASP, Ruby, Java, JavaScript등의 언어를 이용해서 웹페이지를 만들 수 있게된다.
- 우리는 web server - CGI - python 으로 연결시키고자 한다.
- python을 이용해서 web application을 제작할 수 있게 되었다.
- contents를 생성하는 상위적인 일에 전념할 수 있게 된다.

#### python을 배우는 이유
- 페이지 하나는 html 한 개에 해당된다.
- 1억개의 html파일을 가지고 있다면, 하나하나 li를 작성해야할 수 있다.

#### web application의 동작
- 확장자가 py이며, webserver가 아닌 python이 해당 파일을 처리하도록 CGI 기술을 이용한다.
- index.py를 바탕으로 페이지를 생성해서 서버에게 보내준다.
- web browser -> web server -> CGI -> file

#### 원하는 동작
- 사용자가 create 버튼을 누르면 새로운 페이지가 생성되고 목록에 추가된다.


#### 실습 환경 준비
- 이 강의에서는 codeanywhere이라는 프로그램을 이용해서 리눅스 호스팅 서비스를 이용한다.
- 필자는 VMware로 리눅스 환경을 구축해 두었으므로, 해당 환경에서 진행하며 web server는 apache를 이용할 것

#### python 실행
- 기본적으로 linux에 왠만하면 python이 설치되어있다.
- python3 를 치면 대화형 프로그래밍이 시작되며, exit()로 종료할 수 있다.
- python file을 생성해서 실행할 수도 있다.
- index.py를 생성하고 python3 helloworld.py 로 진행.
- 그냥 실행하고싶다면? ./helloworld.py
- 그런데 권한 거부가 뜬다. 보니까 실행권한이 없네,, 준다
- 그러나 또 실행하면 안된다. 어떤 언어인지 구분할 수 없다.
```
type python3 하면 /usr/bin/python3 경로가 뜬다.

따라서 helloworld.py 안에 #!/usr/bin/python3 를 적어주면 해당 프로그램을 이용해서 실행하도록 한다.

각 운영체제 및 환경에따라서 다르게 작성한다.
```

#### 아파치설치 및 세팅
- sudo apt-get install apache2 를 이용하여 설치
- /etc/apache2/sites-available/000-default.conf
   - DocumentRoot를 설정
   - 확장자가 py인 파일은 python을 통해서 실행해라! 를 설정해야함
   - cgi : web-server가 python 이나 php java 등의 애플리케이션을 실행하기 위한 표준, 약속
   - ExecCGI : 해당 파일을 CGI로 실행하는것을 허용
```
/etc/apache2/sites-available/000-default.conf에 추가

 <Directory /home/jeongryul/develop/Backend_Roadmap/pyth
    AddHandler cgi-script .py
    Options ExecCGI
 </Directory>
```

- /etc/apache2/apache2.conf 파일 denied 를 granted 로 변경
- 또한 cgi 모듈을 enable 하기위해 다음 명령어 실행
   - sudo a2enmod cgi
   - sudo service apache2 restart

### python으로 웹 어플리케이션을 만들자
- 사용자로부터 입력을 받아서 웹 어플리케이션을 만들려면 아파치 설정을 바꿔야한다.
- print(1+1) 은 html은 못해.. (동적이잖아)

#### 영상에서 접속 시 에러 발생
- 아파치의 에러확인 경로 :  var/log/apache2/error.log
- 에러 내용 : Bad header: Hello world

- 분석해보자, chrome 오른쪽마우스 -> 검사 -> network - >reload
- 맨 위 파일이 해당 페이지의 html 이다.
- 이 중 content-type에 charset=UTF-8임을 확인할 수 있다.
- image 들은 Content-Type : image/png 같은 형태로 되어있다.

- 따라서 python code에 print("content-type:text/html; charset-UTF-8\n") 넣어주자.
   - webserver는 web browser에게 이 파일의 헤더값을 주도록 약속 되어 있음
   - 또한 한줄 개행해야만하며, 그 다음은 컨텐츠로 간주한다.

- 이제 잘 나온다... 해결!


#### string 문법
- 따옴표 안에 또 따옴표를 넣고싶다면 ' 와 "를 번갈아써야 한다.
- 그러나 escape 문자 \ 를 사용하면 표현할 수 있다.
- newline을 하고 싶으면 print한 번당 개행이 이루어진다.
- 그러나 \n이라는 개행 문자를 넣으면 개행된다.
- docstring이라는 것도 있다.
   - 작은따옴표를 3개를 사용하면 복잡한 형식을 그대로 넣을 수 있다.

#### 포매팅 이란?
- 코드내에서 같은 이름의 변수를 사용하게 될 수도 있다.
- 이런 문제가 생길 가능성을 줄여준다.
- age 변수에 숫자가 아닌 문자가 들어올 수도 있고, python을 사용할 줄 모르는 사람이 사용할 수 있어야 한다.
- 따라서 변수부분을 따로 분리하는 것이 포매팅!
- '{} {}'.format('one','two') 형식으로 사용
- 순서대로 넣는 이것을 postional formatting 이라고 한다.
- 그외에도 여러가지 기능이 있다.
   - Named placeholder
   - '{first} {last}'.format(name='egoing', age=12)
   - 일단 중복이 사라지고, 가독성도 높아졌다.
   - age가 무조건 d가 와야한다면 age:d와 같이 명시에 준다면, 숫자가 아니면 에러가 발생한다.


### 홈페이지를 CGI로 구현하자
- python이 실행이 되려면 실행권한을 줘야함(window는 해당 없음)
- querystring(user parmeter) 를 가져오는 방법
```
// cgi라는 모듈을 사용하겠다.
import cgi 
form = cgi.FieldStorage()
pageId = form["id"].value
print(pageId)
```

### CGI 소개
- index.py라는 어플리케이션(웹 애플리케이션)은 id라는 입력값을 받고 있다.
- 입력에 따라 다른 결과값을 출력한다.
- 따라서 사용자와 상호작용할 수 있다.

- 그럼 도대체 CGI가 뭐냐?
- browser -> httpd -> CGI Application(index.py)
- 웹서버와 CGI application 간에 교류할 수 있는 약속이 필요하다.
- 또한 여러 웹서버(nginx 등), 어플리케이션을 만들 수 있는 언어(java, 루비, php, python) 등이 있다.
- 따라서 둘 간의 프로토콜이 필요하다.
- 이러한 프로토콜은 자유를 위한 구속이라고 생각
- fast cgi, wsgi(python) 등을 쓰기도 하지만 본질적으로는 차이 없다.
- cgi.py라는 파일은 만들면 안된다~~~
- cgi.test()를 이용하면 웹서버가 python application에게 주는 정보를 출력할 수 있다.
- 그중 parameter를 넣으면 QUERY_STRING에 추가되는것을 볼 수 있다.
- php에서도 살펴보면 동일하게, QUERY_STRING으로 들어오게 된다. 

#### 따라서 CGI라는 것은 웹서버와 언어들 사이의 약속이다~~!

