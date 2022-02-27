def test_case():
    # 테스트 케이스 입력
    try:
        test_case = int(input('테스트 케이스 입력 : '))
    except ValueError:
        print('ValueError : Wrong Number!!')
    if not(1 <= test_case <= 50):
        raise ValueError

    return test_case


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self, index):
#         self.head = None
#         self.tail = None
#         self.index = index

#     def append(self, data, index):
#         new_node = Node(data)

#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node


def insert_list(seq):
    idx, num = map(int, input('삽입할 인덱스 위치와 숫자정보를 입력해 주세요 : ').split())
    seq.insert(idx, num)




for t in range(1, test_case() + 1):
    n, m, l = map(int, input('n, m, l 을 차례대로 입력하여 주세요 : ').split())
    
    seq = list(map(int, input('수열을 입력하시오 : ').split()))

    for _ in range(m):
        insert_list(seq)

    print(f'#{t} {seq[l]}')
