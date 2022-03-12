# 테스트 케이스 입력
try:
    test_case = int(input('테스트 케이스 입력 : '))
except ValueError:
    print('ValueError : Wrong Number!!')
if not(1 <= test_case <= 50):
    raise ValueError

hex_numbers = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
    }


for t in range(1, test_case + 1):
    N, hex_number = input('변환시킬 16진수를 입력 : ').rstrip().split()
    bin_number = []

    for i in hex_number:
        bin_number.append(hex_numbers[i])
    
    answer = ''.join(bin_number)

    print(f'#{t} {answer}')

