### 탐색
많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

#### 스택
 - 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
```
stack = []
#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력
```

 
#### 큐
 - 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
```
from collections import deque
#큐 구현을 위해 deque라이브러리 사용
queue = deque()

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력
```
### 

 
