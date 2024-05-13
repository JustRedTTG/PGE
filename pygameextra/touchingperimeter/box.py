class Box:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def would_fit_in(self, r):
        return self.w <= r.w and self.h <= r.h

    def __lt__(self, b):
        return self.w * self.h < b.w * b.h

    def __str__(self):
        return '{} x {}'.format(self.w, self.h)

    def __repr__(self):
        return str(self)
