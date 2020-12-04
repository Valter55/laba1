from enum import Enum, auto
 
 
class Monster(Enum):
    ZOMBIE = auto()
    WARRIOR = auto()
    BEAR = auto()
 
 
print(Monster.ZOMBIE) # Monster.ZOMBIE