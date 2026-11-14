
import stddraw


def draw_triangle(
    x0: float, y0: float,
    x1: float, y1: float,
    x2: float, y2: float
) -> None:
    """
    Draw a triangle using three vertices.

    Args:
        x0, y0: Coordinates of the first vertex.
        x1, y1: Coordinates of the second vertex.
        x2, y2: Coordinates of the third vertex.
    """

    stddraw.line(x0, y0, x1, y1)
    stddraw.line(x1, y1, x2, y2)
    stddraw.line(x2, y2, x0, y0)


# Example usage
draw_triangle(0.2, 0.2, 0.8, 0.2, 0.5, 0.8)

stddraw.show()
