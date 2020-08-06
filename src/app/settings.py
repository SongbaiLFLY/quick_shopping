from profile import profile, profile_api_blueprint, profile_service_blueprint

# 蓝图（添加新的 app 需要到这里添加蓝图）
blueprints = [
    # profile
    profile_api_blueprint,
    profile_service_blueprint,
]

# models
models = [profile]
