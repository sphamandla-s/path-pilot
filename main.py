import pygame
import sys
from grid import Grid

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20  # Number of rows and columns
SQUARE_SIZE = WIDTH // COLS  # Size of each square

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Grid")


def main():
    grid = Grid(ROWS, COLS)
    clock = pygame.time.Clock()

    grid.random_obstacles(200)
    setting_start = True
    setting_end = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Only set points when mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE

                if setting_start:
                    grid.set_start_point(row, col)
                    setting_start = False
                    setting_end = True  # Now allow setting the end point
                    print("Start Point Set")
                elif setting_end:
                    if grid.grid[row][col] == 0:  # Ensure not to overwrite start point
                        grid.set_end_point(row, col)
                        setting_end = False  # End point is set, now stop setting points
                        print("End Point Set")
                else:  # After setting both start and end, set obstacles
                    # Ensure not to overwrite start/end points
                    if (row, col) != grid.start_point or (row, col) != grid.end_point:
                        grid.set_obstacle(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid.find_path()

                if event.key == pygame.K_r:
                    grid.reset()
                    grid.random_obstacles(200)
                    setting_start = True  # Allow setting start point again
                    setting_end = False  # Reset the state for setting points
                    print("Game Reset")

        # Fill the screen with a color (e.g., grey)
        screen.fill((169, 169, 169))

        # Draw the grid
        grid.draw_grid(screen)
        grid.draw_obstacles(screen)
        grid.draw_points(screen)
        grid.draw_path(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
