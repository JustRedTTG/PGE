class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    @property
    def r(self):
        return self.x + self.w

    @property
    def t(self):
        return self.y + self.h

    @property
    def tl(self):
        return self.x, self.t

    @property
    def tr(self):
        return self.r, self.t

    @property
    def bl(self):
        return self.x, self.y

    @property
    def br(self):
        return self.r, self.y

    def __eq__(self, r):
        return (self.x, self.y, self.w, self.h) == (r.x, r.y, r.w, r.h)

    def __lt__(self, r):
        return self.area() < r.area()

    def intersection(self, rect):
        if self.x >= rect.r or self.r <= rect.x or self.y >= rect.t or self.t <= rect.y:
            return None
        x = max(self.x, rect.x)
        y = max(self.y, rect.y)
        r = min(self.r, rect.r)
        t = min(self.t, rect.t)
        return Rect(x, y, r - x, t - y)

    def substracted(self, r):
        i = self.intersection(r)
        if i is None:
            return [self.clone()]
        if i == self:
            return []
        tl = self.inside(r.tl)
        tr = self.inside(r.tr)
        bl = self.inside(r.bl)
        br = self.inside(r.br)
        # check every case
        if tl and not (tr or bl or br):
            return [
                Rect(self.x, self.y, r.x - self.x, self.h),
                Rect(self.x, r.t, self.w, self.t - r.t)
            ]
        if tr and not (tl or bl or br):
            return [
                Rect(self.x, r.t, self.w, self.t - r.t),
                Rect(r.r, self.y, self.r - r.r, self.h)
            ]
        if bl and not (tl or tr or br):
            return [
                Rect(self.x, self.y, self.w, r.y - self.y),
                Rect(self.x, self.y, r.x - self.x, self.h)
            ]
        if br and not (tl or tr or bl):
            return [
                Rect(self.x, self.y, self.w, r.y - self.y),
                Rect(r.r, self.y, self.r - r.r, self.h)
            ]
        if tl and tr and not (bl or br):
            return [
                Rect(self.x, self.y, r.x - self.x, self.h),
                Rect(r.r, self.y, self.r - r.r, self.h),
                Rect(self.x, r.t, self.w, self.t - r.t)
            ]
        if tl and bl and not (tr or br):
            return [
                Rect(self.x, self.y, self.w, r.y - self.y),
                Rect(self.x, r.t, self.w, self.t - r.t),
                Rect(self.x, self.y, r.x - self.x, self.h)
            ]
        if tr and br and not (tl or bl):
            return [
                Rect(self.x, self.y, self.w, r.y - self.y),
                Rect(self.x, r.t, self.w, self.t - r.t),
                Rect(r.r, self.y, self.r - r.r, self.h)
            ]
        if bl and br and not (tl or tr):
            return [
                Rect(self.x, self.y, r.x - self.x, self.h),
                Rect(r.r, self.y, self.r - r.r, self.h),
                Rect(self.x, self.y, self.w, r.y - self.y)
            ]
        if tr and tl and bl and br:
            return [
                Rect(self.x, r.t, self.w, self.t - r.t),
                Rect(self.x, self.y, r.x - self.x, self.h),
                Rect(self.x, self.y, self.w, r.y - self.y),
                Rect(r.r, self.y, self.r - r.r, self.h)
            ]
        if (self.x < r.x < self.r) and (self.r <= r.r):
            return [
                Rect(self.x, self.y, r.x - self.x, self.h),
            ]
        if (self.y < r.y < self.t) and (self.t <= r.t):
            return [
                Rect(self.x, self.y, self.w, r.y - self.y),
            ]
        if (self.x < r.r < self.r) and (r.x <= self.x):
            return [
                Rect(r.r, self.y, self.r - r.r, self.h),
            ]
        if (self.y < r.t < self.t) and (r.y <= self.y):
            return [
                Rect(self.x, r.t, self.w, self.t - r.t),
            ]
        if self.x < r.x < self.r and self.x < r.r < self.r:
            return [
                Rect(self.x, self.y, r.x - self.x, self.h),
                Rect(r.r, self.y, self.r - r.r, self.h)
            ]
        if self.y < r.y < self.t and self.y < r.t < self.t:
            return [
                Rect(self.x, self.y, self.w, r.y - self.y),
                Rect(self.x, r.t, self.w, self.t - r.t)
            ]
        raise Exception('Should never get here! {} - {}'.format(self, r))

    def inside(self, r):
        if isinstance(r, Rect):
            return (r.x < self.x < r.r) and \
                (r.x < self.r < r.r) and \
                (r.y < self.y < r.t) and \
                (r.y < self.t < r.t)
        return (self.x < r[0] < self.r) and (self.y < r[1] < self.t)

    def clone(self):
        return Rect(self.x, self.y, self.w, self.h)
