#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2013, Nahuel Riva
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__revision__ = "$Id$"

__all__ = ['metadata', 'setup']

from distutils.core import setup
from distutils import version
from warnings import warn

import re
import os
import sys
import glob

# Get the base directory
here = os.path.dirname(__file__)
if not here:
    here = os.path.curdir

# Text describing the module (reStructured text)
try:
    readme = os.path.join(here, 'README.TXT')
    long_description = open(readme, 'r').read()
except Exception:
    warn("README file not found or unreadable!")
    long_description = """Krakatau-noff is a collection of analysis tools for Java .class files."""

# Get the list of scripts
scripts = [os.path.join(here, scr) for scr in ['assemble.py', 'disassemble.py', 'decompile.py']]

# find Krakatau -type d
_packages = """Krakatau
Krakatau/ssa
Krakatau/ssa/constraints
Krakatau/ssa/ssa_jumps
Krakatau/ssa/ssa_ops
Krakatau/verifier
Krakatau/util
Krakatau/classfileformat
Krakatau/assembler
Krakatau/java""".split('\n')

# Set the parameters for the setup script
metadata = {

    # Setup instructions
    'provides'          : ['Krakatau'],
    'packages'          : _packages,
    'scripts'           : scripts,

    # Metadata
    'name'              : 'Krakatau-noff',
    'version'           : 'v0.20181212',
    'description'       : 'Analysis tools for Java .class files.',
    'long_description'  : long_description,
    'url'               : 'https://github.com/drstrng/Krakatau-noff',
    'download_url'      : 'https://github.com/drstrng/Krakatau-noff/archive/v0.20181212.tar.gz',
    'keywords'          : ['java', 'jvm', 'class', '.class', 'assembler', 'disassembler', 'decompiler'],
    }

# Execute the setup script
if __name__ == '__main__':
    setup(**metadata)
