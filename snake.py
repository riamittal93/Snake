import pygame
import math

colors = {
            'BLACK': (0, 0, 0),
            'WHITE': (255, 255, 255)
          }
screen_size = width, height = 640, 480
score_pos = (width * 7/10, 15)
score_per_food = 10
# Direction of snake: 0 = right, 1 = up, 2 = left, 3 = down

class Snake:
    def __init__(self):
        self.position = [300, 300]
        self.direction = 0
        self.length = 30
        self.width = 5
        self.growth = 2
        self.speed = 2

    def turn_left(self):
        self.direction += 1
        if self.direction > 3:
            self.direction = 0

    def turn_right(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction = 3

    def draw(self, screen):
        head = self.position
        if self.direction == 0:
            tail = [head[0] - self.length, head[1]]

        if self.direction == 1:
            tail = [head[0], head[1] + self.length]

        if self.direction == 2:
            tail = [head[0] + self.length, head[1]]

        if self.direction == 3:
            tail = [head[0], head[1] - self.length]

        pygame.draw.line(screen, colors['WHITE'], head, tail, self.width)

    def move_forward(self):
        if self.direction == 0:
            self.position[0] += self.speed

        if self.direction == 1:
            self.position[1] -= self.speed

        if self.direction == 2:
            self.position[0] -= self.speed

        if self.direction == 3:
            self.position[1] += self.speed

        # Check for screen bounds
        if self.position[0] > width:
            self.position[0] = 0

        if self.position[0] < 0:
            self.position[0] = width

        if self.position[1] > height:
            self.position[1] = 0

        if self.position[1] < 0:
            self.position[1] = height

    def grow_when_eat(self):
        self.length += self.growth
                 

class FoodPellet:
    def __init__(self):
        self.position = [200, 200]
        self.radius = 5
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, colors['WHITE'], self.position, self.radius, 0)

def distance(a, b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

def is_eating(snake, food):
    ''' Checks if the snake is in eating range  of the food '''
    return distance(snake.position, food.position) <= food.radius

def draw_score(screen, score):
    font = pygame.font.SysFont('UbuntuMono-R', 30)
    text_surface = font.render('score:  ' + str(score), False, colors['WHITE'])
    screen.blit(text_surface, score_pos)

def main():
    pygame.init()

    screen = pygame.display.set_mode(screen_size)

    snake = Snake()
    score = 0
    run = True
    clock = pygame.time.Clock()

    food = FoodPellet()

    while run:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.turn_left()
                if event.key == pygame.K_RIGHT:
                    snake.turn_right()

        screen.fill(colors['BLACK'])

        snake.move_forward()

        if is_eating(snake, food):
            score += score_per_food
            snake.grow_when_eat()

        def draw_everything():
            food.draw(screen)
            snake.draw(screen)
            draw_score(screen, score)

        draw_everything()
        pygame.display.flip()

if __name__ == '__main__':
    main()
