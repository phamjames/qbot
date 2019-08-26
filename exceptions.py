# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class IncorrectTitleFormat(Error):
   """Raised when the input value is too small"""
   pass

class DescriptionTooLong(Error):
   """Raised when the input value is too large"""
   pass

class LobbyAlreadyExists(Error):
   """Raised when the input value is too large"""
   pass