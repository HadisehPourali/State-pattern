from Tool import Tool

class BrushTool(Tool):
    def mouseDown(self):
        print("Brush icon")

    def mouseUp(self):
        print("Draw a line")