def test_case():
    '''
    테스트 케이스 입력 및 반환
    '''
    test_case_number = int(input('테스트 케이스 입력 : '))
    return test_case_number


def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        visiting = stack.pop()

        if visiting not in visited:
            visited.append(visiting)
            stack += list(graph[visiting] - set(visited))
    return visited


for t in range(1, test_case() + 1):
    dict_graph = dict()
    e, n = map(int, input('e와 n의 값을 입력해 주세요 : ').strip().split())
    line_info = list(map(int, input('간선의 정보를 입력해 주세요 : ').strip().split()))

    for key in line_info:
        dict_graph[key] = set()

    for idx in range(0, len(line_info), 2):
        dict_graph[line_info[idx]].add(line_info[idx + 1])


    print(f'#{t} {len(DFS(dict_graph, n))}')


