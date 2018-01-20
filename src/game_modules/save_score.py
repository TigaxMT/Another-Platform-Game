import os


class Save_Score:
    def __init__(self,score="0"):
        self.score = score

    def writeScore(self,score):

        self.readScore()

        self.score = int(self.score)
        score = int(score)

        if score > self.score:
            file = open("Score.txt","w")

            file.write(str(score))

            file.close()

    def readScore(self):

        if os.path.exists("Score.txt"):
            file = open("Score.txt","r")

            self.score = file.read()

            file.close()

        else:
            self.score = "0"
        
        return self.score