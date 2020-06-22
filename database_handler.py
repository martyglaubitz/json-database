import tornado
import tornado.web

import file

class DatabaseHandler(tornado.web.RequestHandler):

    def get(self, db):
        if file.file_for_path_exists(db):
            self.finish({
                'status': 200
            })
            return

        self.set_status(404)
        self.finish({
            'status': 404
        })

    def delete(self, db):
        if not file.file_for_path_exists(db):
            self.set_status(404)
            self.finish({
                'status': 404
            })
            return

        file.delete_folder(db)
        self.finish({
            'status': 200
        })

    def put(self, db):
        if file.file_for_path_exists(db):
            self.set_status(409)
            self.finish({
                'status': 409,
                'message': 'DB with name "' + db + '" already exists'
            })
            return

        file.create_folder(db)
        self.set_status(201)
        self.finish({
            'status': 201,
            'message': 'Created DB with name "' + db + '"'
        })

