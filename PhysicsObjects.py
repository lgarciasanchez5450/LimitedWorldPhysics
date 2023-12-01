from Vector import Vec2
class RigidCircle:
    def __init__(self,pos:Vec2, rad:float):
        self.pos = pos
        self.velocity = Vec2.zero
        self.rad = rad

    
class Constraint:
    def __init__(self,obj1:RigidCircle,obj2:RigidCircle,length:float,stiffness:float):
        self.obj1 = obj1
        self.obj2 = obj2
        self.length = length
        self.stiffness = stiffness