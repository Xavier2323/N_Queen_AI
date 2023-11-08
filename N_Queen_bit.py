def lowbit(x):
    return x & -x

def dfs(M, L, R, qL, qR, table):
    global ans, m, MASK

    if M == MASK:
        ans = ans + 1
        print(table)
        return

    Legal = MASK & ~(M | L | R | qL | qR)
    if m:
        while Legal:
            num = lowbit(Legal)
            Legal ^= num
            m -= 1
            table.append(num.bit_length()-1)
            dfs(M | num, (L | num) << 1, (R | num) >> 1, qL << 1, qR >> 1, table)
            table.pop()
            m += 1


if __name__ == "__main__":
    m = 8 
    MASK = (1 << m) - 1
    ans = 0
    dfs(0, 0, 0, 0, 0, [])
    print(ans)
