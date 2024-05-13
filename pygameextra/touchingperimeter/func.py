def touching_perimeter_left(rects, r):
    return sum(max(0, min(pr.t, r.t) - max(pr.y, r.y)) for pr in rects if pr.x == r.x or pr.r == r.x)

def touching_perimeter_right(rects, r):
    return sum(max(0, min(pr.t, r.t) - max(pr.y, r.y)) for pr in rects if pr.r == r.r or pr.x == r.r)

def touching_perimeter_top(rects, r):
    return sum(max(0, min(pr.r, r.r) - max(pr.x, r.x)) for pr in rects if pr.t == r.t or pr.y == r.t)

def touching_perimeter_bottom(rects, r):
    return sum(max(0, min(pr.r, r.r) - max(pr.x, r.x)) for pr in rects if pr.y == r.y or pr.t == r.y)

def touching_perimeter(rects, r):
    return sum((touching_perimeter_right(rects, r),
                touching_perimeter_top(rects, r),
                touching_perimeter_bottom(rects, r),
                touching_perimeter_left(rects, r)))