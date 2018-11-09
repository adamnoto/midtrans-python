class SnapResponse(object):
    def __init__(self,
                 token=None,
                 status_code=None,
                 error_messages=None,
                 redirect_url=None):

        self.status_code = status_code
        self.token = token
        self.error_messages = error_messages
        self.redirect_url = redirect_url
