from django import template

register = template.Library()


def user_them(value):
    user_theme = value.profile.theme
    return user_theme


register.filter("user_them", user_them)
