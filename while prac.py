# i = 0
# while i < 1000:
#     i = i + 1
#     if i == 500:
#         break
#     print("대기번호:", i, "번 입니다.")
#
# else:
#     print("대기번호가 1000번 초과입니다.")
#
#     print("아진짜너무잠온다이제그만했으면좋겠다오늘머리다썼다나한계다이제그만그만그만")

# 1. 1부터 100까지의 수를 반복 출력
# 2. 반복되는 수가 홀수인지를 확인
# 3. 홀수라면 그 값을 저장
# 4. 저장된 값들의 합을 구함
# index 변수가 하는 역할: 수열 만들기, 반복문 제어
# result 역할: 연산하는 값 저장
index = 1
#result = []
result = 0
while index < 100 :
    index = index + 1
    if index % 2 == 1 :
        #result.append(index)
        result = result + index
#print(sum(result))
print(result)

