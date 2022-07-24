#!/bin/python3

# Complete the 'isBalanced' function below.
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    if len(brackets) % 2 != 0:
        return "NO"
    open_brackets_str = "([{"
    open_brackets = []
    for character in brackets:
        if character in open_brackets_str:
            open_brackets.append(character)
        elif character == ")" and open_brackets[-1] == "(":
            open_brackets.pop()
        elif character == "]" and open_brackets[-1] == "[":
            open_brackets.pop()
        elif character == "}" and open_brackets[-1] == "{":
            open_brackets.pop()
        else:
            return "NO"
    return "YES"


if __name__ == "__main__":

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep="\n")
