from constants import *

def test_width_value():
    assert WIDTH == 600

def test_height_value():
    assert HEIGHT == 600

def test_line_width_value():
    assert LINE_WIDTH == 5

def test_win_line_width_value():
    assert WIN_LINE_WIDTH == 5

def test_board_rows_value():
    assert BOARD_ROWS == 3

def test_board_columns_value():
    assert BOARD_COLUMNS == 3

def test_square_size_value():
    assert SQUARE_SIZE == WIDTH / 3

def test_circle_radius_value():
    assert CIRCLE_RADIUS == 60

def test_circle_width_value():
    assert CIRCLE_WIDTH == 20

def test_cross_width_value():
    assert CROSS_WIDTH == 20

def test_space_value():
    assert SPACE == 55

def test_bg_color_value():
    assert BG_COLOR == (255, 255, 255)

def test_line_color_value():
    assert LINE_COLOR == (0, 0, 0)

def test_circle_color_value():
    assert CIRCLE_COLOR == (239, 65, 53)

def test_cross_color_value():
    assert CROSS_COLOR == (0, 85, 164)