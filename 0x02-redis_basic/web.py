#!/usr/bin/env python3
"""web.py"""

import requests
import redis
import time

def get_page(url: str) -> str:
    redis_client = redis.Redis()

    cached_content = redis_client.get(url)
    if cached_content:
        redis_client.incr(f"count:{url}")
        return cached_content.decode('utf-8')

    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        redis_client.setex(url, 10, content)
        redis_client.incr(f"count:{url}")
        return content
    else:
        return f"Error: Failed to fetch page. Status code: {response.status_code}"

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com"
    content = get_page(url)
    print(content)

