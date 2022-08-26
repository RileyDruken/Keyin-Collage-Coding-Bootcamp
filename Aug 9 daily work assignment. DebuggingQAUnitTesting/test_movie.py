import unittest

from movie import movie
name = 'Test_user'
class movietest(unittest.TestCase):
    def test_age1(self):
        for var in range(18,60):
            self.assertAlmostEqual(movie(var), "Hello Test_User, you are allowed to view any movie unrestricted. The cost of admission is $10.00")

    def test_age2(self):
        for var in range(1, 12):
            self.assertAlmostEqual(movie(var),"Hello Test_User, you are allowed to view G rated movies. The cost of admission is $5.00")

    def test_age4(self):
        for var in range(13, 17):
            self.assertAlmostEqual(movie(var),"Hello Test_User, you are allowed to view PG-13 or G rated movies. The cost of admission is $15.00")

    def test_age3(self):
        for var in range(60, 500):
            self.assertAlmostEqual(movie(var),"Hello Test_User, you are allowed to view any movie unrestricted. The cost of admission is $3.50 with your senior's discount!")


