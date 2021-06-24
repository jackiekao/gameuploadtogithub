@namespace
class SpriteKind:
    星之擊 = SpriteKind.create()
    大招 = SpriteKind.create()
    p2 = SpriteKind.create()
    戰士a = SpriteKind.create()
    戰士b = SpriteKind.create()
    法師a = SpriteKind.create()
    p1 = SpriteKind.create()
    介面之滑鼠 = SpriteKind.create()
    Buttion = SpriteKind.create()
    HELP = SpriteKind.create()
    HELP_BT = SpriteKind.create()
    滑鼠 = SpriteKind.create()
    HELPBT = SpriteKind.create()
    H_MAF = SpriteKind.create()
    AT_BT = SpriteKind.create()
    AT_GO = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    if 頁面面 == 3:
        info.player1.change_life_by(-10)
        sprite.destroy()
        scene.camera_shake(2, 500)
sprites.on_overlap(SpriteKind.法師a, SpriteKind.p1, on_on_overlap)

def on_player2_connected():
    if 頁面面 == 3:
        controller.player2.move_sprite(法師, 100, 0)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_player2_disconnected():
    pass
controller.player2.on_event(ControllerEvent.DISCONNECTED, on_player2_disconnected)

def on_a_pressed():
    global 劍氣, 戰士攻擊
    if HELP_PAGE == 0:
        controller.move_sprite(MAF)
    if onstartpage == 0:
        controller.move_sprite(MAF)
    if onstartpage == 2:
        controller.move_sprite(MAF)
    if 頁面面 == 3:
        if 戰士攻擊 == False:
            if controller.left.is_pressed():
                劍氣 = sprites.create_projectile_from_sprite(img("""
                        ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ....................555555555.....................
                                            ...............555555111555555..5555..............
                                            .............55555551155555.......................
                                            ...........5555111111555..........................
                                            .........555555111115555..........................
                                            ........55551111111155............................
                                            .......555511111115555555.........................
                                            ......5551111111115555555555....55555.............
                                            .....555111111155555..............................
                                            .....551111111155.................................
                                            ....5511111111155.................................
                                            ...55511111111155.................................
                                            ...555111111111155................................
                                            ...555111111111155.......55555....................
                                            ...5551111111111155...............................
                                            ...55511111111111555555...........................
                                            ...5551111111111111555............................
                                            ...555111111111111155555..........................
                                            ...555111111111111155555555555....................
                                            ...555111111115551111115555555555...55555555......
                                            ....55511111111155555555555555555.................
                                            .....555111111115.................................
                                            ......55511111115.................................
                                            ........551111155.................................
                                            .........555511555................................
                                            ...........55551155...............................
                                            ............5555555555............................
                                            ..............55555555555...555555................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                    """),
                    戰士,
                    -150,
                    0)
                劍氣.set_kind(SpriteKind.戰士a)
            else:
                劍氣 = sprites.create_projectile_from_sprite(img("""
                        ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            .....................555555555....................
                                            ..............5555..555555111555555...............
                                            .......................55555115555555.............
                                            ..........................5551111115555...........
                                            ..........................555511111555555.........
                                            ............................55111111115555........
                                            .........................555555511111115555.......
                                            .............55555....5555555555111111111555......
                                            ..............................555551111111555.....
                                            .................................551111111155.....
                                            .................................5511111111155....
                                            .................................55111111111555...
                                            ................................551111111111555...
                                            ....................55555.......551111111111555...
                                            ...............................5511111111111555...
                                            ...........................55555511111111111555...
                                            ............................5551111111111111555...
                                            ..........................555551111111111111555...
                                            ....................555555555551111111111111555...
                                            ......55555555...555555555511111155511111111555...
                                            .................55555555555555555111111111555....
                                            .................................511111111555.....
                                            .................................51111111555......
                                            .................................551111155........
                                            ................................555115555.........
                                            ...............................55115555...........
                                            ............................5555555555............
                                            ................555555...55555555555..............
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                    """),
                    戰士,
                    150,
                    0)
                劍氣.set_kind(SpriteKind.戰士a)
            music.small_crash.play()
            劍氣.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
            戰士攻擊 = True
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_left_released():
    if 頁面面 == 3:
        法師.set_image(img("""
            . . . . . f f 4 4 f f . . . . . 
                        . . . . f 5 4 5 5 4 5 f . . . . 
                        . . . f e 4 5 5 5 5 4 e f . . . 
                        . . f b 3 e 4 4 4 4 e 3 b f . . 
                        . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                        . f 3 3 e b 3 e e 3 b e 3 3 f . 
                        . f 3 3 f f e e e e f f 3 3 f . 
                        . f b b f b f e e f b f b b f . 
                        . f b b e 1 f 4 4 f 1 e b b f . 
                        f f b b f 4 4 4 4 4 4 f b b f f 
                        f b b f f f e e e e f f f b b f 
                        . f e e f b d d d d b f e e f . 
                        . . e 4 c d d d d d d c 4 e . . 
                        . . e f b d b d b d b b f e . . 
                        . . . f f 1 d 1 d 1 d f f . . . 
                        . . . . . f f b b f f . . . . .
        """))
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.RELEASED,
    on_player2_button_left_released)

