# 자료구조와 알고리즘 2024
부경대 Iot 개발자 파이썬 자료구조와 알고리즘 학습 리포지토리

## 1일차
- 자료구조, 알고리즘 개요
- 파이썬 기초, 복습, 함수까지

## 2일차
- 파이썬 기초 복습

![자료구조](https://t1.daumcdn.net/cfile/tistory/23202B4C53FDC5600C)


- 파이썬 자료 구조
    - 선형리스트(배열)
    - 단순 연결 리스트 = 파이썬의 list의 동일

    ![연결리스트](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png)

## 3일차
- 파이썬 자료구조
  - 단순 연결 리스트 다시
  - 원형 연결 리스트(패스) : 마지막 노드가 첫 노드와 연결
  - 스택 : Last In First Out (LIFO)
        - pop - list.pop()
        - push - list.append()

        
   ![stack](https://cs.lmu.edu/~ray/images/stack.gif)
  - 큐 : First In First Out (FIFO)

   ![queue](https://raw.githubusercontent.com/YooChangWoo/ds-and-algorithm/main/images/queue.png)
  - 트리
  - 그래프

## 4일차
- 파이썬 자료구조
  - 큐 다시
  - 이진 트리

    ![이진트리](https://kahee.github.io//assets/post_img/tree3.png)

## 5일차
- 파이썬 자료구조/알고리즘
    - 그래프


    ![그래프개념](https://raw.githubusercontent.com/YooChangWoo/ds-and-algorithm/main/images/graph02.png)

## 6일차 (2024.02.19)
- 파이썬 자료구조 / 알고리즘
    - 재귀호출
    - 정렬
        - 선택정렬 = SELECTION SORT - 최솟값을 찾아서 맨 앞으로 = O(N^2)
        - 삽입정렬 = INSERTION SORT - 기준값 기준 앞 뒤로 보내는 정렬 = O(N^2)
        - 버블정렬 = BUBBLE SORT - 기준값 기준으로 제일 큰값으로 뒤로 정렬 = O(N^2)
        - 퀵정렬 = QUICK SORT - 기준값 기준으로 작은값, 큰값 그룹을 분리한뒤 다시 정렬 재귀 호출 = O(nlogn)


![sorting](https://raw.githubusercontent.com/YooChangWoo/ds-and-algorithm/main/images/sorting.jpg)

## 7일차
- 파이썬 자료구조/알고리즘
    - 검색
  - 코딩테스트

  ### special lecture

## 1일차

변수 정의
- 일반 변수
  - 한개의 값을 저장하는 타입

  - 여러개의 값을 저장하는 타입
    - List : [] -> 여러 자료형의 데이터를 담을 수 있음 (순서=index가 있음)
    - Dict : {} - 여러 자료형의 데이터를 key : value 형태로 담을 수 있음 (순서가 없음)
    - Tuple : () -> 리스트와 동이랗게 사용되며, 다만 수정을 못한다는 차이점만 있음
    - ppend, values, items, len
  
  - for 반복문 
    - 반복문 사용 방법 1 : 인덱스 번호를 이용하는 방법
    - 반복문 사용방법 2 : 값을 이용하는 방법

## 2일차 

함수

  - 함수(function, method, def)>
    - 자주 반복해서 사용되는 프로그램 특정기능을 미리 정의해 놓고 호출해서 사용(재사용성)
    - 값을 전달 받을 수도 있고, 반환(retrun)할 수도 있습니다.
    - 함수는 함수명, 매개변수들, 반환값(return)으로 정의합니다.
    - 특정 기능을 수행하는 용도로 사용하며, 함수 내에서는 값들을 가급적 정의하지 않습니다.(매개변수는 제외)

  - <함수를 생선하는 순서?>
    - 절차적 프로그램으로 사전에 테스트
    - 테스트 시 오류가 없는 경우
    - 정의된 함수에 프록램 코드를 가급적 copy하여 넣기
    - 최종 호출하여 테스트...

  - 함수를 생성
   - 매개변수가 몇개 들어올지 모릅니다.
   - 전달받은 매개변수들을 모두 출력해 주시면 됩니다.
   - 함수 내에서 print 하시면 됩니다.

클래스
  - 클래스
   - 여러 기능 또는 여러 변수들을 정의해서 사용하는 객체
   - 하나의 클래스는 여러 기능을 대표할 수 있는 형태들의 모임
   - 클래스 이름은 대문자로 시작합니다.
   - 클래스 내에서 정의하는 모든 함수의 매개변수는 self가 필수(첫번째 매개변수에 무조건...)
   - self : 클래스 내에 있는 모든 맴버에 접근할 수 있는 객체를 의미합니다.
   - 클래스 내에서 함수를 호출할 때에는 self를 이용해서 함수를 호출해야 하니다.(함수는 자동으로 맴버가 됩니다.)

  - 클래스 생성자
   - 클래스 생성시 초기화 할 값이나, 함수 호출 시 사용합니다.
   - 최초에 초기화할 값이 없거나 호출할 함수가 없으면, 생략 가능합니다.
   - 생략하는 경우 -> 외부에서 클래스 생성시, default 생성자가 자동으로 호출됩니다.
   - 생성자의 역할 : 클래스를 메모리에 올리는 작업을 수행합니다.(메모리 주소를 발급)

