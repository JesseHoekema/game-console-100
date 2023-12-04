input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        `)
    if (Math.randomBoolean()) {
        basic.showIcon(IconNames.Skull)
    } else {
        basic.showIcon(IconNames.Square)
    }
})
input.onGesture(Gesture.Shake, function () {
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
// love meter
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("Love Meter")
    basic.showString("persoon 1 leg je vinger op pin 0 ")
    basic.showString("persoon 2 leg je vinger op pin 1 ")
    basic.showString("en hij begint")
    basic.showNumber(randint(0, 100))
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    timer = randint(5, 10)
    basic.showIcon(IconNames.Chessboard)
    while (timer > 0) {
        timer += -1
        basic.pause(1000)
    }
    basic.showIcon(IconNames.Skull)
})
let timer = 0
let hand = 0
basic.showLeds(`
    # . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    # . . . .
    . # . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    # . . . .
    . # . . .
    . . # . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . .
    `)
basic.showLeds(`
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    `)
basic.showLeds(`
    # . . . #
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    `)
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . . . # .
    . . . . #
    `)
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    . . . . #
    `)
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
basic.showIcon(IconNames.Happy)
music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Nyan), music.PlaybackMode.LoopingInBackground)
