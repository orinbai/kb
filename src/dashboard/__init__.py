from flask import Blueprint

dashbd = Blueprint(
    'dashboard',
    __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

from . import views