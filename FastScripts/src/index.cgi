#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from index import app

CGIHandler().run(app)

