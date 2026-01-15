"""
Unattend Applier - Apply Windows configurations from autounattend.xml files

Usage:
    >>> from unattend_applier import UnattendConfig
    >>> config = UnattendConfig('autounattend.xml')
    >>> config.apply_all()
"""

from .core import UnattendConfig

__version__ = '1.0.0'
__all__ = ['UnattendConfig']