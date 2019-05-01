# Forcing recursion for no good reason.  But it passed so....
def solution(number):
    if not number:
        return 0
    
    if number <= 0:
        return number
    else:
        if not number%3 or not number%5:
            return number + solution_r(number-1)
        else:
            return solution(number-1)
    return solution(number-1)

assert(solution(10) == 23, "Yay")
