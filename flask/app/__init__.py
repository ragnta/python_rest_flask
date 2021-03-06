from flask import Flask
from .dao import InMemoryDaoImpl, DataModel
import datetime
from .controllers import Admin

app = Flask(__name__, static_url_path='', static_folder='../client')
elements = [ DataModel(1, "TRE", datetime.date(2019, 4, 13)), DataModel(2, "HAR", datetime.date(2019, 6, 29)), DataModel(3, "QQQ", datetime.date(2019, 1, 13))]

app.admincontrol = Admin(InMemoryDaoImpl.InMemoryDaoImpl(elements))


from app import routes