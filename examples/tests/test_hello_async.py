import pytest

@pytest.mark.asyncio
async def test_hello_world():
    assert await hello_world() == "Hello, World!"

async def hello_world():
    return "Hello, World!"