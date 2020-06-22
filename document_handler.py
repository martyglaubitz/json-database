import tornado
import tornado.web

import file

class DocumentHandler(tornado.web.RequestHandler):

    def get(self, db, path):
        self.finish({"uri":db, "path":path})

        # if file.file_for_path_exists(path):
        #     self.set_status(404)
        #     self.write(dict(
        #         status = 404,
        #         message = str('No document found for path "', path, '"')
        #     ))
        #     return

        # self.write(dict(
        #     status = 200,
        #     result = file.json_for_path(path)
        # ))

    def delete(self, path):
        if file.file_for_path_exists(path):
            self.set_status(404)
            self.write(dict(
                status = 404,
                message = str('No document found for path "', path, '"')
            ))
            return

        file.delete_file_for_path(path)

        self.write(dict(
            status = 200,
            message = str('Document found for path "', path, '" deleted')
        ))

    def post(self, path):
        write_mode = file.write_json_for_path(path, self.request.body)
        if write_mode.CREATE:
            self.set_status(201)
            self.write(dict(
                status = 201,
                result = self.request.body
            ))
            return

        self.write(dict(
            status = 200,
            result = self.request.body
        ))

    def put(self, path):
        self.post(path)
