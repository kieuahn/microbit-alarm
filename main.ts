input.onButtonPressed(Button.A, function () {
	
})
basic.forever(function () {
    for (let index = 0; index < 2; index++) {
        music.playTone(233, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Half))
    }
    music.rest(music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 4; index++) {
        music.playTone(233, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Quarter))
    }
    music.playTone(196, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 2; index++) {
        music.playTone(233, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Half))
    }
    music.rest(music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 4; index++) {
        music.playTone(233, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Quarter))
    }
    music.playTone(196, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 2; index++) {
        music.playTone(233, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Half))
    }
    music.rest(music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 4; index++) {
        music.playTone(233, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Quarter))
    }
    music.playTone(196, music.beat(BeatFraction.Half))
    music.playTone(262, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 2; index++) {
        music.playTone(220, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Half))
    }
    music.rest(music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 2; index++) {
        music.playTone(220, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Half))
    }
    music.playTone(196, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Half))
    music.rest(music.beat(BeatFraction.Half))
    basic.clearScreen()
})
