from sympy import nsimplify
from fractions import Fraction
from sympy import nsimplify, pi , sqrt


def approximation(result):
        
    expr = result
    f = Fraction(expr).limit_denominator()
    approx_pi = nsimplify(expr, [pi])
    approx_sqrt2 = nsimplify(expr, [sqrt(2)])
    approx_sqrt3 = nsimplify(expr, [sqrt(3)])
    approx_sqrt5 = nsimplify(expr, [sqrt(5)])
    approx_sqrt7 = nsimplify(expr, [sqrt(7)])
    approx_sqrt10 = nsimplify(expr, [sqrt(10)])


    num = f.numerator
    denom = f.denominator
    approx_str_pi = str(approx_pi)
    approx_str_sqrt2 = str(approx_sqrt2)
    approx_str_sqrt3 = str(approx_sqrt3)
    approx_str_sqrt5 = str(approx_sqrt5)
    approx_str_sqrt7 = str(approx_sqrt7)
    approx_str_sqrt10 = str(approx_sqrt10)

    if 'pi' in approx_str_pi and len(approx_str_pi) < 9 :
        return(approx_pi)
    elif ((num < 100 and denom < 10) or (num < 10 and denom < 100)):
        return(f)
    elif 'sqrt' in approx_str_sqrt2 and len(approx_str_sqrt2) < 14:
        return(approx_sqrt2)
    elif 'sqrt' in approx_str_sqrt3 and len(approx_str_sqrt3) < 14:
        return(approx_sqrt3)
    elif 'sqrt' in approx_str_sqrt5 and len(approx_str_sqrt5) < 14:
        return(approx_sqrt5)
    elif 'sqrt' in approx_str_sqrt7 and len(approx_str_sqrt7) < 14:
        return(approx_sqrt7)
    elif 'sqrt' in approx_str_sqrt10 and len(approx_str_sqrt10) < 14:
        return(approx_sqrt10)
    else:
        return(expr)
    

print(approximation(4.7915742375))
