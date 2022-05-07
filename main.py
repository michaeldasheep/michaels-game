def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

sheepy = sprites.create(assets.image("""
    sheepy
"""), SpriteKind.player)
controller.move_sprite(sheepy)
