# 테스트 케이스 입력
try:
    test_case = int(input('테스트 케이스 입력 : '))
except ValueError:
    print('ValueError : Wrong Number!!')
if not(1 <= test_case <= 50):
    raise ValueError


def rotation_queue(arr, m):
    for idx in range(m):
        p = arr.pop(0)
        arr.append(p)
    
    return arr




for i in range(1, test_case + 1):
    num, m = map(int, input('n과 m 을 입력해 주세요 : ').split())
    arr = list(map(int, input(f'{num}개의 자연수를 입력해 주세요 : ').split()))

    rotated_arr = rotation_queue(arr, m)
    print(f'#{i} {rotated_arr[0]}')





