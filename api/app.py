# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:54:17 2021
@author: kaiodeodato
"""

from flask import Flask
from views import views

app = Flask(__name__, static_folder='static')
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)


