# Forcing recursion for no good reason.  But it passed so....

def solution_r(n):
    if n <= 0:
        return n
    else:
        if not n%3 or not n%5:
            return n + solution_r(n-1)
        else:
            return solution_r(n-1)

def solution(number):
    if not number:
        return 0
    return solution_r(number-1)

assert solution(10) == 23, "Oops, recursion is the devil"
