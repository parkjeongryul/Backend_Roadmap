### jenkins

### 폴더 구조
sas src CmakeLists.txt
        main.cpp
        search_logic
        ...
        scripts         install_conda.sh
        misc            conda_environment.yml
        unit_test       CmakeLists.txt
                        model_unittest.cpp
                        sas.unittest
        integration_test
    (template-sas-env)


- scripts
   - install_conda.sh sourceme.sh

- misc
   - conda_environment.yml

- unit_test
   - googletest를 이용
   - CMakeLists.txt
   - CMakeLists.in

- integration_test
   - 통합테스트 이기 떄문에 별도의 빌드과정이 필요하지 않다.
   - robot sample.robot


### 필요한 라이브러리
- misc/conda_environment.yml 파일에 명시

### 빌드 과정
sas/src/CmakeLists.txt

unit_test/CmakeLists.txt에서
sas.unittest 실행파일을 생성한다.

### 설정 옵션 사항
1. unittest 작성했다.
- sas/src/unit_test/parameter_parser_unittest.cpp

- sas/src/unit_test/CMakeLists.txt
parameter_parser_unittest.cpp

- build 하면 됌.
- test_code 작성법은  https://github.com/google/googletest 참고

2. robottest 추가
- sas/src/robot/sample.robot에 추가 검증하고자하는 호출 예제 작성


### jenkins
- tomcat을 이용해서 웹 아카이브 파일 띄움
- css1757.nfra.io:8080/jenkins/job/Template-SAS
- 계정 irteam/irteam
- hook 연동
- build now 버튼