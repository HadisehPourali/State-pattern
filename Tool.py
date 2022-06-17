from abc import ABCMeta, abstractmethod

class Tool(metaclass=ABCMeta):
    @abstractmethod
    def mouseDown(self):
        pass

    @abstractmethod
    def mouseUp(self):
        pass
