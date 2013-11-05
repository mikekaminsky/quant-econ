#Consider the polynomial
#(1)      <-     p(x)=a_0+a_1x+a_2 x^2+...a_n x^n
#Write a function p such that p(x, coeff) that computes the value
# in (1) given a point x and a list of coefficients coeff

#Try to use enumerate() in your loop

def p(x,coeff):
    return sum(a* x**i for i, a in enumerate (coeff))

 