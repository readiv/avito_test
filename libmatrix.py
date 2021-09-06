import aiohttp
import asyncio

dx_dy = [[0,1],[1,0],[0,-1],[-1,0]] # 4 направления обхода матрицы


def matrix2list_recursive(matrix_int, level):
    if level == 0: #Конечные условия выхода при четном размере матрицы. 
        return []
    x = y = (len(matrix_int) - level) // 2 #Начальные координаты
    interim_list = [matrix_int[y][x]]
    if level == 1: #Конечные условия выхода при нечетном размере матрицы. 
        return interim_list
    #Начинаем обход матрицы
    for n in range(4): #Четыре стороны
        for i in range(level - 1): #число шагов
            if ( n == 3 ) and (i == level - 2): #Последний обход на один шаг меньше
                break 
            x = x + dx_dy[n][0]
            y = y + dx_dy[n][1]
            interim_list.append(matrix_int[y][x])
    return interim_list + matrix2list_recursive(matrix_int, level-2)
    

def matrix_str2int(matrix_text:str):
    """ На входе строка с матрицей. На выходе двумерный массив с int """
    matrix_text = matrix_text.split("\n")
    matrix_int = []

    for line in matrix_text:
        if len(line) == 0 or line[0] != "|": # Пропускаем все пустые и все не начинающиеся с |
            continue
        matrix_line = line[1:-1].split("|")
        matrix_int.append([int(item) for item in matrix_line]) # Преобразование строк к int и добавляем к результату 
    return matrix2list_recursive(matrix_int, len(matrix_int))
    

async def get_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            matrix_text = await response.text()
    matrix_int = matrix_str2int(matrix_text)
    return matrix_int


if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    coroutines = [get_matrix("https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"),
                  get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix4.txt"),
                  get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix5.txt"),
                  get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix32.txt")]

    list_matrix = loop.run_until_complete(asyncio.gather(*coroutines))
    for matrix in list_matrix:
        print(matrix)
        pass
