from aiohttp import web

from app.db import init_pg, close_pg
from app.settings import config, BASE_DIR
from app.routes import setup_routes
import aiohttp_jinja2
import jinja2


async def init_app():
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app,
        loader=jinja2.FileSystemLoader(str(BASE_DIR / 'app' / 'templates')))
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_routes(app)
    return app


if __name__ == '__main__':
    app = init_app()
    web.run_app(app, port=9001)
