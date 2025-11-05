import aiofiles
import aiohttp
import asyncio

async def async_http_download(src_url, dest_file, chunk_size=65536):
    async with aiofiles.open(dest_file, 'wb') as fd:
        async with aiohttp.ClientSession() as session:
            async with session.get(src_url) as resp:
                async for chunk in resp.content.iter_chunked(chunk_size):
                    await fd.write(chunk)

SRC_URL = "/path/to/url"
DEST_FILE = "/path/to/file/on/local/machine"

asyncio.run(async_http_download(SRC_URL, DEST_FILE))
