from flask import Flask
from controllers.main_blueprint import main_blueprint


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(main_blueprint)

app.run(debug=True)