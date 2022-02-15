import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='number', type=int, required=False)
    n = parser.parse_args().number if parser.parse_args().number else 10
    res = solution(n)
    print("yay") if res == 23 else print(res)


def solution_r(n):
    # Forcing recursion for no good reason. But it passed so....
    if n <= 0:
        return n
    return solution_r(n - 1) if (n % 3 and n % 5) else n + solution_r(n - 1)


def solution(number):
    if not isinstance(number, int):
        return 0
    return solution_r(number-1)


if __name__ == '__main__':
    main()
