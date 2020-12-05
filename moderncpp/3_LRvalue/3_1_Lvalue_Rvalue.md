#### intro
- lvalue와 rvalue를 정확히 구분해야지 optimization된 code를 짤 수 있다.
- copy 와 move의 차이를 알 수 있다.
- Lvalue 를 Rvalue로 바꿔주는 move 함수 학습
- Lvalue optimization 관련 RVO라는 개념 학습

#### pass by value, optimization, reference
```
void foo (int a){
    int b = a+1;
}

void fooP(int* ap){
    int b = *ap + 1;
}

void fooR(int & a){
    int b = a+1;
}

int main(){
    int a = 0;
    foo(a);
}
```

1. value
- 이 때 stack frame 구조를 보면, main stack frame 위에 foo stackframe이 쌓이고, a 값은 copy가 된다.

2. pointer
- main (a = 0) / foop(ap(main의 a를 가리키는 주소) , b)

3. reference
- pass by pointer의 동작과 똑같다..?? 확인해보니 어셈블리어 코드가 같다.
- pointer가 꼭 필요한 (주소가 필요한) 게 아니라면 되도록 reference로 구현하자. more safe
- a를 재정의 하지 않을 것이라면 const를 앞에 붙이도록 하자.

- 만약 struct와 같은 object가 온다면 copy하면 비효율적


#### vector의 pushback
```
cppreference

void push_back(const T& value)
void push_back(T&& value)
```
- &는 Lvalue, && 는 Rvalue 이다.

#### Lvalue Rvalue란?
- int a = 0; 에서 왼쪽은 lvalue 오른쪽은 rvalue라고 할 수 있다.
- int b = a; 에서는 둘다 lvalue 이다.
- 즉 한 번 부르고 다시 부를 수 있다면 lvalue이고, 다음번에 다시 쓸 수 없다면 rvalue 이다.
- std::string s = "abc" 에서 s는 lvalue, "abc" 는 rvalue

#### std::move란?
- int c = std::move(a); c는 lvalue이지만, 오른쪽은 move를 통해서 rvalue로 바뀐다.
- 코드 예제를 한 번 알아보자.

```
void storeBValue(std::string s){
    std::string b= s;
};

void storeByLRef(std::string & s){
    std::string b= s;
};

void storeByRRef(std::string && s){
    std::string b= s;
};  //wrong

int main(){
    std::string a = "abc";
    storeByValue(a);
    storeByLRef(a);
    storeByRRef(a); //wrong, move를 사용하거나 "abc" 로 바꿔주어야함

}
```

- 함수 호출 전 메모리 : string a = "abc" 에서, "abc"는 heap, a는 스택영역에 존재하며 a는 포인터

1. callbyvalue
- string s라는 object가 생기고, "abc"가 heap에 한번더 복사가되고, 다음 b에 s를 복사하면서 다시한번더 heap에 "abc"가 생성된다.
- 2 copies

2. callbyLRef
- value를 복사하는 것이아니라, a가 가리키던 heap 공간을 s도 가리킨다.
- s가 가리키는 값을 b로 copy한다.
- 1 copy

3. callbyRRef
- 초기 메모리부터 달라진다.
- heap에 "abc" 문자열은 있지만 이걸 가리키는 stack에 변수는 임시로 있을뿐 존재하지않는다.
- 함수가 call이 되면서 s는 이 임시 포인터를 가져가게 된다.
- 그리고 b는 "abc"를 copy해야하는데 틀렸다..!
- s를 계속적으로 지칭할 수 있기때문에 lvalue가 된다.
- 따라서 string b = std::move(s)로 한다면, s는 Rvalue로 바뀌는 것으로 알고 b는 "abc"를 가져가며 0copy가 된다.

#### 관련 질문
좋은 강의 잘들었습니다~
굉장히 기본적인 질문일 수도 있는데요, 문득 궁금한 부분이 있어 질문드려봅니다.

std::string 을 pass by value 로 전달하는 부분 관련하여

제가 std::string를 정확하게 까보진 않았지만 아마 class의 형태이고 멤버 변수로 char* string.value 를 갖는 형태일 것이라고 생각이 들어요.
그렇다면 깊은복사가 일어나야 "abc" 가 heap 메모리에 추가로 복사될 것이고 그렇기에 string class의 복사생성자가 깊은복사로 구현되어 있겠구나라고 생각이 들었습니다.

그렇다면?? 제가 직접 간단하게 my_string class 를 만들고 따로 복사 생성자를 구현하지 않고 디폴트 복사생성자(얕은 복사) 로 구현한다면, call by value 시에 "abc"의 copy 는 일어나지 않을까요?

제가 글을 잘 못 써서 설명이 난해할 수 있겠지만 혹시 답변주실 수 있는분 계시다면 정중하게 의견을 구합니다..!

#### 답변
안녕하세요 박정률님.
제가 이해한 바가 맞다면, class에 member variable로 pointer 를 통한 data관리를 하고 있는 상황이라고 생각되네요.
이런 상황에서 default copy constructor를 사용하게 된다면 포인터정보만! 복사가 됩니다. 포인터가 가르키는 data는 복사가 되지 않습니다. 관련 키워드는 rule of three , rule of five인데 OOP챕터 안의 (https://youtu.be/zlvwlPFbzIo ) 에서 다루고 있습니다. 
포인터를 클래스 멤버로 다루는것은 RAII idiom을 위반하기 때문에 조심스럽게 다루어야 합니다. 이 또한 스마트 포인터를 통해서 방지가 가능합니다. 스마트 포인터 챕터 또한 업로드가 되어있으니까 영상 보시면 이해가 바로 되실겁니다.

여담이지만 std::string은 박정률님이 생각한대로 동작이 되지만 modern C++ compiler는 조금 더 optimization 을 하고 있습니다. 관련 영상은 https://youtu.be/OfN94pLtnB8 입니다. 초기영상이라 강의 품질도 낮고, 중간에 단어 오류도 있지만 동작원리는 충분히 이해하실거라 생각합니다.

또 궁금한점 있으시면 질문 주세요.

#### copy move constructor 관련 영상

- class를 생성했을 때 compiler가 알아서 다음과 같은 메소드를 만들어준다.
1. constructor
2. Destructor
3. copy/move constructor
4. copy/move assignment

#### 관련 키워드 c++ rule of three or five
- 멤버변수로 raw pointer를 사용해서 resoucrce를 관리한다면, copy/move construct, copy/move assignment 를 직접 만들어줘야한다.

```
class Cat{
    public : 
        Cat(string name, int age):mName{move(name),mAge{age}{}; 
}
```

- 위와같이 생성자를 선언하면 default 생성자는 disable 된다.
- 따라서 Cat()=default; 로 파라미터가 없어도 생성 가능하도록 한다.

#### copy constructor
- 동일한 object로 복사하는 경우 호출된다.
```
class Cat{
    public : 
        Cat(const Cat& other) : mName{other.name},mAge{other.mAge}
        {
            std:cout << mName << "copy constructor" << std::endl;
        }
        Cat(Cat&& other):mName{std::move(other.mName)},mAge{other.age} 
}
```

int main(){

    Cat kitty{"kitty",1};
    Cat kitty2{kitty};  // copy 
    Cat kitty3 = kitty; // copy 헷갈리니까 칼리브레이스를 사용하여 생성해주자 ?
}

- 