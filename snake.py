import pygame

speed = 2
growth = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ScreenSize = width, height = 640, 480
# Direction of snake: 0 = right, 1 = up, 2 = left, 3 = down

class Snake:
    def __init__(self):
        self.position = [300, 300]
        self.direction = 0
        self.length = 30
        self.width = 5

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

       
            
        pygame.draw.line(screen, WHITE, head, tail, self.width)

    def move_forward(self):
        if self.direction == 0:
            self.position[0] += speed

        if self.direction == 1:
            self.position[1] -= speed

        if self.direction == 2:
            self.position[0] -= speed

        if self.direction == 3:
            self.position[1] += speed

        if self.position[0] > width:
            self.position[0] = 0

        if self.position[0] < 0:
            self.position[0] = width
            

        if self.position[1] > height:
            self.position[1] = 0
           

        if self.position[1] < 0:
            self.position[1] = height
            
                 

class FoodPellet:
    def __init__(self):
        self.position = [200, 200]
        self.radius = 5
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, WHITE, self.position, self.radius, 0)


def main():
    pygame.init()


    
    screen = pygame.display.set_mode(ScreenSize)

    snake = Snake()

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

        screen.fill(BLACK)

        food.draw(screen)
        snake.move_forward()
        snake.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
