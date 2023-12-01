
from time import perf_counter as time
from numba import njit
from Vector import Vec2Int
from PhysicsObjects import RigidCircle, Constraint

times:dict[str,list] = {}
def profile(func):
    times[str(func.__name__)] = []
    def inner(*args,**kwargs):
        global times 
        start = time()
        value = func(*args,**kwargs)
        end = time()
        times[str(func.__name__)].append(end-start)
        print(f"{func.__name__} took {end - start} seconds")
        return value
    return inner


def insideSquare(px:float,py:float,cx:int,cy:int,s:float):
    return not((px - cx).__abs__() > s/2 or (py - cy).__abs__() > s/2)

@njit
def circleOverlapsSquare(x:float,y:float,r:float,cx:float,cy:float,s:int):
    offset_x = abs(x - cx) - s/2
    offset_y = abs(y - cy) - s/2
    if offset_x < 0: offset_x = 0
    if offset_y < 0: offset_y = 0
    return offset_x*offset_x+offset_y*offset_y < r* r


class Solver:
    def __init__(self,size:Vec2Int,chunk_size:int) -> None:
        self.length = size.x
        self.width = size.y
        self.substeps = 2
        self.chunk_size = chunk_size
        self._space:tuple[tuple[list[RigidCircle],...],...] = tuple(
            (
                tuple(
                    [] for y in range((self.width/chunk_size).__ceil__()) 
                ) for y in range((self.length/chunk_size).__ceil__())
            )
        )
        self.objects:list[RigidCircle] = []
        self.constraints:list[Constraint] = []

    def addObject(self,obj:RigidCircle):
        self.objects.append(obj)
        xchunk = obj.pos.x.__trunc__() // self.chunk_size
        ychunk = obj.pos.y.__trunc__() // self.chunk_size
        self._space[xchunk][ychunk].append(obj)
        


    def update(self):
        for y in range(1,self.width-1):
            for x in range(1,self.length-1):
                surrounding_cells = ((x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1))
                
                for obj in self._space[x][y]:
                    checking_cells = {(0,0),}
                    
                    


    def chunkCoordsOfObj(self,obj:RigidCircle) -> Vec2Int:
        return obj.pos.integerDivision(self.chunk_size)

