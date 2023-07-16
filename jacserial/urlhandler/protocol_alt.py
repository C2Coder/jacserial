#! python
#
# This module implements a special URL handler that allows selecting an
# alternate implementation provided by some backends.
#
# This file is part of pyjacSerial. https://github.com/pyserial/pyserial
# (C) 2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause
#
# URL format:    alt://port[?option[=value][&option[=value]]]
# options:
# - class=X used class named X instead of Serial
#
# example:
#   use poll based implementation on Posix (Linux):
#   python -m jacserial.tools.miniterm alt:///dev/ttyUSB0?class=PosixPollSerial

from __future__ import absolute_import

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

import jacserial


def serial_class_for_url(url):
    """extract host and port from an URL string"""
    parts = urlparse.urlsplit(url)
    if parts.scheme != 'alt':
        raise jacserial.SerialException(
            'expected a string in the form "alt://port[?option[=value][&option[=value]]]": '
            'not starting with alt:// ({!r})'.format(parts.scheme))
    class_name = 'Serial'
    try:
        for option, values in urlparse.parse_qs(parts.query, True).items():
            if option == 'class':
                class_name = values[0]
            else:
                raise ValueError('unknown option: {!r}'.format(option))
    except ValueError as e:
        raise jacserial.SerialException(
            'expected a string in the form '
            '"alt://port[?option[=value][&option[=value]]]": {!r}'.format(e))
    if not hasattr(jacserial, class_name):
        raise ValueError('unknown class: {!r}'.format(class_name))
    cls = getattr(jacserial, class_name)
    if not issubclass(cls, jacserial.Serial):
        raise ValueError('class {!r} is not an instance of Serial'.format(class_name))
    return (''.join([parts.netloc, parts.path]), cls)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    s = jacserial.serial_for_url('alt:///dev/ttyS0?class=PosixPollSerial')
    print(s)
