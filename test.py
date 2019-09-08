import requests
import time
import random
import asyncio

from asgiref.sync import sync_to_async, async_to_sync


def doit_sync(url, seconds=3):
    return requests.get(f'{url}/{seconds}').text


async def syncs_to_asyncs(sync_fn, *args):
    def to_args(sub_args):
        if isinstance(sub_args, list) or isinstance(sub_args, tuple):
            return sub_args
        else:
            return (sub_args,)
    async_fn = sync_to_async(sync_fn)
    completed_tasks, _ = await asyncio.wait([async_fn(*to_args(sub_args)) for sub_args in args])
    return [task.result() for task in completed_tasks]


async_calls = async_to_sync(syncs_to_asyncs)


def main():
    url = "http://127.0.0.1:5000"
    args = [(url, random.randint(1, 5)) for i in range(100)]

    start = time.time()
    result = async_calls(doit_sync, *args)
    print(time.time() - start)

    start = time.time()
    result = [doit_sync(url, seconds) for url, seconds in args]
    print(time.time() - start)


main()
