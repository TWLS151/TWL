# SWEA - 5648
# 원자 소멸 시뮬레이션

# 0.5 초 단위가 있네
# 격자를 두 배로 키우고
# 마지막에 초를 반으로 나누면 되겠다.
# 1초에 1칸이니까
# 0.5초에 0.5 칸 간다.

import sys
sys.stdin = open('input.txt')

dirs = [
    (0, -1), (0, 1), (-1, 0), (1, 0)
]
di, dj = (1, -1, 0, 0), (0, 0, -1, 1)

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(atoms)):
        atoms[i][0] *= 2
        atoms[i][1] *= 2
    ans = 0
    # print(atoms)

    # 전처리 끝
    while atoms:
        # [1] 이동
        for i in range(len(atoms)):
            atoms[i][0]+=dj[atoms[i][2]]
            atoms[i][1]+=di[atoms[i][2]]

        # [2] 충돌, 처리
        v, ddel = set(), set()
        for i in range(len(atoms)):
            cj, ci = atoms[i][0], atoms[i][1]
            if (cj, ci) in v:
                ddel.add((cj, ci))
            else:
                v.add((cj, ci))

        # [3] 제거
        
        for i in range(len(atoms)-1, -1, -1):
            cj, ci = atoms[i][0], atoms[i][1]
            if (cj, ci) in ddel:
                ans += atoms[i][3]
                atoms.pop(i)
            elif max(abs(atoms[i][0]), abs(atoms[i][1])) > 2000:
                atoms.pop(i)

    print(f'#{test_case} {ans}')