def on_player2_button_a_pressed():
    global 火球, 法師攻擊
    if 頁面面 == 3:
        if 法師攻擊 == False:
            if controller.player2.is_pressed(ControllerButton.RIGHT):
                火球 = sprites.create_projectile_from_sprite(img("""
                        ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            .....................aaaaaaaaa....................
                                            ..............aaaa..aaaaaa111aaaaaa...............
                                            .......................aaaaa11aaaaaaa.............
                                            ..........................aaa111111aaaa...........
                                            ..........................aaaa11111aaaaaa.........
                                            ............................aa11111111aaaa........
                                            .........................aaaaaaa1111111aaaa.......
                                            .............aaaaa....aaaaaaaaaa111111111aaa......
                                            ..............................aaaaa1111111aaa.....
                                            .................................aa11111111aa.....
                                            .................................aa111111111aa....
                                            .................................aa111111111aaa...
                                            ................................aa1111111111aaa...
                                            ....................aaaaa.......aa1111111111aaa...
                                            ...............................aa11111111111aaa...
                                            ...........................aaaaaa11111111111aaa...
                                            ............................aaa1111111111111aaa...
                                            ..........................aaaaa1111111111111aaa...
                                            ....................aaaaaaaaaaa1111111111111aaa...
                                            ......aaaaaaaa...aaaaaaaaaa111111aaa11111111aaa...
                                            .................aaaaaaaaaaaaaaaaa111111111aaa....
                                            .................................a11111111aaa.....
                                            .................................a1111111aaa......
                                            .................................aa11111aa........
                                            ................................aaa11aaaa.........
                                            ...............................aa11aaaa...........
                                            ............................aaaaaaaaaa............
                                            ................aaaaaa...aaaaaaaaaaa..............
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                    """),
                    法師,
                    150,
                    0)
                火球.set_kind(SpriteKind.法師a)
            else:
                火球 = sprites.create_projectile_from_sprite(img("""
                        ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ....................aaaaaaaaa.....................
                                            ...............aaaaaa111aaaaaa..aaaa..............
                                            .............aaaaaaa11aaaaa.......................
                                            ...........aaaa111111aaa..........................
                                            .........aaaaaa11111aaaa..........................
                                            ........aaaa11111111aa............................
                                            .......aaaa1111111aaaaaaa.........................
                                            ......aaa111111111aaaaaaaaaa....aaaaa.............
                                            .....aaa1111111aaaaa..............................
                                            .....aa11111111aa.................................
                                            ....aa111111111aa.................................
                                            ...aaa111111111aa.................................
                                            ...aaa1111111111aa................................
                                            ...aaa1111111111aa.......aaaaa....................
                                            ...aaa11111111111aa...............................
                                            ...aaa11111111111aaaaaa...........................
                                            ...aaa1111111111111aaa............................
                                            ...aaa1111111111111aaaaa..........................
                                            ...aaa1111111111111aaaaaaaaaaa....................
                                            ...aaa11111111aaa111111aaaaaaaaaa...aaaaaaaa......
                                            ....aaa111111111aaaaaaaaaaaaaaaaa.................
                                            .....aaa11111111a.................................
                                            ......aaa1111111a.................................
                                            ........aa11111aa.................................
                                            .........aaaa11aaa................................
                                            ...........aaaa11aa...............................
                                            ............aaaaaaaaaa............................
                                            ..............aaaaaaaaaaa...aaaaaa................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                    """),
                    法師,
                    -150,
                    0)
                火球.set_kind(SpriteKind.法師a)
            music.small_crash.play()
            火球.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
            法師攻擊 = True
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def leval_Contreal():
    global Startbutton, HELP2, MAF, ACCOUSED_PAGE, onstartpage, HELP_PAGE
    if onstartpage == 0:
        scene.set_background_image(img("""
            fffffffcbccffffffffffcfbddddddddddd111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffcddffffffcfcfffff
                        fffffffccffffcffffffbfddddddddd11111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfccdbffffffffffffff
                        fffffffcffffffbffffffddddddddd1111111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcffcbfffffffffffcdcf
                        ffffffcffffffffbdffffddddddd11111111111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccffffffdfbfffffff
                        fcfffffffcdcdffdffdccdddddd11111111111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbffffffdffffffff
                        fffffffffdbddcfffffcddddd1111111111111111111111111111111111111111111dddd1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcfffffcfffbfff
                        fcffffbffbffffffffbbddddd111111111111111111111111111111111111111111d11dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdcfffffffffbffff
                        fcbffffffcfffffffcdddd1111111111111111111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccffffffffffffff
                        fdcccffffdbffcffccdddd111111111111111111cc1111111111111111111111111d111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfffffffffffffff
                        fffffffffffffffcdddd1111111111111111111cccc111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfcfffffffffffff
                        ffffffffffffffcbddd11111111111111111111cccc11111111111111111111111111111dddd1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcffffffffffffff
                        fffffffddcfffdddddd11111111111111111111ccccc11111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffffffffffff
                        fffffffdddbffbddd111111111111111111111cccccc111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfffcffffffffff
                        ffffffcbfcccddddd111111111111111111111ccccccc11111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccfffffffffffff
                        fffffffffcfddddd1111111111111111111111ccccccc11111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcffffffffffff
                        ffffffffdfcdddd1111111d11111d111111111cccccccc11111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfbfffcfffffff
                        ffffffffcfbddd11111111111111111111111ccccccccc1111111111111111111111111111111111d1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfffdffffffff
                        fffffffcdcdddd11111111111111111111111cccccccccc1111111ccc111111111ccc111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffffffffff
                        fffffbfffcddd11111111111111111111111ccccccccccc1111111cccc111c1111ccc11111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffffffff
                        fccffdcbfbddd11111111111111111111111cccccccccccc111111cccc11ccc111ccc1111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffffffff
                        fffcffcdfbdd11111111111111111111111ccccccccccccccc1111cc1c11ccc11cccc111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffffffff
                        ffddfffbbbdd1111111111111111111111cccccccccccccccc1111cc1c11ccc11c11c111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfccfffffffff
                        cfdffffbcdd11111111111111111111111cccccccccccccccc1111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfcdfffffffff
                        ffffffccdd111111111111111111111111cccccccccccccccc1111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccfbfffffffff
                        ffcfffbdb111111111111111111111111111cccccccccccc111111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbbdddddddddddddddcfdbffffffff
                        fffffcddddd1111111111111111111111111cc1cc1ccd1cc111111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddbfcfffffffff
                        fffffbdddd11111111111111111111111111cc1cc1ccc1cc1111111ccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbbddddddddddddddddcfcfffffffff
                        ffffcbddddd1111111111111111111111111cccccccccccc11111111ccccccccccc11111111111111111d1ddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddbcfffffffffff
                        fffccddddd11111111111111111111111111cccccccccccc111111111cccccccccc11111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddbbffffffffffff
                        ffdcbddddd11111111111111111111111111cccccccccccc111111111ccccccccc111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddbffffffffffcf
                        ffccddddddd11111111111111111111111111cccccccccc1111111111ccccccccc1111111111111111111dddddddddddddddddddddddddddddddddddddddddddddbddddddbbdddddddbcffffffffffff
                        ffcbdddddd1111111111111111111111111111cccccccc11b11111111ccccccccc111111111111bb1111ddddddddddddddddddddddddddddddddddddddddddbbddbbdddddbbdddddddbccfffffffffff
                        ffcbddddd111111111111111111111111111111cccccccbccccccc111ccccccccc1111111111111b1111dddddddddddddddddddddddddddddddddddddddddddbbddbddddddbddddddddfffffffffffff
                        fcbbdddddd1111111111cccb1ccc1111cccc111ccccccccccccccccc1ccccccccc1111111111111b1111dddddddddddddddddddddddddddddddddddddddddddbbbdbbdddddbdbddddbbbcfffffffffff
                        fcddddddd1111111111ccccb1cccc11ccccc111cccccccccbbccbbbccccccccccc1111111111111b111ddddddddddddddddddddddddddbdddddddddddddddddddbddbbddddbbbddbbbcfffffffffffff
                        ccddddddd1111111111cccccbcccc11ccccc111cccccccccbbcccbbccccccccccc111111111111111111dddddddddddddddddddddddddbbdddddddddddddddddddbddbddddbbddbbbbffffffffffffff
                        ddddddddd1111111111ccc1ccccccccc1ccc111ccccccccccccccccccccccccccc1111111111111b111bdddddddddddddddddddddddddbbdddddddddddddddddddbbbbddddbddbbbbccfffffffffffff
                        dddddddd11111111111cc11ccc11cccc1ccc111ccccccccc1111cccccccccccccc1111111111111b111bddd1dddddddddddddddddddddbdddbdddddddddddddddddbbbddddbbbbbbbccfffffffffffff
                        dddddddd11111111111cccccccbcccccccccc11cccccccc1111111cccccccccccc1111111111111b111bddd1dddddddddddddddddddddbddbbdddddddddddddddddbbbdddbbbbbbbbccfffffffffffff
                        dddddddd11111111111ccccccccccccccccc111ccccccc1111b1111ccccccccccc1111111111111b1dbb1ddddddddddddddbbbbddddddbddbdddddddddddddddddddbbdddbbbbbbbccffffffffffffff
                        dddddddddd111111111cccccccccccccccc1bb1ccccccc1111bb111ccccccccccc11111b1111111b1dbbdddddddddddddddbddbbbddddbdbddddddddddddddddddddbbddbbbbbbbbcbffffffffffffff
                        dddddddddd1111111111cccccccccccccccccccccccccc111111111cccccccccccbb11111111111b1db1dddddddddddddddbdddbbddddbbdddddddddddddddddddddbbdbbbbbbbbccfffffffffffffff
                        dddddddddd11111111111cccccccccccccbccbbccccccc1111111b1cccccccccccbbbb111111111b1db1ddd1ddddddddddbbdddbbbddbbdddddddddddbbddddddddbbbbbbbbbbbcbbcffffffffffffff
                        ddddddddd1d11111111111ccccccccccccbbcbbccccccc1111111b1cccccccccccc1b1111111111bbbddddd1dddddddddbbdddddbbdbbddddddddddddbdddddddddbbbbbbbbbbccbcfffffffffffffff
                        ddddddddd1d11b11111111ccccccccccccbccbcccccccc111111bb1cccccccccccc111111111111bbbdddddddddddddddbbdddddbbbbbddddddddddddbdddddddddbbbbbbbbbbbbcffffffffffffffff
                        ddddddddd1d11b11111111cccccccccccccccccccccccc1111111bbcccccccccccc11111111111bbbdddddddddddddddddddddddbbbbddddddddddddbbdddddbddbbbbbbbbbbbccfffffffffffffffff
                        dddddddddddddbbd1bb111cccccccccccc111d1cccccccd1d1111bbcccccccccccc11111111111bbb1ddddddddddddddddddddddbbbbddddddddddddbbdddddbddbbbbbbbbbbbbccffffffffffffffff
                        dddddddddddddbbd1b1111ccccccccccccddbccccccccccc1ddddbccccccccccccc11111111bb1bb11dddbddddddddddddddddddbbbbddddddddddddbbdddddbdbbbbbbbbbbbbcffffffffffffffffff
                        ddddddddddddddbd1b11bbccccccccccccccccccccccccccbcccccccccccccccccb1d111111bbbbbdddddbbdddddddddddddddddbbbbddddddddddddbbdddddbdbbbbbbbbbbbbcffffffffffffffffff
                        ddddddddddddddbb1b11bbccccccccccccccccccccccccccccccccccccccccccccd1111b1111bbb11ddddbbdddddddddddddddddbbbbddddddddddddbbdddddbbbbbbbbbbbbbbcffffffffffffffffff
                        dddddddddddddddb1b1db1ccccccccccccccccccccccccccccccccccccccccccccc1111d1111bbb11dddddbbddddddddddddddddbbbbbddddddddddddbdddddbbbbbbbbbbbbbbbcfffffffffffffffff
                        ddddddddddddddddbb1bbdccccccccccccccccccccccccccccccccccccccccccccb1111d1111bbbddddddddbddddddddddddddddbbbbbddddddddddddbbdddbbbbbbbbbbbbbbbcffffffffffffffffff
                        ddddddddddddddddbb1bbdccccccccccccccccccccccccccccccccccccccccccccb1b11d1111bbbddddddddbbdbbddddddddddddbbbbbddddddddddddbbddbbbbbbbbbbbbbbbcfcffffffffffffffcff
                        ddddddddddddddddbb1b11cccccccccccccccccccccccccccccccccccccccccccccbbb111111bbbddddddddbbdbdddddddbbddddbbbbbdddddddddddbbbbbbbbbbbbbbbbbbbccfffffffffffffffffff
                        ddddddddddddddddbddbd1ccccccccccccccccccccccccccccccccccccccccccccbbb111d111bbbb1dddddddbbbdddddddbbddddbbbbbddddddddbdbbbbbbbbbbbbbbbbbbbbcfcffffffffffffffffff
                        ddddddddddddddddbbb111cccccccccccccccccccccccccccccccccccccccccccc1bb1111111bbbbddddddddbbbdddddddbdddddbbbbbddddbdddbdbbbbbbbbbbbbbbbbbbbbffffffffffffffffffcff
                        ddddddddddddddddbbd111ccccccccccccccccccccccccccccccccccccccccccccd1bbb11111bbbbdddddddddbbddddddbbdddddbbbbbdddbbdddbbbbbbbbdbbbbbbbbbbbbcfffffffffffffffffffff
                        ddddddddddddddddbbdd1dcccccccccccccccccccccccccccccccccccccccccccc111bb11111bbbbdddd1ddddbbddddddbbdddddbbbbbdddbbddddddbdddddddddbbbbbbbbcfffffffcfffffffffffff
                        dddddddbbdddddbbbbddddcccccccccccccccccccccccccccccccccccccccccccc111bb1111bbbbbdddddddddbbbdddddbbdddddbbbbbddddbdbdddddddddddddddddddddddfffffffffffffffffffff
                        dbddddddddbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccbcccccb11bb1111bbbbbdddddddddbbbdddddbbdddddbbbbbbdddddddddddddddbddddddddddbbcfffffffffffffffffffff
                        ddbddbddbbbbbbbbbbbbbbcccccccccccccccccccccccccccccbccccccccccccccd11b11111bbbbbbddddddddbbbdddddbbddddbbbbbbdddddddddddddddddddddddddddbcffffffffffffffffffffff
                        dbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccc111bb111bbbbbbbbdddddddbbbbddddbbdddbbbbbbddddddddddddddddddddddddddbbbcdfffffffffffffffffffff
                        bbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccbb1bb1bbbbbbbbbbbbdddddbbbbddddbbddbbbbddbbdddddddddddddddddddbddddbccfddfffffffffffffffffffff
                        dbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddbdddddddddddddbcffffffffffffffffffffffffff
                        bbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbdbddddbdddddddddddddddddddddddddddccffffffffffffffffffffffffff
                        bbbbbbbbddbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbddddddddddbddddddddddddddddddddddbdddddbbbffbdfffffffffffffffffffffff
                        bbbbbbbdddddbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbddddbddddddddbdddddddddddddddddddddddddddbddfcbfdffffffffffffffffffffff
                        bbbbddddddddddddddbbbbcccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddbdffdffbcfffffffffffffffffffff
                        bbbddddddddddddbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccbbbdbbdbdddddddbddddbddddddddddddddddddddddddddddddddddddddcffcdfffffffffffffffffcfffffff
                        bbdddddddddddddbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbcccbbbbbddbdddddddddddddddddddddddddddddddddddddddddddddddddbcdffdfcdfffffffffffffffffffffff
                        bddddddddddddddbdbbbbccccccccccccccccccccccccccccccccccccccccccbcbbbcbddddddddddddbddddddddddddddddddddddddddddddddddbddddddddddbfcffffcffffffffffffffffffffffff
                        ddddddddddddddddbdbbbcccccccccccccccccccccccccccccccccccccccccbbcddddcdbddddbbddddbbdddddddddddbdddddddddddddddddddbddddddddddddcbdffffffffffbfffffcffffffffcbff
                        dbdbddddddddbdbdbbbbccccccccccccccccccccccccccccccccccbcccbcbbdbcddddddddddddddddddddddddbddddddddddddddddddddddddddddddddddddddcffffffffffffffffffffffffcfffddf
                        ddddddbddddddddbbbbbcccccccccccccccccccccccccccccccbbcbccbbbbdbdddddddddddbbbddddddddddddddddddddddddddddddddddddddddddddddddddbffffffffffffffffffffffffcdfffcff
                        ddddddddddddbdbbbbbbccccccccccccccccccccccccccccccbbbbbbdddddddbddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddcfffffffffffffffffffffffffffdffff
                        dddddddddddddbbbbbbcccccccccccccccccccccccccccccbbbcddddbdbcdddcddddddddddddddddbdddbddddddddddbdddddddddddddddddddddddddddddddccfffffffffffffffffffffffffffffff
                        ddddddddddddbbbbbbbcccccccccccccccccccccccccccbbddddddddbdbddddbdddddddddddddddddddddddddbbbddddddddddddddddddddddddddddddddddcfcffffffffffffffffcffffffffffffff
                        bdbddddddbddbbbbbbccccccccccccccccccccccccccbddddbbdddddddddddddddddddbddddddddddddddddddddddddddddbdbdddddddddddddddddddddddbffffffffcffffffffffffffffcfcffffff
                        dbddbdddddddbbbbcccccccccccccccccccccccccccdbdbdddddddddddddddddddddddbddddddddbdcbddddddddddddddddddddddddddddddddddddddddddcfffffffffffffffffffffffffffcffffff
                        dddddddddddddddddbcbcccccccccccccccccccccbddcbbcdddbddddddddddddcdbddddddddddddddddddddbdddddddddddddddddddddddddddddddddddddfffbffffffffffffffffffffffffffcffff
                        ddddddddddddcddddddbbccccccccccccccccbcbcbddddddbdbcddddddddddddddddddddddddddcbddddddddddddbdddddddddddddddddddddddddddddddcfffdfffffffffffffffffffffffffffffff
                        dddddddddddbcdddddbddcbbcccccccbcccbbbbbccddbddddbdbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbbddddddddddddddbffffcfffffffffffffffffffffffffffffff
                        bdddddddddcdddddddddbcbbbcbbbcbbbdddbddddbddddddddddddddddbddddddddddddddddbcdddcddddddddddddddddddddddddddccddddddddddddddbddfffffffffffcffffffffffffffffcccfff
                        ddddddddddddbddddbdddbbdbcbddbdbddddddddddbdddddddbdddddcddddddddddddbddddddddddddddddbddddddddbdddddddddddddddddddddddddddcdfffffffffffffffffffffffffffffccfffc
                        dddcdddddddddddddddddcdddddddbdbbbdddbddddddddddddccdddddbddddddddcddddddddcddddddddddddddddddddddddddddddddddddddddcddddddcffffffffffffffffffffffffffffffffffff
                        dddbdddddddddddddddddcdddddddcbddddbbddddddcdbddbdddddddddddbcbbbdcbddddddcbddddddddddddddddddddddddddddbddddddddddddddddddcfffffffffffffffcffffffffffffffffffff
                        bdddddddddddddddddddddddddddbddbdbcbdbbddddbdddddddddddddbbbbbbcbbbbcdbbddddbddbcddddddddddddddddbdddddddddddddddddddddddddcffffbdcffffffffcffffffffffcfffffffff
                        dddddddddddddddddddddddddddbbdddddbcdddddddbddddcdbbdbbbbcccbbccccbcbcbbbbbbbbccbcbbbdbbbbddddddddddddddddddddddddddbbbbdddcffffcfbfffffffffffffffffffffffffffff
                        dddddddddddddddddddbdddddcbbddddddbbdddddddbbddddbbbbbccccccccccccccccccccccccccccbccbcbbccbdbbdddddddddddddddddddbbbbbbddbccfddfffffffffffbbfffffffffffffffffff
                        bbbdddddddbddddddddddddbddcddbdddddbbddbccbcccbbcbbbcbccccccccccccccccccccccccccbcccccccccccccbbbdddddddddddddbbbbccccbbddccfffffcffffffffffffffffffffffffffffff
                        cccbddddddddddddddddddddddbdddddbbbcbcccccbcccccccccccccccccccccccccccccccccccccccccccccccccccbccccbdbdddbdbbbcccbccbbbdddbfffffdfffffffffffffffffffffffffffffff
                        ccccddbdddddddddddcddddccbbbccbbcbbccccccbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccbdddddfffffffffffffffcfffffffffffffffffffff
                        ccbbbbbddddddddddbcdddcccccccccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccccccccccccccccbbddddddbfffffffffffffffffffffffffffffffffffff
                        ccccccbcbbbdddddbcccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbddddddddbfffffffffffffffffffffffffffffffffffff
                        cccccccbccbbbcbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcbdddddddddbcffffffffffffffffcbfffffffffffffffffff
                        cccccccccccbcbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbccccccccccccccccbbdddddbdddbcfffffffffffffffffffffffffffffffffffff
                        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcbbcccccccccccccbbbbddddddddddbcffcffffffffffffffffffffffffffffffffff
                        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccbbcccccbbcccccccbbbbdddddddddddbccffffffffffffffffffffffffffffffffffff
                        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcbddddddbbcbbbdbccccbbdddddbdddddddddcffdffdffffffffffffffffffffffffffffffff
                        cccccccccccccccccccccccccccccccbbccccccccccccccccccccccccccccccccccccccccbcccbbbbbbddddddddddddddbbbbbbdddddcdddddddddddbcfffffffffffffffffffffffffffffffffffffc
                        cccccccccccccccccccccccccccccbbddcbccccbccccccccccccccccccccccccccccccbdbbbbddddbdddddbddddddddddddddddddddddccdddddddddcfffffffffffffffffffffffffffffffffffffff
                        cccccccccccccccccccccccccccbbbcddbbcbbbbbccbbcccccccccccccccccccccbbbddddbbdddddbdccddbdddddddddddddddddddddddddddddddbcffffffffffffffffffffcfffffffffffffffffff
                        ccccccccccccccccccccccccccbddddddbbbbddbbbbdbccccccccccccccccccbcddddddddddbddcbdccbddddddddddddddddddddddddddddddddcbfdffffffffffffffffffffffffffffffffffffffff
                        cccccccccccccccbccccccccbcdddddddddbddddddbbbddbbbbccccccccccccdbdddddddddddbddddddddddddddddddddddddddddddddddddddcfcfffffffffffffffffcbffffffffffffffcffffffff
                        cccccccccccccccccccccfccccbddddddddddddddbcbcdddddbbbcccccbbbcdddddddbdddddddddddddddddddddddddddddddddddddddddddcdffbffffffffffffffffffbffffffffffffcbcffffffff
                        ccccccccccccccccccfccffffccbdddddddddddddddbdbddddddcdbcbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfffdffcfffffbfffffffffdccfffffffffffffffffffff
                        cccccccccccccccffcffcccffffccdddddddddddddcccdddddbdbddbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffddfffffffffffffffddffffffffffffffffffffff
                        cccccccfccffffcffffffcdfffffcfddddddddddddbccbddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfffffffffdfffffffffcffffffffffffffbffffffffffffff
                        ccfcccfffffffffffffffffffffcfccddddddddddbdcdddddddddddddddddddddddddddddddddddddddddddddbccbbccbcbbbdbbbdbfffdffffffffffffffffcfffffffffffffddfffffffffffffffff
                        cffcccffffffffffffffffffffffbcfcdddddddddccbdbdddddddddddddddddddddddddddddddddddddddbddfccccbfcfffffcbcfffcffcffffffffffccfffcffffffffffffffdbfffffffffffffffff
                        fcfffffffffffffffffffffffffffffbcbbdddddbcbcdbbbcbdbddddddddddddddddddddddddddddddbbccffffffffffffffffcbfffffffffffdffffcfffffffffffffffffffccffffffffffffffffff
                        fffffffffffffffffffffffffffffffcfffcdcfffcbcfcbccfccbddddddddddddddddddddddddddddbbbcfffffffffffffffffffcdbffffffffffffcdfdfffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffcffffffdffdfcffffccddddddddddddddddddddddddbdccfffffffffffffffffffffcffffcffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffdfffffbfbfffffbcfbffffffcccbcbcbdddddddddddddccccffffffffffffffffffffffffffffffffffffffffffcfffffffccfffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffccffffffffffffffdfdcfffffddffcffccccffbdbbbdddcfdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffffffffffffffffffffffff
                        fffffffffffffffffffcffffffffffffffffffffffffffffffffddfcfbfffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffcfffffdcfffddffffffffffffffffbffffcbffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffcfffff
                        ffffffffffffffffffffffdfffffffffcfffffffbffffffffffdffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbdffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbffffbffffdfffcddcfffffffffffffffff
                        fffffffffffffffffffffffffffffffffbffffffbffffffffffffffffffffffbfcffffcfffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffdddffffffffffccffffff
        """))
        Startbutton = sprites.create(img("""
                ................................................................
                            ................................................................
                            ................................................................
                            .......ffff....fffff.f......f........ffff..f.......ffffffff.....
                            .......f...f......ffff.....fff.......f..ffffff....fff.ffff......
                            ......ff..........f........f.f.......f.......f........f.........
                            ......fff.........f.......ff.ff......f.......f........f.........
                            ........fff.......f.......f...f......ffffff.ff........f.........
                            ..........fff.....ff.....f.....f.....f.ff..ff.........ff........
                            ............f.....ff.....fffffff.....f.....f..........ff........
                            ...........ff.....f......f.....f.....f.....ff.........f.........
                            ......ff..ff......f.....ff.....ff....f......f.........f.........
                            .......ffff.......f.....f.......f....f.......f........f.........
                            ................................................................
                            ................................................................
                            ................................................................
            """),
            SpriteKind.Buttion)
        HELP2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 2 2 2 2 2 2 . . . . . 
                            . . . . 2 2 . . . . 2 2 . . . . 
                            . . . 2 2 . . . . . . 2 2 . . . 
                            . . . 2 . . . . . . . 2 2 . . . 
                            . . . . . . . . . . . 2 2 . . . 
                            . . . . . . . . . . . 2 2 . . . 
                            . . . . . . . . . . . 2 2 . . . 
                            . . . . . . 2 2 2 2 2 2 . . . . 
                            . . . . . . 2 2 2 2 . . . . . . 
                            . . . . . . 2 2 2 . . . . . . . 
                            . . . . . . 2 2 2 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 2 2 2 . . . . . . . 
                            . . . . . . 2 2 2 . . . . . . .
            """),
            SpriteKind.HELP)
        MAF = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ..........fff...........
                            .........f1f1f..........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ......fffffffffff.......
                            ......f111111111f.......
                            ......ffff111ffff.......
                            .........f111f..........
                            .........fffff..........
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.介面之滑鼠)
        Startbutton.set_position(77, 67)
        HELP2.set_position(153, 7)
    if onstartpage == 1:
        scene.set_background_image(img("""
            8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666666111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111999999999111119999999999999999999999999999999
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111999999999111119999999999999999999999999999999
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111999999999111119999999999999999999999999999999
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111999999999111119999999999999999999999999999999
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111999999999111119999999999999999999999999999999
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111999999999111119999999999999999999999999999999
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111999999999111119999999999999999999999999999999
                        8888888888888888888888888888888888111116666666666666666666666666666666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111111111111111111111111111111166666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111111111111111111111111111111166666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111111111111111111111111111111166666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111111111111111111111111111111166666666666666666666666666666666666666666666611111111111111111111111111111111111111111111111111
                        8888888888888888888888888888888888111111111111111111111111111111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111111111111111111111111111111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        8888888888888888888888888888888888111119999999999999999999991111166666666666666666666666666666666666666666666666666666666666111118888888888888888888888888888888
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111166666666666666666666666666666111119999999999999999999991111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111119999999999999999999991111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111119999999999999999999991111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111111111111111111111111111111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111111111111111111111111111111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111111111111111111111111111111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111111111111111111111111111111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111111111111111111111111111111177777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111118888888888888888888888888888888881111188888888888111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777111111111111111111111111111111111111111111111111111111111116666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
                        1111166666666666666666666666666666111117777777777777777777777777777777777777777777777777777777777777777777777771111166666666666666666666666666666666666666666666
        """))
        MAF.destroy()
        HELP2.destroy()
        Startbutton.destroy()
        ACCOUSED_PAGE = 0
        ATTORS_Contreal()
        onstartpage = 3
    if onstartpage == 2:
        MAF.destroy()
        HELP2.destroy()
        Startbutton.destroy()
        HELP_PAGE = 0
        HELP_Contreal()
        onstartpage = 3
    if onstartpage == 4:
        MAF.destroy()
        START_BT.destroy()
        START_BT1.destroy()
        START_BT2.destroy()
        START_BT3.destroy()
        scene.set_background_image(img("""
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
        """))

def on_on_overlap2(sprite, otherSprite):
    if 頁面面 == 3:
        info.player2.change_life_by(-10)
        sprite.destroy()
        scene.camera_shake(2, 500)
sprites.on_overlap(SpriteKind.戰士b, SpriteKind.p2, on_on_overlap2)

def on_player2_button_up_released():
    if 頁面面 == 3:
        法師.set_image(img("""
            . . . . . f f 4 4 f f . . . . . 
                        . . . . f 5 4 5 5 4 5 f . . . . 
                        . . . f e 4 5 5 5 5 4 e f . . . 
                        . . f b 3 e 4 4 4 4 e 3 b f . . 
                        . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                        . f 3 3 e b 3 e e 3 b e 3 3 f . 
                        . f 3 3 f f e e e e f f 3 3 f . 
                        . f b b f b f e e f b f b b f . 
                        . f b b e 1 f 4 4 f 1 e b b f . 
                        f f b b f 4 4 4 4 4 4 f b b f f 
                        f b b f f f e e e e f f f b b f 
                        . f e e f b d d d d b f e e f . 
                        . . e 4 c d d d d d d c 4 e . . 
                        . . e f b d b d b d b b f e . . 
                        . . . f f 1 d 1 d 1 d f f . . . 
                        . . . . . f f b b f f . . . . .
        """))
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.RELEASED,
    on_player2_button_up_released)

def on_on_overlap3(sprite, otherSprite):
    if 頁面面 == 3:
        info.player2.change_life_by(-5)
        sprite.destroy()
        scene.camera_shake(2, 500)
sprites.on_overlap(SpriteKind.戰士a, SpriteKind.p2, on_on_overlap3)

def on_left_pressed():
    global 忍者攻擊
    if ACCOUSED_PAGE == 0:
        controller.move_sprite(MAF)
    if HELP_PAGE == 0:
        controller.move_sprite(MAF)
    if onstartpage == 0:
        controller.move_sprite(MAF)
    if onstartpage == 2:
        controller.move_sprite(MAF)
    if 頁面面 == 3:
        忍者攻擊 = False
        戰士.set_image(assets.image("""
            myImage3
        """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_player2_button_right_released():
    if 頁面面 == 3:
        法師.set_image(img("""
            . . . . . f f 4 4 f f . . . . . 
                        . . . . f 5 4 5 5 4 5 f . . . . 
                        . . . f e 4 5 5 5 5 4 e f . . . 
                        . . f b 3 e 4 4 4 4 e 3 b f . . 
                        . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                        . f 3 3 e b 3 e e 3 b e 3 3 f . 
                        . f 3 3 f f e e e e f f 3 3 f . 
                        . f b b f b f e e f b f b b f . 
                        . f b b e 1 f 4 4 f 1 e b b f . 
                        f f b b f 4 4 4 4 4 4 f b b f f 
                        f b b f f f e e e e f f f b b f 
                        . f e e f b d d d d b f e e f . 
                        . . e 4 c d d d d d d c 4 e . . 
                        . . e f b d b d b d b b f e . . 
                        . . . f f 1 d 1 d 1 d f f . . . 
                        . . . . . f f b b f f . . . . .
        """))
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.RELEASED,
    on_player2_button_right_released)

def on_player2_button_right_pressed():
    if 頁面面 == 3:
        法師.set_image(img("""
            . . . . . . f f f f 4 4 f . . . 
                        . . . . f f b f 5 4 5 5 4 f . . 
                        . . . f b 3 3 e 4 5 5 5 5 f . . 
                        . . f b 3 3 3 3 e 4 4 4 e f . . 
                        . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                        . . f 3 3 3 3 e b 3 e e 3 3 f . 
                        . . f 3 3 3 3 f f e e e 3 3 f . 
                        . . f b b b b f b f e e e 3 f . 
                        . . f b b b b e 1 f 4 4 e f . . 
                        . f f b b b b f 4 4 4 4 f . . . 
                        . f b b b b f f f e e e f . . . 
                        . . f b b f 4 4 e d d d f . . . 
                        . . . f f e 4 4 e d d d f . . . 
                        . . . . f b e e b d b d b f . . 
                        . . . . f f d 1 d 1 d 1 f f . . 
                        . . . . . . f f b b f f . . . .
        """))
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_on_overlap4(sprite, otherSprite):
    pass
sprites.on_overlap(SpriteKind.介面之滑鼠, SpriteKind.AT_GO, on_on_overlap4)

def PC_SET():
    global ACCOUSED_PAGE
    if pc_set_1 == True:
        pass
    if pc_set_2 == True:
        pass
    if pc_set_3 == True:
        pass
    if pc_set_4 == True:
        pass
    if pc_set_1 == True and pc_set_2 == True or pc_set_3 == True and pc_set_4 == True:
        pause(2000)
        ACCOUSED_PAGE += 1
        ATTORS_Contreal()
    if pc_set_1 == True and pc_set_3 == True or pc_set_1 == True and pc_set_4 == True:
        pause(2000)
        ACCOUSED_PAGE += 1
        ATTORS_Contreal()
    if pc_set_2 == True and pc_set_4 == True or pc_set_2 == True and pc_set_3 == True:
        pause(2000)
        ACCOUSED_PAGE += 1
        ATTORS_Contreal()
def ATTORS_Contreal():
    global START_BT, START_BT1, START_BT2, START_BT3, MAF, pc_set_1, pc_set_2, pc_set_3, pc_set_4, 頁面面, 介面, 戰士攻擊, 戰士特殊攻擊, 戰士跳, 法師攻擊, 法師特殊攻擊, 法師跳, 戰士, 法師
    if ACCOUSED_PAGE == 0:
        pause(500)
        START_BT = sprites.create(assets.image("""
            戰士 右
        """), SpriteKind.AT_BT)
        START_BT1 = sprites.create(assets.image("""弓箭手左"""), SpriteKind.AT_BT)
        START_BT2 = sprites.create(assets.image("""
            槍手左
        """), SpriteKind.AT_BT)
        START_BT3 = sprites.create(assets.image("""
            法師
        """), SpriteKind.AT_BT)
        scene.set_background_image(img("""
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        11111.........................................................................1111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111.22222222...............................................................11111
                        11111........................................................................2221112222222222..............................................................11111
                        11111..........................................................222...........2221222222222222..............................................................11111
                        11111..........................................................222..........22222222222..2222..............................................................11111
                        11111..........................................................2222.........22212222222....................................................................11111
                        11111...........................................................2222.......22221222222222..................................................................11111
                        11111...........................................................22222......222111222222222.................................................................11111
                        11111............................................................22222....222211111.2222222................................................................11111
                        11111.............................................................22222...222.11111...222222...............................................................11111
                        1111111111111111111111111111111111111111111111111111111111111111111222222222211111111112222211111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111122222221111111111112222211111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111112222221111111111222222211111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111222211111112222222222211111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111122211111112222222221111111111111111111111111111111111111111111111111111111111111111111111
                        111112........................................................................1112222222...................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111.......................33...............................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................11111........................................................................11111
                        11111.........................................................................1111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        """))
        MAF = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ..........fff...........
                            .........f1f5f..........
                            ........f11f15f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ......fffffffffff.......
                            ......feeeeeeeeef.......
                            ......ffffeeeffff.......
                            .........feeef..........
                            .........fffff..........
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.介面之滑鼠)
        START_BT.set_position(120, 31)
        START_BT1.set_position(120, 90)
        START_BT2.set_position(42, 31)
        START_BT3.set_position(42, 90)
        pc_set_1 = False
        pc_set_2 = False
        pc_set_3 = False
        pc_set_4 = False
    if ACCOUSED_PAGE == 1:
        MAF.destroy()
        START_BT.destroy()
        START_BT1.destroy()
        START_BT2.destroy()
        START_BT3.destroy()
        頁面面 = 3
        scene.set_background_image(img("""
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        666cc666666666c6666666666666666666666666666cc666666666c6666666666666666666666666666cc666666666c6666666666666666666666666666cc666666666c6666666666666666666666666
                        6ccc666666666cc66666666666666666666666c66ccc666666666cc66666666666666666666666c66ccc666666666cc66666666666666666666666c66ccc666666666cc6666666666666666666666666
                        66c66cc666cc66cc6666cc6666666666666666cc66c66cc666cc66cc6666cc6666666666666666cc66c66cc666cc66cc6666cc6666666666666666cc66c66cc666cc66cc6666cc666666666666666666
                        cccccc66c66cc6cc66c6cc66666666666666cc6ccccccc66c66cc6cc66c6cc66666666666666cc6ccccccc66c66cc6cc66c6cc66666666666666cc6ccccccc66c66cc6cc66c6cc66666666666666cc66
                        ccccc666cc6ccccc6cccc6666666666666cccc66ccccc666cc6ccccc6cccc6666666666666cccc66ccccc666cc6ccccc6cccc6666666666666cccc66ccccc666cc6ccccc6cccc6666666666666cccc66
                        ccccc6cccccccc6ccccc666c666666ccc666ccc6ccccc6cccccccc6ccccc666c666666ccc666ccc6ccccc6cccccccc6ccccc666c666666ccc666ccc6ccccc6cccccccc6ccccc666c666666ccc666ccc6
                        ccccccccccccc66cc66ccccc66ccc666cc666cccccccccccccccc66cc66ccccc66ccc666cc666cccccccccccccccc66cc66ccccc66ccc666cc666cccccccccccccccc66cc66ccccc66ccc666cc666ccc
                        ccccccccccccc6cccc66ccc66c66cc66ccccccccccccccccccccc6cccc66ccc66c66cc66ccccccccccccccccccccc6cccc66ccc66c66cc66ccccccccccccccccccccc6cccc66ccc66c66cc66cccccccc
                        ccecccccccccccccccccccc6cc666cc6ccccccccccbcccccccccccccccccccc6cc666cc6ccccccccccbcccccccccccccccccccc6cc666cc6ccccccccccbcccccccccccccccccccc6cc666cc6cccccccc
                        cceccccccccccccccccccccccb666cccccccccccccbccccccccccccccccccccccb666cccccccccccccbccccccccccccccccccccccb666cccccccccccccbccccccccccccccccccccccb666ccccccccccc
                        cceccccccccccccccccccccccbb66cccccccccccccbccccccccccccccccccccccbb66cccccccccccccbccccccccccccccccccccccbb66cccccccccccccbccccccccccccccccccccccbb66ccccccccccc
                        cceccccccc8bbcccccccc88ccbbbccccccccccccccbccccccc8bbcccccccc88ccbbbccccccccccccccbccccccc8bbcccccccc88ccbbbccccccccccccccbccccccc8bbcccccccc88ccbbbcccccccccccc
                        ccecccccc88cebccccccee8cccbbccccccccccccccbcccccc888bbcccccc888cccbbccccccccccccccbcccccc888bbcccccc888cccbbccccccccccccccbcccccc888bbcccccc888cccbbcccccccccccc
                        ceeccc8cc88eebbbc8ccce88ccbbcccccccccccccbbccc8cc88ccbbbc8ccce88ccbbcccccccccccccbbccc8cc88ccbbbc8ccce88ccbbcccccccccccccbbccc8cc88ccbbbc8ccce88ccbbcccccccccccc
                        ceeccce8cc8ec8cbb88cce88ccbbbccccccccccccbbccce8cc8ce8bbb88cce88ccbbbccccccccccccbbccce8cc8ce8bbb88cce88ccbbbccccccccccccbbccce8cc8ce8bbb88cce88ccbbbccccccccccc
                        ceeccee8888e88cbb88eee8ccccbbccccccccccccbbccee8888c88cbb88eee8ccccbbccccccccccccbbccee8888e88cbb88eee8ccccbbccccccccccccbbccee8888e88cbb88eee8ccccbbccccccccccc
                        eeeccce8888e88cbb88ee88cc8ebbbcc8cccccccbbbccce8888e88cbb88ee88cc8ebbbcc8cccccccbbbccce8888e88cbb88ee88cc8ebbbcc8cccccccbbbccce8888e88cbb88ee88cc8ebbbcc8ccccccc
                        eeeeece8888e888bbb8ee88888cbbbcc888cccccbbbeece8888e888bbb8ee88888cbbbcc888cccccbbbeece8888e888bbb8ee88888cbbbcc888cccccbbbeece8888e888bbb8ee88888cbbbcc888ccccc
                        eeeeeee8888e8888bb8ee8888ecbbb8c88ccccccbbbceee8888e8888bb8ee8888ecbbb8c88ccccccbbbceee8888e8888bb8ee8888ecbbb8c88ccccccbbbceee8888e8888bb8ee8888ecbbb8c88cccccc
                        eeeeeee888e88888bbbee8888e8bbb8888cc88ccbbbceee888e88888bbbee8888e8bbb8888cc88ccbbbceee888e88888bbbee8888e8bbb8888cc88ccbbbceee888e88888bbbee8888e8bbb8888cc88cc
                        eeeeeee888e888888bbee8888e8bbbb8888e888cbbbeeee888e888888bbee8888e8bbbb8888e888cbbbeeee888e888888bbee8888e8bbbb8888e888cbbbeeee888e888888bbee8888e8bbbb8888e888c
                        ee8eeee88ee8888888bb8888ee8bbbb8888e8888bb8eeee88ee8888888bb8888ee8bbbb8888e8888bb8eeee88ee8888888bb8888ee8bbbb8888e8888bb8eeee88ee8888888bb8888ee8bbbb8888e8888
                        ee88eeeee888888888bbb888e888bbb8888e8888bb88eeeee888888888bbb888e888bbb8888e8888bb88eeeee888888888bbb888e888bbb8888e8888bb88eeeee888888888bbb888e888bbb8888e8888
                        ee88eeee8888888888ebbbbee888bbb8888e888bbb88eeee8888888888ebbbbee888bbb8888e888bbb88eeee8888888888ebbbbee888bbb8888e888bbb88eeee8888888888ebbbbee888bbb8888e888b
                        ee88eee88888888888eebbbb8888bbbb888e888bbb88eee88888888888eebbbb8888bbbb888e888bbb88eee88888888888eebbbb8888bbbb888e888bbb88eee88888888888eebbbb8888bbbb888e888b
                        ee88eee88888888888eebbbbbb88bbbb888e888bbb88eee88888888888eebbbbbb88bbbb888e888bbb88eee88888888888eebbbbbb88bbbb888e888bbb88eee88888888888eebbbbbb88bbbb888e888b
                        e8888ee8888888888eeeebbbbbbbbbbbb888e88bb8888ee8888888888eeeebbbbbbbbbbbb888e88bb8888ee8888888888eeeebbbbbbbbbbbb888e88bb8888ee8888888888eeeebbbbbbbbbbbb888e88b
                        e8888eee888888888ee88888bbbbbbbbb888e88bb8888eee888888888ee88888bbbbbbbbb888e88bb8888eee888888888ee88888bbbbbbbbb888e88bb8888eee888888888ee88888bbbbbbbbb888e88b
                        e8888eeee88888888ee888888bbbbbbbb888e8bbb8888eeee88888888ee888888bbbbbbbb888e8bbb8888eeee88888888ee888888bbbbbbbb888e8bbb8888eeee88888888ee888888bbbbbbbb888e8bb
                        e8888eeeee888888eee8888888bbbbbbb888ebbbb8888eeeee888888eee8888888bbbbbbb888ebbbb8888eeeee888888eee8888888bbbbbbb888ebbbb8888eeeee888888eee8888888bbbbbbb888ebbb
                        ee88888eeeee8888eee888888888bbbbb888bbbbee88888eeeee8888eee888888888bbbbb888bbbbee88888eeeee8888eee888888888bbbbb888bbbbee88888eeeee8888eee888888888bbbbb888bbbb
                        8e88888eeeeeee8eee8888888888bbbbb88bbbb88e88888eeeeeee8eee8888888888bbbbb88bbbb88e88888eeeeeee8eee8888888888bbbbb88bbbb88e88888eeeeeee8eee8888888888bbbbb88bbbb8
                        8e888888eeeeeeeeee8888888888bbbbb88bbb888e888888eeeeeeeeee8888888888bbbbb88bbb888e888888eeeeeeeeee8888888888bbbbb88bbb888e888888eeeeeeeeee8888888888bbbbb88bbb88
                        8e888888eeeeeeeee88888888888bbbbb88bb8888e888888eeeeeeeee88888888888bbbbb88bb8888e888888eeeeeeeee88888888888bbbbb88bb8888e888888eeeeeeeee88888888888bbbbb88bb888
                        8ee88888eeeeeee8888888888888bbbbb88bbe888ee88888eeeeeee8888888888888bbbbb88bbe888ee88888eeeeeee8888888888888bbbbb88bbe888ee88888eeeeeee8888888888888bbbbb88bbe88
                        88ee8888eeeeee88888888888888bbbbb88bbe8888ee8888eeeeee88888888888888bbbbb88bbe8888ee8888eeeeee88888888888888bbbbb88bbe8888ee8888eeeeee88888888888888bbbbb88bbe88
                        88eee888eeeeee88888888888888bbbbb8bbbee888eee888eeeeee88888888888888bbbbb8bbbee888eee888eeeeee88888888888888bbbbb8bbbee888eee888eeeeee88888888888888bbbbb8bbbee8
                        8888eeeeeeeeee8888888888888bbbbbb8bbb8e88888eeeeeeeeee8888888888888bbbbbb8bbb8e88888eeeeeeeeee8888888888888bbbbbb8bbb8e88888eeeeeeeeee8888888888888bbbbbb8bbb8e8
                        8888eeeeeeeeee8888888888888bbbbbbbbb88e88888eeeeeeeeee8888888888888bbbbbbbbb88e88888eeeeeeeeee8888888888888bbbbbbbbb88e88888eeeeeeeeee8888888888888bbbbbbbbb88e8
                        888888eeeeeeee8888888888888bbbbbbbbb88ee888888eeeeeeee8888888888888bbbbbbbbb88ee888888eeeeeeee8888888888888bbbbbbbbb88ee888888eeeeeeee8888888888888bbbbbbbbb88ee
                        e8888888eeeeee888888888888bbbbbbbbb8888ee8888888eeeeee888888888888bbbbbbbbb8888ee8888888eeeeee888888888888bbbbbbbbb8888ee8888888eeeeee888888888888bbbbbbbbb8888e
                        ee8888888eeeee888888888888bbbbbbbbb88888ee8888888eeeee888888888888bbbbbbbbb88888ee8888888eeeee888888888888bbbbbbbbb88888ee8888888eeeee888888888888bbbbbbbbb88888
                        ee8888888eeeee888888888888bbbbbbbb888888ee8888888eeeee888888888888bbbbbbbb888888ee8888888eeeee888888888888bbbbbbbb888888ee8888888eeeee888888888888bbbbbbbb888888
                        8e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb888888
                        8e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb888888
                        8e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb888888
                        8e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb8888888e8888888eeeee88888888888bbbbbbbbb888888
                        8ee888888eeeee88888888888bbbbbbbb88888888ee888888eeeee88888888888bbbbbbbb88888888ee888888eeeee88888888888bbbbbbbb88888888ee888888eeeee88888888888bbbbbbbb8888888
                        8ee888888eeeee88888888888bbbbbbbb88888888ee888888eeeee88888888888bbbbbbbb88888888ee888888eeeee88888888888bbbbbbbb88888888ee888888eeeee88888888888bbbbbbbb8888888
                        eee888888eeeee88888888888bbbbbbbb8888888eee888888eeeee88888888888bbbbbbbb8888888eee888888eeeee88888888888bbbbbbbb8888888eee888888eeeee88888888888bbbbbbbb8888888
                        ee8888888eeeee88888888888bbbbbbbb8888888ee8888888eeeee88888888888bbbbbbbb8888888ee8888888eeeee88888888888bbbbbbbb8888888ee8888888eeeee88888888888bbbbbbbb8888888
                        ee8888888eeeeee8888888888bbbbbbbb8888888ee8888888eeeeee8888888888bbbbbbbb8888888ee8888888eeeeee8888888888bbbbbbbb8888888ee8888888eeeeee8888888888bbbbbbbb8888888
                        ee8888888eeeeee8888888888bbbbbbbb8888888ee8888888eeeeee8888888888bbbbbbbb8888888ee8888888eeeeee8888888888bbbbbbbb8888888ee8888888eeeeee8888888888bbbbbbbb8888888
                        ee8888888eeeeee8888888888bbbbbbb88888888ee8888888eeeeee8888888888bbbbbbb88888888ee8888888eeeeee8888888888bbbbbbb88888888ee8888888eeeeee8888888888bbbbbbb88888888
                        e88888888eeeeee8888888888bbbbbbb8888888ee88888888eeeeee8888888888bbbbbbb8888888ee88888888eeeeee8888888888bbbbbbb8888888ee88888888eeeeee8888888888bbbbbbb8888888e
                        e88888888eeeeee8888888888bbbbbbb888888eee88888888eeeeee8888888888bbbbbbb888888eee88888888eeeeee8888888888bbbbbbb888888eee88888888eeeeee8888888888bbbbbbb888888ee
                        e88888888eeeeee8888888888bbbbbbb888888eee88888888eeeeee8888888888bbbbbbb888888eee88888888eeeeee8888888888bbbbbbb888888eee88888888eeeeee8888888888bbbbbbb888888ee
                        888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee
                        888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee
                        888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee888888888eeeeeee888888888bbbbbbb88888eee
                        888888888eeeeeeee88888888bbbbbbb8888eeee888888888eeeeeeee88888888bbbbbbb8888eeee888888888eeeeeeee88888888bbbbbbb8888eeee888888888eeeeeeee88888888bbbbbbb8888eeee
                        888888888eeeeeeee88888888bbbbbbb8888eeee888888888eeeeeeee88888888bbbbbbb8888eeee888888888eeeeeeee88888888bbbbbbb8888eeee888888888eeeeeeee88888888bbbbbbb8888eeee
                        888888888eeeeeeee88888888bbbbbbb8888eee8888888888eeeeeeee88888888bbbbbbb8888eee8888888888eeeeeeee88888888bbbbbbb8888eee8888888888eeeeeeee88888888bbbbbbb8888eeee
                        8888888888eeeeeeee888888bbbbbbbb8888eee88888888888eeeeeeee888888bbbbbbbb8888eee88888888888eeeeeeee888888bbbbbbbb8888eee88888888888eeeeeeee888888bbbbbbbb8888eeee
                        e888888888eeeeeeee888888bbbbbbbbeeeeeeeee888888888eeeeeeee888888bbbbbbbbeeeeeeeee888888888eeeeeeee888888bbbbbbbbeeeeeeeee888888888eeeeeeee888888bbbbbbbbeeeeeeee
                        eeeee88888eeeeeeee888888bbbbbbbbbeeeeeeeeeeee88888eeeeeeee888888bbbbbbbbbeeeeeeeeeeee88888eeeeeeee888888bbbbbbbbbeeeeeeeeeeee88888eeeeeeee888888bbbbbbbbbeeeeeee
                        eeeeeeee88eeeeeeeee888eebbbbbbbbbeeeeeeeeeeeeeee88eeeeeeeee888eebbbbbbbbbeeeeeeeeeeeeeee88eeeeeeeee888eebbbbbbbbbeeeeeeeeeeeeeee88eeeeeeeee888eebbbbbbbbbeeeeeee
                        eeeeeeeeeeeeeeeeeee8eeeebbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeee8eeeebbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeee8eeeebbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeee8eeeebbbbbbbbbeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeee
                        eeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeee
                        eeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeee
                        eeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeebbbbbbbbbbbbeeeee
                        eeeeeeeeeeeeeeeeeee6666666666bbbbbbeeeeeeeeeeeeeeeeeeeeeeee6666666666bbbbbbeeeeeeeeeeeeeeeeeeeeeeee6666666666bbbbbbeeeeeeeeeeeeeeeeeeeeeeee6666666666bbbbbbeeeee
                        eeeeeeeeeeeeee66666666666666666666beeeeeeeeeeeeeeeeeee66666666666666666666beeeeeeeeeeeeeeeeeee66666666666666666666beeeeeeeeeeeeeeeeeee66666666666666666666beeeee
                        eeeeeeeeeee6666666666666666666666666eeeeeeeeeeeeeee6666666666666666666666666eeeeeeeeeeeeeee6666666666666666666666666eeeeeeeeeeeeeee6666666666666666666666666eeee
                        eeeeeeee666666666666666666666666666666eeeeeeeeee666666666666666666666666666666eeeeeeeeee666666666666666666666666666666eeeeeeeeee666666666666666666666666666666ee
                        eeeee66666666666666666666666666666666666eeeee66666666666666666666666666666666666eeeee66666666666666666666666666666666666eeeee66666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
                        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        """))
        介面 = 0
        戰士攻擊 = False
        戰士特殊攻擊 = False
        戰士跳 = False
        法師攻擊 = False
        法師特殊攻擊 = False
        法師跳 = False
        info.set_life(100)
        info.player2.set_life(100)
        戰士 = sprites.create(assets.image("""
            myImage2
        """), SpriteKind.p1)
        法師 = sprites.create(img("""
                . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 4 5 5 5 5 4 e f . . . 
                            . . f b 3 e 4 4 4 4 e 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 e b 3 e e 3 b e 3 3 f . 
                            . f 3 3 f f e e e e f f 3 3 f . 
                            . f b b f b f e e f b f b b f . 
                            . f b b e 1 f 4 4 f 1 e b b f . 
                            f f b b f 4 4 4 4 4 4 f b b f f 
                            f b b f f f e e e e f f f b b f 
                            . f e e f b d d d d b f e e f . 
                            . . e 4 c d d d d d d c 4 e . . 
                            . . e f b d b d b d b b f e . . 
                            . . . f f 1 d 1 d 1 d f f . . . 
                            . . . . . f f b b f f . . . . .
            """),
            SpriteKind.p2)
        戰士.set_position(20, 120)
        法師.set_position(140, 120)
        戰士.ay = 200
        法師.ay = 200
        戰士.set_stay_in_screen(True)
        法師.set_stay_in_screen(True)
        controller.move_sprite(戰士, 100, 0)

def on_on_overlap5(sprite, otherSprite):
    global onstartpage
    if otherSprite == HELP2 and controller.A.is_pressed():
        onstartpage += 2
        leval_Contreal()
sprites.on_overlap(SpriteKind.介面之滑鼠, SpriteKind.HELP, on_on_overlap5)

def on_up_pressed():
    global 戰士跳
    if ACCOUSED_PAGE == 0:
        controller.move_sprite(MAF)
    if onstartpage == 0:
        controller.move_sprite(MAF)
    if 頁面面 == 3:
        if 戰士跳 == False:
            if controller.left.is_pressed():
                戰士.set_image(assets.image("""
                    myImage5
                """))
            else:
                戰士.set_image(assets.image("""
                    myImage1
                """))
            戰士.vy = -125
            戰士跳 = True
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global 星之力, 戰士特殊攻擊
    if ACCOUSED_PAGE == 0:
        controller.move_sprite(MAF)
    if HELP_PAGE == 0:
        controller.move_sprite(MAF)
    if onstartpage == 0:
        controller.move_sprite(MAF)
    if onstartpage == 2:
        controller.move_sprite(MAF)
    if 頁面面 == 3:
        if 戰士特殊攻擊 == False:
            if controller.left.is_pressed():
                星之力 = sprites.create_projectile_from_sprite(img("""
                        ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            .......................999999999..................
                                            ..................999999111999999..9999...........
                                            ................99999991199999....................
                                            ..............9999111111999.......................
                                            ............999999111119999.......................
                                            ...........99991111111199.........................
                                            ..........999911111119999999......................
                                            .........9991111111119999999999....99999..........
                                            ........999111111199999...........................
                                            ........991111111199..............................
                                            .......9911111111199..............................
                                            ......99911111111199..............................
                                            ......999111111111199.............................
                                            ......999111111111199.......99999.................
                                            ......9991111111111199............................
                                            ......99911111111111999999........................
                                            ......9991111111111111999.........................
                                            ......999111111111111199999.......................
                                            ......999111111111111199999999999.................
                                            ......99911111111999999111999999999999.99999999...
                                            .......99911111999999911999999999999..............
                                            ........999119999111111999........................
                                            .........99999999111119999........................
                                            ..........99991111111199..........................
                                            .........999911111119999999.......................
                                            ........9991111111119999999999....99999...........
                                            .......999111111199999999.........................
                                            .......991111111199999999999...999999.............
                                            ......9911111111199...............................
                                            .....99911111111199...............................
                                            .....999111111111199..............................
                                            .....999111111111199.......99999..................
                                            .....9991111111111199.............................
                                            .....99911111111111999999.........................
                                            .....9991111111111111999..........................
                                            .....999111111111111199999........................
                                            .....999111111111111199999999999..................
                                            .....999111111119991111119999999999...99999999....
                                            ......99911111111199999999999999999...............
                                            .......9991111111999999111999999..9999............
                                            ........999111199999991199999.....................
                                            ..........9919999111111999........................
                                            ...........999999111119999........................
                                            ..........99991111111199..........................
                                            .........999911111119999999.......................
                                            ........9991111111119999999999999999999...........
                                            .......999111111199999............................
                                            .......991111111199...............................
                                            ......9911111111199...............................
                                            .....99911111111199...............................
                                            .....999111111111199..............................
                                            .....999111111111199.......99999..................
                                            .....9991111111111199.............................
                                            .....99911111111111999999.........................
                                            .....9991111111111111999..........................
                                            .....999111111111111199999........................
                                            .....999111111111111199999999999..................
                                            .....99911111111999999111999999999999.99999999....
                                            ......99911111999999911999999999999...............
                                            .......999119999111111999.........................
                                            ........99999999111119999.........................
                                            .........99991111111199...........................
                                            ........999911111119999999........................
                                            .......9991111111119999999999....99999............
                                            ......999111111199999999..........................
                                            ......991111111199999999999...999999..............
                                            .....9911111111199................................
                                            ....99911111111199................................
                                            ....999111111111199...............................
                                            ....999111111111199.......99999...................
                                            ....9991111111111199..............................
                                            ....99911111111111999999..........................
                                            ....9991111111111111999...........................
                                            ....999111111111111199999.........................
                                            ....999111111111111199999999999...................
                                            ....999111111119991111119999999999...99999999.....
                                            .....99911111111199999999999999999................
                                            ......999111111119................................
                                            .......99911111119................................
                                            .........991111199................................
                                            ..........999911999...............................
                                            ............99991199..............................
                                            .............9999999999...........................
                                            ...............99999999999...999999...............
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                    """),
                    戰士,
                    -100,
                    0)
                星之力.set_kind(SpriteKind.戰士b)
            else:
                星之力 = sprites.create_projectile_from_sprite(img("""
                        ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................999999999.......................
                                            ...........9999..999999111999999..................
                                            ....................99999119999999................
                                            .......................9991111119999..............
                                            .......................999911111999999............
                                            .........................99111111119999...........
                                            ......................999999911111119999..........
                                            ..........99999....9999999999111111111999.........
                                            ...........................999991111111999........
                                            ..............................991111111199........
                                            ..............................9911111111199.......
                                            ..............................99111111111999......
                                            .............................991111111111999......
                                            .................99999.......991111111111999......
                                            ............................9911111111111999......
                                            ........................99999911111111111999......
                                            .........................9991111111111111999......
                                            .......................999991111111111111999......
                                            .................999999999991111111111111999......
                                            ...99999999.99999999999911199999911111111999......
                                            ..............99999999999911999999911111999.......
                                            ........................999111111999911999........
                                            ........................99991111199999999.........
                                            ..........................99111111119999..........
                                            .......................999999911111119999.........
                                            ...........99999....9999999999111111111999........
                                            .........................999999991111111999.......
                                            .............999999...999999999991111111199.......
                                            ...............................9911111111199......
                                            ...............................99111111111999.....
                                            ..............................991111111111999.....
                                            ..................99999.......991111111111999.....
                                            .............................9911111111111999.....
                                            .........................99999911111111111999.....
                                            ..........................9991111111111111999.....
                                            ........................999991111111111111999.....
                                            ..................999999999991111111111111999.....
                                            ....99999999...999999999911111199911111111999.....
                                            ...............99999999999999999111111111999......
                                            ............9999..9999991119999991111111999.......
                                            .....................999991199999991111999........
                                            ........................9991111119999199..........
                                            ........................999911111999999...........
                                            ..........................99111111119999..........
                                            .......................999999911111119999.........
                                            ...........9999999999999999999111111111999........
                                            ............................999991111111999.......
                                            ...............................991111111199.......
                                            ...............................9911111111199......
                                            ...............................99111111111999.....
                                            ..............................991111111111999.....
                                            ..................99999.......991111111111999.....
                                            .............................9911111111111999.....
                                            .........................99999911111111111999.....
                                            ..........................9991111111111111999.....
                                            ........................999991111111111111999.....
                                            ..................999999999991111111111111999.....
                                            ....99999999.99999999999911199999911111111999.....
                                            ...............99999999999911999999911111999......
                                            .........................999111111999911999.......
                                            .........................99991111199999999........
                                            ...........................99111111119999.........
                                            ........................999999911111119999........
                                            ............99999....9999999999111111111999.......
                                            ..........................999999991111111999......
                                            ..............999999...999999999991111111199......
                                            ................................9911111111199.....
                                            ................................99111111111999....
                                            ...............................991111111111999....
                                            ...................99999.......991111111111999....
                                            ..............................9911111111111999....
                                            ..........................99999911111111111999....
                                            ...........................9991111111111111999....
                                            .........................999991111111111111999....
                                            ...................999999999991111111111111999....
                                            .....99999999...999999999911111199911111111999....
                                            ................99999999999999999111111111999.....
                                            ................................911111111999......
                                            ................................91111111999.......
                                            ................................991111199.........
                                            ...............................999119999..........
                                            ..............................99119999............
                                            ...........................9999999999.............
                                            ...............999999...99999999999...............
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                                            ..................................................
                    """),
                    戰士,
                    100,
                    0)
                星之力.set_kind(SpriteKind.戰士b)
            music.big_crash.play()
            星之力.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
            戰士.say("星之力!!!", 1000)
            controller.move_sprite(戰士, 200, 0)
            戰士.start_effect(effects.trail)
            戰士特殊攻擊 = True
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap6(sprite, otherSprite):
    global MAF, pc_set_1, pc_set_2, pc_set_3, pc_set_4
    if otherSprite == START_BT and controller.A.is_pressed():
        animation.run_image_animation(START_BT,
            [img("""
                    .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                                .........................................................................
                """),
                img("""
                    5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                """)],
            200,
            False)
        MAF.destroy()
        START_BT.set_position(120, 31)
        MAF = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ..........fff...........
                            .........f1f5f..........
                            ........f11f15f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ......fffffffffff.......
                            ......feeeeeeeeef.......
                            ......ffffeeeffff.......
                            .........feeef..........
                            .........fffff..........
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.介面之滑鼠)
        MAF.set_position(120, 31)
        pc_set_1 = True
        PC_SET()
    if otherSprite == START_BT1 and controller.A.is_pressed():
        animation.run_image_animation(START_BT1,
            [img("""
                    9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                """),
                img("""
                    5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                """)],
            200,
            False)
        MAF.destroy()
        START_BT1.set_position(120, 90)
        MAF = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ..........fff...........
                            .........f1f5f..........
                            ........f11f15f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ......fffffffffff.......
                            ......feeeeeeeeef.......
                            ......ffffeeeffff.......
                            .........feeef..........
                            .........fffff..........
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.介面之滑鼠)
        MAF.set_position(120, 90)
        pc_set_2 = True
        PC_SET()
    if otherSprite == START_BT2 and controller.A.is_pressed():
        animation.run_image_animation(START_BT2,
            [img("""
                    9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                """),
                img("""
                    5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                """)],
            200,
            False)
        MAF.destroy()
        START_BT2.set_position(42, 31)
        MAF = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ..........fff...........
                            .........f1f5f..........
                            ........f11f15f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ......fffffffffff.......
                            ......feeeeeeeeef.......
                            ......ffffeeeffff.......
                            .........feeef..........
                            .........fffff..........
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.介面之滑鼠)
        MAF.set_position(42, 31)
        pc_set_3 = True
        PC_SET()
    if otherSprite == START_BT3 and controller.A.is_pressed():
        animation.run_image_animation(START_BT3,
            [img("""
                    9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                                9999999999999999999999999999999999999999999999999999999999999999999999999
                """),
                img("""
                    5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555999999999999999999999999999999999999999999999999999999999999999995555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                                5555555555555555555555555555555555555555555555555555555555555555555555555
                """)],
            200,
            False)
        MAF.destroy()
        START_BT3.set_position(42, 90)
        MAF = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ..........fff...........
                            .........f1f5f..........
                            ........f11f15f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ......fffffffffff.......
                            ......feeeeeeeeef.......
                            ......ffffeeeffff.......
                            .........feeef..........
                            .........fffff..........
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.介面之滑鼠)
        MAF.set_position(42, 90)
        pc_set_4 = True
        PC_SET()
sprites.on_overlap(SpriteKind.介面之滑鼠, SpriteKind.AT_BT, on_on_overlap6)

def on_up_released():
    if ACCOUSED_PAGE == 0:
        controller.move_sprite(MAF)
    if HELP_PAGE == 0:
        controller.move_sprite(MAF)
    if onstartpage == 0:
        controller.move_sprite(MAF)
    if onstartpage == 2:
        controller.move_sprite(MAF)
    if 頁面面 == 3:
        if controller.left.is_pressed():
            戰士.set_image(assets.image("""
                myImage3
            """))
        else:
            戰士.set_image(assets.image("""
                myImage2
            """))
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_right_pressed():
    if HELP_PAGE == 0:
        controller.move_sprite(MAF)
    if onstartpage == 0:
        controller.move_sprite(MAF)
    if onstartpage == 2:
        controller.move_sprite(MAF)
    if 頁面面 == 3:
        戰士.set_image(assets.image("""
            myImage2
        """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_life_zero():
    if 頁面面 == 3:
        game.over(True, effects.confetti)
info.on_life_zero(on_life_zero)

def on_on_overlap7(sprite, otherSprite):
    global HELP_PAGE, onstartpage
    if otherSprite == HELP_BT2 and controller.A.is_pressed():
        HELP_PAGE += 1
        HELP_Contreal()
    if otherSprite == Startbutton and controller.A.is_pressed():
        onstartpage += 1
        leval_Contreal()
sprites.on_overlap(SpriteKind.介面之滑鼠, SpriteKind.Buttion, on_on_overlap7)

def HELP_Contreal():
    global HELP_BT2, MAF, Help__Author, HELP_CON, HELP_AT, HELP_US
    if HELP_PAGE == 0:
        scene.set_background_image(img("""
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999911111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111119999911111111111111111111111111111111111111199999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        """))
        HELP_BT2 = sprites.create(img("""
                ................................................................
                            ................................................................
                            ................................................................
                            .......1111....11111.1......1........1111..1.......1111111......
                            .......1...1......1111.....111.......1..111111....111.1.111.....
                            ......11..........1........1.1.......1.......1........1.........
                            ......111.........1.......11.11......1.......1........1.........
                            ........111.......1.......1...1......111111.11........1.........
                            ..........111.....11.....1.....1.....1.11..11.........11........
                            ............1.....11.....1111111.....1.....1..........11........
                            ...........11.....1......1.....1.....1.....11.........1.........
                            ......11..11......1.....11.....11....1......1.........1.........
                            .......1111.......1.....1.......1....1.......1........1.........
                            ................................................................
                            ................................................................
                            ................................................................
            """),
            SpriteKind.Buttion)
        MAF = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
                            ..........fff...........
                            .........f1f5f..........
                            ........f11f15f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ........f11f11f.........
                            ......fffffffffff.......
                            ......feeeeeeeeef.......
                            ......ffffeeeffff.......
                            .........feeef..........
                            .........fffff..........
                            ........................
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.介面之滑鼠)
        HELP_BT2.set_position(153, 7)
    if HELP_PAGE == 1:
        MAF.destroy()
        HELP_BT2.destroy()
        scene.set_background_image(img("""
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        """))
        Help__Author = textsprite.create("HELP", 0, 15)
        Help__Author.set_position(76, 11)
        HELP_CON = textsprite.create("", 0, 15)
        HELP_CON.set_position(38, 28)
        HELP_AT = textsprite.create("Report", 0, 8)
        HELP_AT.set_position(33, 38)
        HELP_AT = textsprite.create("Author ", 0, 8)
        HELP_AT.set_position(36, 28)
        HELP_US = textsprite.create("About Us", 0, 8)
        HELP_US.set_position(39, 48)
        HELP2.set_position(77, 67)

def on_player2_button_left_pressed():
    if 頁面面 == 3:
        法師.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . f 4 4 f f f f . . . . . . 
                        . . f 4 5 5 4 5 f b f f . . . . 
                        . . f 5 5 5 5 4 e 3 3 b f . . . 
                        . . f e 4 4 4 e 3 3 3 3 b f . . 
                        . f 3 3 3 3 3 3 3 3 3 3 3 f . . 
                        . f 3 3 e e 3 b e 3 3 3 3 f . . 
                        . f 3 3 e e e f f 3 3 3 3 f . . 
                        . . f e e e f b f b b b b f f . 
                        . . . e 4 4 f 1 e b b b b b f . 
                        . . . f 4 4 4 4 f b b b b b f . 
                        . . . f d d d e 4 4 b b b f . . 
                        . . . f d d d e 4 4 f f f . . . 
                        . . f d d d b b e e b b f . . . 
                        . . f b d 1 d 1 d d b f . . . . 
                        . . . f f f b b f f f . . . . .
        """))
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player2_life_zero():
    if 頁面面 == 3:
        game.over(True, effects.confetti)
