def solution(s : str):
    nextIndex = {}
    i = 0
    n = len(s)
    answer = 0
    text_answer = ''
    for j in range(n):
        if s[j] in nextIndex:
            i = max(i, nextIndex[s[j]])

        nextIndex[s[j]] = j + 1
        if j - i + 1 > answer:
            answer = j - i + 1
            text_answer = s[i:j+1]

    s_list = list(s)
    answer_list = list(text_answer)
    count = 0
    for i in range(len(s_list) - len(answer_list) + 1):
        flag = True
        for j in range(len(answer_list)):
            if s_list[i+j] != answer_list[j]:
                flag = False
        if flag:
            count += 1
    return count






def test():
    a = 'ab'
    sol = solution(a)
    assert sol == 1

    a = 'abbab'
    sol = solution(a)
    assert sol == 2

    a = 'abcbabaabcabc'
    sol = solution(a)
    assert sol == 3

    # a = 'ababcd'
    # sol = solution(a)
    # assert sol == 4
    #
    # a = 'abba'
    # sol = solution(a)
    # assert sol == 2


    print("ok")


test()


'abcabcd'