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

