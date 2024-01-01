def strStr(haystack, needle):
    position = 0

    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)):
        print('i = ' + str(i))
        match = True #一致しているものとして探索開始
        for j in range(len(needle)):
            if len(haystack) <= i + j:
                match = False
                return -1
            
            if (haystack[i + j] != needle[j]):
                match = False #一致しなかった
                print('i = ' + str(i) + '   j = ' + str(j))
                print('Break!!')
                break
            else:
                position = i + j - (len(needle) - 1)
                print('i = ' + str(i) + '   j = ' + str(j))
                print('match = ' + str(match))
        if match: #すべての文字が一致していれば出力
            print('True')
            return position
    return -1

haystack = "mississippi"
needle = "issipi"
print(strStr(haystack,needle))