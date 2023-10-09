# app/__init__.py
from utils import logger
from .main import get_targets

app = Flask(__name__)

def startup():
    get_targets():



if __name__ == '__main__':
    # Start Flask app
    app_port = int(os.environ.get('APP_PORT', 8887))
    app.run(debug=False, host='0.0.0.0', port=app_port)
