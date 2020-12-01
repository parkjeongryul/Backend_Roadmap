### 모든 프로그래머들은 bug free 하고싶다.
- unit test
- integration test
- code review
- 위 셋을 모두 통과하고 Q.A 팀에서 bug를 찾아낸다면 debug 모드로 컴파일을 해야한다.

### debug 예제
- g++ -g 라는 옵션을 주면 debug mode로 컴파일을 한다.
- 공식 홈페이지를 보면 extra information이 들어가서 dwarf format 에 대해서 알아보자.
- binary(machine code) - cpp source 연결해주는 info가 있다.
- debug 모드에서는 최적화를 하게되면 위 연결이 일치하기 힘들어서 -Og (디버그용) 최적화 옵션을 넘겨주기도 한다.

### debug 정보
- variable
- break pointer
- call stack (back trace)

### debug 방법
- GDB
- visual studio code

### debug 절차
1. g++ main.cpp -g
2. gdb a.out (gdb 시작)
3. (gdb) start (code를 한줄 씩 실행)
4. (gdb) next
5. ctrl + X + A (interactive command line tool 제공)
6. break 26( 해당 지점에 break point 걸림)
7. break sub (sub 함수에 브레이크가 걸린다.)
8. continue (break 지점에 멈춘다.)
9. step (함수 안으로 들어간다.)
10. print vIn (vIn 벡터의 값을 볼 수 있다.)
11. ctrl+X,2 (assembly 코드가 나온다.)
12. 가장 왼쪽이 명령어가 들어있는 주소이며, 해당하는 assembly 명령어를 알 수 있다.
13. ctrl+X,2 한번 더 누르면 (또다른 뷰, 레지스터에 대해서 볼 수 있고 어떤 값이 들어가는지 알 수 있다)
14. tui reg float (float 을 처리하는 레지스터 보여준다.)

### call stack 보는 법
- bt (backtrace를 출력)

### 더 편하게 하는법 visual studio code
- break point 잡기 위해서는 빨간점 클릭
- start debug 하면 디버깅이 수행된다.
- variable 도 확인 할 수 있고
- step into 라는 버튼으로 함수안에 진입한다.
- call stack이라는 섹션이 따로 있다.

### 마무리
- std::cout을 통해서 출력디버깅하지말고 디버깅하자.!
- 되도록 gdb보단 visual studio code 쓰자 ㅎㅎ