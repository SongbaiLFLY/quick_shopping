import uuid
from datetime import datetime


from cassandra.cqlengine import columns

from libs.aiocqlengine.models import AioModel


class Product(AioModel):

    __table_name__ = 'product'

    manager_id = columns.UUID(partition_key=True)
    product_id = columns.UUID(primary_key=True)
    name = columns.Text(index=True)
    price = columns.Float()
    description = columns.Text()

    created_at = columns.DateTime(default=datetime.utcnow())
    updated_at = columns.DateTime(default=datetime.utcnow())

    @classmethod
    async def new(cls, manager_id, name,price, description):
        return await Product.async_create(manager_id=manager_id,
                                          product_id=str(uuid.uuid4()),
                                          name=name,
                                          price=price,
                                          description=description)

    async def update_product(self, **new_product):
        new_product['updated_at'] = datetime.utcnow()
        return await self.async_update(**new_product)
