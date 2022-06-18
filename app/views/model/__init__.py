from flask import Blueprint
from paddlenlp import Taskflow

model_bp = Blueprint("model", __name__, url_prefix='/model')
ie = Taskflow('information_extraction', schema={'故障触发词': ['部位', '形容词']})

from . import model_view
