#### move란?
```
string a = "jeongryul";
cout << a << endl;

string b = std:move(a);
cout << a << endl;
cout << b << endl;
```

- 과연 어떻게 출력될까?
- b는 잘 출력되었지만 a에 아무것도 나오지 않았다.
- 과정 : a가 stack에 입력, "jeongryul" heap에 입력, resource ownership을 b에게 줌, a는 아무것도 가리키지 못함.

```
void storeByLRef(std::string & s){
    std::string b= s;
    s = "jeongryul"
};

void storeByRRef(std::string && s){
    std::string b= move(s);
};  

int main(){
    std::string a = "abc";
    storeByLRef(a);
    cout << a; //이 떄 a의 값이 "jeongryul"로 바뀌어 출력된다.

```
- 이 때 store