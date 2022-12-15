"""Unitests for Triangle functions."""
from main import obvod, obsah, check_prav, uhly, check
import pytest


def test_obvod():
    """sss>0."""
    assert obvod([10, 30, 25]) == 65
    assert obvod([25.3, 60.8, 33.3]) == 25.3 + 60.8 + 33.3

    # return TypeError or IndexError in other cases
    with pytest.raises(TypeError):
        obvod(True)
    with pytest.raises(TypeError):
        obvod(5+5j)
    with pytest.raises(IndexError):
        obvod("r")


def test_obsah():
    """sss>0."""
    assert obsah([10, 20, 22.36], 26.18) == 99.9999997112

    # return TypeError in other cases
    with pytest.raises(TypeError):
        obsah(True, False)
    with pytest.raises(TypeError):
        obsah(5+5j, 7+9j)
    with pytest.raises(TypeError):
        obsah("r", "b")


def test_uhly():
    """sss>0."""
    assert uhly([158.11388300841898, 364.0054944640259, 206.15528128088303]) \
           == \
           (175.60129464500443, 2.4895529219991284, 1.9091524329963898)

    # return TypeError in other cases
    with pytest.raises(TypeError):
        uhly(True)
    with pytest.raises(TypeError):
        uhly(5+5j)
    with pytest.raises(TypeError):
        uhly("r")


def test_check_prav():
    """sss>0."""
    assert check_prav([3, 4, 5]) is True
    assert check_prav([5, 5, 5]) is False

    with pytest.raises(TypeError):
        check_prav(True)
    with pytest.raises(TypeError):
        check_prav(5+5j)
    with pytest.raises(TypeError):
        check_prav("r")


def test_check():
    """sss>0."""
    assert check([10, 30, 25]) is True

    # return TypeError, SystemExit, IndexError in other cases
    with pytest.raises(SystemExit):
        check([10, 30, 50])
    with pytest.raises(TypeError):
        check(5+5j)
    with pytest.raises(IndexError):
        check("r")
