from Tool import Tool

class SelectionTool(Tool):
    def mouseDown(self):
        print("Selection icon")

    def mouseUp(self):
        print("Draw a dashed rectangle")