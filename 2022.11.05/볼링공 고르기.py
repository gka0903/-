# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# numbers.sort()
# result = 0
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] != numbers[j]:
#             result += 1
# print(result)

# 정답

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지 무게를 답을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
print(data)
print(array)
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기
    print(n)
    print(result)

