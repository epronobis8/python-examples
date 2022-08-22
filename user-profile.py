def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
#we pass a key value pair for additional information, but the users first and last name is required.
user_profile = build_profile('abert', 'einstein', location='princeton', field='physics')
print(user_profile)