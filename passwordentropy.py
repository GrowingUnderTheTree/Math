import math
import matplotlib.pyplot as plt
import numpy as np
import re
import random
import string

print("Enter your password : ")
pwd = input()
yes = len(pwd)
print("The length of your password is : ", yes)
birthday = '^(?:(?:1[6-9]|[2-9]\d)?\d{2})(?:(?:(\/|-|\.)(?:0?[13578]|1[02])\1(?:31))|(?:(\/|-|\.)(?:0?[13-9]|1[' \
           '0-2])\2(?:29|30)))$|^(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[' \
           '3579][26])00)))(\/|-|\.)0?2\3(?:29)$|^(?:(?:1[6-9]|[2-9]\d)?\d{2})(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(' \
           '?:0?[1-9]|1\d|2[0-8])$ '
result = re.match(birthday, pwd)
pool = 72
# assume that there's latin letter, numbers and special character in your password.
arr = np.arange(yes)
character = arr[arr != 0]
size = yes
lengthofarr = len(arr)
minus = lengthofarr - 2
# ans = np.array([math.log2(pool ** character)])
# print(ans)
Entropy = []
Guesses = []
Time = []
for x in range(yes):
    if x < size - 1:
        calc = x + 1
        ans = math.log2(pool ** calc)
        gn = 2 ** ans
        # gn = Number of guesses needed
        time = gn / 100000000000
        print(gn)
        print(ans)
        Entropy.append(ans)
        Guesses.append(gn)
        Time.append(time)
print("The pool of your character is : ", pool)
print("The Entropy is : ", Entropy)
print("The amount of character is : ", character)
print("The guesses needed is : ", Guesses)
print("The time needed(in seconds) is : ", Time)
# plt.plot(character, Entropy)
plt.plot(character, Time)
# Assuming 100 billion guesses per second
plt.title("Time needed to crack password(in seconds)")
plt.show()

pwdgen = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()")
random.shuffle(pwdgen)
password = []
for i in range(9):
    password.append(random.choice(pwdgen))
random.shuffle(password)
x = "".join(password)

print(minus)
print("\n\n\n\n\n")
print("The Entropy of your password is : ", Entropy[minus])
print("The time needed to crack your password by pure bruteforce is : ", Time[minus], " Seconds.")
with open('alot.txt') as file:
    contents = file.read()
    search_word = pwd
    if search_word in contents:
        print('Your password existed in a password database, Not recommended')
        print(x, " is recommended to be used as a password. ")
    else:
        print('Your password does not exist in a password database, recommended')
    if result:
        print("Setting your birthday as password is not recommended too.")
    else:
        print("\n")
