from run import app
from app.routers.user import user

app.register_blueprint(user)