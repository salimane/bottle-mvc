# -*- coding: utf-8 -*-
__version__ = '0.1'
from bottle import Bottle, TEMPLATE_PATH
app = Bottle()
COOKIE_SECRET = 'random'
TEMPLATE_PATH.append("./project/views/")
TEMPLATE_PATH.remove("./views/")
from project.controllers import *


