# # 리스트에서 특정 값의 원소를 모두 제거하기
# a = [1,2,3,4,5,5,5]
#
#
# #remove_List에 포함되지 않은 값 만을 저장
# remove_set = {3,5}
# result = [i for i in a if i not in remove_set]
#
#
# print(result)

# # 리스트의 인덱싱과 슬라이싱
# a = "Hello"
# b = "World"
# print(a + " " + b)
#
# a = "String"
# print(a * 3)
#
# a = "ABCDEF"
# print(a[2:4])

# a = (1,2,3,4)
# print(a)
# a[2] = 7

# #사전 자료형
#
# data = dict()
#
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#
# print(data)
#
# if '사과' in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")
#
# print(list(data.keys()))
# print(list(data.values()))
# print(data.keys())
# print(data.values())


# #사전 자료형 관련 함수
#
# data = dict()
#
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#
# # 키 데이터만 담은 리스트
# key_list = data.keys()
# # 값 데이터만 담은 리스트
# value_list = data.values()
# print(key_list)
# print(value_list)
#
# # 각 키에 따른 값을 하나씩 출력
# for key in key_list:
#     print(data[key])

# #집합 자료형
#
# #집합 자료형 초기화 방법1
# data = set([1,2,3,4,4,5,])
# print(data)
#
# #집합 자료형 초기화 방법2
# data = {1,1,2,3,4,4,5}
# print(data)


# # 정수 1이 존재하는지 확인
# a = {1,2,3}
#
# a.add(3)
#
# print(1 in a)

# #집합 자료형
# a= set([1,2,3,4,5])
# b = set([3,4,5,6,7])
#
# #합집합
# print(a | b)
#
# #교집합
# print(a & b)
#
# #차집합
# print(a - b)


# #집합 자료형 관련 함수
# data = set([1,2,3])
# print(data)
#
# #새로운 원소 추가
# data.add(4)
# print(data)
#
# #새로운 원소 여러개 추가
# data.update([5,6])
# print(data)
#
# #특정한 값을 갖는 원소 삭제
# data.remove(3)
# print(data)

# a = ['H', 'e', 'l', 'l', 'o']
#
# print(set(a))


# a = [1,2,3]
#
# #append 뒤에 붙여준다
# a.append(4)
# print(a)
#
# #넣고 정렬
# a = {0,1,2,5}
#
# a.add(4)
# print(a)

# #입력을 위한 전형적인 소스코드 1)
#
# #데이터의 개수 입력
# n = int(input())
# #각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))
#
# print(n)
# print(data)


# 입력: 1 2 3 4 5
# input().split() : ['1','2','3','4','5']
# map(int , input().split()): map([1,2,3,4,5])

# a = list(map(int, input().split()))
# print(a)

a,b,c,d,e = map(int, input().split())

print(a,b,c,d,e)