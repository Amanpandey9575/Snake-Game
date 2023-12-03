import pygame 
import random
pygame.init()

#Colors
sky_blue = (135,206,235)
red =  (255, 0, 0)
black = (0, 0, 0)


screen_width = 700
screen_height = 500


#Creating window
gamewindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Snakes with Aman")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

def plot_snake(gamewindow, color, snake_list, snake_y, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

#Creating a game loop
def gameloop():
        #Game specific variaables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    snake_size = 15
    fps = 60

    while not exit_game:
        if game_over:

            gamewindow.fill(sky_blue)
            text_screen("Game Over! Press Enter to Continue", red, 170, 230)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
            
        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 3
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 3
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - 3
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 3
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x )<6 and abs(snake_y - food_y)<6:
                
                score +=1
                
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length +=5
                
            
            gamewindow.fill(sky_blue)
            text_screen ("score : "+ str (score) , red, 5,5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length: 
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height :
                game_over = True
                print("Game Over")

            #pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake (gamewindow, black, snk_list, snake_y, snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
gameloop()

