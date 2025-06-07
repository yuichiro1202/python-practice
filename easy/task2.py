import sys

def num_sum(num1, num2: int) -> int:
    if not type(num1) | type(num2) == int:
        print(f"入力された値が無効です")
        sys.exit()
    else:
        result = num1 + num2
    return result


if __name__ == "__main__":
    print(num_sum(3,5))
    print(num_sum(1.5,2))