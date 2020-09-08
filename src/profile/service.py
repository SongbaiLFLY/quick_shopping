from profile.exceptions import ProfileAlreadyExist, ProfileNotFound
from profile.models.profile import Profile
from account.models.account import Account
from profile.models.serializers import (CreateProfileSerializer,
                                        ProfileSerializer,
                                        UpdateProfileSerializer,
                                        UserIdSerializer)

from libs.sanic_api.views import GetView, PostView, PutView, ListView


class CreateProfileService(PostView):
    """创建用户资料
    """
    args_deserializer_class = CreateProfileSerializer
    post_serializer_class = ProfileSerializer

    async def save(self):
        user_id = self.validated_data['user_id']
        account = await Account.async_get(user_id=user_id)
        await account.async_update(role_id=self.validated_data['role_id'])
        try:
            await Profile.async_get(user_id=user_id)
        except Profile.DoesNotExist:
            return await Profile.new(user_id=user_id,
                                     nickname=self.validated_data['nickname'],
                                     gender=self.validated_data['gender'],
                                     role_id=self.validated_data['role_id'])

        raise ProfileAlreadyExist


class GetProfileByIdService(GetView):
    """通过用户ID查找用户资料
    """
    args_deserializer_class = UserIdSerializer
    get_serializer_class = ProfileSerializer

    async def get_object(self):
        try:
            profile = await Profile.async_get(
                user_id=self.validated_data['user_id'])
        except Profile.DoesNotExist:
            raise ProfileNotFound

        return profile


class UpdateProfileService(PutView):
    """更新用户 profile"""
    args_deserializer_class = UpdateProfileSerializer
    put_serializer_class = ProfileSerializer

    async def save(self):
        try:
            profile = await Profile.async_get(
                user_id=self.validated_data['user_id'])
        except Profile.DoesNotExist:
            raise ProfileNotFound

        await profile.update_profile(**self.validated_data)

        return profile


class GetAllManagerService(ListView):
    args_deserializer_class = None
    list_serializer_class = ProfileSerializer
    list_result_name = 'managers'

    async def filter_objects(self):
        managers = await Profile.objects.filter(role_id='MANAGER').async_all()
        return managers
