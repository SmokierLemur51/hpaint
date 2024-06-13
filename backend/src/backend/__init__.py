from .factory import create_app

def run() -> None:
    app = create_app()
    app.run(debug=True)
