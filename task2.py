import asyncio

async def download_file(task_name: str, total_time: int):
    print(f"Starting {task_name} which will take {total_time} seconds...")
    
    remaining_time = total_time
    while remaining_time > 0:
        print(f"{task_name} is running. Time remaining: {remaining_time} seconds.")
        await asyncio.sleep(1)
        remaining_time -= 1

    print(f"{task_name} completed!")

async def main():
    tasks = [
        download_file('Task A', 6),
        download_file('Task B', 4),
        download_file('Task C', 8),
    ]
    
    await asyncio.gather(*tasks)
asyncio.run(main())
