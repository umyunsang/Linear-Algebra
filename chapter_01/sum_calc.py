# 먼저 정수의 개수를 입력 받은 다음, 해당하는 개수만큼의
# 정수를 입력 받아 합을 계산하는 함수 calc() 함수를 작성하라.

# 정수의 개수를 입력받고, 해당하는 개수만큼 정수를 입력받아 그 합을 계산하는 함수
def calc(n):
    total_sum = 0  # 합계를 저장할 변수 초기화
    for i in range(n):  # 0부터 n-1까지 반복
        total_sum += int(input())  # 사용자로부터 정수 입력받아 합계에 추가
    return total_sum  # 최종 합계를 반환


print("Input the number of values to be added => ")
count = int(input())  # 사용자로부터 정수의 개수 입력받기
while count <= 0:  # 입력된 개수가 0 이하인 경우 반복 입력받기
    print("Please enter a positive integer.")
    count = int(input())

print("Sum = ", calc(count))  # 계산된 합계를 출력
