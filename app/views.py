import base64
import hashlib
from yarl import URL
from aiohttp import web
import aiohttp_jinja2
from app import db
import validators as v


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'placeholder': 'Put your url',
            'creation_url': False}


@aiohttp_jinja2.template('index.html')
async def create_url(request):
    url_hash_length = 6
    host = 'shortener'
    form = await request.post()
    original_url = form['url']
    if v.url(original_url):
        m = hashlib.md5()
        m.update(original_url.encode())
        key = base64.b64encode(m.digest()).decode()[:url_hash_length]
        async with request.app['db'].acquire() as conn:
            try:
                await conn.execute(db.url.insert().values({
                    'key': key, 'original_url': original_url}))
            except:
                pass
        short_url = URL.build(scheme='http', host=host, path='/' + key)
        return {'placeholder': short_url,
                'creation_url': True}
    else:
        return {'err_msg': 'invalid input',
                'creation_url': True,
                'placeholder': 'Put your url'}


async def redirect(request):
    key = request.match_info['key']
    async with request.app['db'].acquire() as conn:
        cur = await conn.execute(db.url.select().where(db.url.c.key == key))
        res = dict(await cur.fetchone())
        original_url = res['original_url']
        return web.HTTPFound(location=original_url)
