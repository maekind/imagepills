#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Package commands interface"""

import functools

from imagepils import entrypoint
from imagepils import pils

# Entry points defintionng
size = functools.partial(entrypoint.size, pils.Size)
image2png = functools.partial(entrypoint.image2png, pils.Convert2PNG)
resize = functools.partial(entrypoint.resize, pils.Resize)
