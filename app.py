from flask import Flask


def create_app():
    app = Flask(__name__)
    x=10
    y=10
    @app.route('/')
    def home():
        print("inside home function")
        return 'Hurray GFG - Sudhanshu!'

    @app.route('/test')
    def test():
        return 'Hi Sudhanshu test'

    @app.route('/test111')
    def test1():
        return 'Hi Sudhanshu test'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
