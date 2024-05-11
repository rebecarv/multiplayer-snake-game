import pygame
import colors
import time

class Screen:
    def __init__(self,width,height):
        # Initializing screen
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.font_style = pygame.font.SysFont(None, 30)

    def get_width(self):
        """Returns width of the screen"""
        return self.width
    
    def get_height(self):
        """Returns height of the screen"""
        return self.height

    def multiline_centered_messages(self, messages: list, color):
        """Function for displaying a list of messages on the screen"""
        font = pygame.font.SysFont(None, 30)  # Initialize font
        text_surfaces = [font.render(message, True, color) for message in messages]  # Render the messages

        # Get the dimensions of the text surfaces
        text_widths = [surf.get_width() for surf in text_surfaces]
        text_heights = [surf.get_height() for surf in text_surfaces]

        total_height = sum(text_heights) + (len(messages) - 1) * 5  # Add spacing between messages

        # Calculate the y-coordinate to center the text vertically
        y = (self.height - total_height) // 2

        for text_surface, text_height in zip(text_surfaces, text_heights):
            # Calculate the x-coordinate to center the text horizontally
            x = (self.width - text_surface.get_width()) // 2

            # Blit the text surface onto the screen
            self.screen.blit(text_surface, (x, y))

            # Move down for the next message
            y += text_height + 5

    def horizontal_centered_message(self, message, color, y, size=30):
        """Function for displaying messages on the screen"""
        font = pygame.font.SysFont(None, size) # Initialize font
        text_surface = font.render(message, True, color) # Render the message

        # Get the dimensions of the text surface
        text_width, text_height = text_surface.get_size()

        # Calculate the coordinates to center the text
        x = (self.width - text_width) // 2
        # y = (self.height - text_height) // 2

        # Blit the text surface onto the screen
        self.screen.blit(text_surface, (x, y))

    def starting_screen(self):
        """Displays the starting screen"""
        self.screen.fill(colors.BLACK)
        self.multiline_centered_messages(("Welcome to the ultimate snake game.","Press space to play."), colors.MINT_CREAM)
        pygame.display.flip()

    def render_game_screen(self, controller, all_sprites_list: pygame.sprite.Group, snake1, snake2):
        """Renders the screen during game."""
        if not (snake1.Q and snake2.Q): # Check for winner
            self.winner_message(controller, snake1, snake2)
        else: # No winner. Game continues. Update Sprites
            self.screen.fill(colors.BLACK)
            all_sprites_list.update()
            all_sprites_list.draw(self.screen)

        pygame.display.flip()

    def winner_message(self, controller, snake1, snake2) -> bool:
        """Displays the round winner message on top of the current screen. Returns False if player is trying to quit"""
        # Both snakes died at the same time
        if not snake1.Q and not snake2.Q:
            self.multiline_centered_messages(("Draw!", "Press space to restart."), colors.MINT_CREAM)
            pygame.display.flip()
            run = controller.wait_for_space()
            if not run:
                return False
            self.display_scores(controller, snake1.score,snake2.score)
            snake1.reset(100, 100)
            snake2.reset(self.width - 100, self.height - 100)
        # Player 1 died
        elif not snake1.Q and snake2.Q:
            snake2.score += 1       
            self.multiline_centered_messages(("Player 2 wins!", "Press space to restart."), colors.MINT_CREAM)
            pygame.display.flip()
            run = controller.wait_for_space()
            if not run:
                return False
            self.display_scores(controller, snake1.score,snake2.score)
            snake1.reset(100, 100)
            snake2.reset(self.width - 100, self.height - 100)
        #Player 2 died
        elif snake1.Q and not snake2.Q:
            snake1.score += 1
            self.multiline_centered_messages(("Player 1 wins!", "Press space to restart."), colors.MINT_CREAM)
            pygame.display.flip()
            run = controller.wait_for_space()
            if not run:
                return False
            self.display_scores(controller, snake1.score,snake2.score)
            snake1.reset(100, 100)
            snake2.reset(self.width - 100, self.height - 100)
        return True

    def display_scores(self, controller, score1: int, score2: int) -> bool:
        """Displays scores on the screen"""
        print("Im displaying scores")
        self.screen.fill(colors.BLACK)
        self.multiline_centered_messages(("The current score is:", str(score1) + " : " + str(score2), "Press space to continue."), colors.MINT_CREAM)
        pygame.display.flip()
        time.sleep(1)
        run = controller.wait_for_space()
        return run
        
        

    