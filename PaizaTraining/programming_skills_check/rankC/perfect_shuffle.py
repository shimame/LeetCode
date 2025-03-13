# デッキがn枚ならp回シャッフルしたとき元の状態に戻る。式は2^p≡1(mod n-1)です。
# C162.pyがパーフェクトシャッフルの問題

def find_cycle_length(m):
    x, p = 2, 1
    mod_val = m - 1
    while x % mod_val != 1:
        x = (x * 2) % mod_val
        p += 1
    return p