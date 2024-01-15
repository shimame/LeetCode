def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    answer = []
    if 1 <= n <= 8:
        for i in range(n):
            k = ""
            for j in range(n - i):
                k += "()"
            answer.append(k)
        #for i in range(n):

        return answer
    else:
        return ""


n = 4
print(generateParenthesis(n))  