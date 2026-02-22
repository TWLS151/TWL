import math  # math 모듈

origin_x, origin_y = 0, 0  # 기준점

target_points = [(1, 2), (-2, -3), (3, 1), (-1, 4)]

point_info_lst = []

for point_x, point_y in target_points:
    distance = math.sqrt(
        (point_x - origin_x)**2 + (point_y - origin_y)**2 
    )

    angle_radians = math.atan2(point_y - origin_y, point_x - origin_x)
    angle_degrees = math.degrees(angle_radians)

    point_data = (distance, angle_degrees, (point_x, point_y))
    point_info_lst.append(point_data)

point_info_lst.sort()

snd_closest = point_info_lst[1]

distance_from_origin = snd_closest[0]
angle = snd_closest[1]
pos = snd_closest[2]

print(f'점의 위치: {pos}, 거리: {distance_from_origin:.2f}, 각도: {angle:.2f}')
