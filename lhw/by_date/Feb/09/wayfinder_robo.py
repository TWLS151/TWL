def get_final_position(commands):
    # 시작 위치
    r, c = 0, 0

    # 여기에 코드를 작성하세요.
    move = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }

    for command in commands:
        dr, dc = move[command]
        r += dr
        c += dc

    return r, c

# 테스트
commands = ['E', 'E', 'S', 'W', 'N']
end_r, end_c = get_final_position(commands)
print(f"최종 위치: ({end_r}, {end_c})") # 최종 위치: (0, 1)