from tests.account.test_account_service import AccountService
from tests.docs import api_docs

from app import app


class TestProductApi:
    async def _create_product(self, client, authorization, name, price, description):
        # 创建一个产品
        response = await client.post(
            '/v1/product',
            json={
                'manager_id': authorization['user_id'],
                'name': name,
                'price': price,
                'description': description
            },
            headers={'Authorization': authorization['token']})
        assert response.status == 200
        json_result = await response.json()
        assert json_result['ok']

        return json_result

    @api_docs(title='创建一个产品',
              path='/v1/product',
              method='POST',
              body={
                  'manager_id（必填）': 'manager_ID',
                  'name（必填）': '产品名',
                  'price': '价格',
                  'description': '产品介绍'
              },
              headers={'Authorization': '用户 Token'})
    async def test_create_product(self, client):
        url = '/v1/product'
        authorization = await AccountService.get_token(client,
                                                       app.config.ROLE_MANAGER)
        price = 1.1
        response = await client.post(
            url,
            json={
                'manager_id': authorization['user_id'],
                'name': '产品1',
                'price': price,
                'description': '产品1的介绍'
            },
            headers={'Authorization': authorization['token']})
        assert response.status == 200
        json_result = await response.json()
        price1 = format(json_result['result']['price'], '.1f')
        assert price1 == str(price)
        assert json_result['ok']

        return {'正确响应': json_result}

    @api_docs(title='查询产品',
              path='/v1/product/manager/{manager_id}',
              method='GET',
              headers={'Authorization': '用户 Token'})
    async def test_list_products(self, client):
        authorization = await AccountService.get_token(client,
                                                       app.config.ROLE_MANAGER)
        price = 1.1
        # 创建3个产品
        await self._create_product(client, authorization, '1', price, '1')
        await self._create_product(client, authorization, '2', price, '2')
        await self._create_product(client, authorization, '3', price, '3')

        # 另一个管理员
        authorization2 = await AccountService.get_token(
            client, app.config.ROLE_MANAGER)
        await self._create_product(client, authorization2, '4', price, '4')

        # 按管理员ID查询
        manager1_id = authorization['user_id']
        response1 = await client.get(
            f'/v1/product/manager/{manager1_id}',
            headers={'Authorization': authorization['token']})
        assert response1.status == 200
        json_result1 = await response1.json()
        assert json_result1['ok']

        products = json_result1['result']['products']
        assert products[0]['manager_id'] == manager1_id
        price1 = format(products[0]['price'], '.1f')
        assert price1 == str(price)
        assert len(products) == 3

        manager2_id = authorization2['user_id']
        response2 = await client.get(
            f'/v1/product/manager/{manager2_id}',
            headers={'Authorization': authorization2['token']})
        json_result2 = await response2.json()
        products = json_result2['result']['products']
        assert products[0]['manager_id'] == manager2_id
        price1 = format(products[0]['price'], '.1f')
        assert price1 == str(price)
        assert len(products) == 1

        return {'正确响应': json_result2}
