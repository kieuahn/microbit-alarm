def on_button_pressed_a():
    for index in range(2):
        music.play_tone(196, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    for index2 in range(4):
        music.play_tone(196, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
