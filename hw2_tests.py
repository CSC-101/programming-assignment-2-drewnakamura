import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        point1 = data.Point(2,2)
        point2 = data.Point(10,10)
        self.assertEqual(hw2.create_rectangle(point1, point2), data.Rectangle(data.Point(2,10), data.Point(10,2)))

    def test_create_rectangle_2(self):
        point1 = data.Point(2,2)
        point2 = data.Point(2,2)
        self.assertEqual(hw2.create_rectangle(point1, point2), data.Rectangle(data.Point(2,2), data.Point(2,2)))
    # Part 2
    def test_shorter_duration_than_1(self):
        duration1 = data.Duration(10, 10)
        duration2 = data.Duration(10, 30)
        song1 = data.Song("drew", "drew", duration1)
        song2 = data.Song("bob", "bob", duration2)
        self.assertEqual(hw2.shorter_duration_than(song1, song2), True)

    def test_shorter_duration_than_2(self):
        duration1 = data.Duration(10, 10)
        duration2 = data.Duration(10, 30)
        song1 = data.Song("drew", "drew", duration1)
        thing2 = data.Point(2,2)
        self.assertEqual(hw2.shorter_duration_than(song1, thing2), None)
    # Part 3

    def test_songs_shorter_than_1(self):
        duration1 = data.Duration(5, 5)
        duration2 = data.Duration(6, 6)
        duration3 = data.Duration(7,7)
        cut = data.Duration(7, 5)
        song1 = data.Song("a", "a", duration1)
        song2 = data.Song("b", "b", duration2)
        song3 = data.Song("c", "c", duration3)
        lista = [song1, song2, song3]
        self.assertEqual(hw2.songs_shorter_than(lista, cut), [song1, song2])

    def test_songs_shorter_than_2(self):
        point1 = data.Point(1, 1)
        duration2 = data.Duration(6, 6)
        duration3 = data.Duration(7,7)
        cut = data.Duration(7, 5)
        song2 = data.Song("b", "b", duration2)
        song3 = data.Song("c", "c", duration3)
        lista = [point1, song2, song3]
        self.assertEqual(hw2.songs_shorter_than(lista, cut), [song2])

    # Part 4

    def test_runningTime_1(self):
        duration1 = data.Duration(10, 10)
        duration2 = data.Duration(15, 15)
        duration3 = data.Duration(20, 20)
        song1 = data.Song("a", "a", duration1)
        song2 = data.Song("b", "b", duration2)
        song3 = data.Song("c", "c", duration3)
        lista = [song1, song2, song3]
        playList = [0, 1, 2]
        self.assertEqual(hw2.running_time(lista,playList), data.Duration(45, 45))

    def test_runningTime_2(self):
        duration1 = data.Duration(10, 10)
        duration2 = data.Duration(15, 15)
        duration3 = data.Duration(20, 20)
        song1 = data.Song("a", "a", duration1)
        song2 = data.Song("b", "b", duration2)
        song3 = data.Song("c", "c", duration3)
        lista = [song1, song2, song3]
        playList = [2, 2, 2]
        self.assertEqual(hw2.running_time(lista,playList), data.Duration(61, 0))
    # Part 5
    def test_validate_route_1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertEqual(hw2.validate_route(city_links, route), True)

    def test_validate_route_2(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo']
        self.assertEqual(hw2.validate_route(city_links, route), True)

    def test_validate_route_3(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'atascadero']
        self.assertEqual(hw2.validate_route(city_links, route), False)

    # Part 6
    def test_longest_repetition_1(self):
        lista = [1, 1, 1, 2, 2, 2, 2, 3, 3]
        self.assertEqual(hw2.longest_repetition(lista), [3])

    def test_longest_repetition_2(self):
        lista = []
        self.assertEqual(hw2.longest_repetition(lista), None)




if __name__ == '__main__':
    unittest.main()
