from config import HOST, PORT, DEBUG
from app import create_app


if __name__ == '__main__':
    # app = create_app(host=HOST, port=PORT, debug=DEBUG)
    app = create_app()
