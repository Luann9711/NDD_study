# List2-5th-count_purple
print('Type test case number (T), 1<=T<=50')
T = int(input())
if (T < 1) or (T > 50):
    raise ValueError('T should be a positive integer, 1<=T<=50')
for test_case in range(1, T + 1):
    print('Type number of colored area (N), N is a integer and 2<=N<=30')
    N = int(input())
    if (N < 2) or (N > 30):
        raise ValueError('N should be an integer between 2 and 30')
    colored_area_idx = []
    colored_area_color = []
    for num_area in range(N):
        print('Type'+str(num_area)+'th area left corner index (r1,c1), \
            right corner index (r2,c2),  and color (1 or 2)')
        r1, c1, r2, c2, pcolor = map(int, input().split())
        if not all(0 <= corner_idx <= 9 for corner_idx in [r1, c1, r2, c2]):
            raise ValueError('r1, c1, r2, c2 should be between 0 and 9')
        elif (r1 <= r2) or (c1 <= c2):
            raise ValueError('As left and right corner, r1 < r2 and c1 < c2')
        elif pcolor not in [1, 2]:
            raise ValueError('Color is either 1(red) or 2(blue)')
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if [row, col] not in colored_area_idx:
                    colored_area_idx.append([row, col])
                    colored_area_color.append(pcolor)
                else:
                    exist_idx = colored_area_idx.index([row, col])
                    if colored_area_color[exist_idx] != 3:
                        if colored_area_color[exist_idx] != pcolor:
                            colored_area_color[exist_idx] = 3
    purple = 0
    for count in range(len(colored_area_color)):
        if colored_area_color[count] == 3:
            purple = purple+1
    print("Output: [#Test number] [Number of purple area]")
    print("#"+str(test_case)+" "+str(purple))
