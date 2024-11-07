from flask import Flask

"""
The webserver object
"""
app : Flask = Flask(__name__)
app.config['SECRET_KEY'] = ""


"""
Homepage Endpoint
"""
from .views.index import index
app.register_blueprint(index)

"""
LLM Endpoint
"""
from .views.ai_model import ai_model
app.register_blueprint(ai_model, url_prefix="/ai_model")
