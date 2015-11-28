

class PurifyException(Exception):
    def __init__(self, message, code=None):
        super(PurifyException, self).__init__(message)
        self.code = code


class PurifyFormatException(Exception):
    def __init__(self, message, code=None):
        super(PurifyFormatException, self).__init__(message)
        self.code = code

    def __str__(self):
        return 'Unexpected format returned.  ' + self.message


class PurifyExceptionTooLarge(Exception):
    pass

