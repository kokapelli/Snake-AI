from Block import Block
import numpy as np

class Snake:
    def __init__(self):
        # Spawn the head at x:13, y:13. Have it move up, one block at a time
        # (-1, 0) Move Up 
        # (1, 0) Move Down
        # (0, -1) Move Left
        # (0, 1) Move Right

        self.head = Block([13, 13], [0, -1], None, True)
        self.body = [self.head]
        self.size = 1
        self.createInitSnake()

    def __repr__(self):
        string = ""
        for i in self.body:
            if(not i.isHead):
                string += f"<-{i}"
            else:
                string += str(i)

        return string
    
    def createInitSnake(self, bodyLen=2):
        
        for _ in range(bodyLen):
            self.growSnake()

    def move(self):
        for b in self.body:
            b.move()

    def getHeadLoc(self):
        return self.head.getLoc()

    def getHeadTrajectory(self):
        return self.head.getTrajectory()

    def setHeadTrajectory(self, newTrajectory):
        self.head.setTrajectory(newTrajectory)
        self.head.setTrajectoryChange()

    def getBody(self):
        return self.body

    def getBodyLoc(self):
        bodyLoc = list()
        for b in self.body:
            bodyLoc.append(b.getLoc())

        return bodyLoc

    def getEndPiece(self, end):
        endCoord = end.getLoc()
        endTrajectory = np.array(end.getTrajectory()) # type change to negate array cleaner
        
        return endCoord, endTrajectory

    def growSnake(self):
        end = self.body[-1]
        endCoord, endTrajectory = self.getEndPiece(end)
        # Negate trajectory to place the new piece at the back of the snake
        bodyPartCoord = [x + y for x, y in zip(endCoord, np.negative(endTrajectory))]
        bodyPart = Block(bodyPartCoord, endTrajectory, end)
        self.body.append(bodyPart)
        self.size += 1

    def describeSnake(self):
        for b in self.body:
            print(f"Coord: {b.getLoc()}  Trajectory: {b.getTrajectory()}")