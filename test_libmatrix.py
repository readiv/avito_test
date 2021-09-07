import asyncio
import unittest

from aiohttp.web_exceptions import HTTPClientError
from aioresponses import aioresponses

import libmatrix


class TestLibmatrix(unittest.TestCase):

    def test_404(self):
        loop = asyncio.get_event_loop()
        with aioresponses() as session:
            session.get('https://hello.aio', status=404)
            self.assertEqual(loop.run_until_complete(libmatrix.get_matrix("https://hello.aio")), [])

    def test_500(self):
        loop = asyncio.get_event_loop()
        with aioresponses() as session:
            session.get('https://hello.aio', status=500)
            self.assertEqual(loop.run_until_complete(libmatrix.get_matrix("https://hello.aio")), [])

    def test_exception(self):
        loop = asyncio.get_event_loop()
        with aioresponses() as session:
            session.get('https://hello.aio', exception=HTTPClientError())
            self.assertEqual(loop.run_until_complete(libmatrix.get_matrix("https://hello.aio")), [])

    def test_matrix1(self):
        loop = asyncio.get_event_loop()
        SOURCE_URL = "https://raw.githubusercontent.com/readiv/ls1/master/matrix1.txt"
        TRAVERSAL = [1]
        self.assertEqual(loop.run_until_complete(libmatrix.get_matrix(SOURCE_URL)), TRAVERSAL)

    def test_matrix2(self):
        loop = asyncio.get_event_loop()
        SOURCE_URL = "https://raw.githubusercontent.com/readiv/ls1/master/matrix2.txt"
        TRAVERSAL = [1, 2, 3, 4]
        self.assertEqual(loop.run_until_complete(libmatrix.get_matrix(SOURCE_URL)), TRAVERSAL)

    def test_matrix3(self):
        loop = asyncio.get_event_loop()
        SOURCE_URL = "https://raw.githubusercontent.com/readiv/ls1/master/matrix3.txt"
        TRAVERSAL = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(loop.run_until_complete(libmatrix.get_matrix(SOURCE_URL)), TRAVERSAL)

    def test_matrix4(self):
        loop = asyncio.get_event_loop()
        SOURCE_URL = "https://raw.githubusercontent.com/readiv/ls1/master/matrix4.txt"
        TRAVERSAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(loop.run_until_complete(libmatrix.get_matrix(SOURCE_URL)), TRAVERSAL)

    def test_matrix5(self):
        loop = asyncio.get_event_loop()
        SOURCE_URL = "https://raw.githubusercontent.com/readiv/ls1/master/matrix5.txt"
        TRAVERSAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.assertEqual(loop.run_until_complete(libmatrix.get_matrix(SOURCE_URL)), TRAVERSAL)

    def test_matrix_avito(self):
        loop = asyncio.get_event_loop()
        SOURCE_URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
        TRAVERSAL = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
        self.assertEqual(loop.run_until_complete(libmatrix.get_matrix(SOURCE_URL)), TRAVERSAL)

    def test_matrix32(self):
        loop = asyncio.get_event_loop()
        SOURCE_URL = "https://raw.githubusercontent.com/readiv/ls1/master/matrix32.txt"
        TRAVERSAL = [10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 90,
                     130, 10, 50, 90, 130, 10, 50, 90, 130, 140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160, 130,
                     140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160, 120,
                     80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40,
                     160, 120, 80, 40, 160, 120, 80, 40, 30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 10, 40,
                     30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100,
                     140, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100, 110, 120,
                     90, 100, 110, 120, 90, 100, 110, 120, 90, 100, 110, 120, 90, 100, 110, 120, 90, 100, 110, 120, 90,
                     100, 110, 120, 90, 100, 110, 70, 30, 150, 110, 70, 30, 150, 110, 70, 30, 150, 110, 70, 30, 150, 110,
                     70, 30, 150, 110, 70, 30, 150, 110, 70, 30, 150, 110, 70, 60, 50, 80, 70, 60, 50, 80, 70, 60, 50,
                     80, 70, 60, 50, 80, 70, 60, 50, 80, 70, 60, 50, 80, 70, 60, 50, 80, 70, 110, 150, 30, 70, 110, 150,
                     30, 70, 110, 150, 30, 70, 110, 150, 30, 70, 110, 150, 30, 70, 110, 150, 30, 70, 110, 150, 30, 70, 80,
                     50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, 50,
                     60, 20, 140, 100, 60, 20, 140, 100, 60, 20, 140, 100, 60, 20, 140, 100, 60, 20, 140, 100, 60, 20,
                     140, 100, 60, 20, 140, 100, 90, 120, 110, 100, 90, 120, 110, 100, 90, 120, 110, 100, 90, 120, 110,
                     100, 90, 120, 110, 100, 90, 120, 110, 100, 90, 120, 160, 40, 80, 120, 160, 40, 80, 120, 160, 40, 80, 120,
                     160, 40, 80, 120, 160, 40, 80, 120, 160, 40, 80, 120, 160, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20,
                     30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 130, 90, 50, 10, 130, 90, 50, 10, 130, 90,
                     50, 10, 130, 90, 50, 10, 130, 90, 50, 10, 130, 90, 50, 10, 130, 160, 150, 140, 130, 160, 150, 140, 130,
                     160, 150, 140, 130, 160, 150, 140, 130, 160, 150, 140, 130, 160, 150, 140, 130, 10, 50, 90, 130, 10,
                     50, 90, 130, 10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 90, 130, 140, 150, 160, 130,
                     140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160, 120,
                     80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 30,
                     20, 10, 40, 30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 60, 100, 140, 20,
                     60, 100, 140, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100, 110, 120, 90, 100,
                     110, 120, 90, 100, 110, 120, 90, 100, 110, 120, 90, 100, 110, 120, 90, 100, 110, 70, 30, 150, 110, 70,
                     30, 150, 110, 70, 30, 150, 110, 70, 30, 150, 110, 70, 30, 150, 110, 70, 60, 50, 80, 70, 60, 50, 80, 70,
                     60, 50, 80, 70, 60, 50, 80, 70, 60, 50, 80, 70, 110, 150, 30, 70, 110, 150, 30, 70, 110, 150, 30, 70,
                     110, 150, 30, 70, 110, 150, 30, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70,
                     80, 50, 60, 20, 140, 100, 60, 20, 140, 100, 60, 20, 140, 100, 60, 20, 140, 100, 60, 20, 140, 100, 90,
                     120, 110, 100, 90, 120, 110, 100, 90, 120, 110, 100, 90, 120, 110, 100, 90, 120, 160, 40, 80, 120,
                     160, 40, 80, 120, 160, 40, 80, 120, 160, 40, 80, 120, 160, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20,
                     30, 40, 10, 20, 30, 40, 10, 130, 90, 50, 10, 130, 90, 50, 10, 130, 90, 50, 10, 130, 90, 50, 10, 130,
                     160, 150, 140, 130, 160, 150, 140, 130, 160, 150, 140, 130, 160, 150, 140, 130, 10, 50, 90, 130, 10,
                     50, 90, 130, 10, 50, 90, 130, 10, 50, 90, 130, 140, 150, 160, 130, 140, 150, 160, 130, 140, 150, 160,
                     130, 140, 150, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 160, 120, 80, 40, 30, 20, 10, 40,
                     30, 20, 10, 40, 30, 20, 10, 40, 30, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100, 140, 20, 60, 100,
                     110, 120, 90, 100, 110, 120, 90, 100, 110, 120, 90, 100, 110, 70, 30, 150, 110, 70, 30, 150, 110, 70,
                     30, 150, 110, 70, 60, 50, 80, 70, 60, 50, 80, 70, 60, 50, 80, 70, 110, 150, 30, 70, 110, 150, 30, 70,
                     110, 150, 30, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 20, 140, 100, 60, 20, 140, 100, 60, 20,
                     140, 100, 90, 120, 110, 100, 90, 120, 110, 100, 90, 120, 160, 40, 80, 120, 160, 40, 80, 120, 160, 40,
                     10, 20, 30, 40, 10, 20, 30, 40, 10, 130, 90, 50, 10, 130, 90, 50, 10, 130, 160, 150, 140, 130, 160,
                     150, 140, 130, 10, 50, 90, 130, 10, 50, 90, 130, 140, 150, 160, 130, 140, 150, 160, 120, 80, 40, 160,
                     120, 80, 40, 30, 20, 10, 40, 30, 20, 60, 100, 140, 20, 60, 100, 110, 120, 90, 100, 110, 70, 30, 150,
                     110, 70, 60, 50, 80, 70, 110, 150, 30, 70, 80, 50, 60, 20, 140, 100, 90, 120, 160, 40, 10, 130]
        self.assertEqual(loop.run_until_complete(libmatrix.get_matrix(SOURCE_URL)), TRAVERSAL)


if __name__ == '__main__':
    unittest.main()
