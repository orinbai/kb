# coding = utf8
# Author: oRin

from flask import Flask
from .dashboard import dashbd

app = Flask(__name__)

# 为dashboard添加蓝图
app.register_blueprint(dashbd, url_prefix='/dashboard')