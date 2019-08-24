#images
init:
    image screwdriver:
        "screwdriver.png"
        zoom .2

#flag initializations
default screwdriver = False

# labels this place in the program as the starting point
label start:

# say statements

    stop music

    "You awaken in a dark room."

    play music "rain.mp3"

    "Only a faint, flickering light bulb illuminates the four walls that box you in. The sound of dripping water fills the air as rain pounds on the roof."

    "You try to open the door, only to find it locked."

    play music "spoopy.mp3" fadeout 3.0 fadein 3.0
    show northwall
    with fade
    show screen imagebutton_test()
    show screwdriver at Position(xpos = 0.7, xanchor=0.5, ypos=0.5, yanchor=0.5)

menu:
    "Pick up":
        $ screwdriver = True
        jump screwdriver
    "Ignore":
        $ screwdriver = False

return

#custom positions
# show eileen happy at Position(xpos = 0.5, xanchor=0.5, ypos=0.5,
# yanchor=0.5)

#labels
label screwdriver:
    "The screwdriver was added to your inventory."

# menu:
#
#     "It's a videogame.":
#         jump game
#
#     "It's an interactive book.":
#         jump book
#
# label game:
#
#     "It's a kind of videogame you can play on your computer or a console."
#
#     jump marry
#
# label book:
#
#     "It's like an interactive book that you can read on a computer or a console."
#
#     jump marry
#
# label marry:
#
#     "And so, we become a visual novel creating duo."
