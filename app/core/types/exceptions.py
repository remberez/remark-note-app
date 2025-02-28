class NotFoundError(Exception):
    """Exception for cases where the object is not found."""
    pass


class PermissionDeniedError(Exception):
    """Exception for cases where the user has insufficient permissions."""
    pass
