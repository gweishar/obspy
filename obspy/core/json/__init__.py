# -*- coding: utf-8 -*-
"""
JSON write support

JavaScript Object Notation is a text-based open standard designed for
human-readable data interchange. The JSON format is often used for serializing
and transmitting structured data over a network connection. It is used
primarily to transmit data between a server and web application, serving as an
alternative to XML.

See the module :mod:`obspy.core.json.default` for documentation on the class.
A write function for files and a utility for compact string serialization using
the Default class are located in :mod:`obspy.core.json.core`.

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from .default import Default
from .core import get_dump_kwargs, writeJSON
