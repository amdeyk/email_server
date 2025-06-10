import asyncio
from collections import defaultdict
from typing import Dict

class RateLimiter:
    def __init__(self, rate: int = 60):
        self.rate = rate
        self.calls: Dict[str, int] = defaultdict(int)
        self.lock = asyncio.Lock()

    async def allow(self, key: str) -> bool:
        async with self.lock:
            if self.calls[key] >= self.rate:
                return False
            self.calls[key] += 1
            return True

    async def reset(self) -> None:
        async with self.lock:
            self.calls.clear()
