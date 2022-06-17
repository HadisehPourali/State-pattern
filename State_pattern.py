from Canvas import Canvas
from SelectionTool import SelectionTool
from BrushTool import BrushTool
from EraserTool import EraserTool

class State:
    canvas = Canvas(EraserTool())
    canvas.mouseDown()
    canvas.mouseUp()