
class BoxCollider2D():
    def __init__(self):
        pass
    import math

def check_collision(vectora, scalea, vectorb, scaleb):
    width_a, height_a = 1.0 * scalea.x, 1.0 * scalea.y
    width_b, height_b = 1.0 * scaleb.x, 1.0 * scaleb.y

    radius_a = math.hypot(width_a, height_a) / 2.0
    radius_b = math.hypot(width_b, height_b) / 2.0
    

    dx = vectorb.x - vectora.x
    dy = vectorb.y - vectora.y
    distance_sq = dx * dx + dy * dy
    max_distance_sq = (radius_a + radius_b) ** 2

    if distance_sq > max_distance_sq:
        return False

    half_w_a, half_h_a = width_a / 2.0, height_a / 2.0
    half_w_b, half_h_b = width_b / 2.0, height_b / 2.0
    
    x_overlap = abs(dx) < (half_w_a + half_w_b)
    y_overlap = abs(dy) < (half_h_a + half_h_b)
    
    return x_overlap and y_overlap