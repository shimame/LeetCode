n, m = map(int, input().split())
passed_students = []
for i in range(n):
    # テストの点数, 欠席回数
    score, absence_count = map(int, input().split())
    val = score - absence_count * 5
    if val < 0:
        val = 0
    if val >= m:
        passed_students.append(i+1)
print("\n".join(map(str, passed_students)))