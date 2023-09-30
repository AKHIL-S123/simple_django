from django import template

register = template.Library()

@register.filter(name='has_permission')
def has_permission(user, permission):
    return user.has_perm(permission)

@register.filter(name='has_any_permission')
def has_any_permission(user, permissions):
    permissions_list = permissions.split(',')
    for permission in permissions_list:
        if user.has_perm(permission.strip()):
            return True
    return False