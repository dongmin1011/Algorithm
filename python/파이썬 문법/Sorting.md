# 정렬
 - 데이터를 특정한 기준에 따라 순서대로 나열한 것
 - 일반적으로 문제상황에 따라 적절한 정렬 알고리즘이 공식처럼 사용

---
### 선택 정렬
 * 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

```
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_mindex] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]
  
print(array)
```
선택정렬의 시간 복잡도
  - 선택정렬은 N번만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
  - 전체 연산횟수는 N+(N-1)+(N-2)+...+2
  - 빅오 표기법에 따라 O(N^2)라고 작성

---
### 삽입 정렬
  * 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
  * 선택 정렬에 비해 구현 난이도가 높은 편이지만 효율적으로 작동

```
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else: break
print(array)
```
삽입정렬의 시간 복잡도
 - 시간 복잡도는 O(N^2)이며 선택정렬과 마찬가지로 반복문이 두 번 중첩되어 사용
 - 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
    * 최선의 경우 O(N)

---
### 퀵 정렬
 - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
 - 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘
 - 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
 - 첫번째 데이터를 기준 데이터(pivot)로 설정

이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있다
 - 평균의 경우 O(NlogN)의 시간복잡도
 - 최악의 경우 O(N^2)의 시간복잡도를 가진다.

```
array = [7,5,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
  if start>=end:
    return
  pivot = start
  left = start+1
  right = end
  while left<=right:
    while left <=end and array[left] <= array[pivot]:
      left+=1
    while right>start and array[right]>=array[pivot]:
      right-=1
    
    if left>right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
      
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)
    
 quick_sort(array, 0 , len(array)-1)
    
```
파이썬의 장점을 살린 방식
```
array = [7,5,9,0,3,1,6,2,4,8]
def quick_sort(array):
  if len(array)<=1:
    return array
  pivot = array[0]
  tatil = array[1:]
  
  left_side = [x for x in tail if x<=pivot]
  right_side = [x for x in tail if x>pivot]
  
  return quick_sort(left_side)+[pivot]+quick_sort(right_side)
  
  
```
### 계수정렬
 - 특정한 조건이 부합할 떄만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
   * 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용
 - 데이터의 개수가 N, 데이터 중 최댓값이 K일 때 최악의 경우에도 수행시간 O(N+K)를 보장

```
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]]+=1
  
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
```
계수정렬의 복잡도 분석
 - 시간복잡도와 공간복잡도 모두 O(N+K)
 - 때에 따라서 심각한 비효율성을 초래할 수 있음
 - 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사

