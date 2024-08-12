import random
import pygame
from pathfinding import Pathfinding

SQUARE_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Grid:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid()
        self.start_point = None
        self.end_point = None
        self.path = []

    def create_grid(self):
        """Initialize a grid of empty squares."""
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def draw_grid(self, screen):
        """Draw the grid lines."""
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE,
                                 row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    def draw_obstacles(self, screen):
        """Draw obstacles on the grid."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(
                        screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def set_obstacle(self, row, col):
        """Set a specific cell as an obstacle."""
        # if self.grid[row][col] == 0:  # Ensure not to overwrite start/end points
        #     self.grid[row][col] = 1

        if self.grid[row][col] == 1:
            self.grid[row][col] = 0  # Remove the obstacle if it already exists
        elif self.grid[row][col] == 0:
            self.grid[row][col] = 1  # Set the obstacle if the cell is empty

    def random_obstacles(self, count):
        """Randomly place a specified number of obstacles on the grid."""
        for _ in range(count):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            # Ensure that you're not placing an obstacle where one already exists
            if self.grid[row][col] == 0:
                self.set_obstacle(row, col)

    def set_start_point(self, row, col):
        """Set the start point on the grid."""
        self.start_point = (row, col)
        self.grid[row][col] = 2  # Mark start point with a different value

    def set_end_point(self, row, col):
        """Set the end point on the grid."""
        self.end_point = (row, col)
        self.grid[row][col] = 3  # Mark end point with a different value

    def draw_points(self, screen):
        """Draw the start and end points on the grid."""
        if self.start_point:
            row, col = self.start_point
            # print(f"Drawing start point at ({row}, {col})")  # Debugging output
            pygame.draw.rect(screen, GREEN, (col * SQUARE_SIZE,
                             row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        if self.end_point:
            row, col = self.end_point
            # print(f"Drawing end point at ({row}, {col})")  # Debugging output
            pygame.draw.rect(screen, RED, (col * SQUARE_SIZE,
                             row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_path(self, screen):
        """Draw the path found by the algorithm."""
        for row, col in self.path:
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE,
                             row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def find_path(self):
        """Find the path using the Pathfinding class."""
        pathfinder = Pathfinding(
            self.grid, self.start_point, self.end_point, self.rows, self.cols)
        if pathfinder.find_path():
            self.path = pathfinder.get_path()

    def reset(self):
        """Reset the grid to the initial state."""
        self.grid = self.create_grid()  # Reset the grid
        self.start_point = None  # Clear the start point
        self.end_point = None  # Clear the end point
        self.path = []  # Clear the path
