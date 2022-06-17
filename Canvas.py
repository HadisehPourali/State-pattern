class Canvas:
    def __init__(self, currentTool):
        self.currentTool = currentTool

    def getCurrentTool(self):
        return currentTool

    def mouseDown(self):
        self.currentTool.mouseDown()

    def mouseUp(self):
        self.currentTool.mouseUp()