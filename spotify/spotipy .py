from artist import  Artist
from album import  Album
from song import Song

class SpotiPy:
    def __init__(self):
        self.__artists=[]

    def getArtists(self):
        return  self.__artists


    def addArtists(self,*art):
        temp=True
        for i in art:
            for g in self.__artists:
                if (i).eq(g):
                    temp=False
            if temp:
               self.__artists.append(i)
            temp=True

    def getTopTrendingArtist(self):
        temp=self.getArtists()[0]
        for i in self.__artists:
            if i.totalLikes()>temp.totalLikes():
                temp=i
        return (temp.getFirstName(),temp. getSecondName())

    def getTopTrendingAlbum(self):
        temp=0
        temp1=0
        for i in self.__artists:
            for g in i.getAlbums():
                if temp<g.likeperalalbom():
                    temp1=g
                    temp=g.likeperalalbom()
        return  temp1.getTitle()

    def getTopTrendingSong(self):
        temp=0
        temp1=None
        for i in self.__artists:
            if temp<i.mostLikedSong().getLikes():
                temp=i.mostLikedSong().getLikes()
                temp1=i.mostLikedSong()
        return temp1.getTitle()
    @staticmethod
    def loadFromFile(addres):
        f = open(addres, 'r')
        l = []
        index = 0
        lines = f.readlines()
        data = ''
        for i in lines:
            data += i.strip()
    # first split divide by artists
        artistlist=[]
        temp=[]
        lstArtist=data.split('#')

        #store all info in database
        database=[]
        listofobjectSongs=[]
        singlelistts=[]
        albumms=[]
        for i in lstArtist:
            fordatabase=[]
            ind=i.find('albums')
            sub=i[:ind]
            if sub.__contains__('artists:'):
               sub=sub[9:]
            personlst=sub.split(',')
            name=personlst[0]
            lastname=personlst[1]
            birtyear=personlst[2]
            fordatabase.append(name)
            fordatabase.append(lastname)
            fordatabase.append(birtyear)

            sub=i[i.find('albums:')+8:]
            indsingles=sub.find('singles:')
            singles=sub[indsingles+8:]
            sub=sub[:indsingles]
            album = sub.split('%')

            for i in album:
                #now we have list of albums+singles splitied
                #now lets simplify your list of singles in album
                k=i
                albumname=k[:k.find(',')]
                k=k[k.find(',')+1:]
                albumyear=k[:k.find(',')]
                k=k[k.find('songs:')+7:]
                albumsingles=[]
                albumsingles=(k.split('|'))


                listofobjectSongs=[]
                for i in albumsingles:
                    i = i.replace('}', '')
                    i=i.replace(']','')
                    temp=i.split(',')
                    singletitle=temp[0]
                    timeduration=int((eval((temp[1][:temp[1].find('minutes')-1])))*60)
                    releaseyear=temp[2]
                    likes=int(temp[3])
                    #and finally make objects
                    song=Song(singletitle,timeduration,releaseyear,likes)
                    listofobjectSongs.append(song)



                albumtemp=Album(albumname,albumyear)
                for i in listofobjectSongs:
                    albumtemp.addSongs(i)
                albumms.append(albumtemp)


                singles=singles.replace('{',"")
                singles=singles.replace('}','')
                singles=singles.replace(')',"")
                     # and make singles
                lstofsingle=singles.split('|')
                singlelistts=[]
                for i in lstofsingle:
                        temp=i.split(',')
                        temp[1]=int((eval((temp[1][:temp[1].find('minutes')-1])))*60)
                        songofsingle=Song(temp[0],temp[1],temp[2],int(temp[3]))
                        singlelistts.append(songofsingle)
            artist = (Artist(name, lastname, birtyear, albumms, singlelistts))

            artistlist.append(artist)

        temp=SpotiPy()
        for i in artistlist:
            temp.addArtists(i)
        return temp














       



























































