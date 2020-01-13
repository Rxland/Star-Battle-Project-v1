import pyglet

from random import randint
from pyglet import clock
from pyglet.window import key

  

bgSpeed = -200

rate = 0

class GameWindow(pyglet.window.Window):
    
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args,  **kwargs)
        self.set_location( 80, 80  )
        self.frame_rate = 1 / 60

        
        self.mainBatch = pyglet.graphics.Batch()
        self.score = 0
        
        self.stopAllyShot = False
        self.hitCound = 0
        self.allyHP = 10
        self.enHp = 2
        self.explodeTime = 2
        self.rate = 0
        self.deadElem = False
        self.itemTrue = False
        self.left = False
        self.right = False

        self.loadBg = pyglet.image.load( "app/images/backgrounds/stars.png")

        self.loadEnemy1 = pyglet.image.load( "app/images/Enemy Spaceships/PNG_Parts&Spriter_Animation/Ship1/Ship1.png" ) 

        self.enemy1 = pyglet.sprite.Sprite(self.loadEnemy1,  x = 380, y = 0 )
        enemy1Seq = [pyglet.resource.image('images/anim/Ship1_Explosion_001.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_003.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_008.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_009.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_012.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_013.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_014.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_017.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_019.png'),
                    pyglet.resource.image('images/anim/Ship1_Explosion_020.png')]
        self.enemy1Anim = pyglet.image.Animation.from_image_sequence( enemy1Seq[0:], 0.03 , loop = False )
 

        self.loadItem = pyglet.image.load("app/images/mainShip/Heart (1).png")
        self.item = pyglet.sprite.Sprite(self.loadItem, x = 0, y = 0)
 
        self.bossImg = pyglet.image.load( "app/images/boss/final boss.png" )

        self.boss = pyglet.sprite.Sprite(self.bossImg, x = 250,  y = 700 , batch = self.mainBatch)

        self.bossHP = 150


        self.preLoadText = pyglet.text.Label("Press enter to start", x = 250, y = 300, batch = self.mainBatch)
        self.preLoadText.bold = True
        self.preLoadText.font_size = 30


        self.allyHitText = pyglet.text.Label( "HP: "+ str(self.allyHP), x = 800, y = 20, batch = self.mainBatch)
        self.allyHitText.bold = True
        self.allyHitText.font_size = 14

        self.loadPlayer = pyglet.image.load( "app/images/mainShip/F5S4 v3.png")

        self.player = pyglet.sprite.Sprite(self.loadPlayer, x = 380,  y = 0 , batch = self.mainBatch)
        

        self.allyShot = pyglet.image.load( "app/images/mainShip/Untitled-1.png" )
        self.enemyShot = pyglet.image.load( "app/images/Enemy/shot5_asset.png" )
        self.bossShot = pyglet.image.load( "app/images/Enemy/shot5_asset.png" )



        self.dead = False

        self.allyShotArr = []
        self.enemyShotArr = []
        self.bgList = []
        self.enemy1List = []
        self.explosionList =  []
        self.bossArr = []
        self.bossShotArr = []
        self.bossMainArr = []
        self.itemArr = []


        self.bossMainArr.append( self.boss )
        
        

        self.textt = pyglet.text.Label( "Score: "+ str(self.score), x = 800, y = 570, batch = self.mainBatch)
        self.textt.bold = True
        self.textt.font_size = 14

        self.testEnemy = pyglet.image.load( "app/images/Enemy Spaceships/PNG_Parts&Spriter_Animation/Ship1/Ship1.png" )



        for i in range(2):
            self.bgList.append(pyglet.sprite.Sprite(self.loadBg,  x = 0 , y = ( i * 4096 ) ) ) 

    


    def on_key_press( self, symbol, modfifiers):
        if symbol == key.ENTER:
            self.preLoadText.batch = None
            self.enemy1.batch = None
            for i in range(200):
                self.enemy1List.append( pyglet.sprite.Sprite( self.testEnemy , x = randint(100, 800), y = randint(800, 6000), batch = self.mainBatch ))

        if symbol == key.RIGHT:  
            self.right = True

        if symbol == key.LEFT:
            self.left = True

        if self.player.batch != None and self.stopAllyShot == False:
            if symbol == key.SPACE:
                self.allyShotArr.append( pyglet.sprite.Sprite(self.allyShot, self.player.x + 40  , self.player.y + 90) ) 
            

        if symbol == key.ESCAPE:
            pyglet.app.exit()


    def on_key_release( self, symbol, modfifers ):
        if symbol == key.RIGHT: 
                self.right = False

        if symbol == key.LEFT:    
            self.left = False


    def upTurns(self,  dt ):
        if self.right == True:
            self.player.x += 600 * dt
            if self.player.x >= 800:
                self.player.x = 800
        if self.left == True:
            self.player.x += -600 * dt
            if self.player.x <= 0:
                self.player.x = 0

    

    def on_draw( self ):
        self.clear()
        for i in self.bgList:
            i.draw()
        self.mainBatch.draw()

        for i in self.bossShotArr:
            i.draw()    
        for i in self.allyShotArr:
            i.draw()
  




    def bossShotUpdate(self, dt ):
        self.rate -= dt
        if self.rate <= 0:
            for enemy in self.bossMainArr:
                if randint(0, 5) >= 5:
                    self.bossShotArr.append(pyglet.sprite.Sprite(self.bossShot, x = ( enemy.x + 35 ), y = ( enemy.y - 40 ), batch = self.mainBatch))
                    self.bossShotArr.append(pyglet.sprite.Sprite(self.bossShot, x = ( enemy.x + 210 ), y = ( enemy.y - 40 ), batch = self.mainBatch))
                    self.rate += 1



    def enemyShoot(self, dt):
        self.rate -= dt
        if self.rate <= 0:
            for enemy in self.enemy1List:
                if randint(0, 5) >= 5:
                    self.enemyShotArr.append(pyglet.sprite.Sprite(self.enemyShot, x = enemy.x - 30, y = enemy.y - 50, batch = self.mainBatch))
                    self.rate += 1


    def updateEnemyShot( self, dt ):
        for i in self.enemyShotArr:
            if i.y <= -500:
                self.enemyShotArr.remove(i)
            i.y += -300 * dt
            

    def updateBossShot( self, dt ):
        for i in self.bossShotArr:
            if i.y <= -500:
                self.bossShotArr.remove(i)
            i.y += -300 * dt



    def updateAllyShot( self, dt , score ):
        for i in self.allyShotArr:
            if i.y >= 600:
                self.allyShotArr.remove(i)
            i.y += 1000 * dt 


    def bulletCollision(self, entity, bulletList ):
        for i in bulletList:
            if i.x < entity.x + entity.width and i.x + i.width > entity.x \
                    and i.y < entity.y + entity.height and i.height + i.y > entity.y:
                bulletList.remove(i)
                randItem = randint(1, 15)
                if randItem < 2:
                    self.itemArr.append( pyglet.sprite.Sprite(self.loadItem, x = i.x, y = i.y, batch = self.mainBatch) )
                self.dead = True
        return True      


    
    def EncounterAlly( self ):
        for i in self.enemy1List:
            if i.x < self.player.x  + self.player.width  and i.x + i.width  > self.player.x \
                and i.y < self.player.y + self.player.height and i.height + i.y > self.player.y:
                self.enemy1List.remove(i)
                self.allyHP -= 1
                self.allyHitText.text = "HP: "+ str( self.allyHP )

                self.dead = True
        return True


    def bulletCollisionAlly(self, entity, bullet_list ):
        for i in bullet_list:
            if i.x < entity.x + ( entity.width - 80) and i.x + ( i.width - 80 ) > entity.x \
                    and i.y < entity.y + ( entity.height - 80  ) and ( i.height - 60  ) + i.y > entity.y:
                bullet_list.remove(i)
                self.allyHP -= 1
                self.allyHitText.text = "HP: "+ str( self.allyHP )
                self.allyHit()


    

    def enemyHit(self, entity, enList):
        if self.dead == True and entity in enList and self.hitCound == 0:
            self.explosionList.append( pyglet.sprite.Sprite(self.enemy1Anim,  x = entity.x - 32 , y = entity.y - 32, batch = self.mainBatch) )
            
            enList.remove(entity)
            self.score += 1
            self.textt.text = "Score: "+ str(self.score)
            self.dead = False

 
        
    def updateExplosion( self ):
        for exp in self.explosionList:
            self.explosionList.remove(exp)


    
    def allyHit( self ):
        if self.allyHP <= 0:
            self.gameOverText = pyglet.text.Label( "Game Over", x = 330, y = 300, batch = self.mainBatch)
            self.allyHitText.batch = None
            self.player.batch = None
            self.gameOverText.bold = True
            self.gameOverText.font_size = 34
        return True



    def updateBg( self, dt ):
        for i in self.bgList:
            if i.y <= -4200:
                self.bgList.remove(i)
                self.bgList.append( pyglet.sprite.Sprite(self.loadBg, x = 0 , y = 600 ) )
            i.y += bgSpeed * dt


    def enemyMove( self , dt ):
        for i in self.enemy1List:
            i.y += -50 * dt


    def update(self, dt):
        self.updateBg( dt )
        self.upTurns( dt ) 
        self.enemyMove( dt )
        self.itemUpdate( dt )
        if self.score >= 80:
            self.bossMove( dt )
            for i in self.enemy1List:
                self.enemy1List.remove(i)

        self.updateAllyShot( dt,  self.score )
        self.enemyShoot( dt )
        self.updateBossShot( dt )
        self.updateEnemyShot( dt )
        self.bulletCollisionAlly( self.player, self.enemyShotArr )

        self.hpItem()

        self.bulletCollisionBossAlly( self.player, self.bossShotArr )

        self.bulletCollisionBoss( self.boss , self.allyShotArr )

        self.EncounterAlly()

        for i in self.enemy1List:
            if self.bulletCollision(i, self.allyShotArr ):
                self.updateExplosion()
                self.enemyHit(i, self.enemy1List)
        self.bossShotUpdate( dt )





    def bossMove( self, dt ):
        self.boss.y += -100 * dt

        if self.boss.y <= 400:
            self.boss.y = 400
            self.boss.x += -80 * dt

        if self.boss.x <= -400:
            self.boss.x = 1000


    def itemUpdate(self, dt):
        for i in self.itemArr:
            i.y += -250 * dt 





    def updateBossDie( self ):
        self.BossDeadText = pyglet.text.Label( "You won", x = 350, y = 300, batch = self.mainBatch)
        self.allyHitText.batch = None
        self.allyHP += 1000
        self.BossDeadText.bold = True
        self.BossDeadText.font_size = 34
        
        self.boss.batch = None
        self.stopAllyShot = True
        for i in self.bossMainArr:
            self.bossMainArr.remove(i)
 
  


    def bulletCollisionBoss(self, entity, bulletList ):
        for i in bulletList:
            if i.x < entity.x  + ( entity.width ) and i.x + ( i.width  ) > entity.x \
                    and i.y < entity.y + entity.height and i.height + i.y > entity.y:
                bulletList.remove(i)
                self.bossHP -= 1
                if self.bossHP == 0:
                    self.updateBossDie()
                print( self.bossHP )

                


    def hpItem(self):
        for i in self.itemArr:
            if i.x < self.player.x  + self.player.width  and i.x + i.width  > self.player.x \
                and i.y < self.player.y + self.player.height and i.height + i.y > self.player.y:
                self.itemArr.remove(i)
                self.allyHP += 1
                self.allyHitText.text = "HP: "+ str( self.allyHP )
            


    def bulletCollisionBossAlly(self, entity, bulletList ):
        for i in bulletList:
            if i.x < entity.x + ( entity.width - 80) and i.x + ( i.width - 80 ) > entity.x \
                    and i.y < entity.y + ( entity.height - 50  ) and i.height + i.y > entity.y:
                bulletList.remove(i)
                self.allyHP -= 1
                self.allyHitText.text = "HP: "+ str( self.allyHP )
                self.allyHit()


if __name__ == "__main__":
    window = GameWindow(  width = 900, height =  600, caption =  "Star Battle Project", resizable = False   )
    pyglet.clock.schedule_interval( window.update, window.frame_rate)
    pyglet.app.run()