from song import Song
class Album:
      def __init__(self,title,releaseYear):
             self.__title=title
             self.__releaseYear=releaseYear
             self.__songs =[]
      def getTitle(self):
          return  self.__title

      def getReleaseYear(self):
          return  self.__releaseYear

      def getSongs(self):
          return self.__songs

      def addSongs(self,*songs):
          cnt=0
          temp=True
          for i in songs:
              for g in self.__songs:
                 if i.__eq__(g):
                     temp=False

              if temp :
                cnt+=1
                self.__songs.append(i)
              temp=True

          return cnt


      def sortBy(self,byKey,reverse):
          return self.__songs.sort(byKey,reverse)

      def sortByName(self, reverse):

              return self.sortBy(lambda x: x.getTitle(), reverse=reverse)

      def sortByPopularity(self, reverse):

              return self.sortBy(lambda x: x.getLikes(), reverse=reverse)

      def sortByDuration(self, reverse):

              return self.sortBy(lambda x: x.getDuration(), reverse=reverse)

      def sortByReleaseYear(self, reverse):

              return self.sortBy(lambda x: x.getReleaseYear(), reverse=reverse)

      def likeperalalbom(self):
          temp=0
          for i in self.__songs:
              temp+=i.getLikes()
          return temp

      def __str__(self):
          songs = " "
          for song in self.__songs:
              songs += song.__str__() + "|"
              songs = songs[:len(songs) - 1]
          return f'Title:{self.__title},Release Year:{self.__releaseYear},Songs:{songs}'


