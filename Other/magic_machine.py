
def solution(S):
    new_list = S.split()
    stack = []
    for i in new_list:
        try:
            if i.isnumeric():
                if int(i) in range(0, (2**20)-1):
                    stack.append(int(i))
                else:
                    return -1
            elif i == "DUP":
                stack.append(stack[-1])
            elif i == "POP":
                stack.pop()
            elif i == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif i == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1-num2)

        except Exception:
            return -1

    if stack[-1] > 0:
        return stack[-1]
    else:
        return -1


string = "13 DUP 4 POP 5 DUP + DUP + -"
string2 = "5 6 + -"
string3 = "3 DUP 5 - -"

print(solution(string3))