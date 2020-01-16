from app.views import index, create_url, redirect
from app.settings import BASE_DIR


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/', create_url)
    app.router.add_get('/{key}', redirect)
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=BASE_DIR / 'app' / 'static',
                          name='static')
