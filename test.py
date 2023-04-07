from poc import *
import pytest


# test!
@pytest.mark.parametrize('x', list(range(10)))
def test(x) -> None:
    def ul(x: U) -> L:       return 2*x
    def ur(x: U) -> UR:      return x*x
    def bridge(x: L) -> LR:  return 3*x
    def ld(x: L) -> DL:      return x*x
    def rd(x: R) -> DR:      return x[0] + 2 * x[1]

    args = (ul, ur, bridge, ld, rd)
    assert (
        make_wheatstone_naive(*args)(x) ==
        make_wheatstone1(*args)(x) ==
        make_wheatstone2(*args)(x) ==
        make_wheatstone3(*args)(x)
    )
