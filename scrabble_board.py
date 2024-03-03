from pysvg.builders import ShapeBuilder, StyleBuilder
from pysvg.structure import G, Svg
from pysvg.text import Text


NB_TILES = 15
SIDE_BUFFER = 5
SQUARE_SIZE = 16
SQUARE_BUFFER = 2.5
SQUARE_TILE_OFFSET = 1.5
TILE_SIZE = 15
TEXT_HEIGHT = 8
ENGLISH_LETTER_TILE_OFFSET_X = (
    6  # offset between upper-left corner of the tile and the point at the center (x) and bottom (y) of the letter
)
ENGLISH_LETTER_TILE_OFFSET_Y = (
    10  # offset between upper-left corner of the tile and the point at the center (x) and bottom (y) of the letter
)
ENGLISH_SCORE_TILE_OFFSET_X = (
    14  # offset between upper-left corner of the tile and the point at the right (x) and bottom (y) of the score
)
ENGLISH_SCORE_TILE_OFFSET_Y = (
    14  # offset between upper-left corner of the tile and the point at the right (x) and bottom (y) of the score
)
FRENCH_LETTER_TILE_OFFSET_X = (
    8  # offset between upper-left corner of the tile and the point at the center (x) and bottom (y) of the letter
)
FRENCH_LETTER_TILE_OFFSET_Y = (
    10  # offset between upper-left corner of the tile and the point at the center (x) and bottom (y) of the letter
)
FRENCH_SCORE_TILE_OFFSET_X = (
    1  # offset between upper-left corner of the tile and the point at the right (x) and bottom (y) of the score
)
FRENCH_SCORE_TILE_OFFSET_Y = (
    14  # offset between upper-left corner of the tile and the point at the right (x) and bottom (y) of the score
)
LETTER_FONT_SIZE = 11  # I don't understand the units well enough, this is a number that works well enough
SCORE_FONT_SIZE = 6  # I don't understand the units well enough, this is a number that works well enough

DOUBLE_WORD_LOCATIONS = [  # in tiles coordinates, 0-indexed
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [7, 7],
    [1, 13],
    [2, 12],
    [3, 11],
    [4, 10],
    [13, 13],
    [12, 12],
    [11, 11],
    [10, 10],
    [10, 4],
    [13, 1],
    [12, 2],
    [11, 3],
]
TRIPLE_WORD_LOCATIONS = [  # in tiles coordinates, 0-indexed
    [0, 0],
    [0, 14],
    [14, 0],
    [14, 14],
    [0, 7],
    [7, 0],
    [7, 14],
    [14, 7],
]
DOUBLE_LETTER_LOCATIONS = [  # in tiles coordinates, 0-indexed
    [0, 3],
    [0, 11],
    [2, 6],
    [2, 8],
    [3, 0],
    [3, 7],
    [3, 14],
    [6, 2],
    [6, 6],
    [6, 8],
    [6, 12],
    [7, 3],
    [7, 11],
    [8, 2],
    [8, 6],
    [8, 8],
    [8, 12],
    [11, 0],
    [11, 7],
    [11, 14],
    [12, 6],
    [12, 8],
    [14, 3],
    [14, 11],
]
TRIPLE_LETTER_LOCATIONS = [  # in tiles coordinates, 0-indexed
    [1, 5],
    [1, 9],
    [5, 1],
    [5, 5],
    [5, 9],
    [5, 13],
    [9, 1],
    [9, 5],
    [9, 9],
    [9, 13],
    [13, 5],
    [13, 9],
]


MODIFIER_TILE_OFFSET_X = TILE_SIZE / 2
MODIFIER_TILE_OFFSET_Y = 10.5
MODIFIER_FONT_SIZE = 8  # I don't understand the units well enough, this is a number that works well enough

ENGLISH_LETTER_DISTRIBUTION_DICT = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1,
    " ": 2,
}

ENGLISH_LETTER_SCORE_DICT = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
    " ": 0,
}

FRENCH_LETTER_DISTRIBUTION_DICT = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 3,
    "E": 15,
    "F": 2,
    "G": 2,
    "H": 2,
    "I": 8,
    "J": 1,
    "K": 1,
    "L": 5,
    "M": 3,
    "N": 6,
    "O": 6,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 6,
    "T": 6,
    "U": 6,
    "V": 2,
    "W": 1,
    "X": 1,
    "Y": 1,
    "Z": 1,
    " ": 2,
}

FRENCH_LETTER_SCORE_DICT = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 10,
    "L": 1,
    "M": 2,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 8,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 10,
    "X": 10,
    "Y": 10,
    "Z": 10,
    " ": 0,
}

