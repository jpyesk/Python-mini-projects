from song import Song
from album import Album
class Artist:
    def __init__(self,firstName,lastName,birthYear,albums,singles):
        self.__firstName=firstName
        self.__lastName=lastName
        self.__birthYear=birthYear
        self.__albums=albums
        self.__singles=singles

    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return  self.__lastName

    def getBirthYear(self):
        return self.__birthYear

    def getAlbums(self):
        return self.__albums

    def getSingle(self):
        return  self.__singles

    def mostLikedSong(self):
        temp=0
        music=None
        for i in self.__singles:
            if temp<i.getLikes():
                temp=i.getLikes()
                music=i
        for i in self.__albums:
            for g in i.getSongs():
                if temp<g.getLikes():
                    temp=g.getLikes()
                    music=g
        return music


    def leastLikedSong(self):
        temp=0
        music=0
        for i in self.__singles:
            if temp>i.getLikes() or temp==0:
                temp=i.getLikes()
                music=i
        for i in self.__albums:
            for g in i.getSongs():
                if temp>g.getLikes() or temp==0:
                    temp=g.getLikes()
                    music=g
        return music

    def totalLikes(self):
        output=0
        for i in self.__singles:
            output+=int(i.getLikes())
        for i in self.__albums:
            for g in i.getSongs():
                output+=int(g.getLikes())
        return output


    def __str__(self):
        return f'Name: {self.getFirstName()} {self.getSecondName()},Birth year:{self.getBirthYear()},Total likes:{self.totalLikes()}'
    def  eq(self, other):
        return self.__firstName==other.getFirstName() and self.__lastName==other.getSecondName() and self.__birthYear==other.getBirthYear()

