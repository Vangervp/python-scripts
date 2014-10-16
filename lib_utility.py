"""Exceptions used throughout the package.

Submodules of distutils2 may raise exceptions defined in this module as
well as standard exceptions; in particular, SystemExit is usually raised
for errors that are obviously the end-user's fault (e.g. bad
command-line arguments).
"""


class PackagingError(Exception):
    """The root of all Packaging evil."""

class PackagingFileError(PackagingError):
    """Any problems in the filesystem: expected file not found, etc.
    Typically this is for problems that we detect before IOError or
    OSError could be raised."""

class PackagingPlatformError(PackagingError):
    """We don't know how to do something on the current platform (but
    we do know how to do it on some platform) -- eg. trying to compile
    C files on a platform not supported by a CCompiler subclass."""


###########################################################################
import os

""" utility  """
_PLATFORM = None

def newer(source, target):
    """Tell if the target is newer than the source.

    Returns true if 'source' exists and is more recently modified than
    'target', or if 'source' exists and 'target' doesn't.

    Returns false if both exist and 'target' is the same age or younger
    than 'source'. Raise PackagingFileError if 'source' does not exist.

    Note that this test is not very accurate: files created in the same second
    will have the same "age".
    """
    if not os.path.exists(source):
        raise PackagingFileError("file '%s' does not exist" %
                                 os.path.abspath(source))
    if not os.path.exists(target):
        return True

    return os.stat(source).st_mtime > os.stat(target).st_mtime

if __name__ == "__main__":
    print newer("utility.py", "util.py")
