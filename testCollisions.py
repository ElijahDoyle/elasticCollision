from Ball import Ball
from vector2 import Vector2

def dot_product(vec1,vec2):
    return  vec1.x * vec2.x + vec1.y * vec2.y

# detects when two objects touch
def collisionDetect(obj1,obj2):
    distance = ((obj1.position.x - obj2.position.x)**2 + (obj1.position.y - obj2.position.y)**2)**(1/2)
    if distance < obj1.radius + obj2.radius:
        return True
    else:
        return False

# not really sure what this is but i need it as a controller of some sort
def elasticCollisions(objectList):
    for ball in objectList:
        b1 = ball
        for otherBall in objectList:
            if otherBall != ball:
                b2 = otherBall

                if collisionDetect(b1,b2):
                    collide(b1,b2)
                else:
                    pass

# the meat of this elastic collision project, it takes in two objects as arguments and runs them through elastic collision equations
def collide(obj1,obj2):
    p1 = obj1.position
    p2 = obj2.position
    m1  = obj1.mass
    m2 = obj2.mass
    v1 = obj1.velocity
    v2 = obj1.velocity
    totalMass = m1 + m2

#usually when my variables start with a d, it means they are the difference between two things

    dv1 = obj1.velocity.sub(obj2.velocity)  # the difference between obj1's velocity a