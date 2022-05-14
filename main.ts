tiles.setCurrentTilemap(tilemap`yesss`)
let sheepy = sprites.create(assets.image`sheepy`, SpriteKind.Player)
controller.moveSprite(sheepy)
scene.cameraFollowSprite(sheepy)
