from libmatrix import get_matrix
import asyncio

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]

loop = asyncio.get_event_loop()
def test_get_matrix():
    assert loop.run_until_complete(get_matrix(SOURCE_URL)) == TRAVERSAL

if __name__ == '__main__':
    test_get_matrix()

    coroutines = [get_matrix("https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix1.txt")]
                #   get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix3.txt"),
                #   get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix5.txt"),
                #   get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix32.txt")]

    list_matrix = loop.run_until_complete(asyncio.gather(*coroutines))
    for matrix in list_matrix:
        print(matrix)
        pass