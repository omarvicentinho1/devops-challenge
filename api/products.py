from flask_injector import inject
from providers.ProductProvider import ProductProvider


@inject(data_provider=ProductProvider)
def create_product(data_provider, productPayload) -> str:
    return data_provider.create_product(productPayload)

@inject(data_provider=ProductProvider)
def read_product(data_provider, prodId) -> str:
    return data_provider.read_product(prodId)