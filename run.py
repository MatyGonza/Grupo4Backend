from flask import Flask
from app.views import *
from app.database import init_app

#inicializacion del proyecto Flask
app = Flask(__name__)

init_app(app)

app.route('/',methods=['GET'])(index)

app.route('/api/productos',methods=['GET'])(get_all_productos)

app.route('/api/productos/<int:id>',methods=['GET'])(get_producto)

app.route('/api/productos/', methods=['POST'])(create_producto)

if __name__=='__main__':
    app.run(debug=True)