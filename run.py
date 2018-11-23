import os

# from app import create_app, db
# from app.models import Client, Feature, ClientType

# config_name = os.getenv('FLASK_CONFIG')
# app = create_app(config_name)


# if __name__ == '__main__':
#     app.run()


from app import create_app, db
from app.models import Client, Feature, ClientType

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Client': Client, 'Feature': Feature, 'ClientType': ClientType}