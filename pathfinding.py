import heapq

class Pathfinding:

    def __init__(self, grid, start, end, rows, cols) -> None:
        self.grid = grid
        self.start_point = start
        self.end_point = end
        self.rows = rows
        self.cols = cols
        self.path = []

    def heuristic(self, node1, node2):
        """Calculate the Manhattan distance between two nodes."""
        x1, y1 = node1
        x2, y2 = node2
        return abs(x1 - x2) + abs(y1 - y2)

    def get_neighbors(self, node):
        """Get valid neighboring nodes for a given node."""
        row, col = node
        neighbors = []

        if row > 0:  # Up
            neighbors.append((row - 1, col))
        if row < self.rows - 1:  # Down
            neighbors.append((row + 1, col))
        if col > 0:  # Left
            neighbors.append((row, col - 1))
        if col < self.cols - 1:  # Right
            neighbors.append((row, col + 1))

        return neighbors

    def find_path(self):
        """Implement the A* pathfinding algorithm."""
        if not self.start_point or not self.end_point:
            return False  # No path to find if start or end is missing

        start = self.start_point
        end = self.end_point

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {(row, col): float('inf') for row in range(self.rows) for col in range(self.cols)}
        g_score[start] = 0
        f_score = {(row, col): float('inf') for row in range(self.rows) for col in range(self.cols)}
        f_score[start] = self.heuristic(start, end)

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == end:
                self.reconstruct_path(came_from, current)
                return True

            for neighbor in self.get_neighbors(current):
                if self.grid[neighbor[0]][neighbor[1]] == 1:  # Ignore obstacles
                    continue

                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return False  # No path found


    def reconstruct_path(self, came_from, current):
        """Reconstruct the path from start to end."""
        self.path = []
        while current in came_from:
            self.path.append(current)
            current = came_from[current]
        self.path.reverse()  # Reverse the path to start from the beginning

    def get_path(self):
        """Return the computed path."""
        return self.path
