import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball_number in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f'Силач {name} поднял {ball_number} шар.')
    print(f'Силач {name} закончил соревнование.')


async def start_tournament():
    await asyncio.gather(
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    )


asyncio.run(start_tournament())
