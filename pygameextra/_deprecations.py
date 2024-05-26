from deprecation import deprecated
from pygameextra.version import get as get_version

__version__ = get_version()

RECORDING_DEPRECATION_WRAPPER = deprecated(
    "2.0.0b71", "2.0.0b71", __version__,
    "Recording has been scrapped from PGE"
)
