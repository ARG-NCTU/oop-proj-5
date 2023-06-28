# Aeroblasters

# Author : Prajjwal Pathak (pyguru)
# Date : Thursday, 30 September, 2021

import random
import pygame
from objects import Background, Player, Enemy, Bullet, Explosion, Fuel, \
					Life, Powerup, Superweapon, Button, Message, BlinkingText

pygame.init()
SCREEN = WIDTH, HEIGHT = 530, 860

info = pygame.display.Info()
width = info.current_w
height = info.current_h
if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 75

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

# IMAGES **********************************************************************

plane_img = pygame.image.load('Assets/plane.png')
logo_img = pygame.image.load('Assets/logo.png')
fighter_img = pygame.image.load('Assets/fighter.png')
mark_img = pygame.image.load('Assets/mark.png')
mark_img = pygame.transform.scale(mark_img, (225, 175))
warning_img = pygame.image.load('Assets/warning.png')
warning_img = pygame.transform.scale(warning_img, (225, 156))
chinese_warning_img = pygame.image.load('Assets/chinese_warning.png')
chinese_warning_img = pygame.transform.scale(chinese_warning_img, (225, 136))


home_img = pygame.image.load('Assets/Buttons/homeBtn.png')
replay_img = pygame.image.load('Assets/Buttons/replay.png')
sound_off_img = pygame.image.load("Assets/Buttons/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/Buttons/soundOnBtn.png")


# BUTTONS *********************************************************************

home_btn = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 140+50)
replay_btn = Button(replay_img, (36,36), WIDTH // 2  - 18, HEIGHT//2 + 135+50)
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 +50+ 140)


# FONTS ***********************************************************************

