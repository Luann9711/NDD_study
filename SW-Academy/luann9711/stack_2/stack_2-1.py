# 테스트 케이스 입력
try:
    test_case = int(input('테스트 케이스 입력 : '))
except ValueError:
    print('ValueError : Wrong Number!!')
if not(1 <= test_case <= 50):
    raise ValueError

c = test_case + 1

stack = []
op_check = ['+', '-', '*', '/', '.']
a1 = 0
a2 = 0

def input_code():
    try:
        code = list(map(str, input('256자 이내의 연산코드 입력 : ').split()))
    except ValueError:
        print('ValueError : Over length!!')
    if len(code) > 256:
        raise ValueError
    
    return code

def main(code):
    for i in range(len(code)):
        if code[i].isdigit():
            stack.append(int(code[i]))
        
        elif code[i] == '.':
            return stack.pop()
        
        elif len(stack) < 2:
            return 'error'
        
        elif code[i] == '+': # + 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 + a2)
        elif code[i] == '-': # - 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 - a2) 
        elif code[i] == '*': # * 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 * a2)
        elif code[i] == '/': # / 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 / a2)

while test_case > 0:
    result = main(input_code())
    print(f'#{c - test_case} {result}')
    test_case -= 1

