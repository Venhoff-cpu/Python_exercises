def is_palindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = is_palindrome(s)

if ans:
    print("Yes")
else:
    print("No")


def num_palindrome(num):
    result = 0
    temp = num
    while temp > 0:
        dig = temp % 10
        result = result*10 + dig
        temp = temp//10

    return num == result


print(num_palindrome(121))
print(num_palindrome(223))
