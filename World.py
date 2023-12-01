'''
Can resolve physical problems in a 2 dimensional world
'''
from Vector import Vec2Int

class World:
    def __init__(self, size:Vec2Int, chunk_size:int = 10) -> None:
        self.length = size.x
        self.width = size.y
        self.chunk_size = chunk_size



