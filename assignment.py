
# 과제 1. 별찍기 (4월 20일까지)
# - 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요

for i in range(10,0,-1):
    if i ==6:continue
    print(i* "*")

# 과제 2. 구구단 (4월 20일까지)
# - 구구단 2단을 출력해보세요!
for i in range(1, 10):
    print(2*i)

# 과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)
i = 0
sum = 0
while i < 1000:
    i+=1
    if i%3 == 0:
        sum += i
print(sum)


# 과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
# - mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
sum = 0
for i in mutsa_scores:
    sum += i
avg = sum/len(mutsa_scores)
print(avg)

# 과제 5. input.py 문제 2개 풀기 (4월 20일까지)
