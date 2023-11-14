from services.database import engine
from models import todo as todo_models, user as user_models


def init_models():
    todo_models.Base.metadata.create_all(bind=engine)
    user_models.Base.metadata.create_all(bind=engine)
