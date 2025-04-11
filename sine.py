digit = float(input("Enter the sine value you want to calculate in radians : \n"))
radian = 3.141592654/digit
ans = radian - (radian**3/6)
ans1 = ans + (radian**5/120)
ans2 = ans1 - (radian**7/5040)
trueans = ans2 + (radian**9/362880)
cos = 1 - (radian**2/2)
cos1 = cos + (radian**4/24)
cos2 = cos1 - (radian**6/720)
truecos = cos2 + (radian**8/40320)
tan = trueans/truecos
print("the sine value is : ", trueans)
print("the cosine value is : ", truecos)
print("The tangent value is : ", tan)
