import pygame


class GUI(object):
    def __init__(self):
        self.__initialState = None

    @staticmethod
    def run():
        pygame.init()
        screen = pygame.display.set_mode((800, 600))


    def getInput(self):
        raise NotImplementedError

    def startSearch(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