info.player2.on_life_zero(on_player2_life_zero)

def on_player2_button_up_pressed():
    global 法師跳
    if 頁面面 == 3:
        if 法師跳 == False:
            法師.vy = -150
            法師跳 = True
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_down_pressed():
    if ACCOUSED_PAGE == 0:
        controller.move_sprite(MAF)
    if HELP_PAGE == 0:
        controller.move_sprite(MAF)
    if onstartpage == 0:
        controller.move_sprite(MAF)
    if onstartpage == 2:
        controller.move_sprite(MAF)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

HELP_US: TextSprite = None
HELP_AT: TextSprite = None
HELP_CON: TextSprite = None
Help__Author: TextSprite = None
HELP_BT2: Sprite = None
星之力: Sprite = None
法師跳 = False
法師特殊攻擊 = False
戰士跳 = False
戰士特殊攻擊 = False
介面 = 0
pc_set_4 = False
pc_set_3 = False
pc_set_2 = False
pc_set_1 = False
忍者攻擊 = False
START_BT3: Sprite = None
START_BT2: Sprite = None
START_BT1: Sprite = None
START_BT: Sprite = None
ACCOUSED_PAGE = 0
HELP2: Sprite = None
Startbutton: Sprite = None
火球: Sprite = None
法師攻擊 = False
戰士: Sprite = None
劍氣: Sprite = None
戰士攻擊 = False
MAF: Sprite = None
HELP_PAGE = 0
法師: Sprite = None
頁面面 = 0
onstartpage = 0
onstartpage = 0
leval_Contreal()
while onstartpage == 0:
    music.play_melody("D D B F E E F F ", 120)
    music.play_melody("E E F F D C D D ", 140)

def on_update_interval():
    global 戰士特殊攻擊
    if 頁面面 == 3:
        if 戰士特殊攻擊 == True:
            戰士特殊攻擊 = False
        戰士.say("大招OK")
game.on_update_interval(5000 * 2, on_update_interval)

def on_update_interval2():
    if 頁面面 == 3:
        controller.move_sprite(戰士, 100, 0)
        effects.clear_particles(戰士)
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    global 法師攻擊
    if 頁面面 == 3:
        if 法師攻擊 == True:
            法師攻擊 = False
game.on_update_interval(1000, on_update_interval3)

def on_update_interval4():
    global 戰士跳
    if 頁面面 == 3:
        if 戰士跳 == True:
            戰士跳 = False
game.on_update_interval(1000, on_update_interval4)

def on_update_interval5():
    global 法師跳
    if 頁面面 == 3:
        if 法師跳 == True:
            法師跳 = False
game.on_update_interval(1000, on_update_interval5)

def on_update_interval6():
    global 戰士攻擊
    if 頁面面 == 3:
        if 戰士攻擊 == True:
            戰士攻擊 = False
game.on_update_interval(500, on_update_interval6)
