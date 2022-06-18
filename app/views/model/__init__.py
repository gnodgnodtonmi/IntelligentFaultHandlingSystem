from flask import Blueprint
from paddlenlp import Taskflow
from sentence_transformers import SentenceTransformer

model_bp = Blueprint("model", __name__, url_prefix='/model')
uie_model = Taskflow('information_extraction', schema={'故障触发词': ['部位', '形容词']})
sbert_model = SentenceTransformer("uer/sbert-base-chinese-nli")

from . import model_view
