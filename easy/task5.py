def num_judge(num: int) -> int:
    if num % 2 == 0:
        result = print(f"入力された{num}は、偶数です")
    else:
        result = print(f"入力された{num}は、奇数です")
    return result

if __name__ == "__main__":
    num_judge(5)
    num_judge(6)