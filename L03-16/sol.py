def is_brackets_balanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    in_string = False
    quote_char = ''
    
    for ch in expression:
        if ch in ('"', "'"):
            if not in_string:
                in_string = True
                quote_char = ch
            elif quote_char == ch:
                in_string = False
        elif not in_string:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()
    return len(stack) == 0

expression = input("input: ")

if is_brackets_balanced(expression):
    print("valid parentheses")
else:
    print("invalid parentheses")