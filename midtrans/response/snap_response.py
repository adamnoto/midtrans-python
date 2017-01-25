class SnapResponse(object):
    def __init__(self,
                 status_code,
                 token,
                 error_messages):

        self.status_code = status_code
        self.token = token
        self.error_messages = error_messages
