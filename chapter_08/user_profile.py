def build_profile(first, last, **user_info):
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

profile = build_profile('max', 'min', location='boston', mortheland='ukraine')

print(profile)