game_over_font = 'Fonts/ghostclan.ttf'
tap_to_play_font = 'Fonts/BubblegumSans-Regular.ttf'
score_font = 'Fonts/DalelandsUncialBold-82zA.ttf'
final_score_font = 'Fonts/DroneflyRegular-K78LA.ttf'
final_grade_font = 'Fonts/DroneflyRegular-K78LA.ttf'
game_over_msg1 = Message(WIDTH//2, 225, 20, 'Sorry :(', game_over_font, WHITE, win)
game_over_msg2 = Message(WIDTH//2, 250, 20, 'you did not pass the class', game_over_font, WHITE, win)
game_win_msg1 = Message(WIDTH//2, 225, 20, 'Congratulation :)', game_over_font, WHITE, win)
game_win_msg2 = Message(WIDTH//2, 250, 20, 'you passed the class', game_over_font, WHITE, win)
score_change_msg1 = Message(WIDTH//2, 430, 30, 'After Change score', game_over_font, WHITE, win)
score_change_msg2 = Message(WIDTH//2, 460, 30, 'Professor Wang give you', game_over_font, WHITE, win)
score_change_msg3 = Message(WIDTH//2, 490, 50, 'A+', game_over_font, WHITE, win)



score_msg = Message(WIDTH-50, 28, 30, '0', final_score_font, RED, win)
final_score_msg = Message(WIDTH//2, 300, 30, '0', final_score_font, RED, win)
tap_to_play_msg = tap_to_play = BlinkingText(WIDTH//2, HEIGHT-60, 25, "Click To Play",
				 tap_to_play_font, WHITE, win)
final_grade_msg = Message(WIDTH//2, 350, 50, 'D', final_grade_font, RED, win)

# SOUNDS **********************************************************************

player_bullet_fx = pygame.mixer.Sound('Sounds/gunshot.wav')
player_bullet_fx.set_volume(0.1)
click_fx = pygame.mixer.Sound('Sounds/click.mp3')
click_fx.set_volume(0.5)
enemyblast_fx = pygame.mixer.Sound('Sounds/enemyblast.wav')
enemyblast_fx.set_volume(0.3)
playerblast_fx = pygame.mixer.Sound('Sounds/playerblast.wav')
playerblast_fx.set_volume(0.3)
fuel_fx = pygame.mixer.Sound('Sounds/fuel.wav')
fuel_fx.set_volume(0.3)
playercollision_fx = pygame.mixer.Sound('Sounds/playercollision.mp3')
playercollision_fx.set_volume(0.3)
enemycollision_fx = pygame.mixer.Sound('Sounds/enemycollision.mp3')
enemycollision_fx.set_volume(1.0)

pygame.mixer.music.load('Sounds/Never_Gonna_Give_You_Up.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.3)

# GROUPS & OBJECTS ***********************************************pygame.draw.circle(win, WHITE, (WIDTH//2, HEIGHT//2 + 50), 50, 4)*************

bg = Background(win)
p = Player(269, HEIGHT - 50)

enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()
life_group = pygame.sprite.Group()
superweapon_group = pygame.sprite.Group()

# FUNCTIONS *******************************************************************

def shoot_bullet(use_supperweapon = False):
	x, y = p.rect.center[0], p.rect.y
	if use_supperweapon :
		if p.superweapon > 0:
			for dx in range(-3, 4):
				b = Bullet(x, p.rect.center[1], 10, 6, dx)
				player_bullet_group.add(b)
				b = Bullet(x, p.rect.center[1], 10, -6, dx)
				player_bullet_group.add(b)
			for dy in range(-3, 4):
				b = Bullet(x, p.rect.center[1], 10, dy, 6)
				player_bullet_group.add(b)
				b = Bullet(x, p.rect.center[1], 10, dy, -6)
				player_bullet_group.add(b)
		p.superweapon -= 1
	else:
		if p.powerup == 0:
			b = Bullet(x, y, 6)
			player_bullet_group.add(b)
		elif p.powerup == 1 :
			b = Bullet(x-30, y, 6)
			player_bullet_group.add(b)
			b = Bullet(x+30, y, 6)
			player_bullet_group.add(b)
		elif p.powerup == 2:
			b = Bullet(x-30, y, 6)
			player_bullet_group.add(b)
			b = Bullet(x+30, y, 6)
			player_bullet_group.add(b)
			b = Bullet(x, y, 7)
			player_bullet_group.add(b)
			b = Bullet(x, y+65, 7)
			player_bullet_group.add(b)
		elif p.powerup >= 3:
			b = Bullet(x-50, p.rect.center[1], 6)
			player_bullet_group.add(b)
			b = Bullet(x+50, p.rect.center[1], 6)
			player_bullet_group.add(b)
			b = Bullet(x-35, y, 7)
			player_bullet_group.add(b)
			b = Bullet(x+35, y, 7)
			player_bullet_group.add(b)
			b = Bullet(x, y, 8)
			player_bullet_group.add(b)

	player_bullet_fx.play()

def reset():
	enemy_group.empty()
	player_bullet_group.empty()
	enemy_bullet_group.empty()
	explosion_group.empty()
	fuel_group.empty()
	powerup_group.empty()
	life_group.empty()
	superweapon_group.empty()
	p.reset(p.x, p.y)

# VARIABLES *******************************************************************

level = 1
plane_destroy_count = 0
plane_frequency = 5000
start_time = pygame.time.get_ticks()
boss = 0
bossdie = False

moving_left = False
moving_right = False
moving_up = False
moving_down = False

home_page = True
game_page = False
score_page = False

score = 0
sound_on = True
p.powerup = 0
bonus = 0



running = True
while running:
	#偵測鍵盤和滑鼠輸入
	for event in pygame.event.get():
		#關閉視窗離開遊戲
		if event.type == pygame.QUIT:
			running = False
		#按esc 或 q 離開遊戲
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False
			elif home_page:
				home_page = False
				game_page = True
				click_fx.play()
		#使用上下左右移動 空白鍵射擊
		if event.type == pygame.KEYDOWN and game_page:
			if event.key == pygame.K_LEFT:
				moving_left = True
			if event.key == pygame.K_RIGHT:
				moving_right = True
			if event.key == pygame.K_UP:
				moving_up = True
			if event.key == pygame.K_DOWN:
				moving_down = True
			if event.key == pygame.K_SPACE:
				shoot_bullet()
			if event.key == pygame.K_x:
			    shoot_bullet(use_supperweapon=True)
		#放開按鍵停止移動
		if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
			moving_left = False
		if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			moving_right = False
		if event.type == pygame.KEYUP and event.key == pygame.K_UP:
			moving_up = False
		if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			moving_down = False

		#使用滑鼠移動和射擊
		if event.type == pygame.MOUSEBUTTONDOWN:
			if home_page:
				home_page = False
				game_page = True
				click_fx.play()
			elif game_page:
				x, y = event.pos
				if p.rect.collidepoint((x,y)):
					shoot_bullet()
				else:
					if x <= p.rect.x:
						moving_left = True
					if x >= p.rect.x + 100:
						moving_right = True
					if y <= p.rect.y:
						moving_up = True
					elif y > p.rect.y + 86:
						moving_down = True
		#放開滑鼠停止移動
		if event.type == pygame.MOUSEBUTTONUP:
			moving_left = False
			moving_right = False
			moving_up = False
			moving_down = False

#判斷當前頁面
	#起始畫面
	if home_page:
		win.fill(BLACK)
		win.blit(logo_img, (70, 80))
		win.blit(fighter_img, (WIDTH//2 -100, HEIGHT//2))
		tap_to_play_msg.update()
	#結束畫面
	if score_page:
		win.fill(BLACK)
		win.blit(logo_img, (70, 80))
		
		if bossdie:
			game_win_msg1.update()
			game_win_msg2.update()
		else:
			game_over_msg1.update()
			game_over_msg2.update()
		final_score_msg.update(score)

		if bossdie:
			if score < 10000:
				final_grade_msg.update('A+')
			elif score < 10500:
				final_grade_msg.update('A')
			elif score < 11000:
				final_grade_msg.update('A-')
			elif score < 13000:
				final_grade_msg.update('B+')
			elif score < 14000:
				final_grade_msg.update('B')
			elif score < 15000:
				final_grade_msg.update('B-')
			elif score < 16000:
				final_grade_msg.update('C+')
			elif score < 17000:
				final_grade_msg.update('C')
			else:
				final_grade_msg.update('C-')    
		else:
			final_grade_msg.update('F')

		if score >= 7000 or not bossdie:
			score_change_msg1.update()
			score_change_msg2.update()
			score_change_msg3.update()


		if home_btn.draw(win):
			home_page = True
			game_page = False
			score_page = False
			reset()
			click_fx.play()

			plane_destroy_count = 0
			level = 1
			score = 0
			bossdie = False
			bonus = 0

		if replay_btn.draw(win):
			score_page = False
			game_page = True
			reset()
			click_fx.play()

			plane_destroy_count = 0
			#score = 0
			bossdie = False
			bonus = 0

		if sound_btn.draw(win):
			sound_on = not sound_on

			if sound_on:
				sound_btn.update_image(sound_on_img)
				pygame.mixer.music.play(loops=-1)
			else:
				sound_btn.update_image(sound_off_img)
				pygame.mixer.music.stop()
	#遊戲畫面
	if game_page:

		current_time = pygame.time.get_ticks()
		delta_time = current_time - start_time
		if level == 1 and delta_time >= 0.75*plane_frequency:
			type = 1
			x = random.randint(0, 350 )
			y = -100
			e = Enemy(x, y, type)
			enemy_group.add(e)
			start_time = current_time
		elif level == 2 and delta_time >= 0.75*plane_frequency:
			type = 2
			x = random.randint(0, 350 )
			y = -100
			e = Enemy(x, y, type)
			enemy_group.add(e)
			start_time = current_time
		elif level == 3 and delta_time >= 0.75*plane_frequency:
			type = 3
			x = random.randint(0, 350 )
			y = -100
			e = Enemy(x, y, type)
			enemy_group.add(e)
			start_time = current_time
		elif level == 4 and delta_time >= 1.5*plane_frequency:
			type = 4
			x = 130
			y = -400
			if boss == 0:
				e = Enemy(x, y, type)
				if type == 4:
					boss = 1
			enemy_group.add(e)
			start_time = current_time
			

		if plane_destroy_count:
			if plane_destroy_count % 9 == 0:
				if level < 4:
					level += 1
					plane_destroy_count = 0

		
		
		
		
			

				
				


		p.fuel -= 0.05
		bg.update(1)
		#win.blit(clouds_img, (0, 70))

		p.update(moving_left, moving_right, moving_up, moving_down, explosion_group)
		p.draw(win)

		player_bullet_group.update()
		player_bullet_group.draw(win)
		enemy_bullet_group.update()
		enemy_bullet_group.draw(win)
		explosion_group.update()
		explosion_group.draw(win)
		fuel_group.update()
		fuel_group.draw(win)
		powerup_group.update()
		powerup_group.draw(win)
		life_group.update()
		life_group.draw(win)
		superweapon_group.update()
		superweapon_group.draw(win)

		enemy_group.update(enemy_bullet_group, explosion_group)
		enemy_group.draw(win)

		if p.alive:
			#偵測玩家被敵人子彈擊中
			player_hit = pygame.sprite.spritecollide(p, enemy_bullet_group, False)
			for bullet in player_hit:
				p.health -= bullet.damage
				
				x, y = bullet.rect.center
				explosion = Explosion(x, y, 1)
				explosion_group.add(explosion)

				bullet.kill()
				playercollision_fx.play()
			#偵測敵人被玩家子彈擊中
			for bullet in player_bullet_group:
				planes_hit = pygame.sprite.spritecollide(bullet, enemy_group, False)
				for plane in planes_hit:
					plane.health -= bullet.damage
					if plane.health <= 0:
						if plane.type == 4:
							bossdie = True
						x, y = plane.rect.center
						rand = random.randint(1, 1000000)
						if rand >= 1 and rand <= 400000:
							fuel = Fuel(x, y)
							fuel_group.add(fuel)
						elif rand > 400000 and rand <= 700000 :
							life = Life(x, y)
							life_group.add(life)
						elif rand > 700000 and rand <= 900000 :
							power = Powerup(x, y)
							powerup_group.add(power)
						else:
							superweapon = Superweapon(x, y)
							superweapon_group.add(superweapon)

						plane_destroy_count += 1
						enemyblast_fx.play()
						enemy_group.remove(plane)


					x, y = bullet.rect.center
					explosion = Explosion(x, y, 1)
					explosion_group.add(explosion)

					bullet.kill()
					enemycollision_fx.play()
			#偵測和敵人碰撞
			player_collide = pygame.sprite.spritecollide(p, enemy_group, True)
			if player_collide:
				x, y = p.rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)

				x, y = player_collide[0].rect.center
				explosion = Explosion(x, y, 2)
				explosion_group.add(explosion)
				
				p.health -= 200
		
				
		
				
		#吃道具
			#加油
			if pygame.sprite.spritecollide(p, fuel_group, True):
				p.fuel += 25
				if p.fuel >= 500:
					p.fuel = 500
				fuel_fx.play()
			#增強子彈型態
			if pygame.sprite.spritecollide(p, powerup_group, True):
				p.powerup += 1
				fuel_fx.play()
			#加命
			if pygame.sprite.spritecollide(p, life_group, True):
				p.health += 100
				if p.health > 1000:
					p.health = 1000
				fuel_fx.play()
			#累積超級武器
			if pygame.sprite.spritecollide(p, superweapon_group, True):
				p.superweapon += 1
				fuel_fx.play()

		#判斷遊戲結束
		if not p.alive or p.fuel <= -10 or bossdie :
			playerblast_fx.play()
			if len(explosion_group) == 0:
				game_page = False
				score_page = True
				reset()

		score += 1
		score_msg.update(score)
		#繪製玩家血量油量
		
		pygame.draw.rect(win, GREEN, (55, 800, p.fuel/5, 10), border_radius=4)
		pygame.draw.rect(win, BLACK, (55, 800, 100, 10), 2, border_radius=4)
		pygame.draw.rect(win, RED, (55, 820, p.health/10, 10), border_radius=4)
		pygame.draw.rect(win, BLACK, (55, 820, 100, 10), 2, border_radius=4)
		win.blit(plane_img, (10, 790))
		if level == 4 and boss == 0:
			if bonus == 0:
				fuel = Fuel(100, -40)
				fuel_group.add(fuel)
				life = Life(100, -140)
				life_group.add(life)
				power = Powerup(400, -40)
				powerup_group.add(power)
				superweapon = Superweapon(400, -140)
				superweapon_group.add(superweapon)
				bonus = 1
			if delta_time % 600 > 250:
				win.blit(mark_img, (145, 75))
			if delta_time <= 0.75*plane_frequency:
				win.blit(warning_img, (145, 245))
			else:
				win.blit(chinese_warning_img, (145, 245))
		
		
		#繪製敵人血量
		#if not bossdie:
		for plane in enemy_group:
			if plane.type == 1:
				pygame.draw.rect(win, RED, (plane.rect.x, plane.rect.y-10, plane.health/2, 10), border_radius=4)
				pygame.draw.rect(win, BLACK, (plane.rect.x, plane.rect.y-10, 100, 10), 2, border_radius=4)
			elif plane.type == 2:
				pygame.draw.rect(win, RED, (plane.rect.x, plane.rect.y-10, plane.health/2.5, 10), border_radius=4)
				pygame.draw.rect(win, BLACK, (plane.rect.x, plane.rect.y-10, 100, 10), 2, border_radius=4)
			elif plane.type == 3:
				pygame.draw.rect(win, RED, (plane.rect.x, plane.rect.y-10, plane.health/4, 10), border_radius=4)
				pygame.draw.rect(win, BLACK, (plane.rect.x, plane.rect.y-10, 100, 10), 2, border_radius=4)
			elif plane.type == 4:
				pygame.draw.rect(win, RED, (35, 25, plane.health/25, 10), border_radius=4)
				pygame.draw.rect(win, BLACK, (35, 25, 400, 10), 2, border_radius=4)
			

					

		

		

	pygame.draw.rect(win, WHITE, (0,0, WIDTH, HEIGHT), 5, border_radius=4)
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()