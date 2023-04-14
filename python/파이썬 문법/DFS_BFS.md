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
### 재귀함수
자기 자신을 다시 호출하는 함수
 - 재귀함수를 문제 풀이에서 사용할 경우 재귀함수의 종료조건을 반드시 명시
 - 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
```
def recursive_funtion(i):
  #100번째 호출을 했을 때 종료되도록 종료조건 명시
  if i==0:
    return
  recursive_funtion(i+1)
```
#### 팩토리얼 구현예제
반복적으로 구현한 n!
```
def factorical_iterative(n):
  result = 1
  for i in range(i,n+1):
    result*=i
  return result

```
재귀적으로 구현한 n!
```
def factorical_recursive(n):
  if n<=1:
    return 1
  return n*fatorial_recursive(n-1)
```
#### 최대공약수 계산
유클리드 호제법
 - 두 자연수 A,B에 대하여 A를 B로 나눈 나머지를 R이라고 한다
 - 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다

```
def gcd(a,b):
  if a%b ==0:
    return b
  else:
    return gcd(b,a%b)
    
print(gcd(192,162)
```
#### 재귀함수 유의사항
 - 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성가능
 - 모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현할 수 있음
 - 재귀함수가 반복문보다 유리한경우도 있고 불리한 경우도 있음
 - 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
   + 스택을 사용해야 할 때 스택라이브러리 대신에 재귀함수를 이용하는 방법 사용

### DFS(Depth-First Search)
  - 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색
  - 스택 자료구조(재귀함수)를 이용
    1. 탐색의 시작 노드를 스택에 삽입하고 방문처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄.
    3. 2번의 과정을 수행할 수 없을 때까지 반복

#### DFS소스코드 예제
```
def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
 
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
```
### BFS(Breadth-First Search)
 - 너비우선탐색이라고 부르며 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
 - 큐 자료구조를 이용
   1. 탐색 시작 노드를 큐에 삽입하고 방문처리
   2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
   3. 2번의 과정을 수행할 수 없을 때까지 반복

```
from collections import deque
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    
    for i in graph[v]:
      if not visited[i]:
        queue.append(o)
        visited[i] = True
```




 
