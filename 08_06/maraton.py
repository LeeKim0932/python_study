
# 마라톤 완주를 하지 못한 선수 


def solution(participant, completion):
    answer = ' '
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


participant = ["leo","kiki","eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))
