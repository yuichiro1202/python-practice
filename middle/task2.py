def word_count(text: str) -> str:
    count_result = print(len(text.split()))
    return count_result

if __name__ == "__main__":
    word_count("I like Pyhton")