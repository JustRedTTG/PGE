import pygameextra as pe
pe.init()
pe.Settings.UPDATE_AUTO = True
pe.display.make((100, 100), "Test pe.draw")
def test_rect():
    pe.fill.full(pe.color.black)
    pe.draw.rect(pe.color.white, (0, 0, 25, 25), 0)
    for x in range(0, 25):
        for y in range(0, 25):
            assert pe.display_a.get_at((x,y)) == pe.color.white
    pe.Layer[1][1] = (25, 25)
    pe.fill.full(pe.color.black)
    pe.draw.rect(pe.color.red, (0, 0, 25, 25), 0, layer=1)
    for x in range(25, 50):
        for y in range(25, 50):
            assert pe.display_a.get_at((x, y)) == pe.color.red


def test_line():
    pe.fill.full(pe.color.black)
    pe.draw.line(pe.color.green, (0, 0), (100, 100), 1)
    for i in range(0, 100):
        assert pe.display_a.get_at((i, i)) == pe.color.green


def test_circle():
    pe.fill.full(pe.color.black)
    pe.draw.circle(pe.color.yellow, (50, 50), 5, 0)
    assert pe.display_a.get_at((50, 50)) == pe.color.yellow
    assert pe.display_a.get_at((51, 50)) == pe.color.yellow
    assert pe.display_a.get_at((52, 50)) == pe.color.yellow
    assert pe.display_a.get_at((53, 50)) == pe.color.yellow
    assert pe.display_a.get_at((54, 50)) == pe.color.yellow


def test_ellipse():
    pe.fill.full(pe.color.black)
    pe.draw.ellipse(pe.color.yellow, (0, 0, 100, 100))
    for x in range(0, 100):
        assert pe.display_a.get_at((x, 50)) == pe.color.yellow