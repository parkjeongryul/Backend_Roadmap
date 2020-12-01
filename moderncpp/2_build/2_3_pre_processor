#### preprocessor 란?
- #include, #define, #ifdef, #pragma once 등 에 개입

```
#define ABCD 2
#ifdef ABCD
#else
#endif

- 컴파일러에게 보내주기전에 코드를 수정한다.
- 치환해주는 것

#### 실제 코드 내 응용

```
#define MAX_UINT16 65535
#define MAX(a,b) (((a)>(b))) ?(a):(b))

- 해당 값으로 치환되서 결과 값이 나온다.

#### modern c++에서 #define의 사용을 최소화하는 것이 좋다.
- 이렇게 macro로 사용하는 것보다 stl을 사용하는것이 더 안전하다.
    ```
     numeric_limits<uint16_t>::max()  //최댓값
     std::max(10,100);
    ```

#### constexpr 사용
- c++17의 새로운 feature 이다. 나중에 다시 알아보자.
```
constexpr int ABCD = 2;

if constexpr(ABCD){

}

else{

}
```


#### predefined macros 들도 있다.
- __FILE__
- __LINE__
- __DATE__
- __TIME__
- 위 시간은 compile 했을 때의 시간을 알 수있는 것.
- runtime의 시간은 아니다.


#### cat code에서 응용
- #include 는 단순히 코드 복사 붙여넣기이다.
- <> 는 standard library, "" 는 user specific header이다.
- 일반적으로 #include 는 cpp에서 하는 것이 원칙이나, header에서 필요한 경우 헤더에 써준다.

#### 문제점 
- zoo.cpp 를 만들고, 해당 클래스가 cat.cpp를 사용한다면?
- cat.h를 두번 include 하게 될 수 있는데! 에러가 난다.. (redefinition)

#### 해결책
- 이 떄 preprocessor의 #ifndef , #define, #endif 를 헤더파일에 적어주면 컴파일이 잘된다
- 위 내용을 한줄로 #pragma once 로 해버릴 수 있다.

#### 마무리
- #define, #ifdef, #include
- modernc++ 에서는 constexpr if 나 constexpr 및 c++ standard library 추천
- #include 는 copy & paste 가 되는 것인데 재정의 방지를 위해 #pragma once 를 사용하자.
- __FILE__, __LINE__ , __linux__ , __APPLE__ 등 각 OS 에 맞는 predefined macro 를 사용할 수 있다.
