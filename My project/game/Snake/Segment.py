from Main import SEG_SIZE , c
class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="white")