#discrete fourier transform
import scipy.constants
import math
def dft(xn, cycles, currenttimeindex, numofsamples):
    inside = (2 * scipy.constants.pi * cycles * currenttimeindex)/numofsamples
    sinusoid = complex(math.cos(inside),-1 * math.sin(inside))
    ans = xn * sinusoid
    return ans
k = 1
xn = [1,0,-1,0]
N = len(xn)
initial = 0
for i in range(0,N-1):
    initial += dft(xn[i],k,i,N)
print(initial)

def magnitude(results):
    re = results.real
    im = results.imag
    ans = math.sqrt((re*re)+(im*im))
    return ans

print(magnitude(initial))

def decibels(magnitude):
    ans = 20 * math.log10(magnitude)
    return ans

print(decibels(magnitude(initial)))