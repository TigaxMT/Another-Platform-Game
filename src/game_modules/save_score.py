import os


class Save_Score:
    def __init__(self,score=None):
        self.score = score

    def writeScore(self,score):

        old_score = self.readScore()

        old_score = int(old_score)
        score = int(score)

        if score > old_score:
            file = open("Score.txt","w")

            file.write(str(score))

            file.close()

    def readScore(self):

        if os.path.exists("Score.txt"):
            file = open("Score.txt","r")

            self.score = file.read()

            file.close()
        
        else:
            pass

        return self.score