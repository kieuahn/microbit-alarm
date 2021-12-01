def on_button_pressed_a():
    for index in range(2):
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index2 in range(4):
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(196, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index3 in range(2):
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index4 in range(4):
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(196, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index5 in range(2):
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index6 in range(4):
        music.play_tone(233, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(196, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index7 in range(2):
        music.play_tone(220, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index8 in range(2):
        music.play_tone(220, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(196, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for index9 in range(2):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(196, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(233, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    basic.show_string("Hello!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index10 in range(2):
        music.play_tone(233, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    for index11 in range(2):
        music.play_tone(196, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    for index12 in range(2):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(233, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index13 in range(2):
        music.play_tone(196, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    for index14 in range(2):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
