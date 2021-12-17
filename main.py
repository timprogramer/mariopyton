import wrap,random
wrap.world.create_world(600,700,200,200)
xenemy=random.randint(100,300)
yenemy=random.randint(100,300)
xcoin=random.randint(50,550)
ycoin=random.randint(50,650)

#создание спрайтов
wrap.sprite.add("pacman",xenemy,yenemy,"enemy_blue_right1")
wrap.sprite.add("mario-items",xcoin,ycoin,"coin")
#if
if wrap.sprite.get_y(0)>wrap.sprite.get_y(1):
    wrap.sprite.set_costume(0,"enemy_blue_up1")
else:
    wrap.sprite.set_costume(0,"enemy_blue_down2")
wrap.actions.move_to(0,xenemy,ycoin)
if wrap.sprite.get_x(1)>wrap.sprite.get_x(0):
    wrap.sprite.set_costume(0,"enemy_blue_right2")
else:
    wrap.sprite.set_costume(0,"enemy_blue_left2")
wrap.actions.move_to(0,xcoin,ycoin)
wrap.sprite.remove(1)
