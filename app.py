# from flask import Flask
# from flask_cors import CORS
# from config import Config
# from app.models import db
# import os

# app = Flask(__name__)
# app.config.from_object(Config)
# CORS(app)

# db.init_app(app)

# from app.routes import *

# # if __name__ == "__main__":
# #     app.run(debug=True)

# if __name__ == "__main__":
#     app.run(debug=True if os.getenv("FLASK_DEBUG") == "True" else False)

from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(debug=debug_mode)
