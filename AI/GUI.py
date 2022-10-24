from copy import deepcopy

import pygame

from AI import State


class GUI(object):
    """This class handles the all the functionality of GUI of the grid table only"""

    def __init__(
            self, finishing_state: State, nodes_expanded: int, time_taken, max_depth
    ):
        pygame.init()  # REQUIRED for pygame setup, nothing will work without it
        self.actual_position = None
        self.expected_position = None
        self.screen = None
        self.finishing_state = finishing_state
        self.nodes_expanded = nodes_expanded
        self.font = pygame.font.SysFont("arial", 32)
        self.labels_font = pygame.font.SysFont("arial", 24)
        self.width = 800
        self.height = 600

        # Defining buttons and labels
        self.next_button = pygame.Rect(15, self.height - 50, 90, 40)
        self.next_label = self.labels_font.render("Next Step", True, (0, 0, 0))
        self.cost_label = self.labels_font.render(
            "Path Cost: " + str(self.finishing_state.previous_cost), True, (0, 0, 0)
        )
        self.nodes_expanded_label = self.labels_font.render(
            "Nodes Expanded: " + str(self.nodes_expanded), True, (0, 0, 0)
        )
        self.search_depth_label = self.labels_font.render(
            "Max Depth: " + str(max_depth), True, (0, 0, 0)
        )
        self.running_time_label = self.labels_font.render(
            "Time Taken: " + str(time_taken), True, (0, 0, 0)
        )

    def print_buttons(self, in_transit: bool = False):
        """Adds the buttons and labels to the screen before updating the display"""

        # Disable the "Next Step" button while cells are moving
        if not in_transit:
            pygame.draw.rect(self.screen, (0, 0, 0), self.next_button, 1)
            self.screen.blit(self.next_label, (20, self.height - 50))

        self.screen.blit(self.cost_label, (130, self.height - 50))
        self.screen.blit(self.nodes_expanded_label, (280, self.height - 50))
        self.screen.blit(self.search_depth_label, (500, self.height - 50))
        self.screen.blit(self.running_time_label, (650, self.height - 50))

    def print_grid(self, grid):
        """Adds the cells to the screen and updates the display"""

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:  # The empty cell should not be printed
                    continue
                surface = self.font.render(str(grid[i][j]), True, (0, 0, 0))    # Add cell number to a surface
                self.screen.blit(surface, self.actual_position[i][j])           # Add the surface to the screen
        pygame.display.update()

    def transition(self, current_state: State, target_state: State):
        """Handles the transition between two states
        Redraw all the screen with its grid, buttons, and labels then updates the display."""

        x1, y1 = target_state.find_empty()
        x2, y2 = current_state.find_empty()

        actual_x = self.actual_position[x1][y1][0]
        actual_y = self.actual_position[x1][y1][1]
        target_x = self.expected_position[x2][y2][0]
        target_y = self.expected_position[x2][y2][1]
        while actual_x != target_x or actual_y != target_y:
            self.screen.fill((255, 255, 255))
            self.print_buttons(in_transit=True)

            if actual_x < target_x:
                actual_x += 1
                if actual_x > target_x:
                    actual_x = target_x

            elif actual_x > target_x:
                actual_x -= 1
                if actual_x < target_x:
                    actual_x = target_x

            if actual_y < target_y:
                actual_y += 1
                if actual_y > target_y:
                    actual_y = target_y

            elif actual_y > target_y:
                actual_y -= 1
                if actual_y < target_y:
                    actual_y = target_y

            self.actual_position[x1][y1] = (actual_x, actual_y)
            self.print_grid(current_state.get_grid())

        self.print_buttons(in_transit=False)
        pygame.display.update()
        self.actual_position = deepcopy(self.expected_position)

    def run(self):
        """GUI entry point"""

        icon = pygame.image.load("ai.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("AI Search")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((255, 255, 255))
        pygame.display.update()

        # Default position for each cell
        self.expected_position = [
            [
                (self.width / 6, self.height / 6),
                (self.width / 2, self.height / 6),
                (5 * self.width / 6, self.height / 6),
            ],
            [
                (self.width / 6, self.height / 2),
                (self.width / 2, self.height / 2),
                (5 * self.width / 6, self.height / 2),
            ],
            [
                (self.width / 6, 5 * self.height / 6),
                (self.width / 2, 5 * self.height / 6),
                (5 * self.width / 6, 5 * self.height / 6),
            ],
        ]

        self.actual_position = deepcopy(self.expected_position)     # A copy of positions to be used in transition

        # Make the list of states from finish to start and reverse it
        states = [self.finishing_state]
        current_state = self.finishing_state
        while current_state.previous_state is not None:
            states.append(current_state.previous_state)
            current_state = current_state.previous_state
        states.reverse()

        # Initial Frame, later frames will be handled by the transition method
        self.print_grid(states[0].get_grid())
        self.print_buttons()

        state_index = 0
        running: bool = True
        while running:
            pygame.display.update()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.next_button.collidepoint(x, y) and state_index + 1 != len(
                            states
                    ):  # Next Step button is clicked
                        self.transition(states[state_index], states[state_index + 1])
                        state_index += 1
                if event.type == pygame.QUIT:
                    running = False
