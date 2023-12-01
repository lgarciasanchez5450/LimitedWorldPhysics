from typing import final
from math import cos, sin, pi,sqrt,floor,atan2
from random import random
class Vec2:
	__slots__  = ('x','y')
	def __init__(self,x:float,y:float):
		self.x = x
		self.y = y

	@final
	@classmethod
	@property
	def zero(cls):
		return Vec2(0.0,0.0)
	
	@final
	@classmethod
	@property
	def random(cls):
		'''A random Vector2 with a random distribution from [-1,1] on both x and y axis'''
		return Vec2(random()*2-1,random()*2-1)
		
	@final
	@classmethod
	@property
	def randdir(cls):
		angle = 2*pi*random()
		return Vec2(cos(angle),sin(angle))
	

	def __eq__(self,__object: "Vec2"):
		return self.x == __object.x and self.y == __object.y
	
	def __add__(self,__object: "Vec2"):
		return Vec2(self.x + __object.x,self.y + __object.y)
	
	def __sub__(self,__object: "Vec2"):
		return Vec2(self.x - __object.x,self.y - __object.y)
	
	def __mul__(self,__object:float|int):
		return Vec2(self.x *__object,self.y * __object)
	
	def __truediv__(self,__object:float|int):
		return Vec2(self.x / __object, self.y / __object)
	
	def __floordiv__(self,__object: float|int):
		return Vec2(self.x // __object, self.y // __object)
	
	def integerDivision(self,__object:int):
		return Vec2Int((self.x//__object).__trunc__(), (self.y//__object).__trunc__())

	def dot(self,__object: "Vec2"):
		return Vec2(self.x*__object.x,self.y*__object.y)
	
	def vector_mul(self,__object: "Vec2"):
		return Vec2(self.x*__object.x,self.y*__object.y)
	
	def __getitem__(self,__index:int) -> float:
		return (self.x,self.y)[__index]
	
	@property
	def x_comp(self):
		return Vec2(self.x,0)
	
	@property
	def y_comp(self):
		return Vec2(0,self.y)
	
	def __iadd__(self,__object: "Vec2"):
		self.x += __object.x
		self.y += __object.y
		return self

	def __isub__(self,__object: "Vec2"):
		self.x -= __object.x
		self.y -= __object.y
		return self

	def __imul__(self,__object:float|int):
		self.x *= __object
		self.y *= __object
		return self

	def __str__(self) -> str:
		return f"Vec2(x:{self.x}, y:{self.y})"	
	
	def __neg__(self):
		return Vec2(-self.x,-self.y)
	
	def inverse(self):
		return Vec2(1/self.x,1/self.y)
	
	def __matmul__(self,__object: "Vec2"):
		return Vec2(self.x * __object.x,self.y * __object.y)

	@property
	def isZero(self) -> bool:
		return self.x == self.y == 0.0
	
	def magnitude_squared(self):
		return self.x*self.x+self.y*self.y
	
	def magnitude(self):
		return sqrt(self.magnitude_squared())
	
	def reset(self):
		'''Reset each axis to 0'''
		self.x = 0.0
		self.y = 0.0

	def __bool__(self):
		return (self.x or self.y).__bool__()
	
	def __iter__(self):
		yield self.x
		yield self.y
	
	def set_to(self,__object: "Vec2"):
		self.x = __object.x
		self.y = __object.y

	def from_tuple(self,tup:tuple[float,float]):
		self.x = tup[0]
		self.y = tup[1]

	@property
	def tuple(self):
		return (self.x,self.y)

	def copy(self):
		return Vec2(self.x,self.y)
	
	def rotate(self,theta:float|int):
		cs = cos(theta)
		sn = sin(theta)
		px = self.x * cs - self.y * sn
		py = self.x * sn + self.y * cs
		self.x = px
		self.y = py

	def floored(self):
		return Vec2Int(floor(self.x),floor(self.y))

	def get_angle(self) -> float:
		return atan2(self.y,self.x)



class Vec2Int:
	__slots__  = ('x','y')
	def __init__(self,x:int,y:int):
		self.x = x
		self.y = y
		
	@final
	@classmethod
	@property
	def zero(cls):
		return Vec2Int(0,0)
	

	def __eq__(self,__object: "Vec2Int"):
		return self.x == __object.x and self.y == __object.y
	
	def __add__(self,__object: "Vec2Int"):
		return Vec2Int(self.x + __object.x,self.y + __object.y)
	
	def __sub__(self,__object: "Vec2Int"):
		return Vec2Int(self.x - __object.x,self.y - __object.y)
	
	def __mul__(self,__object:int):
		return Vec2Int(self.x *__object,self.y * __object)
	
	def __floordiv__(self,__object: "Vec2Int"):
		return Vec2Int(self.x // __object.x, self.y // __object.y)
	
	def dot(self,__object: "Vec2Int"):
		return Vec2Int(self.x*__object.x,self.y*__object.y)
	
	def vector_mul(self,__object: "Vec2Int"):
		return Vec2Int(self.x*__object.x,self.y*__object.y)
	
	def __getitem__(self,__index:int) -> int:
		return (self.x,self.y)[__index]
	
	
	def __iadd__(self,__object: "Vec2Int"):
		self.x += __object.x
		self.y += __object.y
		return self

	def __isub__(self,__object: "Vec2Int"):
		self.x -= __object.x
		self.y -= __object.y
		return self

	def __imul__(self,__object:int):
		self.x *= __object
		self.y *= __object
		return self

	def __str__(self) -> str:
		return f"Vec2Int(x:{self.x}, y:{self.y})"	
	
	def __neg__(self):
		return Vec2Int(-self.x,-self.y)
	
	
	def __matmul__(self,__object: "Vec2Int"):
		return Vec2Int(self.x * __object.x,self.y * __object.y)

	@property
	def isZero(self) -> bool:
		return self.x == self.y == 0
	
	def magnitude_squared(self):
		return self.x*self.x+self.y*self.y
	
	def magnitude(self):
		return sqrt(self.magnitude_squared())
	
	def reset(self):
		'''Reset each axis to 0'''
		self.x = 0
		self.y = 0

	def __bool__(self):
		return (self.x or self.y).__bool__()
	
	def __iter__(self):
		yield self.x
		yield self.y
	
	def set_to(self,__object: "Vec2Int"):
		self.x = __object.x
		self.y = __object.y

	@property
	def tuple(self):
		return (self.x,self.y)

	def copy(self):
		return Vec2Int(self.x,self.y)
	
	def rotate(self,theta:float|int):
		cs = cos(theta)
		sn = sin(theta)
		px = self.x * cs - self.y * sn
		py = self.x * sn + self.y * cs
		self.x = round(px)
		self.y = round(py)

	def get_angle(self) -> float|int:
		return atan2(self.y,self.x)
