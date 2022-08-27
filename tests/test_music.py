import pygameextra as pe
pe.init()
from os import path
import pytest
scriptpath = str(path.realpath(__file__)).replace("test_music.py",'')

def test_load():
    pe.music.load(scriptpath+"testing_assets/test-music.ogg")


def test_play():
    pe.music.play(0)
    assert pe.music.get_t() > 0
    pe.time.sleep(100)


def test_pause():
    pe.music.pause()


def test_unpause():
    pe.music.unpause()


def test_restart():
    cur = pe.music.get_t()
    pe.music.restart()
    assert pe.music.get_t() < cur


def test_stop():
    pe.music.stop()


def test_set_v():
    pe.music.set_v(0.37)
    assert pe.music.volume == 0.37


def test_get_v():
    assert round(pe.music.get_v(), 2) == pytest.approx(0.35, 0.39)
    assert pe.music.volume == pytest.approx(0.35, 0.39)


def test_set_t():
    pe.music.stop()
    pe.music.play(1)
    pe.time.sleep(10)
    pe.music.set_t(537)
    assert pe.music.get_t() >= 537


def test_get_t():
    assert pe.music.get_t() >= 537


def test_fade():
    pe.music.fade(0)
    pe.music.fade(1)
    pe.music.fade(10)
    pe.music.fade(100)