class ARSError(Exception):
    """A generic high-level ARS exception"""
    pass


class ARSDataTypeError(Exception):
    """An error raised when an un-handled Remedy data type is encountered"""
    pass
