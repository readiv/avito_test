import aiohttp
import asyncio


async def get_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            matrix_text = await response.text()
    print(matrix_text,"\n")


if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    coroutines = [get_matrix("https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"),
                  get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix4.txt"),
                  get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix5.txt"),
                  get_matrix("https://raw.githubusercontent.com/readiv/avito_test/main/matrix32.txt")]

    loop.run_until_complete(asyncio.gather(*coroutines))
