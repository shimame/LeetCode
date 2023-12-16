s = "MCMXCIV"
answer = 0
romans = list(s)
i = 0

while(i != len(romans)):
    if(romans[i] == 'I'):
        if(i+1 != len(romans)):
            if(romans[i+1] == 'V'):
                answer = answer + 4
                i = i + 1
            elif(romans[i+1] == 'X'):
                answer = answer + 9
                i = i + 1
            else: answer = answer + 1
        else: answer = answer + 1
    elif(romans[i] == 'V'):
        answer = answer + 5
    elif(romans[i] == 'X'):
        if(i+1 != len(romans)):
            if(romans[i+1] == 'L'):
                answer = answer + 40
                i = i + 1
            elif(romans[i+1] == 'C'):
                answer = answer + 90
                i = i + 1
            else: answer = answer + 10
        else: answer = answer + 10
    elif(romans[i] == 'L'):
        answer = answer + 50
    elif(romans[i] == 'C'):
        if(i+1 != len(romans)):
            if(romans[i+1] == 'D'):
                answer = answer + 400
                i = i + 1
            elif(romans[i+1] == 'M'):
                answer = answer + 900
                i = i + 1
            else: answer = answer + 100
        else: answer = answer + 100
    elif(romans[i] == 'D'):
        answer = answer + 500
    elif(romans[i] == 'M'):
        answer = answer + 1000
    i = i + 1
print("計算結果：" + str(answer))