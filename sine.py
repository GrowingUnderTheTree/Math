digit = float(input("Enter the sine value you want to calculate : \n"))
angle = 180/digit
radian = 3.141592654/angle
ans = radian - (radian**3/(3 * 2 * 1))
ans1 = ans + (radian**5/(5 * 4 * 3 * 2 * 1))
ans2 = ans1 - (radian**7/(7 * 6 * 5 * 4 * 3 * 2 * 1))
trueans = ans2 + (radian**9/(9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1))
cos = 1 - (radian**2/(2 * 1))
cos1 = cos + (radian**4/(4 * 3 * 2 * 1))
cos2 = cos1 - (radian**6/(6 * 5 * 4 * 3 * 2 * 1))
truecos = cos2 + (radian**8/(8 * 7 * 6 * 5 * 4 * 3 * 2 * 1))
tan = trueans/truecos
print("the sine value is : ", trueans)
print("the cosine value is : ", truecos)
print("The tangent value is : ", tan)