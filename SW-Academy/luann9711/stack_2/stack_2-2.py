def f2(i, j, N):
    if maze[i][j] == 3:
        return 1
    
    else:
        maze[i][j] = 1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            print(ni, nj)

            # 탐색방향이 통로이면
            if (0 <= ni < N) and (0 <= nj < N) and (maze[ni][nj] != 1):
                if f2(ni, nj, N):
                    print(ni, nj)
                    return 1
        return 0


# 테스트 케이스 입력
try:
    test_case = int(input('테스트 케이스 입력 : '))
except ValueError:
    print('ValueError : Wrong Number!!')
if not(1 <= test_case <= 50):
    raise ValueError


for t in range(1, test_case + 1):    
    N = int(input('미로의 크기 N 을 입력하세요 : '))
    maze = [list(map(int, input('미로를 구성해 주세요 : '))) for _ in range(N)]
    
    # for a in range(N):
    #     for b in range(N):
    #         maze[a][b] == int(maze[a][b])
    
    for a in range(N):
        if 2 in maze[a]:
            start=(a, maze[a].index(2))
    
    print(f'#{t} {f2(start[0], start[1], N)}')



    








