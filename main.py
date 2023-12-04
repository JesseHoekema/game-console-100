def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        """)
    if Math.random_boolean():
        basic.show_icon(IconNames.SKULL)
    else:
        basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# love meter
# 

def on_logo_pressed():
    basic.show_string("Love Meter")
    basic.show_string("persoon 1 leg je vinger op pin 0 ")
    basic.show_string("persoon 2 leg je vinger op pin 1 ")
    basic.show_string("en hij begint")
    basic.show_number(randint(0, 100))
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global timer
    timer = randint(5, 10)
    basic.show_icon(IconNames.CHESSBOARD)
    while timer > 0:
        timer += -1
        basic.pause(1000)
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.B, on_button_pressed_b)

timer = 0
hand = 0
basic.show_leds("""
    # . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.show_leds("""
    # . . . .
    . # . . .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.show_leds("""
    # . . . .
    . # . . .
    . . # . .
    . . . . .
    . . . . .
    """)
basic.show_leds("""
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . .
    """)
basic.show_leds("""
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    """)
basic.show_leds("""
    # . . . #
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    """)
basic.show_leds("""
    # . . . #
    . # . # .
    . . # . .
    . . . # .
    . . . . #
    """)
basic.show_leds("""
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    . . . . #
    """)
basic.show_leds("""
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    """)
basic.show_icon(IconNames.HAPPY)
music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
    music.PlaybackMode.UNTIL_DONE)
music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)