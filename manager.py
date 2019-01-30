import sys
sys.path.append('app/')

from aiohttp.web import Application, run_app

from app import RestResource
from app.models import Note
from sqlalchemy import engine_from_config


notes = {}
app = Application()
person_resource = RestResource('notes', Note, notes, ('title', 'description', 'created_at', 'created_by', 'priority'), 'title')
person_resource.register(app.router)


if __name__ == '__main__':

    run_app(app, port=3000)
