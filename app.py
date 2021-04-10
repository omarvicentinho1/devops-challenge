import os
import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.ProductProvider import ProductProvider

from injector import Binder

def configure(binder: Binder) -> Binder:
    binder.bind(
        ProductProvider
    )


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs
    app.add_api('product-service-docs.yml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=int(os.environ.get('PORT', 8080))) # os.environ is handy if you intend to launch on heroku