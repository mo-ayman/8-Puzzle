class GUI(object):
    def __init__(self):
        self.__initialState = None

    def getInput(self):
        raise NotImplementedError

    def startSearch(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

