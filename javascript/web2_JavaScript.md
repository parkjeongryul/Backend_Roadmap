### 수업 소개

#### HTML로는 한계가 있다.

- 사용자와 상호작용하고 싶다!

- html은 정적이다.
- 그러나 우리가 아는 프로그램은 사용자의 움직임에 반응

- javascript -> 동적으로 수행
- HTML이 정보를 사진이라면 javascript는 마치 영화처럼 움직이도록 하는 것

### 수업의 목적

- 실습을 통해서 진행
- 주간모드 야간모드 버튼을 눌러서 만들기

- 페이지에서 오른쪽마우스 - 검사 - elements 들어가면 html을 구성하는 태그를 볼 수 있다.
- 각각 버튼을 누르면 해당 태그가 바뀐다.

  - onclick 속성 다음에는 자바스크립트가 와야한다.
  - 클릭 시 해당 코드를 수행하는 것
  - style 속성 다음에는 css가 와야한다.

- 자바스크립트에서 body 코드의 style을 설정하면, 실제 html 코드 body 태그에 style이 동적으로 변경된다.

### HTML과 JS의 만남 : script 태그

- 자바스크립트를 넣는 법!

  - <script></script> 안에 넣어준다.
  - document.write('hello world') 써 줄 수 있다.

- 그런데 그냥 hello world하는 것과 뭐가다르냐?
  - 동적으로 1+1과 같은 꼐산이 가능하다.

### HTML과 JS의 만남 : 이벤트

- <input type = "button" value = "hi">
- alert이라는 자바스크립트 코드를 넣고싶다.
- <input type = "button" value = "hi" onclick= "alert('hi')">
- onclick 속성을 만나면 alert이라는 동작을 수행하는것을 대기하고 있다?(= event)
- 몇가지 정해진 이벤트가 있다. 10 ~ 20개 정도
  - onchange 등
- 다음을 이용하여 사용자와 상호작용하는 웹페이지를 만들 것

- javascript keydown event attribute 검색
  - key를 누르면 이벤트 발생

### HTML과 JS의 만남 (콘솔)

- 파일을 만들 필요 없이 자바스크립트를 실행할 수 있다.
- 어떤 text를 복사해서 몇개의 문자로 이루어져있는지 알고싶다면?
- alert("문자열".length) 하면 알 수 있다.

- 콘솔에서 실행하는 자바스크립트는 해당 웹페이지를 대상으로 동작한다.
- 페북 참가자 추첨
  - 오른쪽마우스 - 검사 - elements (html 코드)
  - esc누르면 console이 밑에 뜬다.
  - 해당 html을 이용해서 필요에 따라서 코드를 작성해 문제를 해결

### 데이터타입 - 문자열과 숫자

- 어느 형태의 data type이 있는가?
- 총 6개의 타입과 객체가 있다.
- Boolean, NULL, Undefined, Number,String,Symbol
- console을 실행해서 그냥 1+1을 적어줘도 2가 뜬다.
- 문자열의 유용한 기능
  - 'hello world'.length
  - 'hello world'.toUpperCase()
  - 'hello world'.indexOf('o')
  - 'hello world'.indexOf('world')
- 실행을 유보하고 싶으면 shift+ enter
- 변수를 사용하고싶으면 가급적 var을 쓰는게 좋은 습관

### 웹브라우저 제어

- html은 한 번 화면에 표시되면 바꿀 수 있는 능력이 없는 정적언어

1. css의 문법을 살펴보고
2. 자바스크립트로 원하는 문법 선택

### css 기초 : style 속성

- 그냥 style 안에 css의 속성을 나열하면된다..ㅎㅎ

- h1은 헤더1이라는 디자인을 가지고 있어서, 아무 의미없는 태그 지정을 위해서 div 태그를 사용
- div는 화면 전체를 쓰기 떄문에 줄바꿈이 된다(무색 무취)
- 줄바꿈 또한 되지 않는, 즉 전체를 쓰지않는 span 태그
- span 지정을 굉장히 많은 키워드를 지정하고 싶다면??
  - head태그안에 style 태그를 지정하고, 그안에 .class 를 사용하여, 스타일을 지정할 수 있다.

### css 기초 : 선택자

- 선택자를 잘 사용해야 주고싶은 효과를 효율적으로 줄 수 있다.
- javascript라는 텍스트를 초록색으로 하고싶다!
- id="first" 라고 지정하면, #id 형식으로 해당하는 스타일 지정 가능

- class라는 말은 무언가를 grouping 단위, id는 개별 단위
- id는 해당 페이지에서 중복되지 않아야됌
- 클래스로 광범위하게 주고, id로 예외적으로 지정할 수 있는 것
- 우선순위 태그명 < class < id

### 제어할 태그 선택하기

- css selector 검색 (MDN)
- queryselectory함수 안에 지정
  - document.querySelector('body') // body태그
  - #idname , .classname
  - document.querySelector('body').style.backgroundColor = 'black';

### 프로그램, 프로그래밍, 프로그래머

- html vs js
- html은 컴퓨터언어이지만 프로그래밍 언어는 아님,
- js는 둘다 해당
- 프로그램 : 시간의 순서에따라 수행되는 의미가 내포됌

### 조건문

- 비교연산자 ===, equal이 세 개네..

### 한 버튼으로 토글동작시키기

- 검색어 : javascript element get value
- document.querySelector('#night_day').value 로 가져오면 된다.

### refactoring 및 중복제거

- document.querySelector('#id_name) => this로 바꾸자.
- var target = documnet.querySelector('body'); 로 사용

### 반복문

- queryselectorAll('a') 를 통해서 모든 a를 선택할 수 있음

```
var alist = document.querySelectorAll('a');
var i = 0;

while(i < alist.length){
console.log(alist[i]);
alist[i].style.color = 'powderblue';
i = i + 1;
}
```

### 객체

- 굉장히 중요하지만 어렵다 ?
- .(dot) 은 access operator라고 한다.

- 문법

```
var coworkers = {
    "programmer":"egoing",
    "designer":"leezche"
};

document.write("programmer : "+coworkers.programmer+"<br>");
document.write("designer : "+coworkers.designer+"<br>");
coworkers.bookkeeper = "duru"; // 이렇게 추가가 된다고 ?
document.write("bookkepper : "+coworkers.bookkeeper+"<br>")
coworkers.["data scientist"] = "taeho";
document.write("data scientist : " + coworkers["data scientist"] + "<br>");
```

### 객체와 반복문

- javascript object iterator
- 객체가 거의 map의 느낌

```
// 위에 절에 이어서
for(var key in corworkers){
    document.write(key+'<br>');
}

```

- for문에서 반환은 key값

### 객체프로퍼티와 메소드

- 다음과 같이 method 정의

```
coworkers.showAll = function(){
    for(var key in corworkers){
    document.write(key+'<br>');
}
}
```

- coworkers의 객체를 for문으로 출력하면, 함수조차 출력된다.(if문으로 빼거나 해야함)
- 그리고 해당 함수 내에서 메소드를 가진 객체를 가리키는 this를 사용하자

### 객체의 활용

- 객체의 멤버로 객체가 안되는지 ?
- for의 in은 객체에서만 사용가능한지? 배열은 안되는지


### 파일로 쪼개서 정리 정돈하기
- script src= "source" 
- 위와같이 소스를 지정하면 브라우저가 해당 파일을 같이 올린다.
- 웹서버 입장에서 사실 파일을 여러개 가져오는건 좋지않다.
- 하지만 파일을 쪼개서 올리는것이 브라우저가 cache를 하기 때문에 더 효율적이다.

## 라이브러리와 프레임워크