from datetime import datetime

from cassdran.cqlenigne import columns

from app import app
from libs.aiocqlengine import AioModel


class Profile(AioModel):
    __table_name__ = 'profile'

    user_id = columns.UUID(primary_key=True)
    nickname = columns.Text(custom_index=True)
    role_id = columns.Text(default=app.config.ROLE_USER, custom_index=True)

    created_at = columns.DateTime(default=datetime.utcnow)
    updated_at = columns.DateTime(default=datetime.utcnow)

    @classmethod
    async def new(cls, user_id, nickname, role_id):
        return await Profile.async_create(user_id=user_id,
                                          nickname=nickname,
                                          role_id=role_id)

    async def update_profile(self, **profiles):
        profiles['updated_at'] = datetime.utcnow()
        new_profile = await self.async_update(**profiles)
        return new_profile
