if __name__ == '__main__':
    from app.core import app
    from app.dashboards import *

    app.run_server(debug=True)
