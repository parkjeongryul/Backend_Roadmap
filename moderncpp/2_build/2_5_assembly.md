#### assembly
- 실제 프로그래밍하면서 직접 다룰 일없다.
- 빠른 코드를 짜기 위해서는 benchmark와 profile을 직접 찍어보는 것이 더 정확하다.

#### 학습 목표
- compiler마다 C++ 을 어떤식으로 optimization 하는지
- architecture 마다 어떤식으로 machine code가 generate 되는 지 (필자는 x86-64)

#### 코드 예제
- multiply 함수, devide 함수 짜서 -s 옵션을 준다.
- .s 파일이 생기며 머신코드가 생기며 name mangling을 염두해서 함수이름을 보자.

#### compiler explorer 라는 웹서비스가 있다.
- 어떤 코드에 대한 assembly를 보여주며, 해당 명령어가 어떤 명령어인지도 알 수 있고, -O2 옵션을 줄 수도 있다.
- 또한 다른 컴파일러 및 아키텍처에서의 어셈블리 코드또한 확인 할 수 있다.
- compiler explorer 로 확인하는 것이 더 알기 쉽다.

#### 코드 예제2
- a*8 or a<<3 각각 작성해보자.
- 비트연산이 빨라보이지만, assembly 언어를 확인해보면 똑같은걸 알 수 있다!!

- a/13 을 하면 assembly코드는 5줄이고, a/b 함수는 3줄인데 왜??
   - idiv 라는 명령어가 imul 명령어보다 5배정도 clock이 많이 필요하다.
   - 실제 assembly code line은 짧겠지만 computation에 필요한 시간은 아래쪽이 더 빠르다.


#### if else 문과 switch
- switch case가 더 효율적인 것을 알 수있다.
- assembly code 라인수가 더 적고 효율적이다.
- 그러나 clang compiler 로 보면 완벽히 동일한 것을 볼 수있다.

#### 마무리
- *2, *4 등을 비트 연산으로 바꿔봤자 효율성이 없다.
- 이정도의 optimaztion은 그냥 컴파일러를 믿어라
- devide (a,b) , devide(a,13) 오른쪽이 코드가 더 길었지만 computation 시간이 짧다.
- 어셈블리 코드가 짧다고 더 빠른코드가 아니다.

- if else / switch 를 비교할 떄 gcc 에서는 차이가 있었지만 clang에서는 차이가 없다.
- 일반적으로 clang이 좋은 코드를 만들어 주긴하지만 benchmark 를 돌려보는 것이 확실하다.
- 따라서 modern compiler 에서는 가독성을 해치지 않아도 충분히 좋은 코드를 만들어 주는것을 알 수 있었다.

