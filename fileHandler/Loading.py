#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Functions and classes for easier file handling during loading.
:author: Manuel Tuschen
:date: 24.06.2016
:license: FreeBSD

License
----------
Copyright (c) 2016, Manuel Tuschen
All rights reserved.
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


from __future__ import division, absolute_import, unicode_literals, print_function
import os
import glob

def prepareLoading(filename, path=None, extension=None):

    # prepare filename
    if extension is not None:
        filename = os.path.splitext(filename)[0]
        filename += extension

    filename = os.path.join(path, filename)

    # check if file exists
    if not os.path.isfile(filename):
        raise IOError('File {f} does not exist'.format(f=filename))

    return filename


def multiLoading(identifier='*', path=None, extension=None, SUBDIRS=False):

    # prepare path
    if path is None:
        path = os.getcwd()
    path = os.path.expanduser(path)

    # eventually including subdirectories
    if SUBDIRS == True:
        os.path.join(path,'*')

    # add extension if given
    if not extension is None:
        identifier = os.path.splitext(identifier)[0]
        identifier += extension

    # search for all filenames
    filename = os.path.join(path, identifier)

    filenames = sorted(glob.glob(filename))

    return filenames

