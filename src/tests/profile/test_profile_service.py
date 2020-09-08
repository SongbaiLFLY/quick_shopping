

class ProfileService:
    @classmethod
    async def create_profile(cls, client, user_id, nickname, role_id):
        url = '/service/v1/profile'

        await client.post(url,
                          json={
                              'user_id': user_id,
                              'nickname': nickname,
                              'role_id': role_id
                          })


class TestProfileService:
    async def test_get_profile(self, client):
        account_id = '123456789@qq.com'
        # 获取验证码
        response = await client.post('/service/v1/account/send_code',
                                     json={'account_id': account_id})
        assert response.status == 200
        json_result = await response.json()
        validate_token = json_result['result']['validate_token']
        validate_code = json_result['result']['validate_code']

        url = '/v1/account'
        response = await client.post(url,
                                     json={
                                         'account_id': account_id,
                                         'password': '123456789@qq.com',
                                         'validate_token': validate_token,
                                         'validate_code': validate_code,
                                     })
        assert response.status == 200
        response = await client.post('/v1/login',
                                     json={
                                         'account_id': '123456789@qq.com',
                                         'password': '123456789@qq.com'
                                     })
        assert response.status == 200
        json_result = await response.json()
        user_id = json_result['result']['user_id']
        # 创建
        url = '/v1/profile'
        response = await client.post(url,
                                     json={
                                         'user_id': user_id,
                                         'nickname': 'tester',
                                         'gender': 1,
                                         'role_id': 'MANAGER'
                                     })

        assert response.status == 200
        assert json_result['ok']
        response = await client.get(f'/service/v1/profile/{user_id}')
        assert response.status == 200

        json_result = await response.json()
        assert json_result['ok']

        profile = json_result['result']
        assert profile['user_id'] == user_id
        assert profile['nickname'] == 'tester'

    async def test_update_profile(self, client):
        account_id = '123456789@qq.com'
        # 获取验证码
        response = await client.post('/service/v1/account/send_code',
                                     json={'account_id': account_id})
        assert response.status == 200
        json_result = await response.json()
        validate_token = json_result['result']['validate_token']
        validate_code = json_result['result']['validate_code']

        url = '/v1/account'
        response = await client.post(url,
                                     json={
                                         'account_id': account_id,
                                         'password': '123456789@qq.com',
                                         'validate_token': validate_token,
                                         'validate_code': validate_code,
                                     })
        assert response.status == 200
        response = await client.post('/v1/login',
                                     json={
                                         'account_id': '123456789@qq.com',
                                         'password': '123456789@qq.com'
                                     })
        assert response.status == 200
        json_result = await response.json()
        user_id = json_result['result']['user_id']
        # 创建
        url = '/v1/profile'
        response = await client.post(url,
                                     json={
                                         'user_id': user_id,
                                         'nickname': 'tester',
                                         'gender': 1,
                                         'role_id': 'MANAGER'
                                     })

        assert response.status == 200
        assert json_result['ok']
        # 查询
        response = await client.get(f'/service/v1/profile/{user_id}')
        assert response.status == 200
        json_result = await response.json()

        profile = json_result['result']
        assert profile['nickname'] == 'tester'

        # 更新 profile
        await client.put(f'/service/v1/profile/{user_id}',
                         json={
                             'nickname': 'tester2',
                         })

        # 再次查询
        response2 = await client.get(f'/service/v1/profile/{user_id}')
        assert response2.status == 200
        json_result2 = await response2.json()

        new_profile = json_result2['result']
        assert new_profile['nickname'] == 'tester2'
