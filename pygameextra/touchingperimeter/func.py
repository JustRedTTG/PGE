def touching_perimeter_left(rects, r):
    return sum(max(0, min(pr.bottom, r.bottom) - max(pr.y, r.y)) for pr in rects if pr.x == r.x or pr.right == r.x)


def touching_perimeter_right(rects, r):
    return sum(
        max(0, min(pr.bottom, r.bottom) - max(pr.y, r.y)) for pr in rects if pr.right == r.right or pr.x == r.right)


def touching_perimeter_top(rects, r):
    return sum(
        max(0, min(pr.right, r.right) - max(pr.x, r.x)) for pr in rects if pr.bottom == r.bottom or pr.y == r.bottom)


def touching_perimeter_bottom(rects, r):
    return sum(max(0, min(pr.right, r.right) - max(pr.x, r.x)) for pr in rects if pr.y == r.y or pr.bottom == r.y)


def touching_perimeter(rects, r):
    return sum((touching_perimeter_right(rects, r),
                touching_perimeter_top(rects, r),
                touching_perimeter_bottom(rects, r),
                touching_perimeter_left(rects, r)))
