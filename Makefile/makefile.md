#### Makefile이 필요한 이유
1. 반복되는 컴파일 작업이 지겹고 시간이 오래 걸려서
2. 수정된 파일만 컴파일 할 수 있어서
3. 대규모 프로젝트나, 공동 프로젝트에서 반드시 필요


#### 컴파일 과정
소스 파일(*.c) ->(컴파일러)
-> 목적 파일(.o) 기계어  
기계어와 라이브러리 묶어서-> 실행파일 (a.out)


### Makefile 만드는 방법
- 목적파일 만들기 위해선 gcc -c kor.c main.c usa.c (각각 소스의 목적파일이 생성됌)
- gcc -o app.out kor.o main.o usa.o (들을 링킹해서 실행파일 만든다)
- ./app.out

### Makefile 구조
- TARGET (만들고자 하는것 ) : DEPENDENCY (필요한 얘들)
(tab)    command
```
app.out : main.o kor.o usa.o
    gcc -o app.out main.o kor.o usa.o
main.o : 
    gcc -c main.c
kor.o : 
    gcc -c kor.c
usa.o : 
    gcc -c usa.c

- 순서대로 실행이 되기때문에 처음부터 target을 놓던가 all 옵션을 줘야함
- 맨위에 all : app.out 두면 target이 어디에 놓여도 괜찮다.
```

### 추가 테크닉
- 환경변수 빼주자
```
CC = gcc
사용 시에 $(CC)

$(TARGET) : main.o kor.o usa.o
    $(CC) -o $(TARGET) main.o kor.o usa.o

OBJS = main.o kor.o usa.o

$(TARGET) : $(OBJS)
    $(CC) -o $(TARGET) $(OBJS)

shell 안에서 %@라는 것은 $TARGET , $^는 $(OBJS) 즉 dependency

```

- 만약에 OBJS 파일이 더 늘어난다면? 또 넣어줘야하나?
- .c.o : (makefile의 공간에 있는 모든 c를 o로 컴파일한다)
    $(CC) -c -o $@ $<
    - .o file을 target, $<는 .c파일들

-CFLAGS = 컴파일 옵션 
   - Wall (warning)
   - g debuinging
-LDFLAGS = 링크 옵션
   - -lopenssl -lc (라이브러리 링크할 것)

```
$(CC) $(LDFLAGS) -o $@ $^

```
- 만들어진 목적파일 지우는 커맨드
clean : 
    rm -f $(OBJS) $(TARGET)

- 만약에 한 개의 파일만 수정한다면(touch 등으로 최신 수정시간 바꾸기)
- 바뀐파일만 컴파일해서 실행파일 생성해준다.
/--------------------------------/