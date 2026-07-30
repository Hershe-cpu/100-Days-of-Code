def process_test_cases(t):
    if t == 0:
        return ""

    x = int(input())
    yns = list(map(int, input().split()))

    total = sum(map(lambda n: n ** 4 if n <= 0 else 0, yns))

    rest = process_test_cases(t - 1)
    return str(total) + "\n" + rest


def main():
    n = int(input())
    print(process_test_cases(n))


if __name__ == "__main__":
    main()