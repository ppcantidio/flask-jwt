class CommonError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = int(status_code)


class InvalidData(Exception):
    def __init__(self, error):
        self.error = error