TOTAL_SIZE = 2 * SIDE_BUFFER + NB_TILES * SQUARE_SIZE + (NB_TILES - 1) * SQUARE_BUFFER


shape_builder = ShapeBuilder()

# STEP 1: the tiles and the mesh

tiles_and_grid_svg = Svg(
    width=f"{TOTAL_SIZE}mm",
    height=f"{TOTAL_SIZE}mm",
)
# manually setting the viewbox so that all units are in mm across the document
tiles_and_grid_svg._attributes["viewBox"] = f"0 0 {TOTAL_SIZE} {TOTAL_SIZE}"

tiles_and_grid_svg.addElement(
    shape_builder.createRect(
        0,
        0,
        TOTAL_SIZE,
        TOTAL_SIZE,
        SIDE_BUFFER,
        SIDE_BUFFER,
        strokewidth=2,
        stroke="red",
    )
)


for i in range(NB_TILES):
    for j in range(NB_TILES):
        tiles_and_grid_svg.addElement(
            shape_builder.createRect(
                SIDE_BUFFER + i * SQUARE_SIZE + i * SQUARE_BUFFER,
                SIDE_BUFFER + j * SQUARE_SIZE + j * SQUARE_BUFFER,
                SQUARE_SIZE,
                SQUARE_SIZE,
                1,
                1,
                strokewidth=0.2,
                stroke="red",
            )
        )


for i in range(NB_TILES):
    for j in range(NB_TILES):
        tiles_and_grid_svg.addElement(
            shape_builder.createRect(
                SIDE_BUFFER + i * SQUARE_SIZE + i * SQUARE_BUFFER + 0.5 * (SQUARE_SIZE - TILE_SIZE),
                SIDE_BUFFER + j * SQUARE_SIZE + j * SQUARE_BUFFER + 0.5 * (SQUARE_SIZE - TILE_SIZE),
                TILE_SIZE,
                TILE_SIZE,
                1,
                1,
                strokewidth=0.2,
                stroke="red",
            )
        )


english_letters_list = []
for key, value in ENGLISH_LETTER_DISTRIBUTION_DICT.items():
    english_letters_list += [key] * value

french_letters_list = []
for key, value in FRENCH_LETTER_DISTRIBUTION_DICT.items():
    french_letters_list += [key] * value

letters_list = english_letters_list + french_letters_list

letter_style = StyleBuilder()
letter_style.setFontFamily(fontfamily="Helvetica Neue")
letter_style.setFontSize(LETTER_FONT_SIZE)
letter_style.setFilling(fill="back")
letter_style.style_dict["text-anchor"] = "middle"

letter_counter = 0
for j in range(NB_TILES):
    for i in range(NB_TILES):

        # handling english tiles
        if letter_counter < len(english_letters_list):
            current_letter = letters_list[letter_counter]
            current_score = ENGLISH_LETTER_SCORE_DICT[current_letter]

            # small hack to make the letters with a score of 10 prettier
            if len(str(current_score)) > 1:
                additional_letter_offset_x = -1
                additional_letter_offset_y = -1
            else:
                additional_letter_offset_x = 0
                additional_letter_offset_y = 0

            letter_text = Text(
                current_letter,
                SIDE_BUFFER
                + i * SQUARE_SIZE
                + i * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + ENGLISH_LETTER_TILE_OFFSET_X
                + additional_letter_offset_x,
                SIDE_BUFFER
                + j * SQUARE_SIZE
                + j * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + ENGLISH_LETTER_TILE_OFFSET_Y
                + additional_letter_offset_y,
            )
            score_text = Text(
                current_score,
                SIDE_BUFFER
                + i * SQUARE_SIZE
                + i * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + ENGLISH_SCORE_TILE_OFFSET_X,
                SIDE_BUFFER
                + j * SQUARE_SIZE
                + j * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + ENGLISH_SCORE_TILE_OFFSET_Y,
            )
            score_style = StyleBuilder()
            score_style.setFontFamily(fontfamily="Helvetica Neue")
            score_style.setFontSize(SCORE_FONT_SIZE)
            score_style.setFilling(fill="black")
            score_style.style_dict["text-anchor"] = "end"

        # handling french tiles
        elif letter_counter < len(english_letters_list) + len(french_letters_list):
            current_letter = letters_list[letter_counter]
            current_score = FRENCH_LETTER_SCORE_DICT[current_letter]

            # small hack to make the letters with a score of 10 prettier
            if len(str(current_score)) > 1:
                additional_letter_offset_x = 1
                additional_letter_offset_y = -1
            else:
                additional_letter_offset_x = 0
                additional_letter_offset_y = 0

            letter_text = Text(
                current_letter,
                SIDE_BUFFER
                + i * SQUARE_SIZE
                + i * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + FRENCH_LETTER_TILE_OFFSET_X
                + additional_letter_offset_x,
                SIDE_BUFFER
                + j * SQUARE_SIZE
                + j * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + FRENCH_LETTER_TILE_OFFSET_Y
                + additional_letter_offset_y,
            )
            score_text = Text(
                current_score,
                SIDE_BUFFER
                + i * SQUARE_SIZE
                + i * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + FRENCH_SCORE_TILE_OFFSET_X,
                SIDE_BUFFER
                + j * SQUARE_SIZE
                + j * SQUARE_BUFFER
                + 0.5 * (SQUARE_SIZE - TILE_SIZE)
                + FRENCH_SCORE_TILE_OFFSET_Y,
            )
            score_style = StyleBuilder()
            score_style.setFontFamily(fontfamily="Helvetica Neue")
            score_style.setFontSize(SCORE_FONT_SIZE)
            score_style.setFilling(fill="black")
            score_style.style_dict["text-anchor"] = "start"

        if letter_counter < len(letters_list):
            letter_text.set_style(letter_style.getStyle())
            tiles_and_grid_svg.addElement(letter_text)
            score_text.set_style(score_style.getStyle())
            tiles_and_grid_svg.addElement(score_text)
            letter_counter += 1

