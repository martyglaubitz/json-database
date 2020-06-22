import asyncio

import sys

import tornado.ioloop
import tornado.web

import configuration
import database_handler
import document_handler

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == "__main__":
    tornado_app = tornado.web.Application([
        (r"/(?P<db>[\w-]+)/?", database_handler.DatabaseHandler),
        (r"/(?P<db>[\w-]+)/(?P<path>.+)", document_handler.DocumentHandler),
    ], debug=True)

    tornado_app.listen(configuration.port)
    tornado.ioloop.IOLoop.current().start()
