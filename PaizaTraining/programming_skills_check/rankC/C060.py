# 辞書に載せる単語の数を表す整数 N、1 ページに掲載する単語の数 K、調べたいページの番号 P 
n, k, p = map(int, input().split())
words = input().split()
words.sort()
for i in range(n):
    if i == p - 1:
        print("\n".join(words[k*i:k*(i+1)]))