tiles_and_grid_svg.save(f"outputs/tiles_and_grid.svg")

# STEP 2: the base board

base_board_svg = Svg(
    width=f"{TOTAL_SIZE}mm",
    height=f"{TOTAL_SIZE}mm",
)
# manually setting the viewbox so that all units are in mm across the document
base_board_svg._attributes["viewBox"] = f"0 0 {TOTAL_SIZE} {TOTAL_SIZE}"

base_board_svg.addElement(
    shape_builder.createRect(
        0,
        0,
        TOTAL_SIZE,
        TOTAL_SIZE,
        SIDE_BUFFER,
        SIDE_BUFFER,
        strokewidth=2,
        stroke="red",
    )
)


modifier_style = StyleBuilder()
modifier_style.setFontFamily(fontfamily="Helvetica Neue")
modifier_style.setFontSize(MODIFIER_FONT_SIZE)
modifier_style.setFilling(fill="black")
modifier_style.style_dict["text-anchor"] = "middle"


for dw in DOUBLE_WORD_LOCATIONS:
    modifier_text = Text(
        "DW",
        SIDE_BUFFER
        + dw[0] * SQUARE_SIZE
        + dw[0] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_X,
        SIDE_BUFFER
        + dw[1] * SQUARE_SIZE
        + dw[1] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_Y,
    )
    modifier_text.set_style(modifier_style.getStyle())
    base_board_svg.addElement(modifier_text)

for tw in TRIPLE_WORD_LOCATIONS:
    modifier_text = Text(
        "TW",
        SIDE_BUFFER
        + tw[0] * SQUARE_SIZE
        + tw[0] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_X,
        SIDE_BUFFER
        + tw[1] * SQUARE_SIZE
        + tw[1] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_Y,
    )
    modifier_text.set_style(modifier_style.getStyle())
    base_board_svg.addElement(modifier_text)

for dl in DOUBLE_LETTER_LOCATIONS:
    modifier_text = Text(
        "DL",
        SIDE_BUFFER
        + dl[0] * SQUARE_SIZE
        + dl[0] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_X,
        SIDE_BUFFER
        + dl[1] * SQUARE_SIZE
        + dl[1] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_Y,
    )
    modifier_text.set_style(modifier_style.getStyle())
    base_board_svg.addElement(modifier_text)

for tl in TRIPLE_LETTER_LOCATIONS:
    modifier_text = Text(
        "TL",
        SIDE_BUFFER
        + tl[0] * SQUARE_SIZE
        + tl[0] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_X,
        SIDE_BUFFER
        + tl[1] * SQUARE_SIZE
        + tl[1] * SQUARE_BUFFER
        + 0.5 * (SQUARE_SIZE - TILE_SIZE)
        + MODIFIER_TILE_OFFSET_Y,
    )
    modifier_text.set_style(modifier_style.getStyle())
    base_board_svg.addElement(modifier_text)

base_board_svg.save(f"outputs/base_board.svg")
