import pygame
import sys

class PygameWrapper:
    def __init__(self, width, height, title="Pygame Window"):
        self.width = width
        self.height = height
        self.title = title

        # Initialize Pygame
        pygame.init()
        self.clock = pygame.time.Clock()

        # Create the game window
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # Set initial state
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(60)  # Cap frame rate at 60 FPS
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Update game logic here
        pass

    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw game objects here

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    # Create an instance of PygameWrapper
    game = PygameWrapper(800, 600)
    # Run the game
    game.run()
