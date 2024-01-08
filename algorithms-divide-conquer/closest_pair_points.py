import math


def closest_points(p_x, p_y):
    if len(p_x) + len(p_y) <= 4:
        min_dist = math.inf
        min_pair = []
        points = p_x + p_y
        points = list(set(points))
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist_p = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if dist_p < min_dist:
                    min_dist = dist_p
                    min_pair = [points[i], points[j]]
        return min_pair
    q_x, r_x = (p_x[:len(p_x)//2], p_x[len(p_x)//2:])
    q_y, r_y = (p_y[:len(p_y)//2], p_y[len(p_y)//2:])
    p1, q1 = closest_points(q_x, q_y)
    p2, q2 = closest_points(r_x, r_y)
