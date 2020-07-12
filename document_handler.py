import tornado
import tornado.web

import file

class DocumentHandler(tornado.web.RequestHandler):

    def get(self, db, path):
        if not file.file_for_path_exists(db, path + ".json"):
            self.set_status(404)
            self.write(dict(
                status = 404,
                message = 'No document found for db "' + db + '" and path "' + path + '"'
            ))
            return

        self.write(dict(
            status = 200,
            result = file.json_for_path(db, path + ".json")
        ))

    def delete(self, db, path):
        if not file.file_for_path_exists(db, path + ".json"):
            self.set_status(404)
            self.write(dict(
                status = 404,
                message = 'No document found for db "' + db + '" and path "' + path + '"'
            ))
            return

        file.delete_file_for_path(path)

        self.write(dict(
            status = 200,
            message = 'Deleted document for db "' + db + '" and path "' + path + '"'
        ))

    def post(self, db, path):
       if not file.file_for_path_exists(db, path + ".json"):
            self.set_status(404)
            self.write(dict(
                status = 404,
                message = 'No document found for db "' + db + '" and path "' + path + '"'
            ))
            return

    def put(self, db, path):
        if file.file_for_path_exists(db, path + ".json"):
            self.set_status(409)
            self.write(dict(
                status = 409,
                message = 'No document found for db "' + db + '" and path "' + path + '"'
            ))
            return

        
        

    def put(self, path):
        if file.file_for_path_exists(path):
            self.set_status(409)
            self.write(dict(
                status = 409,
                message = 'Document found for path "' +  path + '" already exists'
            ))
            return

        self.post(path)
