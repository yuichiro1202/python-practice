def fib(n: int) -> int:
    """
    フィボナッチ数列をリストで管理する版
    大きな数でも効率的に計算可能
    """
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    
    # リストで管理
    fib = [0, 1, 1]  # F(0), F(1), F(2)
    
    for num in range(3, n + 1):
        fib.append(fib[num-1] + fib[num-2])
    return fib[n]

if __name__ == "__main__":
    print(fib(10))

