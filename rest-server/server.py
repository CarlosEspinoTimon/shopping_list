from server import server, db
from server.models import *

# @server.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'Hero': Hero}

if __name__ == '__main__':
    server.run(debug=True)
