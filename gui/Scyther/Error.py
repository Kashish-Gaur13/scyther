#!/usr/bin/python
#
# Scyther interface error classes
#

#---------------------------------------------------------------------------

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ScytherError(Error):
    """Exception raised for errors generated by the backend

    Attributes:
        errorlist -- list of error lines are retrieved from the
        backend
    """

    def __init__(self, errorlist):
        self.errorlist = errorlist

    def __str__(self):
        s = "Scyther backend reported the following errors:\n"
        s = s + "\n".join(self.errorlist)
        return s

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class BinaryError(Error):
    """Raised when the Scyther executable is not found.

    Attributes:
        file -- file location at which we should have been able to find it.
    """

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "Could not find Scyther executable at '%s'" % (self.file)


class NoBinaryError(Error):
    """Raised when the Scyther executable is not defined.

    Attributes:
        None.
    """

    def __str__(self):
        return "Scyther class attribute 'program' was not defined."


class UnknownPlatformError(Error):
    """Raised when the platform is not supported yet.

    Attributes:
        platform -- string describing the platform.
    """

    def __init__(self, platform):
        self.platform = platform

    def __str__(self):
        return "The %s platform is currently unsupported." % self.platform

class StringListError(Error):
    """Raised when the a string should be a list of strings or a string

    Attributes:
        obj -- object that did not fit
    """

    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return "Got %s instead of a (list of) string." % self.obj

# vim: set ts=4 sw=4 et list lcs=tab\:>-:
