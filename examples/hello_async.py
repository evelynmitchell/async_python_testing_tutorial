"""Async hello world example."""
import asyncio

async def main():
    """Print 'Hello ...' and '... World!' with a 1 second pause in between.`"""
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
