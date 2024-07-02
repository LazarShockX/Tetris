import pygame, sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 400)

k_down_held = False
k_left_held = False
k_right_held = False

left_move_counter = 0
right_move_counter = 0
down_move_counter = 0
move_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                k_left_held = True
            if event.key == pygame.K_RIGHT and not game.game_over:
                k_right_held = True
            if event.key == pygame.K_DOWN and not game.game_over:
                k_down_held = True
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
            if event.key == pygame.K_SPACE and not game.game_over:
                game.drop_block()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                k_left_held = False
            if event.key == pygame.K_RIGHT:
                k_right_held = False
            if event.key == pygame.K_DOWN:
                k_down_held = False
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    if k_left_held and not game.game_over:
        left_move_counter += 1
        if left_move_counter >= move_speed:
            game.move_left()
            left_move_counter = 0

    if k_right_held and not game.game_over:
        right_move_counter += 1
        if right_move_counter >= move_speed:
            game.move_right()
            right_move_counter = 0

    if k_down_held and not game.game_over:
        down_move_counter += 1
        if down_move_counter >= move_speed:
            game.move_down()
            game.update_score(0, 1)
            down_move_counter = 0

    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)