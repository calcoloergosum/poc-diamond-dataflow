"""Demonstration of series-parallel representation of Wheatstone graph"""
from typing import Callable, Tuple, TypeVar, Any


U = int  # up; source
L = int  # left
UR = int  # right1
LR = int  # right2
R = Tuple[LR, UR]

DL = int  # bottom
DR = int  # bottom
D = Tuple[DL, DR]  # down; sink


def make_wheatstone_naive(
    ul: Callable[[U], L],
    ur: Callable[[U], UR],
    bridge: Callable[[L], LR],
    ld: Callable[[L], DL],
    rd: Callable[[R], DR]
) -> Callable[[U], D]:
    r"""
    This graph is not series parallel.
    U
    | \
    |  \
    L -> R
      \  |
       \ |
         D
    """
    def wheatstone(x: U) -> D:
        l = ul(x)
        return (ld(l), rd((bridge(l), ur(x))))
    return wheatstone


# Let's make it series parallel!
X = TypeVar("X")
Y = TypeVar("Y")
Z = TypeVar("Z")


def s(
    bef: Callable[[X,], Y],
    aft: Callable[[Y,], Z],
) -> Callable[[X,], Z]:
    """Series composition"""
    def _(x: X) -> Z:
        return aft(bef(x))
    return _


def p(
    l: Callable[[X,], Y],
    r: Callable[[X,], Z],
) -> Callable[[X,], Tuple[Y, Z]]:
    """Parallel composition"""
    def _(x: X) -> Tuple[Y, Z]:
        return (l(x), r(x))
    return _


def left(xy: Tuple[X, Any]) -> X:
    """Simple left getter"""
    return xy[0]

def right(xy: Tuple[Any, Y]) -> Y:
    """Simple right getter"""
    return xy[1]


# There are 3 possible series-parallel representations with modified edges
# Strategy 1; Delegate data pass of `ld` to `bridge` and `rd``
def make_wheatstone1(
    ul: Callable[[U], L],
    ur: Callable[[U], UR],
    bridge: Callable[[L], LR],
    ld: Callable[[L], DL],
    rd: Callable[[R], DR]
) -> Callable[[U], D]:
    r"""
    Modification strategy #1
    U
    | \
    |  \
    L => R'
         |
         |
         D
    """
    return s(
        p(
            s(
                ul, p(ld, bridge)
            ),
            ur
        ),
        p(
            s(left, left),
            s(
                p(s(left, right), right),
                rd
            )
        )
    )

# Strategy 2; Delegate data pass of `ur` to `ul` and `bridge`
def make_wheatstone2(
    ul: Callable[[U], L],
    ur: Callable[[U], UR],
    bridge: Callable[[L], LR],
    ld: Callable[[L], DL],
    rd: Callable[[R], DR]
) -> Callable[[U], D]:
    r"""
    Modification strategy #2
    U
    |
    |
    L' => R
      \  |
       \ |
         D
    """
    return s(
        p(ul, ur),
        p(
            s(left, ld),
            s(
                p(
                    s(left, bridge),
                    right
                ),
                rd,
            )
        )
    )


# Strategy 3; Hide the bridge
def make_wheatstone3(
    ul: Callable[[U], L],
    ur: Callable[[U], UR],
    bridge: Callable[[L], LR],
    ld: Callable[[L], DL],
    rd: Callable[[R], DR]
) -> Callable[[U], D]:
    r"""
    Modification strategy #3
    U
    ||
    ||
    LR
    ||
    ||
    D
    """
    return s(
        p(ul, ur),
        p(
            s(left, ld),
            s(
                p(
                    s(left, bridge),
                    right
                ),
                rd,
            )
        )
    )
