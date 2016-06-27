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
    """
    Prepare for loading a file, i.e. check if it exists ... .
    ----------
    filename : string
        The name of the file to load
    path : string, optional
        The path where the file is located. If none is given, the current
        working directory is assumed.
    extension : string, optional
        File extension to append at the filename e.g ".png".

    Returns
    ----------
    filename : string
        The full filename including the path and extension.
    """
    #prepare path
    path = os.path.expanduser(path)

    # prepare filename
    if extension is not None:
        if extension[0] != '.':
            extension = '.' + extension
        filename = os.path.splitext(filename)[0]
        filename += extension

    filename = os.path.join(path, filename)

    # check if file exists
    if not os.path.isfile(filename):
        raise IOError('File {f} does not exist'.format(f=filename))

    return filename


def multiLoading(identifier='*', directory=None, extension=None, SUBDIRS=False):
    """
    Find directories of multiple files.
    ----------
    identifier : string
        Regular expression which must be present in the files to find.
    directory : string, optional
        The path where the file is located. If none is given, the current
        working directory is assumed.
    extension : string, optional
        File extension which must be present in the files to find.

    Returns
    ----------
    filenames : list
        A list with all filenames including the path, to look for.
    """
    # prepare path
    if directory is None:
        directory = os.getcwd()
    directory = os.path.expanduser(directory)


    # add extension if given
    if not extension is None:
        identifier = os.path.splitext(identifier)[0]
        identifier += extension


    # eventually including subdirectories
    if SUBDIRS:
        filenames = []
        for root, dirs, files in os.walk(directory, topdown=False):
            new_files = (glob.glob(os.path.join(root, identifier)))
            for file in new_files:
                filenames.append(file)

    else:
        filenames = glob.glob(os.path.join(directory, identifier))

    return sorted(filenames)

