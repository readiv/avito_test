import aiohttp
import asyncio


def matrix_text2int(matrix_text:str):
    """ На входе строка с матрицей. На выходе двумерный массив с int """
    matrix_text = matrix_text.split("\n")
    matrix_int = []

    for line in matrix_text:
        if len(line) == 0 or line[0] != "|": # Пропускаем все пустые и все не начинающиеся с |
            continue
        matrix_line = line[1:-1].split("|")
        matrix_int.append([int(item) for item in matrix_line]) # Преобразование строк к int и добавляем к результату 

    return matrix_int
    

async def get_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            matrix_text = await response.text()
    matrix_int = matrix_text2int(matrix_text)
    return matrix_int


if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    coroutines = [get_matrix("https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt")]
                #   get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix4.txt"),
                #   get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix5.txt"),
                #   get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix32.txt")]

    list_matrix = loop.run_until_complete(asyncio.gather(*coroutines))
    for matrix in list_matrix:
        for line in matrix:
            print(line)
            pass
