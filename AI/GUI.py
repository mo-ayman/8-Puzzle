from copy import deepcopy

import pygame

from AI import State


class GUI(object):
    def __init__(self, initial_state: State):
        pygame.init()
        self.actual_position = None
        self.expected_position = None
        self.screen = None
        self.initial_state = initial_state
        self.font = pygame.font.SysFont('arial', 32)

    def print_grid(self, grid):
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    continue
                surface = self.font.render(str(grid[i][j]), True, (0, 0, 0))
                self.screen.blit(surface, self.actual_position[i][j])
        pygame.display.update()

    def transition(self, current_state: State, target_state: State):
        x1, y1 = target_state.find_empty()
        x2, y2 = current_state.find_empty()

        actual_x = self.actual_position[x1][y1][0]
        actual_y = self.actual_position[x1][y1][1]
        target_x = self.expected_position[x2][y2][0]
        target_y = self.expected_position[x2][y2][1]
        while actual_x != target_x or actual_y != target_y:
            self.screen.fill((255, 255, 255))

            if actual_x < target_x:
                actual_x += 0.1
                if actual_x > target_x:
                    actual_x = target_x

            elif actual_x > target_x:
                actual_x -= 0.1
                if actual_x < target_x:
                    actual_x = target_x

            if actual_y < target_y:
                actual_y += 0.1
                if actual_y > target_y:
                    actual_y = target_y

            elif actual_y > target_y:
                actual_y -= 0.1
                if actual_y < target_y:
                    actual_y = target_y

            self.actual_position[x1][y1] = (actual_x, actual_y)
            self.print_grid(current_state.grid)

    def run(self):
        icon = pygame.image.load("ai.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("AI Search")
        width = 800
        height = 600
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((255, 255, 255))
        pygame.display.update()

        self.expected_position = [[(width / 6, height / 6), (width / 2, height / 6), (5 * width / 6, height / 6)],
                                  [(width / 6, height / 2), (width / 2, height / 2), (5 * width / 6, height / 2)],
                                  [(width / 6, 5 * height / 6), (width / 2, 5 * height / 6),
                                   (5 * width / 6, 5 * height / 6)]]

        self.actual_position = deepcopy(self.expected_position)

        while True:
            print(self.initial_state)
            if self.initial_state.previous_state is None:
                break
            self.transition(self.initial_state, self.initial_state.previous_state)
            self.initial_state = self.initial_state.previous_state

        running: bool = True
        while running:
            events = pygame.event.get()
            for event in events:
                print(event)
                if event.type == pygame.QUIT:
                    running = False
