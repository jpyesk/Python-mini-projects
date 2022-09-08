class Song:
    def __init__(self, title, releaseYear, duration=60, likes=0):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes

    def getTitle(self):
        return self.__title

    def getLikes(self):
        return self.__likes

    def getDuration(self):
        return self.__duration

    def getReleaseYear(self):
        return self.__releaseYear

    def like(self):
        self.__likes += 1

    def dislike(self):
        self.__likes -= 1

    def setDuration(self, x):
        if self.__likes == x or x < 0 or x > 720:
            return False
        else:
            self.__duration = x
            return True

    def __str__(self):
        return f"Title:{self.getTitle()},Duration:{int(self.getDuration() )/ 60} minutes,Release year:{self.getReleaseYear()},Likes:{self.getLikes()}"

    def __eq__(self, other):
        c=self.__releaseYear
        return (self.__title==other.getTitle())and (self.__duration==other.getDuration())and (c==other.getReleaseYear())


