import data

# Write your functions for each part in the space below.

# Part 1
"""
The purpose of this function is to create a rectangle object with two points.
point_a = point input
point_b = point input
left_x = smallest x
right_x = largest x
top_y = largest y
bottom_y = smalled y
def create_rectangle(point_a:data.Point, point_b:data.Point) -> data.Rectangle:
    return data.Rectangle(newPoint_a, newPoint_b)
create_rectangle(data.Point(2,2), data.Point(10,10)
should return data.Rectangle(data.Point(2,10), data.Point(10, 2))
"""
def create_rectangle(point_a:data.Point, point_b:data.Point)-> data.Rectangle:
    left_x = min(point_a.x, point_b.x)
    right_x = max(point_a.x, point_b.x)
    top_y = max(point_a.y, point_b.y)
    bottom_y = min(point_a.y, point_b.y)
    newPoint_a = data.Point(left_x, top_y)
    newPoint_b = data.Point(right_x, bottom_y)
    return data.Rectangle(newPoint_a,newPoint_b)

# Part 2
"""
The purpose of this function is to take a pair of either a song or a movie, and return if the first is shorter than the second.
thing1 = any object
thing2 = any object
def shorter_duration_than(thing1:any, thing2:any)->bool:
    return bool
    
duration1 = data.Duration(10, 10)
duration 2 = data.Duration(20,20)
song1 = data.Song("Drew", "Drew", duration1)
song2 = data.Song("Bob", "Bob", duration2)
shorter_duration_than(song1, song2)
Should return true
"""
def shorter_duration_than(thing1:any, thing2:any)->bool:
    if(type(thing1) == type(thing2)):
        if(thing1.duration.minutes * 60 + thing1.duration.seconds  < thing2.duration.minutes* 60 + thing2.duration.seconds):
            return True
        return False
    return None

# Part 3
"""
The purpose of this function is to take a list of songs and a maximum time, then return the list of songs with the duration less than the maximum duraiton
songs  = is a list of all the songs list that is of type song
list = list of songs 

def songs_shorter_than(list:list[data.Song], duration:data.Duration)->list[data.Song]:
    songs = [type songs]

    return list of songs

duration1 = data.Duration(10, 10)
duration 2 = data.Duration(20,20)
cut = data.Duration(15, 15)
song1 = data.Song("Drew", "Drew", duration1)
song2 = data.Song("Bob", "Bob", duration2)
list = [song1, song2]
songs_shorter_than(list, cut)
Should return [song1]
"""
def songs_shorter_than(list:list[any], duration:data.Duration)->list[data.Song]:
    songs = [song for song in list if type(song) == data.Song]

    return [song for song in songs if song.duration.minutes*60 + song.duration.seconds < duration.minutes*60 + duration.seconds]

# Part 4
"""
The purpose of this function is to find the total duration of a play list from a list of songs.
totalSeconds = int
lista = list of data.Song
playList = list of int

def running_time(lista:list[data.Song], playList:list[int]) -> data.Duration:
    totalSeconds = 0
    return data.Duration
    
duration1 = data.Duration(10, 10)
duration2 = data.Duration(15, 15)
duration3 = data.Duration(20, 20)
song1 = data.Song("a", "a", duration1)
song2 = data.Song("b", "b", duration2)
song3 = data.Song("c", "c", duration3)
lista = [song1, song2, song3]
playList = [0, 1, 2]
running_time(lista,playList)
Should return data.Duration(45, 45))
"""

def running_time(lista:list[data.Song], playList:list[int]) -> data.Duration:
    totalSeconds = 0
    for num in playList:
        totalSeconds += (lista[num]).duration.minutes * 60 + (lista[num]).duration.seconds
    return data.Duration(totalSeconds//60, totalSeconds%60)


# Part 5
"""
The purpose of this function is to take a list of strings and verify if the connections are possible through a list of lists of strings.

list_city = list[list[str]]
list_route = list[str]

def validate_route(list_city:list[list[str]], list_route:list[str])->bool:
return boolean

city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
               ]
route = ['san luis obispo', 'santa margarita', 'atascadero']
validate_route(city_links, route)
should return True
"""
def validate_route(list_city:list[list[str]], list_route:list[str])->bool:
    if(len(list_route) <=1):
        return True

    for num in range(len(list_route)-1):
        notFound = True
        if [list_route[num], list_route[num+1]] in list_city or [list_route[num+1], list_route[num]] in list_city:
            notFound = False
        if notFound == True:
            return False

    return True

# Part 6
"""
The purpose of this function is to find the start of the longest repition within a list of integers.

list = a list of int
longest = int
longest_idx = int

def longest_repetition(list:list[int]):
    return [longest_indx]
    

lista = [1, 1, 1, 2, 2, 2, 2, 3, 3]
longest_repetition(lista)
Should return 3

"""
def longest_repetition(list:list[int]):
    longest = 0
    longest_indx = 0
    for x in range(len(list)-1):
        attempt = 0
        for y in range(len(list) - x -1):
            if(list[x+y] == list[(x+y+1)]):
                attempt += 1
            else:
                break
        if(attempt > longest):
            longest = attempt
            longest_indx = x
    if longest == 0:
        return None
    return [longest_indx]
