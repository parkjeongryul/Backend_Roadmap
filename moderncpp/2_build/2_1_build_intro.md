#### Build Process

- c++은 header, cpp 로 이루어짐.

#### 빌드하기 위해 필요한 파일
main.cpp
cat.cpp
cat.h

#### 순서
1. Pre processor 가 개입이 된다.
	- #include, #define 등
    - 단순히 코드를 치환하는 역할을한다고 생각하면 된다.
	- cat.h 를 가져와서 각각 translation unit 생성 (main.cpp + cat.h , cat.cpp + cat.h)
	
2. Compiler 가 translation unit을 obj 파일로 만든다.
	- machine code, global(static) 변수의 initialization 등 data

3. Linker 개입
	- 실행가능한 excitable 파일을 만든다.
	- 실행하기 위한 additional 한 파일

4. 프로세스가 뜬다.


### 컴파일러 종류
- visual c++, gcc 등

### 컴파일 옵션
- g++ main.cpp -o (out파일의 네임)
- 실행과정중에 일어날 수 있는 warnning을 만들 수있다. ( -Wall)
- Werror : 모든 원인이 error 로 출력한다. (빌드 안됌)
- —std=c++17 을 이용하면 버전을 올릴 수 있다.
- 디버그 정보를 알 고 싶다면 (-g)
- 자세한 과정을 보는 옵션 (-v)
- optimization level 설정 (-O2)
- machine architecture , 해당 아키텍처에 최적화된 (march = cpu-type), native 를 주거나 x86를 준다.

### 마무리
- clang 같은 경우 cross compile 을 해준다.