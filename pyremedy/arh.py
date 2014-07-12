'''Wrapper for ar.h

Generated with:
/home/d235183/.virtualenv/dockethead-8.1/bin/ctypesgen.py /opt/dockethead/include/ar.h -o arh.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

ARLong32 = c_int # /opt/dockethead/include/artypes.h: 57

ARULong32 = c_uint # /opt/dockethead/include/artypes.h: 77

ARUIntPtr = c_size_t # /opt/dockethead/include/artypes.h: 101

ARBoolean = c_ubyte # /opt/dockethead/include/ar.h: 275

AREntryIdType = c_char * (15 + 1) # /opt/dockethead/include/ar.h: 278

ARInternalId = ARULong32 # /opt/dockethead/include/ar.h: 280

ARNameType = c_char * (254 + 1) # /opt/dockethead/include/ar.h: 282

ARPasswordType = c_char * (30 + 1) # /opt/dockethead/include/ar.h: 284

ARAuthType = c_char * (2047 + 1) # /opt/dockethead/include/ar.h: 286

ARFileNameType = c_char * (255 + 1) # /opt/dockethead/include/ar.h: 288

ARAccessNameType = c_char * (254 + 1) # /opt/dockethead/include/ar.h: 290

AREncryptedPasswordType = c_char * (120 + 1) # /opt/dockethead/include/ar.h: 292

ARServerNameType = c_char * (64 + 1) # /opt/dockethead/include/ar.h: 294

ARTimestamp = ARLong32 # /opt/dockethead/include/ar.h: 296

ARLicenseNameType = c_char * (50 + 1) # /opt/dockethead/include/ar.h: 299

ARLicenseKeyType = c_char * (30 + 1) # /opt/dockethead/include/ar.h: 301

ARHostIDType = c_char * (100 + 1) # /opt/dockethead/include/ar.h: 303

ARLocaleType = c_char * (64 + 1) # /opt/dockethead/include/ar.h: 305

ARCMenuType = c_char * (255 + 1) # /opt/dockethead/include/ar.h: 307

ARTableNameType = c_char * (2047 + 1) # /opt/dockethead/include/ar.h: 309

ARTime = ARLong32 # /opt/dockethead/include/ar.h: 310

ARCurrencyCodeType = c_char * (3 + 1) # /opt/dockethead/include/ar.h: 311

# /opt/dockethead/include/ar.h: 319
class struct_ARTextString(Structure):
    pass

struct_ARTextString.__slots__ = [
    'length',
    'string',
]
struct_ARTextString._fields_ = [
    ('length', c_uint),
    ('string', String),
]

ARTextString = struct_ARTextString # /opt/dockethead/include/ar.h: 319

# /opt/dockethead/include/ar.h: 327
class struct_AREntryIdList(Structure):
    pass

struct_AREntryIdList.__slots__ = [
    'numItems',
    'entryIdList',
]
struct_AREntryIdList._fields_ = [
    ('numItems', c_uint),
    ('entryIdList', POINTER(AREntryIdType)),
]

AREntryIdList = struct_AREntryIdList # /opt/dockethead/include/ar.h: 327

# /opt/dockethead/include/ar.h: 335
class struct_ARInternalIdList(Structure):
    pass

struct_ARInternalIdList.__slots__ = [
    'numItems',
    'internalIdList',
]
struct_ARInternalIdList._fields_ = [
    ('numItems', c_uint),
    ('internalIdList', POINTER(ARInternalId)),
]

ARInternalIdList = struct_ARInternalIdList # /opt/dockethead/include/ar.h: 335

# /opt/dockethead/include/ar.h: 343
class struct_ARInternalIdListList(Structure):
    pass

struct_ARInternalIdListList.__slots__ = [
    'numItems',
    'internalIdListList',
]
struct_ARInternalIdListList._fields_ = [
    ('numItems', c_uint),
    ('internalIdListList', POINTER(ARInternalIdList)),
]

ARInternalIdListList = struct_ARInternalIdListList # /opt/dockethead/include/ar.h: 343

# /opt/dockethead/include/ar.h: 351
class struct_ARLocaleList(Structure):
    pass

struct_ARLocaleList.__slots__ = [
    'numItems',
    'localeList',
]
struct_ARLocaleList._fields_ = [
    ('numItems', c_uint),
    ('localeList', POINTER(ARLocaleType)),
]

ARLocaleList = struct_ARLocaleList # /opt/dockethead/include/ar.h: 351

# /opt/dockethead/include/ar.h: 359
class struct_ARNameList(Structure):
    pass

struct_ARNameList.__slots__ = [
    'numItems',
    'nameList',
]
struct_ARNameList._fields_ = [
    ('numItems', c_uint),
    ('nameList', POINTER(ARNameType)),
]

ARNameList = struct_ARNameList # /opt/dockethead/include/ar.h: 359

# /opt/dockethead/include/ar.h: 367
class struct_ARNamePtrList(Structure):
    pass

struct_ARNamePtrList.__slots__ = [
    'numItems',
    'namePtrList',
]
struct_ARNamePtrList._fields_ = [
    ('numItems', c_uint),
    ('namePtrList', POINTER(POINTER(c_char))),
]

ARNamePtrList = struct_ARNamePtrList # /opt/dockethead/include/ar.h: 367

# /opt/dockethead/include/ar.h: 372
class struct_ARFileNameList(Structure):
    pass

struct_ARFileNameList.__slots__ = [
    'numItems',
    'fileNameList',
]
struct_ARFileNameList._fields_ = [
    ('numItems', c_uint),
    ('fileNameList', POINTER(ARFileNameType)),
]

ARFileNameList = struct_ARFileNameList # /opt/dockethead/include/ar.h: 372

# /opt/dockethead/include/ar.h: 379
class struct_ARAccessNameList(Structure):
    pass

struct_ARAccessNameList.__slots__ = [
    'numItems',
    'nameList',
]
struct_ARAccessNameList._fields_ = [
    ('numItems', c_uint),
    ('nameList', POINTER(ARAccessNameType)),
]

ARAccessNameList = struct_ARAccessNameList # /opt/dockethead/include/ar.h: 379

# /opt/dockethead/include/ar.h: 387
class struct_ARAccessNamePtrList(Structure):
    pass

struct_ARAccessNamePtrList.__slots__ = [
    'numItems',
    'namePtrList',
]
struct_ARAccessNamePtrList._fields_ = [
    ('numItems', c_uint),
    ('namePtrList', POINTER(POINTER(c_char))),
]

ARAccessNamePtrList = struct_ARAccessNamePtrList # /opt/dockethead/include/ar.h: 387

# /opt/dockethead/include/ar.h: 393
class struct_ARPasswordList(Structure):
    pass

struct_ARPasswordList.__slots__ = [
    'numItems',
    'nameList',
]
struct_ARPasswordList._fields_ = [
    ('numItems', c_uint),
    ('nameList', POINTER(ARPasswordType)),
]

ARPasswordList = struct_ARPasswordList # /opt/dockethead/include/ar.h: 393

# /opt/dockethead/include/ar.h: 400
class struct_ARServerNameList(Structure):
    pass

struct_ARServerNameList.__slots__ = [
    'numItems',
    'nameList',
]
struct_ARServerNameList._fields_ = [
    ('numItems', c_uint),
    ('nameList', POINTER(ARServerNameType)),
]

ARServerNameList = struct_ARServerNameList # /opt/dockethead/include/ar.h: 400

# /opt/dockethead/include/ar.h: 408
class struct_ARTextStringList(Structure):
    pass

struct_ARTextStringList.__slots__ = [
    'numItems',
    'stringList',
]
struct_ARTextStringList._fields_ = [
    ('numItems', c_uint),
    ('stringList', POINTER(POINTER(c_char))),
]

ARTextStringList = struct_ARTextStringList # /opt/dockethead/include/ar.h: 408

# /opt/dockethead/include/ar.h: 416
class struct_ARTimestampList(Structure):
    pass

struct_ARTimestampList.__slots__ = [
    'numItems',
    'timestampList',
]
struct_ARTimestampList._fields_ = [
    ('numItems', c_uint),
    ('timestampList', POINTER(ARTimestamp)),
]

ARTimestampList = struct_ARTimestampList # /opt/dockethead/include/ar.h: 416

# /opt/dockethead/include/ar.h: 424
class struct_ARUnsignedIntList(Structure):
    pass

struct_ARUnsignedIntList.__slots__ = [
    'numItems',
    'intList',
]
struct_ARUnsignedIntList._fields_ = [
    ('numItems', c_uint),
    ('intList', POINTER(c_uint)),
]

ARUnsignedIntList = struct_ARUnsignedIntList # /opt/dockethead/include/ar.h: 424

# /opt/dockethead/include/ar.h: 432
class struct_ARUnsignedIntPtrList(Structure):
    pass

struct_ARUnsignedIntPtrList.__slots__ = [
    'numItems',
    'intPtrList',
]
struct_ARUnsignedIntPtrList._fields_ = [
    ('numItems', c_uint),
    ('intPtrList', POINTER(POINTER(c_uint))),
]

ARUnsignedIntPtrList = struct_ARUnsignedIntPtrList # /opt/dockethead/include/ar.h: 432

# /opt/dockethead/include/ar.h: 454
class struct_ARByteList(Structure):
    pass

struct_ARByteList.__slots__ = [
    'type',
    'noval_',
    'numItems',
    'bytes',
]
struct_ARByteList._fields_ = [
    ('type', ARULong32),
    ('noval_', ARULong32),
    ('numItems', c_uint),
    ('bytes', POINTER(c_ubyte)),
]

ARByteList = struct_ARByteList # /opt/dockethead/include/ar.h: 454

# /opt/dockethead/include/ar.h: 465
class struct_ARLocalizationInfo(Structure):
    pass

struct_ARLocalizationInfo.__slots__ = [
    'locale',
    'charSet',
    'timeZone',
    'customDateFormat',
    'customTimeFormat',
    'separators',
]
struct_ARLocalizationInfo._fields_ = [
    ('locale', c_char * (64 + 1)),
    ('charSet', c_char * (15 + 1)),
    ('timeZone', c_char * (64 + 1)),
    ('customDateFormat', c_char * (32 + 1)),
    ('customTimeFormat', c_char * (32 + 1)),
    ('separators', c_char * (15 + 1)),
]

ARLocalizationInfo = struct_ARLocalizationInfo # /opt/dockethead/include/ar.h: 465

# /opt/dockethead/include/ar.h: 495
class struct_ARControlStruct(Structure):
    pass

struct_ARControlStruct.__slots__ = [
    'cacheId',
    'operationTime',
    'user',
    'password',
    'localeInfo',
    'sessionId',
    'authString',
    'server',
]
struct_ARControlStruct._fields_ = [
    ('cacheId', ARLong32),
    ('operationTime', ARTimestamp),
    ('user', ARAccessNameType),
    ('password', ARPasswordType),
    ('localeInfo', ARLocalizationInfo),
    ('sessionId', ARUIntPtr),
    ('authString', ARAuthType),
    ('server', c_char * (64 + 1)),
]

ARControlStruct = struct_ARControlStruct # /opt/dockethead/include/ar.h: 495

# /opt/dockethead/include/ar.h: 505
class struct_ARStatusStruct(Structure):
    pass

struct_ARStatusStruct.__slots__ = [
    'messageType',
    'messageNum',
    'messageText',
    'appendedText',
]
struct_ARStatusStruct._fields_ = [
    ('messageType', c_uint),
    ('messageNum', ARLong32),
    ('messageText', String),
    ('appendedText', String),
]

ARStatusStruct = struct_ARStatusStruct # /opt/dockethead/include/ar.h: 505

# /opt/dockethead/include/ar.h: 513
class struct_ARStatusList(Structure):
    pass

struct_ARStatusList.__slots__ = [
    'numItems',
    'statusList',
]
struct_ARStatusList._fields_ = [
    ('numItems', c_uint),
    ('statusList', POINTER(ARStatusStruct)),
]

ARStatusList = struct_ARStatusList # /opt/dockethead/include/ar.h: 513

# /opt/dockethead/include/ar.h: 521
class struct_ARStatusListList(Structure):
    pass

struct_ARStatusListList.__slots__ = [
    'numItems',
    'statusListList',
]
struct_ARStatusListList._fields_ = [
    ('numItems', c_uint),
    ('statusListList', POINTER(ARStatusList)),
]

ARStatusListList = struct_ARStatusListList # /opt/dockethead/include/ar.h: 521

# /opt/dockethead/include/ar.h: 531
class struct_ARMessageStruct(Structure):
    pass

struct_ARMessageStruct.__slots__ = [
    'messageType',
    'messageNum',
    'messageText',
    'usePromptingPane',
]
struct_ARMessageStruct._fields_ = [
    ('messageType', c_uint),
    ('messageNum', ARLong32),
    ('messageText', String),
    ('usePromptingPane', ARBoolean),
]

ARMessageStruct = struct_ARMessageStruct # /opt/dockethead/include/ar.h: 531

# /opt/dockethead/include/ar.h: 699
class struct_ARCoordStruct(Structure):
    pass

struct_ARCoordStruct.__slots__ = [
    'x',
    'y',
]
struct_ARCoordStruct._fields_ = [
    ('x', ARLong32),
    ('y', ARLong32),
]

ARCoordStruct = struct_ARCoordStruct # /opt/dockethead/include/ar.h: 699

# /opt/dockethead/include/ar.h: 706
class struct_ARCoordList(Structure):
    pass

struct_ARCoordList.__slots__ = [
    'numItems',
    'coords',
]
struct_ARCoordList._fields_ = [
    ('numItems', c_uint),
    ('coords', POINTER(ARCoordStruct)),
]

ARCoordList = struct_ARCoordList # /opt/dockethead/include/ar.h: 706

# /opt/dockethead/include/ar.h: 719
class struct_ARBufStruct(Structure):
    pass

struct_ARBufStruct.__slots__ = [
    'bufSize',
    'buffer',
]
struct_ARBufStruct._fields_ = [
    ('bufSize', ARULong32),
    ('buffer', POINTER(c_ubyte)),
]

ARBufStruct = struct_ARBufStruct # /opt/dockethead/include/ar.h: 719

# /opt/dockethead/include/ar.h: 725
class union_anon_1(Union):
    pass

union_anon_1.__slots__ = [
    'filename',
    'buf',
]
union_anon_1._fields_ = [
    ('filename', String),
    ('buf', ARBufStruct),
]

# /opt/dockethead/include/ar.h: 731
class struct_ARLocStruct(Structure):
    pass

struct_ARLocStruct.__slots__ = [
    'locType',
    'u',
]
struct_ARLocStruct._fields_ = [
    ('locType', ARULong32),
    ('u', union_anon_1),
]

ARLocStruct = struct_ARLocStruct # /opt/dockethead/include/ar.h: 731

# /opt/dockethead/include/ar.h: 741
class struct_ARAttachStruct(Structure):
    pass

struct_ARAttachStruct.__slots__ = [
    'name',
    'origSize',
    'compSize',
    'loc',
]
struct_ARAttachStruct._fields_ = [
    ('name', String),
    ('origSize', ARLong32),
    ('compSize', ARLong32),
    ('loc', ARLocStruct),
]

ARAttachStruct = struct_ARAttachStruct # /opt/dockethead/include/ar.h: 741

# /opt/dockethead/include/ar.h: 749
class struct_ARFuncCurrencyStruct(Structure):
    pass

struct_ARFuncCurrencyStruct.__slots__ = [
    'value',
    'currencyCode',
]
struct_ARFuncCurrencyStruct._fields_ = [
    ('value', String),
    ('currencyCode', ARCurrencyCodeType),
]

ARFuncCurrencyStruct = struct_ARFuncCurrencyStruct # /opt/dockethead/include/ar.h: 749

# /opt/dockethead/include/ar.h: 757
class struct_ARFuncCurrencyList(Structure):
    pass

struct_ARFuncCurrencyList.__slots__ = [
    'numItems',
    'funcCurrencyList',
]
struct_ARFuncCurrencyList._fields_ = [
    ('numItems', c_uint),
    ('funcCurrencyList', POINTER(ARFuncCurrencyStruct)),
]

ARFuncCurrencyList = struct_ARFuncCurrencyList # /opt/dockethead/include/ar.h: 757

# /opt/dockethead/include/ar.h: 767
class struct_ARCurrencyStruct(Structure):
    pass

struct_ARCurrencyStruct.__slots__ = [
    'value',
    'currencyCode',
    'conversionDate',
    'funcList',
]
struct_ARCurrencyStruct._fields_ = [
    ('value', String),
    ('currencyCode', ARCurrencyCodeType),
    ('conversionDate', ARTimestamp),
    ('funcList', ARFuncCurrencyList),
]

ARCurrencyStruct = struct_ARCurrencyStruct # /opt/dockethead/include/ar.h: 767

# /opt/dockethead/include/ar.h: 774
class struct_ARCurrencyList(Structure):
    pass

struct_ARCurrencyList.__slots__ = [
    'numItems',
    'currencyList',
]
struct_ARCurrencyList._fields_ = [
    ('numItems', c_uint),
    ('currencyList', POINTER(ARCurrencyStruct)),
]

ARCurrencyList = struct_ARCurrencyList # /opt/dockethead/include/ar.h: 774

# /opt/dockethead/include/ar.h: 782
class union_anon_2(Union):
    pass

union_anon_2.__slots__ = [
    'noval_',
    'keyNum',
    'intVal',
    'realVal',
    'charVal',
    'diaryVal',
    'enumVal',
    'timeVal',
    'maskVal',
    'timeOfDayVal',
    'byteListVal',
    'decimalVal',
    'attachVal',
    'ulongVal',
    'coordListVal',
    'dateVal',
    'currencyVal',
    'ptrVal',
]
union_anon_2._fields_ = [
    ('noval_', c_size_t),
    ('keyNum', c_uint),
    ('intVal', ARLong32),
    ('realVal', c_double),
    ('charVal', String),
    ('diaryVal', String),
    ('enumVal', ARULong32),
    ('timeVal', ARTimestamp),
    ('maskVal', ARULong32),
    ('timeOfDayVal', ARTime),
    ('byteListVal', POINTER(ARByteList)),
    ('decimalVal', String),
    ('attachVal', POINTER(ARAttachStruct)),
    ('ulongVal', ARULong32),
    ('coordListVal', POINTER(ARCoordList)),
    ('dateVal', c_int),
    ('currencyVal', POINTER(ARCurrencyStruct)),
    ('ptrVal', POINTER(None)),
]

# /opt/dockethead/include/ar.h: 814
class struct_ARValueStruct(Structure):
    pass

struct_ARValueStruct.__slots__ = [
    'dataType',
    'u',
]
struct_ARValueStruct._fields_ = [
    ('dataType', c_uint),
    ('u', union_anon_2),
]

ARValueStruct = struct_ARValueStruct # /opt/dockethead/include/ar.h: 814

# /opt/dockethead/include/ar.h: 822
class struct_ARValueList(Structure):
    pass

struct_ARValueList.__slots__ = [
    'numItems',
    'valueList',
]
struct_ARValueList._fields_ = [
    ('numItems', c_uint),
    ('valueList', POINTER(ARValueStruct)),
]

ARValueList = struct_ARValueList # /opt/dockethead/include/ar.h: 822

# /opt/dockethead/include/ar.h: 830
class struct_ARValuePtrList(Structure):
    pass

struct_ARValuePtrList.__slots__ = [
    'numItems',
    'valuePtrList',
]
struct_ARValuePtrList._fields_ = [
    ('numItems', c_uint),
    ('valuePtrList', POINTER(POINTER(ARValueStruct))),
]

ARValuePtrList = struct_ARValuePtrList # /opt/dockethead/include/ar.h: 830

# /opt/dockethead/include/ar.h: 838
class struct_ARValueListList(Structure):
    pass

struct_ARValueListList.__slots__ = [
    'numItems',
    'valueListList',
]
struct_ARValueListList._fields_ = [
    ('numItems', c_uint),
    ('valueListList', POINTER(ARValueList)),
]

ARValueListList = struct_ARValueListList # /opt/dockethead/include/ar.h: 838

# /opt/dockethead/include/ar.h: 856
class struct_AREntryListFieldStruct(Structure):
    pass

struct_AREntryListFieldStruct.__slots__ = [
    'fieldId',
    'columnWidth',
    'separator',
]
struct_AREntryListFieldStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('columnWidth', c_uint),
    ('separator', c_char * 10),
]

AREntryListFieldStruct = struct_AREntryListFieldStruct # /opt/dockethead/include/ar.h: 856

# /opt/dockethead/include/ar.h: 863
class struct_AREntryListFieldList(Structure):
    pass

struct_AREntryListFieldList.__slots__ = [
    'numItems',
    'fieldsList',
]
struct_AREntryListFieldList._fields_ = [
    ('numItems', c_uint),
    ('fieldsList', POINTER(AREntryListFieldStruct)),
]

AREntryListFieldList = struct_AREntryListFieldList # /opt/dockethead/include/ar.h: 863

# /opt/dockethead/include/ar.h: 871
class struct_AREntryListFieldListList(Structure):
    pass

struct_AREntryListFieldListList.__slots__ = [
    'numItems',
    'listFieldList',
]
struct_AREntryListFieldListList._fields_ = [
    ('numItems', c_uint),
    ('listFieldList', POINTER(AREntryListFieldList)),
]

AREntryListFieldListList = struct_AREntryListFieldListList # /opt/dockethead/include/ar.h: 871

# /opt/dockethead/include/ar.h: 882
class struct_AREntryListStruct(Structure):
    pass

struct_AREntryListStruct.__slots__ = [
    'entryId',
    'shortDesc',
]
struct_AREntryListStruct._fields_ = [
    ('entryId', AREntryIdList),
    ('shortDesc', String),
]

AREntryListStruct = struct_AREntryListStruct # /opt/dockethead/include/ar.h: 882

# /opt/dockethead/include/ar.h: 893
class struct_AREntryFuncListStruct(Structure):
    pass

struct_AREntryFuncListStruct.__slots__ = [
    'entryId',
    'funcId',
    'shortDesc',
]
struct_AREntryFuncListStruct._fields_ = [
    ('entryId', AREntryIdList),
    ('funcId', c_int),
    ('shortDesc', String),
]

AREntryFuncListStruct = struct_AREntryFuncListStruct # /opt/dockethead/include/ar.h: 893

# /opt/dockethead/include/ar.h: 900
class struct_AREntryListList(Structure):
    pass

struct_AREntryListList.__slots__ = [
    'numItems',
    'entryList',
]
struct_AREntryListList._fields_ = [
    ('numItems', c_uint),
    ('entryList', POINTER(AREntryListStruct)),
]

AREntryListList = struct_AREntryListList # /opt/dockethead/include/ar.h: 900

# /opt/dockethead/include/ar.h: 907
class struct_AREntryFuncListList(Structure):
    pass

struct_AREntryFuncListList.__slots__ = [
    'numItems',
    'entryList',
]
struct_AREntryFuncListList._fields_ = [
    ('numItems', c_uint),
    ('entryList', POINTER(AREntryFuncListStruct)),
]

AREntryFuncListList = struct_AREntryFuncListList # /opt/dockethead/include/ar.h: 907

# /opt/dockethead/include/ar.h: 914
class struct_AREntryIdListList(Structure):
    pass

struct_AREntryIdListList.__slots__ = [
    'numItems',
    'entryIdList',
]
struct_AREntryIdListList._fields_ = [
    ('numItems', c_uint),
    ('entryIdList', POINTER(AREntryIdList)),
]

AREntryIdListList = struct_AREntryIdListList # /opt/dockethead/include/ar.h: 914

# /opt/dockethead/include/ar.h: 922
class struct_ARFieldValueStruct(Structure):
    pass

struct_ARFieldValueStruct.__slots__ = [
    'fieldId',
    'value',
]
struct_ARFieldValueStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('value', ARValueStruct),
]

ARFieldValueStruct = struct_ARFieldValueStruct # /opt/dockethead/include/ar.h: 922

# /opt/dockethead/include/ar.h: 930
class struct_ARFieldValueList(Structure):
    pass

struct_ARFieldValueList.__slots__ = [
    'numItems',
    'fieldValueList',
]
struct_ARFieldValueList._fields_ = [
    ('numItems', c_uint),
    ('fieldValueList', POINTER(ARFieldValueStruct)),
]

ARFieldValueList = struct_ARFieldValueList # /opt/dockethead/include/ar.h: 930

# /opt/dockethead/include/ar.h: 941
class struct_AREntryListFieldValueStruct(Structure):
    pass

struct_AREntryListFieldValueStruct.__slots__ = [
    'entryId',
    'entryValues',
]
struct_AREntryListFieldValueStruct._fields_ = [
    ('entryId', AREntryIdList),
    ('entryValues', POINTER(ARFieldValueList)),
]

AREntryListFieldValueStruct = struct_AREntryListFieldValueStruct # /opt/dockethead/include/ar.h: 941

# /opt/dockethead/include/ar.h: 949
class struct_AREntryListFieldValueList(Structure):
    pass

struct_AREntryListFieldValueList.__slots__ = [
    'numItems',
    'entryList',
]
struct_AREntryListFieldValueList._fields_ = [
    ('numItems', c_uint),
    ('entryList', POINTER(AREntryListFieldValueStruct)),
]

AREntryListFieldValueList = struct_AREntryListFieldValueList # /opt/dockethead/include/ar.h: 949

# /opt/dockethead/include/ar.h: 957
class struct_ARFieldFuncValueStruct(Structure):
    pass

struct_ARFieldFuncValueStruct.__slots__ = [
    'fieldId',
    'funcId',
    'value',
]
struct_ARFieldFuncValueStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('funcId', c_int),
    ('value', ARValueStruct),
]

ARFieldFuncValueStruct = struct_ARFieldFuncValueStruct # /opt/dockethead/include/ar.h: 957

# /opt/dockethead/include/ar.h: 965
class struct_ARFieldFuncValueList(Structure):
    pass

struct_ARFieldFuncValueList.__slots__ = [
    'numItems',
    'fieldValueList',
]
struct_ARFieldFuncValueList._fields_ = [
    ('numItems', c_uint),
    ('fieldValueList', POINTER(ARFieldFuncValueStruct)),
]

ARFieldFuncValueList = struct_ARFieldFuncValueList # /opt/dockethead/include/ar.h: 965

# /opt/dockethead/include/ar.h: 972
class struct_AREntryListFieldFuncValueStruct(Structure):
    pass

struct_AREntryListFieldFuncValueStruct.__slots__ = [
    'entryId',
    'entryValues',
]
struct_AREntryListFieldFuncValueStruct._fields_ = [
    ('entryId', AREntryIdList),
    ('entryValues', POINTER(ARFieldFuncValueList)),
]

AREntryListFieldFuncValueStruct = struct_AREntryListFieldFuncValueStruct # /opt/dockethead/include/ar.h: 972

# /opt/dockethead/include/ar.h: 980
class struct_AREntryListFieldFuncValueList(Structure):
    pass

struct_AREntryListFieldFuncValueList.__slots__ = [
    'numItems',
    'entryList',
]
struct_AREntryListFieldFuncValueList._fields_ = [
    ('numItems', c_uint),
    ('entryList', POINTER(AREntryListFieldFuncValueStruct)),
]

AREntryListFieldFuncValueList = struct_AREntryListFieldFuncValueList # /opt/dockethead/include/ar.h: 980

# /opt/dockethead/include/ar.h: 987
class struct_ARBooleanList(Structure):
    pass

struct_ARBooleanList.__slots__ = [
    'numItems',
    'booleanList',
]
struct_ARBooleanList._fields_ = [
    ('numItems', c_uint),
    ('booleanList', POINTER(ARBoolean)),
]

ARBooleanList = struct_ARBooleanList # /opt/dockethead/include/ar.h: 987

# /opt/dockethead/include/ar.h: 995
class struct_ARBooleanListList(Structure):
    pass

struct_ARBooleanListList.__slots__ = [
    'numItems',
    'booleanList',
]
struct_ARBooleanListList._fields_ = [
    ('numItems', c_uint),
    ('booleanList', POINTER(ARBooleanList)),
]

ARBooleanListList = struct_ARBooleanListList # /opt/dockethead/include/ar.h: 995

# /opt/dockethead/include/ar.h: 1002
class struct_ARFieldValueListList(Structure):
    pass

struct_ARFieldValueListList.__slots__ = [
    'numItems',
    'valueListList',
]
struct_ARFieldValueListList._fields_ = [
    ('numItems', c_uint),
    ('valueListList', POINTER(ARFieldValueList)),
]

ARFieldValueListList = struct_ARFieldValueListList # /opt/dockethead/include/ar.h: 1002

# /opt/dockethead/include/ar.h: 1009
class struct_ARFieldFuncValueListList(Structure):
    pass

struct_ARFieldFuncValueListList.__slots__ = [
    'numItems',
    'valueListList',
]
struct_ARFieldFuncValueListList._fields_ = [
    ('numItems', c_uint),
    ('valueListList', POINTER(ARFieldFuncValueList)),
]

ARFieldFuncValueListList = struct_ARFieldFuncValueListList # /opt/dockethead/include/ar.h: 1009

# /opt/dockethead/include/ar.h: 1189
class struct_ARQualifierStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 1041
class struct_ARStatHistoryValue(Structure):
    pass

struct_ARStatHistoryValue.__slots__ = [
    'enumVal',
    'userOrTime',
]
struct_ARStatHistoryValue._fields_ = [
    ('enumVal', ARULong32),
    ('userOrTime', c_uint),
]

ARStatHistoryValue = struct_ARStatHistoryValue # /opt/dockethead/include/ar.h: 1041

# /opt/dockethead/include/ar.h: 1057
class struct_ARQueryValueStruct(Structure):
    pass

struct_ARQueryValueStruct.__slots__ = [
    'schema',
    'server',
    'qualifier',
    'valueField',
    'multiMatchCode',
]
struct_ARQueryValueStruct._fields_ = [
    ('schema', ARNameType),
    ('server', c_char * (64 + 1)),
    ('qualifier', POINTER(struct_ARQualifierStruct)),
    ('valueField', ARInternalId),
    ('multiMatchCode', c_uint),
]

ARQueryValueStruct = struct_ARQueryValueStruct # /opt/dockethead/include/ar.h: 1057

# /opt/dockethead/include/ar.h: 1073
class struct_ARCurrencyPartStruct(Structure):
    pass

struct_ARCurrencyPartStruct.__slots__ = [
    'fieldId',
    'partTag',
    'currencyCode',
]
struct_ARCurrencyPartStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('partTag', c_uint),
    ('currencyCode', ARCurrencyCodeType),
]

ARCurrencyPartStruct = struct_ARCurrencyPartStruct # /opt/dockethead/include/ar.h: 1073

# /opt/dockethead/include/ar.h: 1146
class struct_ARArithOpStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 1119
class union_anon_3(Union):
    pass

union_anon_3.__slots__ = [
    'noval_',
    'fieldId',
    'value',
    'arithOp',
    'statHistory',
    'valueSet',
    'variable',
    'queryValue',
    'currencyField',
]
union_anon_3._fields_ = [
    ('noval_', c_size_t),
    ('fieldId', ARInternalId),
    ('value', ARValueStruct),
    ('arithOp', POINTER(struct_ARArithOpStruct)),
    ('statHistory', ARStatHistoryValue),
    ('valueSet', ARValueList),
    ('variable', c_uint),
    ('queryValue', POINTER(ARQueryValueStruct)),
    ('currencyField', POINTER(ARCurrencyPartStruct)),
]

# /opt/dockethead/include/ar.h: 1137
class struct_ARFieldValueOrArithStruct(Structure):
    pass

struct_ARFieldValueOrArithStruct.__slots__ = [
    'tag',
    'u',
]
struct_ARFieldValueOrArithStruct._fields_ = [
    ('tag', c_uint),
    ('u', union_anon_3),
]

ARFieldValueOrArithStruct = struct_ARFieldValueOrArithStruct # /opt/dockethead/include/ar.h: 1137

struct_ARArithOpStruct.__slots__ = [
    'operation',
    'operandLeft',
    'operandRight',
]
struct_ARArithOpStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARFieldValueOrArithStruct),
    ('operandRight', ARFieldValueOrArithStruct),
]

ARArithOpStruct = struct_ARArithOpStruct # /opt/dockethead/include/ar.h: 1152

# /opt/dockethead/include/ar.h: 1170
class struct_ARRelOpStruct(Structure):
    pass

struct_ARRelOpStruct.__slots__ = [
    'operation',
    'operandLeft',
    'operandRight',
]
struct_ARRelOpStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARFieldValueOrArithStruct),
    ('operandRight', ARFieldValueOrArithStruct),
]

ARRelOpStruct = struct_ARRelOpStruct # /opt/dockethead/include/ar.h: 1170

# /opt/dockethead/include/ar.h: 1183
class struct_ARAndOrStruct(Structure):
    pass

struct_ARAndOrStruct.__slots__ = [
    'operandLeft',
    'operandRight',
]
struct_ARAndOrStruct._fields_ = [
    ('operandLeft', POINTER(struct_ARQualifierStruct)),
    ('operandRight', POINTER(struct_ARQualifierStruct)),
]

ARAndOrStruct = struct_ARAndOrStruct # /opt/dockethead/include/ar.h: 1183

# /opt/dockethead/include/ar.h: 1192
class union_anon_4(Union):
    pass

union_anon_4.__slots__ = [
    'andor',
    '_not',
    'relOp',
    'fieldId',
]
union_anon_4._fields_ = [
    ('andor', ARAndOrStruct),
    ('_not', POINTER(struct_ARQualifierStruct)),
    ('relOp', POINTER(ARRelOpStruct)),
    ('fieldId', ARInternalId),
]

struct_ARQualifierStruct.__slots__ = [
    'operation',
    'u',
]
struct_ARQualifierStruct._fields_ = [
    ('operation', c_uint),
    ('u', union_anon_4),
]

ARQualifierStruct = struct_ARQualifierStruct # /opt/dockethead/include/ar.h: 1203

# /opt/dockethead/include/ar.h: 1211
class struct_ARQualifierList(Structure):
    pass

struct_ARQualifierList.__slots__ = [
    'numItems',
    'qualifierList',
]
struct_ARQualifierList._fields_ = [
    ('numItems', c_uint),
    ('qualifierList', POINTER(ARQualifierStruct)),
]

ARQualifierList = struct_ARQualifierList # /opt/dockethead/include/ar.h: 1211

# /opt/dockethead/include/ar.h: 1221
class struct_ARSortStruct(Structure):
    pass

struct_ARSortStruct.__slots__ = [
    'fieldId',
    'sortOrder',
]
struct_ARSortStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('sortOrder', c_uint),
]

ARSortStruct = struct_ARSortStruct # /opt/dockethead/include/ar.h: 1221

# /opt/dockethead/include/ar.h: 1229
class struct_ARSortList(Structure):
    pass

struct_ARSortList.__slots__ = [
    'numItems',
    'sortList',
]
struct_ARSortList._fields_ = [
    ('numItems', c_uint),
    ('sortList', POINTER(ARSortStruct)),
]

ARSortList = struct_ARSortList # /opt/dockethead/include/ar.h: 1229

# /opt/dockethead/include/ar.h: 1237
class struct_ARSortListList(Structure):
    pass

struct_ARSortListList.__slots__ = [
    'numItems',
    'sortListList',
]
struct_ARSortListList._fields_ = [
    ('numItems', c_uint),
    ('sortListList', POINTER(ARSortList)),
]

ARSortListList = struct_ARSortListList # /opt/dockethead/include/ar.h: 1237

# /opt/dockethead/include/ar.h: 1251
class struct_ARStatisticsResultStruct(Structure):
    pass

struct_ARStatisticsResultStruct.__slots__ = [
    'groupByValues',
    'result',
]
struct_ARStatisticsResultStruct._fields_ = [
    ('groupByValues', ARValueList),
    ('result', ARValueStruct),
]

ARStatisticsResultStruct = struct_ARStatisticsResultStruct # /opt/dockethead/include/ar.h: 1251

# /opt/dockethead/include/ar.h: 1259
class struct_ARStatisticsResultList(Structure):
    pass

struct_ARStatisticsResultList.__slots__ = [
    'numItems',
    'resultList',
]
struct_ARStatisticsResultList._fields_ = [
    ('numItems', c_uint),
    ('resultList', POINTER(ARStatisticsResultStruct)),
]

ARStatisticsResultList = struct_ARStatisticsResultList # /opt/dockethead/include/ar.h: 1259

# /opt/dockethead/include/ar.h: 1270
class struct_ARIndexStruct(Structure):
    pass

struct_ARIndexStruct.__slots__ = [
    'numFields',
    'fieldIds',
    'unique',
    'indexName',
    'dataMappingUsageCnt',
]
struct_ARIndexStruct._fields_ = [
    ('numFields', c_uint),
    ('fieldIds', ARInternalId * 16),
    ('unique', ARBoolean),
    ('indexName', ARNameType),
    ('dataMappingUsageCnt', c_uint),
]

ARIndexStruct = struct_ARIndexStruct # /opt/dockethead/include/ar.h: 1270

# /opt/dockethead/include/ar.h: 1278
class struct_ARIndexList(Structure):
    pass

struct_ARIndexList.__slots__ = [
    'numItems',
    'indexList',
]
struct_ARIndexList._fields_ = [
    ('numItems', c_uint),
    ('indexList', POINTER(ARIndexStruct)),
]

ARIndexList = struct_ARIndexList # /opt/dockethead/include/ar.h: 1278

# /opt/dockethead/include/ar.h: 1286
class struct_ARIndexListList(Structure):
    pass

struct_ARIndexListList.__slots__ = [
    'numItems',
    'indexListList',
]
struct_ARIndexListList._fields_ = [
    ('numItems', c_uint),
    ('indexListList', POINTER(ARIndexList)),
]

ARIndexListList = struct_ARIndexListList # /opt/dockethead/include/ar.h: 1286

# /opt/dockethead/include/ar.h: 1301
class struct_ARDayStruct(Structure):
    pass

struct_ARDayStruct.__slots__ = [
    'monthday',
    'weekday',
    'hourmask',
    'minute',
]
struct_ARDayStruct._fields_ = [
    ('monthday', ARLong32),
    ('weekday', ARLong32),
    ('hourmask', ARLong32),
    ('minute', c_uint),
]

ARDayStruct = struct_ARDayStruct # /opt/dockethead/include/ar.h: 1301

# /opt/dockethead/include/ar.h: 1308
class union_anon_5(Union):
    pass

union_anon_5.__slots__ = [
    'formName',
    'dirPath',
]
union_anon_5._fields_ = [
    ('formName', ARNameType),
    ('dirPath', String),
]

# /opt/dockethead/include/ar.h: 1317
class struct_ARArchiveInfoStruct(Structure):
    pass

struct_ARArchiveInfoStruct.__slots__ = [
    'enable',
    'archiveType',
    'u',
    'archiveTime',
    'query',
    'archiveFrom',
]
struct_ARArchiveInfoStruct._fields_ = [
    ('enable', c_uint),
    ('archiveType', c_uint),
    ('u', union_anon_5),
    ('archiveTime', ARDayStruct),
    ('query', ARQualifierStruct),
    ('archiveFrom', ARNameType),
]

ARArchiveInfoStruct = struct_ARArchiveInfoStruct # /opt/dockethead/include/ar.h: 1317

# /opt/dockethead/include/ar.h: 1325
class struct_ARArchiveInfoList(Structure):
    pass

struct_ARArchiveInfoList.__slots__ = [
    'numItems',
    'archiveInfoList',
]
struct_ARArchiveInfoList._fields_ = [
    ('numItems', c_uint),
    ('archiveInfoList', POINTER(ARArchiveInfoStruct)),
]

ARArchiveInfoList = struct_ARArchiveInfoList # /opt/dockethead/include/ar.h: 1325

# /opt/dockethead/include/ar.h: 1343
class struct_ARAuditInfoStruct(Structure):
    pass

struct_ARAuditInfoStruct.__slots__ = [
    'enable',
    'style',
    'formName',
    'query',
    'auditMask',
]
struct_ARAuditInfoStruct._fields_ = [
    ('enable', c_uint),
    ('style', c_uint),
    ('formName', ARNameType),
    ('query', ARQualifierStruct),
    ('auditMask', c_uint),
]

ARAuditInfoStruct = struct_ARAuditInfoStruct # /opt/dockethead/include/ar.h: 1343

# /opt/dockethead/include/ar.h: 1349
class struct_ARAuditInfoList(Structure):
    pass

struct_ARAuditInfoList.__slots__ = [
    'numItems',
    'auditInfoList',
]
struct_ARAuditInfoList._fields_ = [
    ('numItems', c_uint),
    ('auditInfoList', POINTER(ARAuditInfoStruct)),
]

ARAuditInfoList = struct_ARAuditInfoList # /opt/dockethead/include/ar.h: 1349

# /opt/dockethead/include/ar.h: 1393
class struct_ARPropStruct(Structure):
    pass

struct_ARPropStruct.__slots__ = [
    'prop',
    'value',
]
struct_ARPropStruct._fields_ = [
    ('prop', ARULong32),
    ('value', ARValueStruct),
]

ARPropStruct = struct_ARPropStruct # /opt/dockethead/include/ar.h: 1393

# /opt/dockethead/include/ar.h: 1401
class struct_ARPropList(Structure):
    pass

struct_ARPropList.__slots__ = [
    'numItems',
    'props',
]
struct_ARPropList._fields_ = [
    ('numItems', c_uint),
    ('props', POINTER(ARPropStruct)),
]

ARPropList = struct_ARPropList # /opt/dockethead/include/ar.h: 1401

# /opt/dockethead/include/ar.h: 1409
class struct_ARPropListList(Structure):
    pass

struct_ARPropListList.__slots__ = [
    'numItems',
    'propsList',
]
struct_ARPropListList._fields_ = [
    ('numItems', c_uint),
    ('propsList', POINTER(ARPropList)),
]

ARPropListList = struct_ARPropListList # /opt/dockethead/include/ar.h: 1409

# /opt/dockethead/include/ar.h: 1417
class struct_ARDisplayInstanceStruct(Structure):
    pass

struct_ARDisplayInstanceStruct.__slots__ = [
    'vui',
    'props',
]
struct_ARDisplayInstanceStruct._fields_ = [
    ('vui', ARInternalId),
    ('props', ARPropList),
]

ARDisplayInstanceStruct = struct_ARDisplayInstanceStruct # /opt/dockethead/include/ar.h: 1417

# /opt/dockethead/include/ar.h: 1428
class struct_ARDisplayInstanceList(Structure):
    pass

struct_ARDisplayInstanceList.__slots__ = [
    'commonProps',
    'numItems',
    'dInstanceList',
]
struct_ARDisplayInstanceList._fields_ = [
    ('commonProps', ARPropList),
    ('numItems', c_uint),
    ('dInstanceList', POINTER(ARDisplayInstanceStruct)),
]

ARDisplayInstanceList = struct_ARDisplayInstanceList # /opt/dockethead/include/ar.h: 1428

# /opt/dockethead/include/ar.h: 1436
class struct_ARDisplayInstanceListList(Structure):
    pass

struct_ARDisplayInstanceListList.__slots__ = [
    'numItems',
    'dInstanceList',
]
struct_ARDisplayInstanceListList._fields_ = [
    ('numItems', c_uint),
    ('dInstanceList', POINTER(ARDisplayInstanceList)),
]

ARDisplayInstanceListList = struct_ARDisplayInstanceListList # /opt/dockethead/include/ar.h: 1436

# /opt/dockethead/include/ar.h: 1444
class struct_ARDisplayInstanceListPtrList(Structure):
    pass

struct_ARDisplayInstanceListPtrList.__slots__ = [
    'numItems',
    'dInstanceListPtrList',
]
struct_ARDisplayInstanceListPtrList._fields_ = [
    ('numItems', c_uint),
    ('dInstanceListPtrList', POINTER(POINTER(ARDisplayInstanceList))),
]

ARDisplayInstanceListPtrList = struct_ARDisplayInstanceListPtrList # /opt/dockethead/include/ar.h: 1444

# /opt/dockethead/include/ar.h: 2785
class union_anon_6(Union):
    pass

union_anon_6.__slots__ = [
    'noval_',
    'fieldId',
    'statHistory',
    'currencyField',
]
union_anon_6._fields_ = [
    ('noval_', c_size_t),
    ('fieldId', ARInternalId),
    ('statHistory', ARStatHistoryValue),
    ('currencyField', POINTER(ARCurrencyPartStruct)),
]

# /opt/dockethead/include/ar.h: 2795
class struct_ARAssignFieldStruct(Structure):
    pass

struct_ARAssignFieldStruct.__slots__ = [
    'server',
    'schema',
    'qualifier',
    'tag',
    'u',
    'noMatchOption',
    'multiMatchOption',
]
struct_ARAssignFieldStruct._fields_ = [
    ('server', c_char * (64 + 1)),
    ('schema', ARNameType),
    ('qualifier', ARQualifierStruct),
    ('tag', c_uint),
    ('u', union_anon_6),
    ('noMatchOption', c_uint),
    ('multiMatchOption', c_uint),
]

ARAssignFieldStruct = struct_ARAssignFieldStruct # /opt/dockethead/include/ar.h: 2795

# /opt/dockethead/include/ar.h: 2810
class struct_ARDDEStruct(Structure):
    pass

struct_ARDDEStruct.__slots__ = [
    'serviceName',
    'topic',
    'item',
    'action',
    'pathToProgram',
    'command',
]
struct_ARDDEStruct._fields_ = [
    ('serviceName', String),
    ('topic', String),
    ('item', String),
    ('action', c_uint),
    ('pathToProgram', String),
    ('command', String),
]

ARDDEStruct = struct_ARDDEStruct # /opt/dockethead/include/ar.h: 2810

# /opt/dockethead/include/ar.h: 2820
class struct_ARAssignSQLStruct(Structure):
    pass

struct_ARAssignSQLStruct.__slots__ = [
    'server',
    'sqlCommand',
    'valueIndex',
    'noMatchOption',
    'multiMatchOption',
]
struct_ARAssignSQLStruct._fields_ = [
    ('server', c_char * (64 + 1)),
    ('sqlCommand', String),
    ('valueIndex', c_uint),
    ('noMatchOption', c_uint),
    ('multiMatchOption', c_uint),
]

ARAssignSQLStruct = struct_ARAssignSQLStruct # /opt/dockethead/include/ar.h: 2820

# /opt/dockethead/include/ar.h: 2841
class union_anon_7(Union):
    pass

union_anon_7.__slots__ = [
    'fieldId',
    'value',
]
union_anon_7._fields_ = [
    ('fieldId', ARInternalId),
    ('value', ARValueStruct),
]

# /opt/dockethead/include/ar.h: 2847
class struct_ARCOMValueStruct(Structure):
    pass

struct_ARCOMValueStruct.__slots__ = [
    'valueIId',
    'transId',
    'noval_',
    'valueType',
    'u',
]
struct_ARCOMValueStruct._fields_ = [
    ('valueIId', String),
    ('transId', ARInternalId),
    ('noval_', ARULong32),
    ('valueType', c_uint),
    ('u', union_anon_7),
]

ARCOMValueStruct = struct_ARCOMValueStruct # /opt/dockethead/include/ar.h: 2847

# /opt/dockethead/include/ar.h: 2856
class struct_ARCOMMethodParmStruct(Structure):
    pass

struct_ARCOMMethodParmStruct.__slots__ = [
    'parmName',
    'parmType',
    'parmValue',
]
struct_ARCOMMethodParmStruct._fields_ = [
    ('parmName', String),
    ('parmType', c_uint),
    ('parmValue', ARCOMValueStruct),
]

ARCOMMethodParmStruct = struct_ARCOMMethodParmStruct # /opt/dockethead/include/ar.h: 2856

# /opt/dockethead/include/ar.h: 2864
class struct_ARCOMMethodParmList(Structure):
    pass

struct_ARCOMMethodParmList.__slots__ = [
    'numItems',
    'parameterList',
]
struct_ARCOMMethodParmList._fields_ = [
    ('numItems', c_uint),
    ('parameterList', POINTER(ARCOMMethodParmStruct)),
]

ARCOMMethodParmList = struct_ARCOMMethodParmList # /opt/dockethead/include/ar.h: 2864

# /opt/dockethead/include/ar.h: 2875
class struct_ARCOMMethodStruct(Structure):
    pass

struct_ARCOMMethodStruct.__slots__ = [
    'methodName',
    'methodIId',
    'methodType',
    'methodValue',
    'parameterList',
]
struct_ARCOMMethodStruct._fields_ = [
    ('methodName', String),
    ('methodIId', String),
    ('methodType', c_uint),
    ('methodValue', ARCOMValueStruct),
    ('parameterList', ARCOMMethodParmList),
]

ARCOMMethodStruct = struct_ARCOMMethodStruct # /opt/dockethead/include/ar.h: 2875

# /opt/dockethead/include/ar.h: 2883
class struct_ARCOMMethodList(Structure):
    pass

struct_ARCOMMethodList.__slots__ = [
    'numItems',
    'methodList',
]
struct_ARCOMMethodList._fields_ = [
    ('numItems', c_uint),
    ('methodList', POINTER(ARCOMMethodStruct)),
]

ARCOMMethodList = struct_ARCOMMethodList # /opt/dockethead/include/ar.h: 2883

# /opt/dockethead/include/ar.h: 2894
class struct_ARAutomationStruct(Structure):
    pass

struct_ARAutomationStruct.__slots__ = [
    'autoServerName',
    'clsId',
    'action',
    'isVisible',
    'methodList',
]
struct_ARAutomationStruct._fields_ = [
    ('autoServerName', String),
    ('clsId', String),
    ('action', String),
    ('isVisible', ARBoolean),
    ('methodList', ARCOMMethodList),
]

ARAutomationStruct = struct_ARAutomationStruct # /opt/dockethead/include/ar.h: 2894

# /opt/dockethead/include/ar.h: 2955
class struct_ARArithOpAssignStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 3048
class struct_ARFunctionAssignStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 2928
class struct_ARAssignFilterApiStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 2912
class union_anon_8(Union):
    pass

union_anon_8.__slots__ = [
    'noval_',
    'value',
    'field',
    'process',
    'arithOp',
    'function',
    'dde',
    'sql',
    'filterApi',
]
union_anon_8._fields_ = [
    ('noval_', c_size_t),
    ('value', ARValueStruct),
    ('field', POINTER(ARAssignFieldStruct)),
    ('process', String),
    ('arithOp', POINTER(struct_ARArithOpAssignStruct)),
    ('function', POINTER(struct_ARFunctionAssignStruct)),
    ('dde', POINTER(ARDDEStruct)),
    ('sql', POINTER(ARAssignSQLStruct)),
    ('filterApi', POINTER(struct_ARAssignFilterApiStruct)),
]

# /opt/dockethead/include/ar.h: 2925
class struct_ARAssignStruct(Structure):
    pass

struct_ARAssignStruct.__slots__ = [
    'assignType',
    'u',
]
struct_ARAssignStruct._fields_ = [
    ('assignType', c_uint),
    ('u', union_anon_8),
]

ARAssignStruct = struct_ARAssignStruct # /opt/dockethead/include/ar.h: 2925

struct_ARAssignFilterApiStruct.__slots__ = [
    'serviceName',
    'numItems',
    'inputValues',
    'valueIndex',
]
struct_ARAssignFilterApiStruct._fields_ = [
    ('serviceName', ARNameType),
    ('numItems', c_uint),
    ('inputValues', POINTER(ARAssignStruct)),
    ('valueIndex', c_uint),
]

ARAssignFilterApiStruct = struct_ARAssignFilterApiStruct # /opt/dockethead/include/ar.h: 2936

# /opt/dockethead/include/ar.h: 2944
class struct_ARFieldAssignStruct(Structure):
    pass

struct_ARFieldAssignStruct.__slots__ = [
    'fieldId',
    'assignment',
]
struct_ARFieldAssignStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('assignment', ARAssignStruct),
]

ARFieldAssignStruct = struct_ARFieldAssignStruct # /opt/dockethead/include/ar.h: 2944

# /opt/dockethead/include/ar.h: 2952
class struct_ARFieldAssignList(Structure):
    pass

struct_ARFieldAssignList.__slots__ = [
    'numItems',
    'fieldAssignList',
]
struct_ARFieldAssignList._fields_ = [
    ('numItems', c_uint),
    ('fieldAssignList', POINTER(ARFieldAssignStruct)),
]

ARFieldAssignList = struct_ARFieldAssignList # /opt/dockethead/include/ar.h: 2952

struct_ARArithOpAssignStruct.__slots__ = [
    'operation',
    'operandLeft',
    'operandRight',
]
struct_ARArithOpAssignStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARAssignStruct),
    ('operandRight', ARAssignStruct),
]

ARArithOpAssignStruct = struct_ARArithOpAssignStruct # /opt/dockethead/include/ar.h: 2961

struct_ARFunctionAssignStruct.__slots__ = [
    'functionCode',
    'noval_',
    'numItems',
    'parameterList',
]
struct_ARFunctionAssignStruct._fields_ = [
    ('functionCode', c_uint),
    ('noval_', ARULong32),
    ('numItems', c_uint),
    ('parameterList', POINTER(ARAssignStruct)),
]

ARFunctionAssignStruct = struct_ARFunctionAssignStruct # /opt/dockethead/include/ar.h: 3055

# /opt/dockethead/include/ar.h: 3089
class struct_ARFilterActionNotifyAdvanced(Structure):
    pass

struct_ARFilterActionNotifyAdvanced.__slots__ = [
    '_from',
    'replyTo',
    'cc',
    'bcc',
    'organization',
    'mailboxName',
    'headerTemplate',
    'footerTemplate',
    'contentTemplate',
    'reserved1',
    'reserved2',
    'reserved3',
]
struct_ARFilterActionNotifyAdvanced._fields_ = [
    ('_from', String),
    ('replyTo', String),
    ('cc', String),
    ('bcc', String),
    ('organization', String),
    ('mailboxName', String),
    ('headerTemplate', String),
    ('footerTemplate', String),
    ('contentTemplate', String),
    ('reserved1', ARULong32),
    ('reserved2', ARULong32),
    ('reserved3', ARULong32),
]

ARFilterActionNotifyAdvanced = struct_ARFilterActionNotifyAdvanced # /opt/dockethead/include/ar.h: 3089

# /opt/dockethead/include/ar.h: 3120
class struct_ARFilterActionNotify(Structure):
    pass

struct_ARFilterActionNotify.__slots__ = [
    'user',
    'notifyText',
    'notifyPriority',
    'notifyMechanism',
    'notifyMechanismXRef',
    'subjectText',
    'fieldIdListType',
    'fieldIdList',
    'notifyBehavior',
    'notifyPermission',
    'notifyAdvanced',
]
struct_ARFilterActionNotify._fields_ = [
    ('user', String),
    ('notifyText', String),
    ('notifyPriority', c_uint),
    ('notifyMechanism', c_uint),
    ('notifyMechanismXRef', ARInternalId),
    ('subjectText', String),
    ('fieldIdListType', c_uint),
    ('fieldIdList', ARInternalIdList),
    ('notifyBehavior', c_uint),
    ('notifyPermission', c_uint),
    ('notifyAdvanced', POINTER(ARFilterActionNotifyAdvanced)),
]

ARFilterActionNotify = struct_ARFilterActionNotify # /opt/dockethead/include/ar.h: 3120

# /opt/dockethead/include/ar.h: 3129
class struct_ARFilterStatusStruct(Structure):
    pass

struct_ARFilterStatusStruct.__slots__ = [
    'messageType',
    'messageNum',
    'messageText',
]
struct_ARFilterStatusStruct._fields_ = [
    ('messageType', c_uint),
    ('messageNum', ARLong32),
    ('messageText', String),
]

ARFilterStatusStruct = struct_ARFilterStatusStruct # /opt/dockethead/include/ar.h: 3129

# /opt/dockethead/include/ar.h: 3137
class struct_ARPushFieldsStruct(Structure):
    pass

struct_ARPushFieldsStruct.__slots__ = [
    'field',
    'assign',
]
struct_ARPushFieldsStruct._fields_ = [
    ('field', ARAssignFieldStruct),
    ('assign', ARAssignStruct),
]

ARPushFieldsStruct = struct_ARPushFieldsStruct # /opt/dockethead/include/ar.h: 3137

# /opt/dockethead/include/ar.h: 3145
class struct_ARPushFieldsList(Structure):
    pass

struct_ARPushFieldsList.__slots__ = [
    'numItems',
    'pushFieldsList',
]
struct_ARPushFieldsList._fields_ = [
    ('numItems', c_uint),
    ('pushFieldsList', POINTER(ARPushFieldsStruct)),
]

ARPushFieldsList = struct_ARPushFieldsList # /opt/dockethead/include/ar.h: 3145

# /opt/dockethead/include/ar.h: 3154
class struct_ARPushFieldsActionStruct(Structure):
    pass

struct_ARPushFieldsActionStruct.__slots__ = [
    'pushFieldsList',
    'sampleServer',
    'sampleSchema',
]
struct_ARPushFieldsActionStruct._fields_ = [
    ('pushFieldsList', ARPushFieldsList),
    ('sampleServer', ARServerNameType),
    ('sampleSchema', ARNameType),
]

ARPushFieldsActionStruct = struct_ARPushFieldsActionStruct # /opt/dockethead/include/ar.h: 3154

# /opt/dockethead/include/ar.h: 3163
class struct_ARSetFieldsActionStruct(Structure):
    pass

struct_ARSetFieldsActionStruct.__slots__ = [
    'fieldList',
    'sampleServer',
    'sampleSchema',
]
struct_ARSetFieldsActionStruct._fields_ = [
    ('fieldList', ARFieldAssignList),
    ('sampleServer', ARServerNameType),
    ('sampleSchema', ARNameType),
]

ARSetFieldsActionStruct = struct_ARSetFieldsActionStruct # /opt/dockethead/include/ar.h: 3163

# /opt/dockethead/include/ar.h: 3170
class struct_ARSQLStruct(Structure):
    pass

struct_ARSQLStruct.__slots__ = [
    'server',
    'command',
]
struct_ARSQLStruct._fields_ = [
    ('server', c_char * (64 + 1)),
    ('command', String),
]

ARSQLStruct = struct_ARSQLStruct # /opt/dockethead/include/ar.h: 3170

# /opt/dockethead/include/ar.h: 3180
class struct_AROverlaidStruct(Structure):
    pass

struct_AROverlaidStruct.__slots__ = [
    'name',
    'objType',
    'schemaName',
    'id',
    'inheritMask',
    'extendMask',
]
struct_AROverlaidStruct._fields_ = [
    ('name', ARNameType),
    ('objType', c_uint),
    ('schemaName', ARNameType),
    ('id', ARInternalId),
    ('inheritMask', c_uint),
    ('extendMask', c_uint),
]

AROverlaidStruct = struct_AROverlaidStruct # /opt/dockethead/include/ar.h: 3180

# /opt/dockethead/include/ar.h: 3193
class struct_ARGotoActionStruct(Structure):
    pass

struct_ARGotoActionStruct.__slots__ = [
    'tag',
    'fieldIdOrValue',
]
struct_ARGotoActionStruct._fields_ = [
    ('tag', c_uint),
    ('fieldIdOrValue', ARULong32),
]

ARGotoActionStruct = struct_ARGotoActionStruct # /opt/dockethead/include/ar.h: 3193

# /opt/dockethead/include/ar.h: 3207
class struct_ARCallGuideStruct(Structure):
    pass

struct_ARCallGuideStruct.__slots__ = [
    'serverName',
    'guideName',
    'guideMode',
    'guideTableId',
    'inputValueFieldPairs',
    'outputValueFieldPairs',
    'sampleServer',
    'sampleGuide',
]
struct_ARCallGuideStruct._fields_ = [
    ('serverName', ARServerNameType),
    ('guideName', ARNameType),
    ('guideMode', c_int),
    ('guideTableId', ARInternalId),
    ('inputValueFieldPairs', ARFieldAssignList),
    ('outputValueFieldPairs', ARFieldAssignList),
    ('sampleServer', ARServerNameType),
    ('sampleGuide', ARNameType),
]

ARCallGuideStruct = struct_ARCallGuideStruct # /opt/dockethead/include/ar.h: 3207

# /opt/dockethead/include/ar.h: 3223
class struct_ARExitGuideStruct(Structure):
    pass

struct_ARExitGuideStruct.__slots__ = [
    'closeAll',
]
struct_ARExitGuideStruct._fields_ = [
    ('closeAll', ARBoolean),
]

ARExitGuideStruct = struct_ARExitGuideStruct # /opt/dockethead/include/ar.h: 3223

# /opt/dockethead/include/ar.h: 3229
class struct_ARGotoGuideLabelStruct(Structure):
    pass

struct_ARGotoGuideLabelStruct.__slots__ = [
    'label',
]
struct_ARGotoGuideLabelStruct._fields_ = [
    ('label', String),
]

ARGotoGuideLabelStruct = struct_ARGotoGuideLabelStruct # /opt/dockethead/include/ar.h: 3229

# /opt/dockethead/include/ar.h: 3240
class struct_ARSvcActionStruct(Structure):
    pass

struct_ARSvcActionStruct.__slots__ = [
    'serverName',
    'serviceSchema',
    'requestIdMap',
    'inputFieldMapping',
    'outputFieldMapping',
    'sampleServer',
    'sampleSchema',
]
struct_ARSvcActionStruct._fields_ = [
    ('serverName', ARServerNameType),
    ('serviceSchema', ARNameType),
    ('requestIdMap', ARInternalId),
    ('inputFieldMapping', ARFieldAssignList),
    ('outputFieldMapping', ARFieldAssignList),
    ('sampleServer', ARServerNameType),
    ('sampleSchema', ARNameType),
]

ARSvcActionStruct = struct_ARSvcActionStruct # /opt/dockethead/include/ar.h: 3240

# /opt/dockethead/include/ar.h: 3263
class union_anon_9(Union):
    pass

union_anon_9.__slots__ = [
    'notify',
    'message',
    'logFile',
    'setFields',
    'process',
    'pushFields',
    'sqlCommand',
    'gotoAction',
    'callGuide',
    'exitGuide',
    'gotoGuide',
    'serviceAction',
]
union_anon_9._fields_ = [
    ('notify', ARFilterActionNotify),
    ('message', ARFilterStatusStruct),
    ('logFile', String),
    ('setFields', ARSetFieldsActionStruct),
    ('process', String),
    ('pushFields', ARPushFieldsActionStruct),
    ('sqlCommand', ARSQLStruct),
    ('gotoAction', ARGotoActionStruct),
    ('callGuide', ARCallGuideStruct),
    ('exitGuide', ARExitGuideStruct),
    ('gotoGuide', ARGotoGuideLabelStruct),
    ('serviceAction', ARSvcActionStruct),
]

# /opt/dockethead/include/ar.h: 3279
class struct_ARFilterActionStruct(Structure):
    pass

struct_ARFilterActionStruct.__slots__ = [
    'action',
    'u',
]
struct_ARFilterActionStruct._fields_ = [
    ('action', c_uint),
    ('u', union_anon_9),
]

ARFilterActionStruct = struct_ARFilterActionStruct # /opt/dockethead/include/ar.h: 3279

# /opt/dockethead/include/ar.h: 3286
class struct_ARFilterActionList(Structure):
    pass

struct_ARFilterActionList.__slots__ = [
    'numItems',
    'actionList',
]
struct_ARFilterActionList._fields_ = [
    ('numItems', c_uint),
    ('actionList', POINTER(ARFilterActionStruct)),
]

ARFilterActionList = struct_ARFilterActionList # /opt/dockethead/include/ar.h: 3286

# /opt/dockethead/include/ar.h: 3294
class struct_ARFilterActionListList(Structure):
    pass

struct_ARFilterActionListList.__slots__ = [
    'numItems',
    'actionListList',
]
struct_ARFilterActionListList._fields_ = [
    ('numItems', c_uint),
    ('actionListList', POINTER(ARFilterActionList)),
]

ARFilterActionListList = struct_ARFilterActionListList # /opt/dockethead/include/ar.h: 3294

# /opt/dockethead/include/ar.h: 3348
class struct_ARMacroParmStruct(Structure):
    pass

struct_ARMacroParmStruct.__slots__ = [
    'name',
    'value',
]
struct_ARMacroParmStruct._fields_ = [
    ('name', ARNameType),
    ('value', String),
]

ARMacroParmStruct = struct_ARMacroParmStruct # /opt/dockethead/include/ar.h: 3348

# /opt/dockethead/include/ar.h: 3355
class struct_ARMacroParmList(Structure):
    pass

struct_ARMacroParmList.__slots__ = [
    'numItems',
    'parms',
]
struct_ARMacroParmList._fields_ = [
    ('numItems', c_uint),
    ('parms', POINTER(ARMacroParmStruct)),
]

ARMacroParmList = struct_ARMacroParmList # /opt/dockethead/include/ar.h: 3355

# /opt/dockethead/include/ar.h: 3363
class struct_ARActiveLinkMacroStruct(Structure):
    pass

struct_ARActiveLinkMacroStruct.__slots__ = [
    'macroName',
    'macroText',
    'macroParms',
]
struct_ARActiveLinkMacroStruct._fields_ = [
    ('macroName', ARNameType),
    ('macroText', String),
    ('macroParms', ARMacroParmList),
]

ARActiveLinkMacroStruct = struct_ARActiveLinkMacroStruct # /opt/dockethead/include/ar.h: 3363

ARActiveLinkSvcActionStruct = ARSvcActionStruct # /opt/dockethead/include/ar.h: 3365

# /opt/dockethead/include/ar.h: 3387
class struct_ARFieldCharacteristics(Structure):
    pass

struct_ARFieldCharacteristics.__slots__ = [
    'option',
    'fieldId',
    'charMenu',
    'props',
    'focus',
    'accessOption',
]
struct_ARFieldCharacteristics._fields_ = [
    ('option', c_uint),
    ('fieldId', ARInternalId),
    ('charMenu', String),
    ('props', ARPropList),
    ('focus', c_uint),
    ('accessOption', c_uint),
]

ARFieldCharacteristics = struct_ARFieldCharacteristics # /opt/dockethead/include/ar.h: 3387

# /opt/dockethead/include/ar.h: 3406
class struct_AROpenDlgStruct(Structure):
    pass

struct_AROpenDlgStruct.__slots__ = [
    'serverName',
    'schemaName',
    'vuiLabel',
    'closeBox',
    'inputValueFieldPairs',
    'outputValueFieldPairs',
    'windowMode',
    'targetLocation',
    'query',
    'noMatchContinue',
    'suppressEmptyLst',
    'msg',
    'pollinginterval',
    'reportString',
    'sortOrderList',
]
struct_AROpenDlgStruct._fields_ = [
    ('serverName', ARServerNameType),
    ('schemaName', ARNameType),
    ('vuiLabel', ARNameType),
    ('closeBox', ARBoolean),
    ('inputValueFieldPairs', ARFieldAssignList),
    ('outputValueFieldPairs', ARFieldAssignList),
    ('windowMode', c_int),
    ('targetLocation', String),
    ('query', ARQualifierStruct),
    ('noMatchContinue', ARBoolean),
    ('suppressEmptyLst', ARBoolean),
    ('msg', ARMessageStruct),
    ('pollinginterval', ARULong32),
    ('reportString', String),
    ('sortOrderList', ARSortList),
]

AROpenDlgStruct = struct_AROpenDlgStruct # /opt/dockethead/include/ar.h: 3406

# /opt/dockethead/include/ar.h: 3412
class struct_ARCommitChangesStruct(Structure):
    pass

struct_ARCommitChangesStruct.__slots__ = [
    'schemaName',
]
struct_ARCommitChangesStruct._fields_ = [
    ('schemaName', ARNameType),
]

ARCommitChangesStruct = struct_ARCommitChangesStruct # /opt/dockethead/include/ar.h: 3412

# /opt/dockethead/include/ar.h: 3418
class struct_ARCloseWndStruct(Structure):
    pass

struct_ARCloseWndStruct.__slots__ = [
    'closeAll',
]
struct_ARCloseWndStruct._fields_ = [
    ('closeAll', ARBoolean),
]

ARCloseWndStruct = struct_ARCloseWndStruct # /opt/dockethead/include/ar.h: 3418

# /opt/dockethead/include/ar.h: 3424
class struct_ARWaitStruct(Structure):
    pass

struct_ARWaitStruct.__slots__ = [
    'continueButtonTitle',
]
struct_ARWaitStruct._fields_ = [
    ('continueButtonTitle', String),
]

ARWaitStruct = struct_ARWaitStruct # /opt/dockethead/include/ar.h: 3424

# /opt/dockethead/include/ar.h: 3517
class union_anon_10(Union):
    pass

union_anon_10.__slots__ = [
    'macro',
    'setFields',
    'process',
    'message',
    'characteristics',
    'dde',
    'pushFields',
    'sqlCommand',
    'automation',
    'openDlg',
    'commitChanges',
    'closeWnd',
    'callGuide',
    'exitGuide',
    'gotoGuide',
    'waitAction',
    'gotoAction',
    'service',
]
union_anon_10._fields_ = [
    ('macro', ARActiveLinkMacroStruct),
    ('setFields', ARSetFieldsActionStruct),
    ('process', String),
    ('message', ARMessageStruct),
    ('characteristics', ARFieldCharacteristics),
    ('dde', ARDDEStruct),
    ('pushFields', ARPushFieldsActionStruct),
    ('sqlCommand', ARSQLStruct),
    ('automation', ARAutomationStruct),
    ('openDlg', AROpenDlgStruct),
    ('commitChanges', ARCommitChangesStruct),
    ('closeWnd', ARCloseWndStruct),
    ('callGuide', ARCallGuideStruct),
    ('exitGuide', ARExitGuideStruct),
    ('gotoGuide', ARGotoGuideLabelStruct),
    ('waitAction', ARWaitStruct),
    ('gotoAction', ARGotoActionStruct),
    ('service', ARActiveLinkSvcActionStruct),
]

# /opt/dockethead/include/ar.h: 3539
class struct_ARActiveLinkActionStruct(Structure):
    pass

struct_ARActiveLinkActionStruct.__slots__ = [
    'action',
    'u',
]
struct_ARActiveLinkActionStruct._fields_ = [
    ('action', c_uint),
    ('u', union_anon_10),
]

ARActiveLinkActionStruct = struct_ARActiveLinkActionStruct # /opt/dockethead/include/ar.h: 3539

# /opt/dockethead/include/ar.h: 3546
class struct_ARActiveLinkActionList(Structure):
    pass

struct_ARActiveLinkActionList.__slots__ = [
    'numItems',
    'actionList',
]
struct_ARActiveLinkActionList._fields_ = [
    ('numItems', c_uint),
    ('actionList', POINTER(ARActiveLinkActionStruct)),
]

ARActiveLinkActionList = struct_ARActiveLinkActionList # /opt/dockethead/include/ar.h: 3546

# /opt/dockethead/include/ar.h: 3554
class struct_ARActiveLinkActionListList(Structure):
    pass

struct_ARActiveLinkActionListList.__slots__ = [
    'numItems',
    'actionListList',
]
struct_ARActiveLinkActionListList._fields_ = [
    ('numItems', c_uint),
    ('actionListList', POINTER(ARActiveLinkActionList)),
]

ARActiveLinkActionListList = struct_ARActiveLinkActionListList # /opt/dockethead/include/ar.h: 3554

# /opt/dockethead/include/ar.h: 3569
class struct_ARPermissionStruct(Structure):
    pass

struct_ARPermissionStruct.__slots__ = [
    'groupId',
    'permissions',
]
struct_ARPermissionStruct._fields_ = [
    ('groupId', ARInternalId),
    ('permissions', c_uint),
]

ARPermissionStruct = struct_ARPermissionStruct # /opt/dockethead/include/ar.h: 3569

# /opt/dockethead/include/ar.h: 3576
class struct_ARPermissionList(Structure):
    pass

struct_ARPermissionList.__slots__ = [
    'numItems',
    'permissionList',
]
struct_ARPermissionList._fields_ = [
    ('numItems', c_uint),
    ('permissionList', POINTER(ARPermissionStruct)),
]

ARPermissionList = struct_ARPermissionList # /opt/dockethead/include/ar.h: 3576

# /opt/dockethead/include/ar.h: 3583
class struct_ARPermissionListList(Structure):
    pass

struct_ARPermissionListList.__slots__ = [
    'numItems',
    'permissionList',
]
struct_ARPermissionListList._fields_ = [
    ('numItems', c_uint),
    ('permissionList', POINTER(ARPermissionList)),
]

ARPermissionListList = struct_ARPermissionListList # /opt/dockethead/include/ar.h: 3583

# /opt/dockethead/include/ar.h: 3590
class struct_ARPermissionListPtrList(Structure):
    pass

struct_ARPermissionListPtrList.__slots__ = [
    'numItems',
    'permissionListPtrList',
]
struct_ARPermissionListPtrList._fields_ = [
    ('numItems', c_uint),
    ('permissionListPtrList', POINTER(POINTER(ARPermissionList))),
]

ARPermissionListPtrList = struct_ARPermissionListPtrList # /opt/dockethead/include/ar.h: 3590

# /opt/dockethead/include/ar.h: 3612
class struct_ARGroupInfoStruct(Structure):
    pass

struct_ARGroupInfoStruct.__slots__ = [
    'groupId',
    'groupType',
    'groupName',
    'groupCategory',
    'groupParent',
    'groupOverlay',
]
struct_ARGroupInfoStruct._fields_ = [
    ('groupId', ARInternalId),
    ('groupType', c_uint),
    ('groupName', ARAccessNameList),
    ('groupCategory', c_uint),
    ('groupParent', ARInternalId),
    ('groupOverlay', c_uint),
]

ARGroupInfoStruct = struct_ARGroupInfoStruct # /opt/dockethead/include/ar.h: 3612

# /opt/dockethead/include/ar.h: 3619
class struct_ARGroupInfoList(Structure):
    pass

struct_ARGroupInfoList.__slots__ = [
    'numItems',
    'groupList',
]
struct_ARGroupInfoList._fields_ = [
    ('numItems', c_uint),
    ('groupList', POINTER(ARGroupInfoStruct)),
]

ARGroupInfoList = struct_ARGroupInfoList # /opt/dockethead/include/ar.h: 3619

# /opt/dockethead/include/ar.h: 3628
class struct_ARRoleInfoStruct(Structure):
    pass

struct_ARRoleInfoStruct.__slots__ = [
    'roleId',
    'roleName',
    'roleType',
]
struct_ARRoleInfoStruct._fields_ = [
    ('roleId', c_int),
    ('roleName', ARNameType),
    ('roleType', c_int),
]

ARRoleInfoStruct = struct_ARRoleInfoStruct # /opt/dockethead/include/ar.h: 3628

# /opt/dockethead/include/ar.h: 3636
class struct_ARRoleInfoList(Structure):
    pass

struct_ARRoleInfoList.__slots__ = [
    'numItems',
    'roleList',
]
struct_ARRoleInfoList._fields_ = [
    ('numItems', c_uint),
    ('roleList', POINTER(ARRoleInfoStruct)),
]

ARRoleInfoList = struct_ARRoleInfoList # /opt/dockethead/include/ar.h: 3636

# /opt/dockethead/include/ar.h: 3655
class struct_ARUserLicenseStruct(Structure):
    pass

struct_ARUserLicenseStruct.__slots__ = [
    'licenseTag',
    'licenseType',
    'currentLicenseType',
    'licensePool',
    'appLicenseDescriptor',
    'lastAccess',
]
struct_ARUserLicenseStruct._fields_ = [
    ('licenseTag', c_uint),
    ('licenseType', c_uint),
    ('currentLicenseType', c_uint),
    ('licensePool', ARInternalId),
    ('appLicenseDescriptor', ARLicenseNameType),
    ('lastAccess', ARTimestamp),
]

ARUserLicenseStruct = struct_ARUserLicenseStruct # /opt/dockethead/include/ar.h: 3655

# /opt/dockethead/include/ar.h: 3663
class struct_ARUserLicenseList(Structure):
    pass

struct_ARUserLicenseList.__slots__ = [
    'numItems',
    'licenseList',
]
struct_ARUserLicenseList._fields_ = [
    ('numItems', c_uint),
    ('licenseList', POINTER(ARUserLicenseStruct)),
]

ARUserLicenseList = struct_ARUserLicenseList # /opt/dockethead/include/ar.h: 3663

ARAppLicensePoolStruct = ARUserLicenseStruct # /opt/dockethead/include/ar.h: 3665

# /opt/dockethead/include/ar.h: 3671
class struct_ARAppLicensePoolList(Structure):
    pass

struct_ARAppLicensePoolList.__slots__ = [
    'numItems',
    'appLicenseList',
]
struct_ARAppLicensePoolList._fields_ = [
    ('numItems', c_uint),
    ('appLicenseList', POINTER(ARAppLicensePoolStruct)),
]

ARAppLicensePoolList = struct_ARAppLicensePoolList # /opt/dockethead/include/ar.h: 3671

# /opt/dockethead/include/ar.h: 3678
class struct_ARLicenseNameList(Structure):
    pass

struct_ARLicenseNameList.__slots__ = [
    'numItems',
    'nameList',
]
struct_ARLicenseNameList._fields_ = [
    ('numItems', c_uint),
    ('nameList', POINTER(ARLicenseNameType)),
]

ARLicenseNameList = struct_ARLicenseNameList # /opt/dockethead/include/ar.h: 3678

# /opt/dockethead/include/ar.h: 3687
class struct_ARLicenseDateStruct(Structure):
    pass

struct_ARLicenseDateStruct.__slots__ = [
    'month',
    'day',
    'year',
]
struct_ARLicenseDateStruct._fields_ = [
    ('month', c_int),
    ('day', c_int),
    ('year', c_int),
]

ARLicenseDateStruct = struct_ARLicenseDateStruct # /opt/dockethead/include/ar.h: 3687

# /opt/dockethead/include/ar.h: 3703
class struct_ARLicenseInfoStruct(Structure):
    pass

struct_ARLicenseInfoStruct.__slots__ = [
    'licKey',
    'licType',
    'licSubtype',
    'issuedDate',
    'expireDate',
    'siteName',
    'hostId',
    'numLicenses',
    'tokenList',
    'comment',
]
struct_ARLicenseInfoStruct._fields_ = [
    ('licKey', ARLicenseKeyType),
    ('licType', ARLicenseNameType),
    ('licSubtype', ARLicenseNameType),
    ('issuedDate', ARLicenseDateStruct),
    ('expireDate', ARLicenseDateStruct),
    ('siteName', String),
    ('hostId', String),
    ('numLicenses', c_int),
    ('tokenList', String),
    ('comment', String),
]

ARLicenseInfoStruct = struct_ARLicenseInfoStruct # /opt/dockethead/include/ar.h: 3703

# /opt/dockethead/include/ar.h: 3711
class struct_ARLicenseInfoList(Structure):
    pass

struct_ARLicenseInfoList.__slots__ = [
    'numItems',
    'licenseInfoList',
]
struct_ARLicenseInfoList._fields_ = [
    ('numItems', c_uint),
    ('licenseInfoList', POINTER(ARLicenseInfoStruct)),
]

ARLicenseInfoList = struct_ARLicenseInfoList # /opt/dockethead/include/ar.h: 3711

# /opt/dockethead/include/ar.h: 3721
class struct_ARLicenseValidStruct(Structure):
    pass

struct_ARLicenseValidStruct.__slots__ = [
    'numLicenses',
    'isDemo',
    'expireDate',
    'tokenList',
]
struct_ARLicenseValidStruct._fields_ = [
    ('numLicenses', c_int),
    ('isDemo', ARBoolean),
    ('expireDate', ARLicenseDateStruct),
    ('tokenList', String),
]

ARLicenseValidStruct = struct_ARLicenseValidStruct # /opt/dockethead/include/ar.h: 3721

# /opt/dockethead/include/ar.h: 3729
class struct_ARLicenseValidList(Structure):
    pass

struct_ARLicenseValidList.__slots__ = [
    'numItems',
    'licenseValidateInfoList',
]
struct_ARLicenseValidList._fields_ = [
    ('numItems', c_uint),
    ('licenseValidateInfoList', POINTER(ARLicenseValidStruct)),
]

ARLicenseValidList = struct_ARLicenseValidList # /opt/dockethead/include/ar.h: 3729

# /opt/dockethead/include/ar.h: 3737
class struct_ARHostIDTypeList(Structure):
    pass

struct_ARHostIDTypeList.__slots__ = [
    'numItems',
    'idList',
]
struct_ARHostIDTypeList._fields_ = [
    ('numItems', c_uint),
    ('idList', POINTER(ARHostIDType)),
]

ARHostIDTypeList = struct_ARHostIDTypeList # /opt/dockethead/include/ar.h: 3737

# /opt/dockethead/include/ar.h: 3754
class struct_ARUserInfoStruct(Structure):
    pass

struct_ARUserInfoStruct.__slots__ = [
    'userName',
    'licenseInfo',
    'connectTime',
    'lastAccess',
    'defaultNotifyMech',
    'emailAddr',
]
struct_ARUserInfoStruct._fields_ = [
    ('userName', ARAccessNameType),
    ('licenseInfo', ARUserLicenseList),
    ('connectTime', ARTimestamp),
    ('lastAccess', ARTimestamp),
    ('defaultNotifyMech', c_uint),
    ('emailAddr', String),
]

ARUserInfoStruct = struct_ARUserInfoStruct # /opt/dockethead/include/ar.h: 3754

# /opt/dockethead/include/ar.h: 3761
class struct_ARUserInfoList(Structure):
    pass

struct_ARUserInfoList.__slots__ = [
    'numItems',
    'userList',
]
struct_ARUserInfoList._fields_ = [
    ('numItems', c_uint),
    ('userList', POINTER(ARUserInfoStruct)),
]

ARUserInfoList = struct_ARUserInfoList # /opt/dockethead/include/ar.h: 3761

# /opt/dockethead/include/ar.h: 3770
class struct_ARWorkflowLockStruct(Structure):
    pass

struct_ARWorkflowLockStruct.__slots__ = [
    'lockType',
    'lockKey',
]
struct_ARWorkflowLockStruct._fields_ = [
    ('lockType', c_int),
    ('lockKey', ARPasswordType),
]

ARWorkflowLockStruct = struct_ARWorkflowLockStruct # /opt/dockethead/include/ar.h: 3770

# /opt/dockethead/include/ar.h: 3785
class struct_ARIntegerLimitsStruct(Structure):
    pass

struct_ARIntegerLimitsStruct.__slots__ = [
    'rangeLow',
    'rangeHigh',
]
struct_ARIntegerLimitsStruct._fields_ = [
    ('rangeLow', ARLong32),
    ('rangeHigh', ARLong32),
]

ARIntegerLimitsStruct = struct_ARIntegerLimitsStruct # /opt/dockethead/include/ar.h: 3785

# /opt/dockethead/include/ar.h: 3795
class struct_ARRealLimitsStruct(Structure):
    pass

struct_ARRealLimitsStruct.__slots__ = [
    'rangeLow',
    'rangeHigh',
    'precision',
]
struct_ARRealLimitsStruct._fields_ = [
    ('rangeLow', c_double),
    ('rangeHigh', c_double),
    ('precision', c_int),
]

ARRealLimitsStruct = struct_ARRealLimitsStruct # /opt/dockethead/include/ar.h: 3795

# /opt/dockethead/include/ar.h: 3837
class struct_ARCharLimitsStruct(Structure):
    pass

struct_ARCharLimitsStruct.__slots__ = [
    'maxLength',
    'menuStyle',
    'qbeMatchOperation',
    'charMenu',
    'pattern',
    'fullTextOptions',
    'lengthUnits',
    'storageOptionForCLOB',
]
struct_ARCharLimitsStruct._fields_ = [
    ('maxLength', c_uint),
    ('menuStyle', c_uint),
    ('qbeMatchOperation', c_uint),
    ('charMenu', ARNameType),
    ('pattern', String),
    ('fullTextOptions', c_uint),
    ('lengthUnits', c_uint),
    ('storageOptionForCLOB', c_uint),
]

ARCharLimitsStruct = struct_ARCharLimitsStruct # /opt/dockethead/include/ar.h: 3837

# /opt/dockethead/include/ar.h: 3843
class struct_ARDiaryLimitsStruct(Structure):
    pass

struct_ARDiaryLimitsStruct.__slots__ = [
    'fullTextOptions',
]
struct_ARDiaryLimitsStruct._fields_ = [
    ('fullTextOptions', c_uint),
]

ARDiaryLimitsStruct = struct_ARDiaryLimitsStruct # /opt/dockethead/include/ar.h: 3843

# /opt/dockethead/include/ar.h: 3854
class struct_AREnumItemStruct(Structure):
    pass

struct_AREnumItemStruct.__slots__ = [
    'itemName',
    'itemNumber',
]
struct_AREnumItemStruct._fields_ = [
    ('itemName', ARNameType),
    ('itemNumber', ARULong32),
]

AREnumItemStruct = struct_AREnumItemStruct # /opt/dockethead/include/ar.h: 3854

# /opt/dockethead/include/ar.h: 3861
class struct_AREnumItemList(Structure):
    pass

struct_AREnumItemList.__slots__ = [
    'numItems',
    'enumItemList',
]
struct_AREnumItemList._fields_ = [
    ('numItems', c_uint),
    ('enumItemList', POINTER(AREnumItemStruct)),
]

AREnumItemList = struct_AREnumItemList # /opt/dockethead/include/ar.h: 3861

# /opt/dockethead/include/ar.h: 3871
class struct_AREnumQueryStruct(Structure):
    pass

struct_AREnumQueryStruct.__slots__ = [
    'schema',
    'server',
    'qualifier',
    'nameField',
    'numberField',
]
struct_AREnumQueryStruct._fields_ = [
    ('schema', ARNameType),
    ('server', c_char * (64 + 1)),
    ('qualifier', ARQualifierStruct),
    ('nameField', ARInternalId),
    ('numberField', ARInternalId),
]

AREnumQueryStruct = struct_AREnumQueryStruct # /opt/dockethead/include/ar.h: 3871

# /opt/dockethead/include/ar.h: 3876
class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    'regularList',
    'customList',
    'queryList',
]
union_anon_11._fields_ = [
    ('regularList', ARNameList),
    ('customList', AREnumItemList),
    ('queryList', AREnumQueryStruct),
]

# /opt/dockethead/include/ar.h: 3883
class struct_AREnumLimitsStruct(Structure):
    pass

struct_AREnumLimitsStruct.__slots__ = [
    'listStyle',
    'u',
]
struct_AREnumLimitsStruct._fields_ = [
    ('listStyle', c_uint),
    ('u', union_anon_11),
]

AREnumLimitsStruct = struct_AREnumLimitsStruct # /opt/dockethead/include/ar.h: 3883

# /opt/dockethead/include/ar.h: 3894
class struct_ARAttachLimitsStruct(Structure):
    pass

struct_ARAttachLimitsStruct.__slots__ = [
    'maxSize',
    'attachType',
    'fullTextOptions',
]
struct_ARAttachLimitsStruct._fields_ = [
    ('maxSize', ARULong32),
    ('attachType', c_uint),
    ('fullTextOptions', c_uint),
]

ARAttachLimitsStruct = struct_ARAttachLimitsStruct # /opt/dockethead/include/ar.h: 3894

# /opt/dockethead/include/ar.h: 3911
class struct_ARTableLimitsStruct(Structure):
    pass

struct_ARTableLimitsStruct.__slots__ = [
    'numColumns',
    'qualifier',
    'maxRetrieve',
    'schema',
    'server',
    'sampleSchema',
    'sampleServer',
]
struct_ARTableLimitsStruct._fields_ = [
    ('numColumns', c_uint),
    ('qualifier', ARQualifierStruct),
    ('maxRetrieve', c_uint),
    ('schema', ARNameType),
    ('server', ARServerNameType),
    ('sampleSchema', ARNameType),
    ('sampleServer', ARServerNameType),
]

ARTableLimitsStruct = struct_ARTableLimitsStruct # /opt/dockethead/include/ar.h: 3911

# /opt/dockethead/include/ar.h: 3931
class struct_ARColumnLimitsStruct(Structure):
    pass

struct_ARColumnLimitsStruct.__slots__ = [
    'parent',
    'dataField',
    'dataSource',
    'colLength',
]
struct_ARColumnLimitsStruct._fields_ = [
    ('parent', ARInternalId),
    ('dataField', ARInternalId),
    ('dataSource', c_uint),
    ('colLength', c_uint),
]

ARColumnLimitsStruct = struct_ARColumnLimitsStruct # /opt/dockethead/include/ar.h: 3931

# /opt/dockethead/include/ar.h: 3939
class struct_ARDecimalLimitsStruct(Structure):
    pass

struct_ARDecimalLimitsStruct.__slots__ = [
    'rangeLow',
    'rangeHigh',
    'precision',
]
struct_ARDecimalLimitsStruct._fields_ = [
    ('rangeLow', String),
    ('rangeHigh', String),
    ('precision', c_int),
]

ARDecimalLimitsStruct = struct_ARDecimalLimitsStruct # /opt/dockethead/include/ar.h: 3939

# /opt/dockethead/include/ar.h: 3945
class struct_ARViewLimits(Structure):
    pass

struct_ARViewLimits.__slots__ = [
    'maxLength',
]
struct_ARViewLimits._fields_ = [
    ('maxLength', c_uint),
]

ARViewLimits = struct_ARViewLimits # /opt/dockethead/include/ar.h: 3945

# /opt/dockethead/include/ar.h: 3951
class struct_ARDisplayLimits(Structure):
    pass

struct_ARDisplayLimits.__slots__ = [
    'maxLength',
    'lengthUnits',
]
struct_ARDisplayLimits._fields_ = [
    ('maxLength', c_uint),
    ('lengthUnits', c_uint),
]

ARDisplayLimits = struct_ARDisplayLimits # /opt/dockethead/include/ar.h: 3951

# /opt/dockethead/include/ar.h: 3958
class struct_ARDateLimitsStruct(Structure):
    pass

struct_ARDateLimitsStruct.__slots__ = [
    'minDate',
    'maxDate',
]
struct_ARDateLimitsStruct._fields_ = [
    ('minDate', c_int),
    ('maxDate', c_int),
]

ARDateLimitsStruct = struct_ARDateLimitsStruct # /opt/dockethead/include/ar.h: 3958

# /opt/dockethead/include/ar.h: 3968
class struct_ARCurrencyDetailStruct(Structure):
    pass

struct_ARCurrencyDetailStruct.__slots__ = [
    'currencyCode',
    'precision',
]
struct_ARCurrencyDetailStruct._fields_ = [
    ('currencyCode', ARCurrencyCodeType),
    ('precision', c_int),
]

ARCurrencyDetailStruct = struct_ARCurrencyDetailStruct # /opt/dockethead/include/ar.h: 3968

# /opt/dockethead/include/ar.h: 3976
class struct_ARCurrencyDetailList(Structure):
    pass

struct_ARCurrencyDetailList.__slots__ = [
    'numItems',
    'currencyDetailList',
]
struct_ARCurrencyDetailList._fields_ = [
    ('numItems', c_uint),
    ('currencyDetailList', POINTER(ARCurrencyDetailStruct)),
]

ARCurrencyDetailList = struct_ARCurrencyDetailList # /opt/dockethead/include/ar.h: 3976

# /opt/dockethead/include/ar.h: 3987
class struct_ARCurrencyLimitsStruct(Structure):
    pass

struct_ARCurrencyLimitsStruct.__slots__ = [
    'rangeLow',
    'rangeHigh',
    'precision',
    'functionalCurrencies',
    'allowableCurrencies',
]
struct_ARCurrencyLimitsStruct._fields_ = [
    ('rangeLow', String),
    ('rangeHigh', String),
    ('precision', c_int),
    ('functionalCurrencies', ARCurrencyDetailList),
    ('allowableCurrencies', ARCurrencyDetailList),
]

ARCurrencyLimitsStruct = struct_ARCurrencyLimitsStruct # /opt/dockethead/include/ar.h: 3987

# /opt/dockethead/include/ar.h: 3994
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    'intLimits',
    'realLimits',
    'charLimits',
    'diaryLimits',
    'enumLimits',
    'maskLimits',
    'attachLimits',
    'tableLimits',
    'columnLimits',
    'decimalLimits',
    'viewLimits',
    'displayLimits',
    'dateLimits',
    'currencyLimits',
]
union_anon_12._fields_ = [
    ('intLimits', ARIntegerLimitsStruct),
    ('realLimits', ARRealLimitsStruct),
    ('charLimits', ARCharLimitsStruct),
    ('diaryLimits', ARDiaryLimitsStruct),
    ('enumLimits', AREnumLimitsStruct),
    ('maskLimits', AREnumLimitsStruct),
    ('attachLimits', ARAttachLimitsStruct),
    ('tableLimits', ARTableLimitsStruct),
    ('columnLimits', ARColumnLimitsStruct),
    ('decimalLimits', ARDecimalLimitsStruct),
    ('viewLimits', ARViewLimits),
    ('displayLimits', ARDisplayLimits),
    ('dateLimits', ARDateLimitsStruct),
    ('currencyLimits', ARCurrencyLimitsStruct),
]

# /opt/dockethead/include/ar.h: 4013
class struct_ARFieldLimitStruct(Structure):
    pass

struct_ARFieldLimitStruct.__slots__ = [
    'dataType',
    'u',
]
struct_ARFieldLimitStruct._fields_ = [
    ('dataType', c_uint),
    ('u', union_anon_12),
]

ARFieldLimitStruct = struct_ARFieldLimitStruct # /opt/dockethead/include/ar.h: 4013

# /opt/dockethead/include/ar.h: 4019
class struct_ARFieldLimitList(Structure):
    pass

struct_ARFieldLimitList.__slots__ = [
    'numItems',
    'fieldLimitList',
]
struct_ARFieldLimitList._fields_ = [
    ('numItems', c_uint),
    ('fieldLimitList', POINTER(ARFieldLimitStruct)),
]

ARFieldLimitList = struct_ARFieldLimitList # /opt/dockethead/include/ar.h: 4019

# /opt/dockethead/include/ar.h: 4025
class struct_ARFieldLimitPtrList(Structure):
    pass

struct_ARFieldLimitPtrList.__slots__ = [
    'numItems',
    'fieldLimitPtrList',
]
struct_ARFieldLimitPtrList._fields_ = [
    ('numItems', c_uint),
    ('fieldLimitPtrList', POINTER(POINTER(ARFieldLimitStruct))),
]

ARFieldLimitPtrList = struct_ARFieldLimitPtrList # /opt/dockethead/include/ar.h: 4025

# /opt/dockethead/include/ar.h: 4157
class struct_ARCharMenuStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 4040
class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    'menuValue',
    'childMenu',
]
union_anon_13._fields_ = [
    ('menuValue', String),
    ('childMenu', POINTER(struct_ARCharMenuStruct)),
]

# /opt/dockethead/include/ar.h: 4046
class struct_ARCharMenuItemStruct(Structure):
    pass

struct_ARCharMenuItemStruct.__slots__ = [
    'menuLabel',
    'menuType',
    'u',
]
struct_ARCharMenuItemStruct._fields_ = [
    ('menuLabel', ARNameType),
    ('menuType', c_uint),
    ('u', union_anon_13),
]

ARCharMenuItemStruct = struct_ARCharMenuItemStruct # /opt/dockethead/include/ar.h: 4046

# /opt/dockethead/include/ar.h: 4060
class struct_ARCharMenuQueryStruct(Structure):
    pass

struct_ARCharMenuQueryStruct.__slots__ = [
    'schema',
    'server',
    'qualifier',
    'labelField',
    'valueField',
    'sortOnLabel',
    'sampleSchema',
    'sampleServer',
]
struct_ARCharMenuQueryStruct._fields_ = [
    ('schema', ARNameType),
    ('server', c_char * (64 + 1)),
    ('qualifier', ARQualifierStruct),
    ('labelField', ARInternalId * 5),
    ('valueField', ARInternalId),
    ('sortOnLabel', ARBoolean),
    ('sampleSchema', ARNameType),
    ('sampleServer', ARServerNameType),
]

ARCharMenuQueryStruct = struct_ARCharMenuQueryStruct # /opt/dockethead/include/ar.h: 4060

# /opt/dockethead/include/ar.h: 4069
class struct_ARCharMenuFileStruct(Structure):
    pass

struct_ARCharMenuFileStruct.__slots__ = [
    'fileLocation',
    'filename',
]
struct_ARCharMenuFileStruct._fields_ = [
    ('fileLocation', c_uint),
    ('filename', String),
]

ARCharMenuFileStruct = struct_ARCharMenuFileStruct # /opt/dockethead/include/ar.h: 4069

# /opt/dockethead/include/ar.h: 4078
class struct_ARCharMenuSQLStruct(Structure):
    pass

struct_ARCharMenuSQLStruct.__slots__ = [
    'server',
    'sqlCommand',
    'labelIndex',
    'valueIndex',
]
struct_ARCharMenuSQLStruct._fields_ = [
    ('server', c_char * (64 + 1)),
    ('sqlCommand', String),
    ('labelIndex', c_int * 5),
    ('valueIndex', c_int),
]

ARCharMenuSQLStruct = struct_ARCharMenuSQLStruct # /opt/dockethead/include/ar.h: 4078

# /opt/dockethead/include/ar.h: 4085
class struct_ARCharMenuList(Structure):
    pass

struct_ARCharMenuList.__slots__ = [
    'numItems',
    'charMenuList',
]
struct_ARCharMenuList._fields_ = [
    ('numItems', c_uint),
    ('charMenuList', POINTER(ARCharMenuItemStruct)),
]

ARCharMenuList = struct_ARCharMenuList # /opt/dockethead/include/ar.h: 4085

# /opt/dockethead/include/ar.h: 4096
class struct_ARCharMenuSSStruct(Structure):
    pass

struct_ARCharMenuSSStruct.__slots__ = [
    'menuName',
    'keywordList',
    'parameterList',
    'externList',
    'server',
    'schema',
]
struct_ARCharMenuSSStruct._fields_ = [
    ('menuName', ARNameType),
    ('keywordList', ARFieldValueList),
    ('parameterList', ARFieldValueList),
    ('externList', ARQualifierList),
    ('server', String),
    ('schema', String),
]

ARCharMenuSSStruct = struct_ARCharMenuSSStruct # /opt/dockethead/include/ar.h: 4096

# /opt/dockethead/include/ar.h: 4107
class struct_ARCharMenuDDFormStruct(Structure):
    pass

struct_ARCharMenuDDFormStruct.__slots__ = [
    'schemaType',
    'includeHidden',
]
struct_ARCharMenuDDFormStruct._fields_ = [
    ('schemaType', c_uint),
    ('includeHidden', ARBoolean),
]

ARCharMenuDDFormStruct = struct_ARCharMenuDDFormStruct # /opt/dockethead/include/ar.h: 4107

# /opt/dockethead/include/ar.h: 4114
class struct_ARCharMenuDDFieldStruct(Structure):
    pass

struct_ARCharMenuDDFieldStruct.__slots__ = [
    'fieldType',
    'schema',
]
struct_ARCharMenuDDFieldStruct._fields_ = [
    ('fieldType', c_uint),
    ('schema', ARNameType),
]

ARCharMenuDDFieldStruct = struct_ARCharMenuDDFieldStruct # /opt/dockethead/include/ar.h: 4114

# /opt/dockethead/include/ar.h: 4141
class union_anon_14(Union):
    pass

union_anon_14.__slots__ = [
    'formDefn',
    'fieldDefn',
]
union_anon_14._fields_ = [
    ('formDefn', ARCharMenuDDFormStruct),
    ('fieldDefn', ARCharMenuDDFieldStruct),
]

# /opt/dockethead/include/ar.h: 4147
class struct_ARCharMenuDDStruct(Structure):
    pass

struct_ARCharMenuDDStruct.__slots__ = [
    'server',
    'nameType',
    'valueFormat',
    'structType',
    'u',
]
struct_ARCharMenuDDStruct._fields_ = [
    ('server', c_char * (64 + 1)),
    ('nameType', c_uint),
    ('valueFormat', c_uint),
    ('structType', c_uint),
    ('u', union_anon_14),
]

ARCharMenuDDStruct = struct_ARCharMenuDDStruct # /opt/dockethead/include/ar.h: 4147

# /opt/dockethead/include/ar.h: 4160
class union_anon_15(Union):
    pass

union_anon_15.__slots__ = [
    'menuList',
    'menuQuery',
    'menuFile',
    'menuSQL',
    'menuSS',
    'menuDD',
]
union_anon_15._fields_ = [
    ('menuList', ARCharMenuList),
    ('menuQuery', ARCharMenuQueryStruct),
    ('menuFile', ARCharMenuFileStruct),
    ('menuSQL', ARCharMenuSQLStruct),
    ('menuSS', ARCharMenuSSStruct),
    ('menuDD', ARCharMenuDDStruct),
]

struct_ARCharMenuStruct.__slots__ = [
    'menuType',
    'u',
]
struct_ARCharMenuStruct._fields_ = [
    ('menuType', c_uint),
    ('u', union_anon_15),
]

ARCharMenuStruct = struct_ARCharMenuStruct # /opt/dockethead/include/ar.h: 4170

# /opt/dockethead/include/ar.h: 4176
class struct_ARCharMenuStructList(Structure):
    pass

struct_ARCharMenuStructList.__slots__ = [
    'numItems',
    'list',
]
struct_ARCharMenuStructList._fields_ = [
    ('numItems', c_uint),
    ('list', POINTER(ARCharMenuStruct)),
]

ARCharMenuStructList = struct_ARCharMenuStructList # /opt/dockethead/include/ar.h: 4176

# /opt/dockethead/include/ar.h: 4398
class struct_ARStructItemStruct(Structure):
    pass

struct_ARStructItemStruct.__slots__ = [
    'type',
    'name',
    'selectedElements',
]
struct_ARStructItemStruct._fields_ = [
    ('type', c_uint),
    ('name', ARNameType),
    ('selectedElements', ARNameList),
]

ARStructItemStruct = struct_ARStructItemStruct # /opt/dockethead/include/ar.h: 4398

# /opt/dockethead/include/ar.h: 4405
class struct_ARStructItemList(Structure):
    pass

struct_ARStructItemList.__slots__ = [
    'numItems',
    'structItemList',
]
struct_ARStructItemList._fields_ = [
    ('numItems', c_uint),
    ('structItemList', POINTER(ARStructItemStruct)),
]

ARStructItemList = struct_ARStructItemList # /opt/dockethead/include/ar.h: 4405

# /opt/dockethead/include/ar.h: 5269
class struct_ARServerInfoRequestList(Structure):
    pass

struct_ARServerInfoRequestList.__slots__ = [
    'numItems',
    'requestList',
]
struct_ARServerInfoRequestList._fields_ = [
    ('numItems', c_uint),
    ('requestList', POINTER(c_uint)),
]

ARServerInfoRequestList = struct_ARServerInfoRequestList # /opt/dockethead/include/ar.h: 5269

# /opt/dockethead/include/ar.h: 5276
class struct_ARServerInfoStruct(Structure):
    pass

struct_ARServerInfoStruct.__slots__ = [
    'operation',
    'value',
]
struct_ARServerInfoStruct._fields_ = [
    ('operation', c_uint),
    ('value', ARValueStruct),
]

ARServerInfoStruct = struct_ARServerInfoStruct # /opt/dockethead/include/ar.h: 5276

# /opt/dockethead/include/ar.h: 5283
class struct_ARServerInfoList(Structure):
    pass

struct_ARServerInfoList.__slots__ = [
    'numItems',
    'serverInfoList',
]
struct_ARServerInfoList._fields_ = [
    ('numItems', c_uint),
    ('serverInfoList', POINTER(ARServerInfoStruct)),
]

ARServerInfoList = struct_ARServerInfoList # /opt/dockethead/include/ar.h: 5283

# /opt/dockethead/include/ar.h: 5337
class struct_ARFullTextInfoRequestList(Structure):
    pass

struct_ARFullTextInfoRequestList.__slots__ = [
    'numItems',
    'requestList',
]
struct_ARFullTextInfoRequestList._fields_ = [
    ('numItems', c_uint),
    ('requestList', POINTER(c_uint)),
]

ARFullTextInfoRequestList = struct_ARFullTextInfoRequestList # /opt/dockethead/include/ar.h: 5337

# /opt/dockethead/include/ar.h: 5342
class union_anon_16(Union):
    pass

union_anon_16.__slots__ = [
    'valueList',
    'value',
]
union_anon_16._fields_ = [
    ('valueList', ARValueList),
    ('value', ARValueStruct),
]

# /opt/dockethead/include/ar.h: 5350
class struct_ARFullTextInfoStruct(Structure):
    pass

struct_ARFullTextInfoStruct.__slots__ = [
    'infoType',
    'u',
]
struct_ARFullTextInfoStruct._fields_ = [
    ('infoType', c_uint),
    ('u', union_anon_16),
]

ARFullTextInfoStruct = struct_ARFullTextInfoStruct # /opt/dockethead/include/ar.h: 5350

# /opt/dockethead/include/ar.h: 5357
class struct_ARFullTextInfoList(Structure):
    pass

struct_ARFullTextInfoList.__slots__ = [
    'numItems',
    'fullTextInfoList',
]
struct_ARFullTextInfoList._fields_ = [
    ('numItems', c_uint),
    ('fullTextInfoList', POINTER(ARFullTextInfoStruct)),
]

ARFullTextInfoList = struct_ARFullTextInfoList # /opt/dockethead/include/ar.h: 5357

# /opt/dockethead/include/ar.h: 5369
class struct_ARStatusHistoryStruct(Structure):
    pass

struct_ARStatusHistoryStruct.__slots__ = [
    'user',
    'timeVal',
]
struct_ARStatusHistoryStruct._fields_ = [
    ('user', ARAccessNameType),
    ('timeVal', ARTimestamp),
]

ARStatusHistoryStruct = struct_ARStatusHistoryStruct # /opt/dockethead/include/ar.h: 5369

# /opt/dockethead/include/ar.h: 5376
class struct_ARStatusHistoryList(Structure):
    pass

struct_ARStatusHistoryList.__slots__ = [
    'numItems',
    'statHistList',
]
struct_ARStatusHistoryList._fields_ = [
    ('numItems', c_uint),
    ('statHistList', POINTER(ARStatusHistoryStruct)),
]

ARStatusHistoryList = struct_ARStatusHistoryList # /opt/dockethead/include/ar.h: 5376

# /opt/dockethead/include/ar.h: 5384
class struct_ARDiaryStruct(Structure):
    pass

struct_ARDiaryStruct.__slots__ = [
    'user',
    'timeVal',
    'value',
]
struct_ARDiaryStruct._fields_ = [
    ('user', ARAccessNameType),
    ('timeVal', ARTimestamp),
    ('value', String),
]

ARDiaryStruct = struct_ARDiaryStruct # /opt/dockethead/include/ar.h: 5384

# /opt/dockethead/include/ar.h: 5391
class struct_ARDiaryList(Structure):
    pass

struct_ARDiaryList.__slots__ = [
    'numItems',
    'diaryList',
]
struct_ARDiaryList._fields_ = [
    ('numItems', c_uint),
    ('diaryList', POINTER(ARDiaryStruct)),
]

ARDiaryList = struct_ARDiaryList # /opt/dockethead/include/ar.h: 5391

# /opt/dockethead/include/ar.h: 5414
class union_anon_17(Union):
    pass

union_anon_17.__slots__ = [
    'interval',
    'date',
]
union_anon_17._fields_ = [
    ('interval', ARLong32),
    ('date', ARDayStruct),
]

# /opt/dockethead/include/ar.h: 5420
class struct_AREscalationTmStruct(Structure):
    pass

struct_AREscalationTmStruct.__slots__ = [
    'escalationTmType',
    'u',
]
struct_AREscalationTmStruct._fields_ = [
    ('escalationTmType', c_uint),
    ('u', union_anon_17),
]

AREscalationTmStruct = struct_AREscalationTmStruct # /opt/dockethead/include/ar.h: 5420

# /opt/dockethead/include/ar.h: 5427
class struct_AREscalationTmList(Structure):
    pass

struct_AREscalationTmList.__slots__ = [
    'numItems',
    'escalationTmList',
]
struct_AREscalationTmList._fields_ = [
    ('numItems', c_uint),
    ('escalationTmList', POINTER(AREscalationTmStruct)),
]

AREscalationTmList = struct_AREscalationTmList # /opt/dockethead/include/ar.h: 5427

# /opt/dockethead/include/ar.h: 5458
class struct_ARJoinMappingStruct(Structure):
    pass

struct_ARJoinMappingStruct.__slots__ = [
    'schemaIndex',
    'realId',
]
struct_ARJoinMappingStruct._fields_ = [
    ('schemaIndex', c_uint),
    ('realId', ARInternalId),
]

ARJoinMappingStruct = struct_ARJoinMappingStruct # /opt/dockethead/include/ar.h: 5458

# /opt/dockethead/include/ar.h: 5464
class struct_ARViewMappingStruct(Structure):
    pass

struct_ARViewMappingStruct.__slots__ = [
    'fieldName',
]
struct_ARViewMappingStruct._fields_ = [
    ('fieldName', ARNameType),
]

ARViewMappingStruct = struct_ARViewMappingStruct # /opt/dockethead/include/ar.h: 5464

# /opt/dockethead/include/ar.h: 5470
class struct_ARVendorMappingStruct(Structure):
    pass

struct_ARVendorMappingStruct.__slots__ = [
    'fieldName',
]
struct_ARVendorMappingStruct._fields_ = [
    ('fieldName', ARNameType),
]

ARVendorMappingStruct = struct_ARVendorMappingStruct # /opt/dockethead/include/ar.h: 5470

# /opt/dockethead/include/ar.h: 5486
class struct_ARInheritanceMappingStruct(Structure):
    pass

struct_ARInheritanceMappingStruct.__slots__ = [
    'srcSchema',
    'referenceMask',
    'dataMappingId',
]
struct_ARInheritanceMappingStruct._fields_ = [
    ('srcSchema', ARNameType),
    ('referenceMask', c_uint),
    ('dataMappingId', c_uint),
]

ARInheritanceMappingStruct = struct_ARInheritanceMappingStruct # /opt/dockethead/include/ar.h: 5486

# /opt/dockethead/include/ar.h: 5492
class union_anon_18(Union):
    pass

union_anon_18.__slots__ = [
    'join',
    'view',
    'vendor',
    'inheritance',
]
union_anon_18._fields_ = [
    ('join', ARJoinMappingStruct),
    ('view', ARViewMappingStruct),
    ('vendor', ARVendorMappingStruct),
    ('inheritance', ARInheritanceMappingStruct),
]

# /opt/dockethead/include/ar.h: 5500
class struct_ARFieldMappingStruct(Structure):
    pass

struct_ARFieldMappingStruct.__slots__ = [
    'fieldType',
    'u',
]
struct_ARFieldMappingStruct._fields_ = [
    ('fieldType', c_uint),
    ('u', union_anon_18),
]

ARFieldMappingStruct = struct_ARFieldMappingStruct # /opt/dockethead/include/ar.h: 5500

# /opt/dockethead/include/ar.h: 5507
class struct_ARFieldMappingList(Structure):
    pass

struct_ARFieldMappingList.__slots__ = [
    'numItems',
    'mappingList',
]
struct_ARFieldMappingList._fields_ = [
    ('numItems', c_uint),
    ('mappingList', POINTER(ARFieldMappingStruct)),
]

ARFieldMappingList = struct_ARFieldMappingList # /opt/dockethead/include/ar.h: 5507

# /opt/dockethead/include/ar.h: 5514
class struct_ARFieldMappingPtrList(Structure):
    pass

struct_ARFieldMappingPtrList.__slots__ = [
    'numItems',
    'mappingPtrList',
]
struct_ARFieldMappingPtrList._fields_ = [
    ('numItems', c_uint),
    ('mappingPtrList', POINTER(POINTER(ARFieldMappingStruct))),
]

ARFieldMappingPtrList = struct_ARFieldMappingPtrList # /opt/dockethead/include/ar.h: 5514

# /opt/dockethead/include/ar.h: 5615
class struct_ARJoinSchema(Structure):
    pass

struct_ARJoinSchema.__slots__ = [
    'memberA',
    'memberB',
    'joinQual',
    'option',
]
struct_ARJoinSchema._fields_ = [
    ('memberA', ARNameType),
    ('memberB', ARNameType),
    ('joinQual', ARQualifierStruct),
    ('option', c_uint),
]

ARJoinSchema = struct_ARJoinSchema # /opt/dockethead/include/ar.h: 5615

# /opt/dockethead/include/ar.h: 5621
class struct_ARViewSchema(Structure):
    pass

struct_ARViewSchema.__slots__ = [
    'tableName',
    'keyField',
]
struct_ARViewSchema._fields_ = [
    ('tableName', c_char * (2047 + 1)),
    ('keyField', ARNameType),
]

ARViewSchema = struct_ARViewSchema # /opt/dockethead/include/ar.h: 5621

# /opt/dockethead/include/ar.h: 5629
class struct_ARVendorSchema(Structure):
    pass

struct_ARVendorSchema.__slots__ = [
    'vendorName',
    'tableName',
]
struct_ARVendorSchema._fields_ = [
    ('vendorName', ARNameType),
    ('tableName', c_char * (2047 + 1)),
]

ARVendorSchema = struct_ARVendorSchema # /opt/dockethead/include/ar.h: 5629

# /opt/dockethead/include/ar.h: 5634
class union_anon_19(Union):
    pass

union_anon_19.__slots__ = [
    'join',
    'view',
    'vendor',
]
union_anon_19._fields_ = [
    ('join', ARJoinSchema),
    ('view', ARViewSchema),
    ('vendor', ARVendorSchema),
]

# /opt/dockethead/include/ar.h: 5641
class struct_ARCompoundSchema(Structure):
    pass

struct_ARCompoundSchema.__slots__ = [
    'schemaType',
    'u',
]
struct_ARCompoundSchema._fields_ = [
    ('schemaType', c_uint),
    ('u', union_anon_19),
]

ARCompoundSchema = struct_ARCompoundSchema # /opt/dockethead/include/ar.h: 5641

# /opt/dockethead/include/ar.h: 5648
class struct_ARCompoundSchemaList(Structure):
    pass

struct_ARCompoundSchemaList.__slots__ = [
    'numItems',
    'compoundSchema',
]
struct_ARCompoundSchemaList._fields_ = [
    ('numItems', c_uint),
    ('compoundSchema', POINTER(ARCompoundSchema)),
]

ARCompoundSchemaList = struct_ARCompoundSchemaList # /opt/dockethead/include/ar.h: 5648

# /opt/dockethead/include/ar.h: 5660
class struct_ARDataMappingInfoStruct(Structure):
    pass

struct_ARDataMappingInfoStruct.__slots__ = [
    'id',
    'name',
    'primaryKeyIndexName',
    'foreignKeyFieldIdList',
    'opMask',
    'readOrder',
    'writeOrder',
]
struct_ARDataMappingInfoStruct._fields_ = [
    ('id', c_uint),
    ('name', ARNameType),
    ('primaryKeyIndexName', ARNameType),
    ('foreignKeyFieldIdList', ARInternalIdList),
    ('opMask', c_uint),
    ('readOrder', c_uint),
    ('writeOrder', c_uint),
]

ARDataMappingInfoStruct = struct_ARDataMappingInfoStruct # /opt/dockethead/include/ar.h: 5660

# /opt/dockethead/include/ar.h: 5667
class struct_ARDataMappingInfoList(Structure):
    pass

struct_ARDataMappingInfoList.__slots__ = [
    'numItems',
    'dataMappingInfoList',
]
struct_ARDataMappingInfoList._fields_ = [
    ('numItems', c_uint),
    ('dataMappingInfoList', POINTER(ARDataMappingInfoStruct)),
]

ARDataMappingInfoList = struct_ARDataMappingInfoList # /opt/dockethead/include/ar.h: 5667

# /opt/dockethead/include/ar.h: 5676
class struct_ARSchemaInheritanceStruct(Structure):
    pass

struct_ARSchemaInheritanceStruct.__slots__ = [
    'srcSchema',
    'inheritAll',
    'dataMappingId',
    'dataMappingInfoList',
]
struct_ARSchemaInheritanceStruct._fields_ = [
    ('srcSchema', ARNameType),
    ('inheritAll', ARBoolean),
    ('dataMappingId', c_uint),
    ('dataMappingInfoList', ARDataMappingInfoList),
]

ARSchemaInheritanceStruct = struct_ARSchemaInheritanceStruct # /opt/dockethead/include/ar.h: 5676

# /opt/dockethead/include/ar.h: 5683
class struct_ARSchemaInheritanceList(Structure):
    pass

struct_ARSchemaInheritanceList.__slots__ = [
    'numItems',
    'schemaInheritanceList',
]
struct_ARSchemaInheritanceList._fields_ = [
    ('numItems', c_uint),
    ('schemaInheritanceList', POINTER(ARSchemaInheritanceStruct)),
]

ARSchemaInheritanceList = struct_ARSchemaInheritanceList # /opt/dockethead/include/ar.h: 5683

# /opt/dockethead/include/ar.h: 5690
class struct_ARSchemaInheritanceListList(Structure):
    pass

struct_ARSchemaInheritanceListList.__slots__ = [
    'numItems',
    'schemaInheritanceListList',
]
struct_ARSchemaInheritanceListList._fields_ = [
    ('numItems', c_uint),
    ('schemaInheritanceListList', POINTER(ARSchemaInheritanceList)),
]

ARSchemaInheritanceListList = struct_ARSchemaInheritanceListList # /opt/dockethead/include/ar.h: 5690

# /opt/dockethead/include/ar.h: 5704
class struct_ARSupportFileInfoStruct(Structure):
    pass

struct_ARSupportFileInfoStruct.__slots__ = [
    'fileType',
    'fileId',
    'timestamp',
    'content',
    'contentLen',
]
struct_ARSupportFileInfoStruct._fields_ = [
    ('fileType', c_uint),
    ('fileId', ARInternalId),
    ('timestamp', ARTimestamp),
    ('content', String),
    ('contentLen', c_uint),
]

ARSupportFileInfoStruct = struct_ARSupportFileInfoStruct # /opt/dockethead/include/ar.h: 5704

# /opt/dockethead/include/ar.h: 5711
class struct_ARSupportFileInfoList(Structure):
    pass

struct_ARSupportFileInfoList.__slots__ = [
    'numItems',
    'sfList',
]
struct_ARSupportFileInfoList._fields_ = [
    ('numItems', c_uint),
    ('sfList', POINTER(ARSupportFileInfoStruct)),
]

ARSupportFileInfoList = struct_ARSupportFileInfoList # /opt/dockethead/include/ar.h: 5711

# /opt/dockethead/include/ar.h: 5720
class struct_ARStatisticsStruct(Structure):
    pass

struct_ARStatisticsStruct.__slots__ = [
    'operation',
    'field',
]
struct_ARStatisticsStruct._fields_ = [
    ('operation', c_uint),
    ('field', ARFieldValueOrArithStruct),
]

ARStatisticsStruct = struct_ARStatisticsStruct # /opt/dockethead/include/ar.h: 5720

# /opt/dockethead/include/ar.h: 5727
class struct_ARStatisticsList(Structure):
    pass

struct_ARStatisticsList.__slots__ = [
    'numItems',
    'statisticsList',
]
struct_ARStatisticsList._fields_ = [
    ('numItems', c_uint),
    ('statisticsList', POINTER(ARStatisticsStruct)),
]

ARStatisticsList = struct_ARStatisticsList # /opt/dockethead/include/ar.h: 5727

# /opt/dockethead/include/ar.h: 5762
class struct_ARDisplayStruct(Structure):
    pass

struct_ARDisplayStruct.__slots__ = [
    'displayTag',
    'label',
    'labelLocation',
    'type',
    'length',
    'numRows',
    'option',
    'x',
    'y',
]
struct_ARDisplayStruct._fields_ = [
    ('displayTag', ARNameType),
    ('label', ARNameType),
    ('labelLocation', c_uint),
    ('type', c_uint),
    ('length', c_uint),
    ('numRows', c_uint),
    ('option', c_uint),
    ('x', c_int),
    ('y', c_int),
]

ARDisplayStruct = struct_ARDisplayStruct # /opt/dockethead/include/ar.h: 5762

# /opt/dockethead/include/ar.h: 5769
class struct_ARDisplayList(Structure):
    pass

struct_ARDisplayList.__slots__ = [
    'numItems',
    'displayList',
]
struct_ARDisplayList._fields_ = [
    ('numItems', c_uint),
    ('displayList', POINTER(ARDisplayStruct)),
]

ARDisplayList = struct_ARDisplayList # /opt/dockethead/include/ar.h: 5769

# /opt/dockethead/include/ar.h: 5976
class struct_ARContainerOwnerObj(Structure):
    pass

struct_ARContainerOwnerObj.__slots__ = [
    'type',
    'ownerName',
]
struct_ARContainerOwnerObj._fields_ = [
    ('type', c_uint),
    ('ownerName', ARNameType),
]

ARContainerOwnerObj = struct_ARContainerOwnerObj # /opt/dockethead/include/ar.h: 5976

# /opt/dockethead/include/ar.h: 5983
class struct_ARContainerOwnerObjList(Structure):
    pass

struct_ARContainerOwnerObjList.__slots__ = [
    'numItems',
    'ownerObjList',
]
struct_ARContainerOwnerObjList._fields_ = [
    ('numItems', c_uint),
    ('ownerObjList', POINTER(ARContainerOwnerObj)),
]

ARContainerOwnerObjList = struct_ARContainerOwnerObjList # /opt/dockethead/include/ar.h: 5983

# /opt/dockethead/include/ar.h: 5990
class struct_ARContainerOwnerObjListList(Structure):
    pass

struct_ARContainerOwnerObjListList.__slots__ = [
    'numItems',
    'ownerObjListList',
]
struct_ARContainerOwnerObjListList._fields_ = [
    ('numItems', c_uint),
    ('ownerObjListList', POINTER(ARContainerOwnerObjList)),
]

ARContainerOwnerObjListList = struct_ARContainerOwnerObjListList # /opt/dockethead/include/ar.h: 5990

# /opt/dockethead/include/ar.h: 5997
class struct_ARContainerOwnerObjId(Structure):
    pass

struct_ARContainerOwnerObjId.__slots__ = [
    'type',
    'ownerId',
]
struct_ARContainerOwnerObjId._fields_ = [
    ('type', c_uint),
    ('ownerId', c_uint),
]

ARContainerOwnerObjId = struct_ARContainerOwnerObjId # /opt/dockethead/include/ar.h: 5997

# /opt/dockethead/include/ar.h: 6004
class struct_ARContainerOwnerObjIdList(Structure):
    pass

struct_ARContainerOwnerObjIdList.__slots__ = [
    'numItems',
    'ownerObjIdList',
]
struct_ARContainerOwnerObjIdList._fields_ = [
    ('numItems', c_uint),
    ('ownerObjIdList', POINTER(ARContainerOwnerObjId)),
]

ARContainerOwnerObjIdList = struct_ARContainerOwnerObjIdList # /opt/dockethead/include/ar.h: 6004

# /opt/dockethead/include/ar.h: 6014
class struct_ARExtReferenceStruct(Structure):
    pass

struct_ARExtReferenceStruct.__slots__ = [
    'permittedGroups',
    'value',
]
struct_ARExtReferenceStruct._fields_ = [
    ('permittedGroups', ARInternalIdList),
    ('value', ARValueStruct),
]

ARExtReferenceStruct = struct_ARExtReferenceStruct # /opt/dockethead/include/ar.h: 6014

# /opt/dockethead/include/ar.h: 6022
class union_anon_20(Union):
    pass

union_anon_20.__slots__ = [
    'name',
    'extRef',
]
union_anon_20._fields_ = [
    ('name', ARNameType),
    ('extRef', ARExtReferenceStruct),
]

# /opt/dockethead/include/ar.h: 6028
class struct_ARReferenceUnion(Structure):
    pass

struct_ARReferenceUnion.__slots__ = [
    'dataType',
    'u',
]
struct_ARReferenceUnion._fields_ = [
    ('dataType', c_uint),
    ('u', union_anon_20),
]

ARReferenceUnion = struct_ARReferenceUnion # /opt/dockethead/include/ar.h: 6028

# /opt/dockethead/include/ar.h: 6037
class struct_ARReferenceStruct(Structure):
    pass

struct_ARReferenceStruct.__slots__ = [
    'label',
    'description',
    'type',
    'reference',
]
struct_ARReferenceStruct._fields_ = [
    ('label', String),
    ('description', String),
    ('type', c_uint),
    ('reference', ARReferenceUnion),
]

ARReferenceStruct = struct_ARReferenceStruct # /opt/dockethead/include/ar.h: 6037

# /opt/dockethead/include/ar.h: 6044
class struct_ARReferenceList(Structure):
    pass

struct_ARReferenceList.__slots__ = [
    'numItems',
    'referenceList',
]
struct_ARReferenceList._fields_ = [
    ('numItems', c_uint),
    ('referenceList', POINTER(ARReferenceStruct)),
]

ARReferenceList = struct_ARReferenceList # /opt/dockethead/include/ar.h: 6044

# /opt/dockethead/include/ar.h: 6051
class struct_ARReferenceListList(Structure):
    pass

struct_ARReferenceListList.__slots__ = [
    'numItems',
    'referenceListList',
]
struct_ARReferenceListList._fields_ = [
    ('numItems', c_uint),
    ('referenceListList', POINTER(ARReferenceList)),
]

ARReferenceListList = struct_ARReferenceListList # /opt/dockethead/include/ar.h: 6051

# /opt/dockethead/include/ar.h: 6058
class struct_ARReferenceTypeList(Structure):
    pass

struct_ARReferenceTypeList.__slots__ = [
    'numItems',
    'refType',
]
struct_ARReferenceTypeList._fields_ = [
    ('numItems', c_uint),
    ('refType', POINTER(c_int)),
]

ARReferenceTypeList = struct_ARReferenceTypeList # /opt/dockethead/include/ar.h: 6058

# /opt/dockethead/include/ar.h: 6067
class struct_ARContainerInfo(Structure):
    pass

struct_ARContainerInfo.__slots__ = [
    'name',
    'type',
    'ownerList',
]
struct_ARContainerInfo._fields_ = [
    ('name', ARNameType),
    ('type', c_uint),
    ('ownerList', ARContainerOwnerObjList),
]

ARContainerInfo = struct_ARContainerInfo # /opt/dockethead/include/ar.h: 6067

# /opt/dockethead/include/ar.h: 6074
class struct_ARContainerInfoList(Structure):
    pass

struct_ARContainerInfoList.__slots__ = [
    'numItems',
    'conInfoList',
]
struct_ARContainerInfoList._fields_ = [
    ('numItems', c_uint),
    ('conInfoList', POINTER(ARContainerInfo)),
]

ARContainerInfoList = struct_ARContainerInfoList # /opt/dockethead/include/ar.h: 6074

# /opt/dockethead/include/ar.h: 6081
class struct_ARContainerTypeList(Structure):
    pass

struct_ARContainerTypeList.__slots__ = [
    'numItems',
    'type',
]
struct_ARContainerTypeList._fields_ = [
    ('numItems', c_uint),
    ('type', POINTER(c_int)),
]

ARContainerTypeList = struct_ARContainerTypeList # /opt/dockethead/include/ar.h: 6081

# /opt/dockethead/include/ar.h: 6106
class struct_ARSignalStruct(Structure):
    pass

struct_ARSignalStruct.__slots__ = [
    'signalType',
    'sigArgument',
]
struct_ARSignalStruct._fields_ = [
    ('signalType', c_int),
    ('sigArgument', String),
]

ARSignalStruct = struct_ARSignalStruct # /opt/dockethead/include/ar.h: 6106

# /opt/dockethead/include/ar.h: 6113
class struct_ARSignalList(Structure):
    pass

struct_ARSignalList.__slots__ = [
    'numItems',
    'signalList',
]
struct_ARSignalList._fields_ = [
    ('numItems', c_uint),
    ('signalList', POINTER(ARSignalStruct)),
]

ARSignalList = struct_ARSignalList # /opt/dockethead/include/ar.h: 6113

# /opt/dockethead/include/ar.h: 6126
class union_anon_21(Union):
    pass

union_anon_21.__slots__ = [
    'schemaList',
]
union_anon_21._fields_ = [
    ('schemaList', POINTER(ARNameList)),
]

# /opt/dockethead/include/ar.h: 6131
class struct_ARWorkflowConnectStruct(Structure):
    pass

struct_ARWorkflowConnectStruct.__slots__ = [
    'type',
    'u',
]
struct_ARWorkflowConnectStruct._fields_ = [
    ('type', c_uint),
    ('u', union_anon_21),
]

ARWorkflowConnectStruct = struct_ARWorkflowConnectStruct # /opt/dockethead/include/ar.h: 6131

# /opt/dockethead/include/ar.h: 6138
class struct_ARWorkflowConnectList(Structure):
    pass

struct_ARWorkflowConnectList.__slots__ = [
    'numItems',
    'workflowConnectList',
]
struct_ARWorkflowConnectList._fields_ = [
    ('numItems', c_uint),
    ('workflowConnectList', POINTER(ARWorkflowConnectStruct)),
]

ARWorkflowConnectList = struct_ARWorkflowConnectList # /opt/dockethead/include/ar.h: 6138

# /opt/dockethead/include/ar.h: 6146
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'ifElse',
    'action',
]
struct_anon_22._fields_ = [
    ('ifElse', c_uint),
    ('action', c_uint),
]

# /opt/dockethead/include/ar.h: 6144
class union_anon_23(Union):
    pass

union_anon_23.__slots__ = [
    'workflow',
    'fieldId',
]
union_anon_23._fields_ = [
    ('workflow', struct_anon_22),
    ('fieldId', ARInternalId),
]

# /opt/dockethead/include/ar.h: 6155
class struct_ARLocalizedRequestStruct(Structure):
    pass

struct_ARLocalizedRequestStruct.__slots__ = [
    'name',
    'messageType',
    'u',
]
struct_ARLocalizedRequestStruct._fields_ = [
    ('name', ARNameType),
    ('messageType', c_uint),
    ('u', union_anon_23),
]

ARLocalizedRequestStruct = struct_ARLocalizedRequestStruct # /opt/dockethead/include/ar.h: 6155

# /opt/dockethead/include/ar.h: 6162
class struct_ARLocalizedRequestList(Structure):
    pass

struct_ARLocalizedRequestList.__slots__ = [
    'numItems',
    'localizedRequestList',
]
struct_ARLocalizedRequestList._fields_ = [
    ('numItems', c_uint),
    ('localizedRequestList', POINTER(ARLocalizedRequestStruct)),
]

ARLocalizedRequestList = struct_ARLocalizedRequestList # /opt/dockethead/include/ar.h: 6162

# /opt/dockethead/include/ar.h: 6286
class struct_ARConfigSvrEvents(Structure):
    pass

struct_ARConfigSvrEvents.__slots__ = [
    'events',
]
struct_ARConfigSvrEvents._fields_ = [
    ('events', ARBoolean * 18),
]

ARConfigSvrEvents = struct_ARConfigSvrEvents # /opt/dockethead/include/ar.h: 6286

# /opt/dockethead/include/ar.h: 6309
class struct_ARFieldInfoStruct(Structure):
    pass

struct_ARFieldInfoStruct.__slots__ = [
    'fieldId',
    'fieldName',
    'timestamp',
    'fieldMap',
    'dataType',
    'option',
    'createMode',
    'fieldOption',
    'defaultVal',
    'permList',
    'limit',
    'dInstanceList',
    'owner',
    'lastChanged',
    'helpText',
    'changeDiary',
    'objPropList',
]
struct_ARFieldInfoStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('fieldName', ARNameType),
    ('timestamp', ARTimestamp),
    ('fieldMap', ARFieldMappingStruct),
    ('dataType', c_uint),
    ('option', c_uint),
    ('createMode', c_uint),
    ('fieldOption', c_uint),
    ('defaultVal', ARValueStruct),
    ('permList', ARPermissionList),
    ('limit', ARFieldLimitStruct),
    ('dInstanceList', ARDisplayInstanceList),
    ('owner', ARAccessNameType),
    ('lastChanged', ARAccessNameType),
    ('helpText', String),
    ('changeDiary', String),
    ('objPropList', ARPropList),
]

ARFieldInfoStruct = struct_ARFieldInfoStruct # /opt/dockethead/include/ar.h: 6309

# /opt/dockethead/include/ar.h: 6316
class struct_ARFieldInfoList(Structure):
    pass

struct_ARFieldInfoList.__slots__ = [
    'numItems',
    'fieldList',
]
struct_ARFieldInfoList._fields_ = [
    ('numItems', c_uint),
    ('fieldList', POINTER(ARFieldInfoStruct)),
]

ARFieldInfoList = struct_ARFieldInfoList # /opt/dockethead/include/ar.h: 6316

# /opt/dockethead/include/ar.h: 6342
class struct_ARExportFieldInfoStruct(Structure):
    pass

struct_ARExportFieldInfoStruct.__slots__ = [
    'fieldId',
    'fieldName',
    'timestamp',
    'fieldMap',
    'dataType',
    'option',
    'createMode',
    'fieldOption',
    'defaultVal',
    'permList',
    'addPermList',
    'limit',
    'dInstanceList',
    'owner',
    'lastChanged',
    'helpText',
    'changeDiary',
    'objPropList',
]
struct_ARExportFieldInfoStruct._fields_ = [
    ('fieldId', ARInternalId),
    ('fieldName', ARNameType),
    ('timestamp', ARTimestamp),
    ('fieldMap', ARFieldMappingStruct),
    ('dataType', c_uint),
    ('option', c_uint),
    ('createMode', c_uint),
    ('fieldOption', c_uint),
    ('defaultVal', ARValueStruct),
    ('permList', ARPermissionList),
    ('addPermList', ARPermissionList),
    ('limit', ARFieldLimitStruct),
    ('dInstanceList', ARDisplayInstanceList),
    ('owner', ARAccessNameType),
    ('lastChanged', ARAccessNameType),
    ('helpText', String),
    ('changeDiary', String),
    ('objPropList', ARPropList),
]

ARExportFieldInfoStruct = struct_ARExportFieldInfoStruct # /opt/dockethead/include/ar.h: 6342

# /opt/dockethead/include/ar.h: 6349
class struct_ARExportFieldInfoList(Structure):
    pass

struct_ARExportFieldInfoList.__slots__ = [
    'numItems',
    'fieldList',
]
struct_ARExportFieldInfoList._fields_ = [
    ('numItems', c_uint),
    ('fieldList', POINTER(ARExportFieldInfoStruct)),
]

ARExportFieldInfoList = struct_ARExportFieldInfoList # /opt/dockethead/include/ar.h: 6349

# /opt/dockethead/include/ar.h: 6365
class struct_ARVuiInfoStruct(Structure):
    pass

struct_ARVuiInfoStruct.__slots__ = [
    'vuiId',
    'vuiName',
    'timestamp',
    'props',
    'owner',
    'locale',
    'vuiType',
    'lastChanged',
    'helpText',
    'changeDiary',
    'smObjProp',
]
struct_ARVuiInfoStruct._fields_ = [
    ('vuiId', ARInternalId),
    ('vuiName', ARNameType),
    ('timestamp', ARTimestamp),
    ('props', ARPropList),
    ('owner', ARAccessNameType),
    ('locale', ARLocaleType),
    ('vuiType', c_uint),
    ('lastChanged', ARAccessNameType),
    ('helpText', String),
    ('changeDiary', String),
    ('smObjProp', ARPropList),
]

ARVuiInfoStruct = struct_ARVuiInfoStruct # /opt/dockethead/include/ar.h: 6365

# /opt/dockethead/include/ar.h: 6372
class struct_ARVuiInfoList(Structure):
    pass

struct_ARVuiInfoList.__slots__ = [
    'numItems',
    'vuiList',
]
struct_ARVuiInfoList._fields_ = [
    ('numItems', c_uint),
    ('vuiList', POINTER(ARVuiInfoStruct)),
]

ARVuiInfoList = struct_ARVuiInfoList # /opt/dockethead/include/ar.h: 6372

# /opt/dockethead/include/ar.h: 6536
class union_anon_24(Union):
    pass

union_anon_24.__slots__ = [
    'charBuffer',
    'fileName',
    'url',
]
union_anon_24._fields_ = [
    ('charBuffer', String),
    ('fileName', String),
    ('url', String),
]

# /opt/dockethead/include/ar.h: 6543
class struct_ARXMLInputDoc(Structure):
    pass

struct_ARXMLInputDoc.__slots__ = [
    'docType',
    'u',
]
struct_ARXMLInputDoc._fields_ = [
    ('docType', c_uint),
    ('u', union_anon_24),
]

ARXMLInputDoc = struct_ARXMLInputDoc # /opt/dockethead/include/ar.h: 6543

# /opt/dockethead/include/ar.h: 6548
class union_anon_25(Union):
    pass

union_anon_25.__slots__ = [
    'charBuffer',
    'fileName',
    'fileHandle',
]
union_anon_25._fields_ = [
    ('charBuffer', String),
    ('fileName', String),
    ('fileHandle', c_uint),
]

# /opt/dockethead/include/ar.h: 6555
class struct_ARXMLOutputDoc(Structure):
    pass

struct_ARXMLOutputDoc.__slots__ = [
    'docType',
    'u',
]
struct_ARXMLOutputDoc._fields_ = [
    ('docType', c_uint),
    ('u', union_anon_25),
]

ARXMLOutputDoc = struct_ARXMLOutputDoc # /opt/dockethead/include/ar.h: 6555

# /opt/dockethead/include/ar.h: 6561
class struct_ARXMLParsedStream(Structure):
    pass

struct_ARXMLParsedStream.__slots__ = [
    'xmlStream',
]
struct_ARXMLParsedStream._fields_ = [
    ('xmlStream', POINTER(None)),
]

ARXMLParsedStream = struct_ARXMLParsedStream # /opt/dockethead/include/ar.h: 6561

# /opt/dockethead/include/ar.h: 6567
class struct_ARXMLParserHandle(Structure):
    pass

struct_ARXMLParserHandle.__slots__ = [
    'handle',
]
struct_ARXMLParserHandle._fields_ = [
    ('handle', POINTER(None)),
]

ARXMLParserHandle = struct_ARXMLParserHandle # /opt/dockethead/include/ar.h: 6567

# /opt/dockethead/include/ar.h: 6623
class struct_ARDateStruct(Structure):
    pass

struct_ARDateStruct.__slots__ = [
    'year',
    'month',
    'day',
]
struct_ARDateStruct._fields_ = [
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
]

ARDateStruct = struct_ARDateStruct # /opt/dockethead/include/ar.h: 6623

# /opt/dockethead/include/ar.h: 6713
class struct_ARComplexEntryGetIn(Structure):
    pass

# /opt/dockethead/include/ar.h: 6741
class struct_ARComplexEntryGetOut(Structure):
    pass

# /opt/dockethead/include/ar.h: 6758
class struct_ARComplexEntryCreate(Structure):
    pass

# /opt/dockethead/include/ar.h: 6780
class struct_ARComplexEntrySet(Structure):
    pass

# /opt/dockethead/include/ar.h: 6810
class struct_ARComplexEntryService(Structure):
    pass

# /opt/dockethead/include/ar.h: 6828
class struct_ARComplexEntryServiceOut(Structure):
    pass

# /opt/dockethead/include/ar.h: 6710
class struct_ARComplexEntryGetInList(Structure):
    pass

struct_ARComplexEntryGetInList.__slots__ = [
    'numItems',
    'list',
]
struct_ARComplexEntryGetInList._fields_ = [
    ('numItems', c_uint),
    ('list', POINTER(struct_ARComplexEntryGetIn)),
]

ARComplexEntryGetInList = struct_ARComplexEntryGetInList # /opt/dockethead/include/ar.h: 6710

struct_ARComplexEntryGetIn.__slots__ = [
    'qualifier',
    'docMappingName',
    'portName',
    'operationName',
    'inputMappingName',
    'outputMappingName',
    'formName',
    'mapType',
    'primaryKeyId',
    'distinguishingKeyId',
    'foreignKeyId',
    'fieldIdList',
    'complexChildren',
]
struct_ARComplexEntryGetIn._fields_ = [
    ('qualifier', ARQualifierStruct),
    ('docMappingName', ARNameType),
    ('portName', ARNameType),
    ('operationName', ARNameType),
    ('inputMappingName', ARNameType),
    ('outputMappingName', ARNameType),
    ('formName', ARNameType),
    ('mapType', c_int),
    ('primaryKeyId', ARInternalId),
    ('distinguishingKeyId', ARInternalId),
    ('foreignKeyId', ARInternalId),
    ('fieldIdList', ARInternalIdList),
    ('complexChildren', ARComplexEntryGetInList),
]

ARComplexEntryGetIn = struct_ARComplexEntryGetIn # /opt/dockethead/include/ar.h: 6729

# /opt/dockethead/include/ar.h: 6738
class struct_ARComplexEntryGetOutList(Structure):
    pass

struct_ARComplexEntryGetOutList.__slots__ = [
    'numItems',
    'list',
]
struct_ARComplexEntryGetOutList._fields_ = [
    ('numItems', c_uint),
    ('list', POINTER(struct_ARComplexEntryGetOut)),
]

ARComplexEntryGetOutList = struct_ARComplexEntryGetOutList # /opt/dockethead/include/ar.h: 6738

struct_ARComplexEntryGetOut.__slots__ = [
    'entryId',
    'fieldValueList',
    'numLists',
    'complexChildrenLists',
]
struct_ARComplexEntryGetOut._fields_ = [
    ('entryId', AREntryIdList),
    ('fieldValueList', ARFieldValueList),
    ('numLists', c_uint),
    ('complexChildrenLists', POINTER(ARComplexEntryGetOutList)),
]

ARComplexEntryGetOut = struct_ARComplexEntryGetOut # /opt/dockethead/include/ar.h: 6748

# /opt/dockethead/include/ar.h: 6756
class struct_ARComplexEntryCreateList(Structure):
    pass

struct_ARComplexEntryCreateList.__slots__ = [
    'numItems',
    'list',
]
struct_ARComplexEntryCreateList._fields_ = [
    ('numItems', c_uint),
    ('list', POINTER(struct_ARComplexEntryCreate)),
]

ARComplexEntryCreateList = struct_ARComplexEntryCreateList # /opt/dockethead/include/ar.h: 6756

struct_ARComplexEntryCreate.__slots__ = [
    'formName',
    'serverName',
    'foreignKeyFieldId',
    'parent',
    'children',
    'fieldValueList',
    'primaryKey',
    'distinguishingKey',
    'entryId',
]
struct_ARComplexEntryCreate._fields_ = [
    ('formName', ARNameType),
    ('serverName', ARServerNameType),
    ('foreignKeyFieldId', ARInternalId),
    ('parent', POINTER(struct_ARComplexEntryCreate)),
    ('children', ARComplexEntryCreateList),
    ('fieldValueList', ARFieldValueList),
    ('primaryKey', ARFieldValueStruct),
    ('distinguishingKey', ARFieldValueStruct),
    ('entryId', AREntryIdType),
]

ARComplexEntryCreate = struct_ARComplexEntryCreate # /opt/dockethead/include/ar.h: 6770

# /opt/dockethead/include/ar.h: 6778
class struct_ARComplexEntrySetList(Structure):
    pass

struct_ARComplexEntrySetList.__slots__ = [
    'numItems',
    'list',
]
struct_ARComplexEntrySetList._fields_ = [
    ('numItems', c_int),
    ('list', POINTER(struct_ARComplexEntrySet)),
]

ARComplexEntrySetList = struct_ARComplexEntrySetList # /opt/dockethead/include/ar.h: 6778

struct_ARComplexEntrySet.__slots__ = [
    'formName',
    'serverName',
    'primaryKey',
    'distinguishingKey',
    'foreignKeyFieldId',
    'parent',
    'children',
    'fieldValueList',
]
struct_ARComplexEntrySet._fields_ = [
    ('formName', ARNameType),
    ('serverName', ARServerNameType),
    ('primaryKey', ARFieldValueStruct),
    ('distinguishingKey', ARFieldValueStruct),
    ('foreignKeyFieldId', ARInternalId),
    ('parent', POINTER(struct_ARComplexEntrySet)),
    ('children', ARComplexEntrySetList),
    ('fieldValueList', ARFieldValueList),
]

ARComplexEntrySet = struct_ARComplexEntrySet # /opt/dockethead/include/ar.h: 6791

# /opt/dockethead/include/ar.h: 6802
class struct_ARComplexEntryOptions(Structure):
    pass

struct_ARComplexEntryOptions.__slots__ = [
    'getEntries',
    'startAt',
    'setEntries',
    'setFullDocument',
    'mergeOption',
    'mergeQualifier',
]
struct_ARComplexEntryOptions._fields_ = [
    ('getEntries', c_int),
    ('startAt', c_int),
    ('setEntries', c_int),
    ('setFullDocument', c_int),
    ('mergeOption', c_int),
    ('mergeQualifier', ARInternalIdList),
]

ARComplexEntryOptions = struct_ARComplexEntryOptions # /opt/dockethead/include/ar.h: 6802

# /opt/dockethead/include/ar.h: 6808
class struct_ARComplexEntryServiceList(Structure):
    pass

struct_ARComplexEntryServiceList.__slots__ = [
    'numItems',
    'list',
]
struct_ARComplexEntryServiceList._fields_ = [
    ('numItems', c_uint),
    ('list', POINTER(struct_ARComplexEntryService)),
]

ARComplexEntryServiceList = struct_ARComplexEntryServiceList # /opt/dockethead/include/ar.h: 6808

struct_ARComplexEntryService.__slots__ = [
    'formName',
    'serverName',
    'primaryKey',
    'distinguishingKey',
    'foreignKeyFieldId',
    'parent',
    'children',
    'fieldValueList',
]
struct_ARComplexEntryService._fields_ = [
    ('formName', ARNameType),
    ('serverName', ARServerNameType),
    ('primaryKey', ARFieldValueStruct),
    ('distinguishingKey', ARFieldValueStruct),
    ('foreignKeyFieldId', ARInternalId),
    ('parent', POINTER(struct_ARComplexEntryService)),
    ('children', ARComplexEntryServiceList),
    ('fieldValueList', ARFieldValueList),
]

ARComplexEntryService = struct_ARComplexEntryService # /opt/dockethead/include/ar.h: 6820

# /opt/dockethead/include/ar.h: 6826
class struct_ARComplexEntryServiceOutList(Structure):
    pass

struct_ARComplexEntryServiceOutList.__slots__ = [
    'numItems',
    'list',
]
struct_ARComplexEntryServiceOutList._fields_ = [
    ('numItems', c_uint),
    ('list', POINTER(struct_ARComplexEntryServiceOut)),
]

ARComplexEntryServiceOutList = struct_ARComplexEntryServiceOutList # /opt/dockethead/include/ar.h: 6826

struct_ARComplexEntryServiceOut.__slots__ = [
    'entryId',
    'fieldValueList',
    'numLists',
    'complexChildrenList',
]
struct_ARComplexEntryServiceOut._fields_ = [
    ('entryId', AREntryIdList),
    ('fieldValueList', ARFieldValueList),
    ('numLists', c_uint),
    ('complexChildrenList', POINTER(ARComplexEntryServiceOutList)),
]

ARComplexEntryServiceOut = struct_ARComplexEntryServiceOut # /opt/dockethead/include/ar.h: 6834

# /opt/dockethead/include/ar.h: 6841
class struct_ARXMLValueInfoStruct(Structure):
    pass

struct_ARXMLValueInfoStruct.__slots__ = [
    'infoType',
    'value',
]
struct_ARXMLValueInfoStruct._fields_ = [
    ('infoType', c_int),
    ('value', ARValueStruct),
]

ARXMLValueInfoStruct = struct_ARXMLValueInfoStruct # /opt/dockethead/include/ar.h: 6841

# /opt/dockethead/include/ar.h: 6848
class struct_ARXMLValueInfoList(Structure):
    pass

struct_ARXMLValueInfoList.__slots__ = [
    'numItems',
    'infoList',
]
struct_ARXMLValueInfoList._fields_ = [
    ('numItems', c_int),
    ('infoList', POINTER(struct_ARXMLValueInfoStruct)),
]

ARXMLValueInfoList = struct_ARXMLValueInfoList # /opt/dockethead/include/ar.h: 6848

# /opt/dockethead/include/ar.h: 6865
class struct_ARObjectInfoStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 6863
class struct_ARObjectInfoList(Structure):
    pass

struct_ARObjectInfoList.__slots__ = [
    'numItems',
    'objectInfoList',
]
struct_ARObjectInfoList._fields_ = [
    ('numItems', c_uint),
    ('objectInfoList', POINTER(struct_ARObjectInfoStruct)),
]

ARObjectInfoList = struct_ARObjectInfoList # /opt/dockethead/include/ar.h: 6863

struct_ARObjectInfoStruct.__slots__ = [
    'type',
    'subType',
    'name',
    'appBlockName',
    'objectInfoList',
]
struct_ARObjectInfoStruct._fields_ = [
    ('type', c_uint),
    ('subType', c_uint),
    ('name', ARNameType),
    ('appBlockName', ARNameType),
    ('objectInfoList', struct_ARObjectInfoList),
]

ARObjectInfoStruct = struct_ARObjectInfoStruct # /opt/dockethead/include/ar.h: 6876

# /opt/dockethead/include/ar.h: 6899
class struct_AREntryReturn(Structure):
    pass

struct_AREntryReturn.__slots__ = [
    'entryId',
    'status',
]
struct_AREntryReturn._fields_ = [
    ('entryId', AREntryIdType),
    ('status', ARStatusList),
]

AREntryReturn = struct_AREntryReturn # /opt/dockethead/include/ar.h: 6899

# /opt/dockethead/include/ar.h: 6905
class struct_ARXMLEntryReturn(Structure):
    pass

struct_ARXMLEntryReturn.__slots__ = [
    'outputDoc',
    'status',
]
struct_ARXMLEntryReturn._fields_ = [
    ('outputDoc', String),
    ('status', ARStatusList),
]

ARXMLEntryReturn = struct_ARXMLEntryReturn # /opt/dockethead/include/ar.h: 6905

# /opt/dockethead/include/ar.h: 6910
class union_anon_26(Union):
    pass

union_anon_26.__slots__ = [
    'createEntryReturn',
    'setEntryReturn',
    'deleteEntryReturn',
    'mergeEntryReturn',
    'xmlCreateEntryReturn',
    'xmlSetEntryReturn',
    'xmlDeleteEntryReturn',
]
union_anon_26._fields_ = [
    ('createEntryReturn', AREntryReturn),
    ('setEntryReturn', ARStatusList),
    ('deleteEntryReturn', ARStatusList),
    ('mergeEntryReturn', AREntryReturn),
    ('xmlCreateEntryReturn', ARXMLEntryReturn),
    ('xmlSetEntryReturn', ARXMLEntryReturn),
    ('xmlDeleteEntryReturn', ARStatusList),
]

# /opt/dockethead/include/ar.h: 6920
class struct_ARBulkEntryReturn(Structure):
    pass

struct_ARBulkEntryReturn.__slots__ = [
    'entryCallType',
    'u',
]
struct_ARBulkEntryReturn._fields_ = [
    ('entryCallType', c_uint),
    ('u', union_anon_26),
]

ARBulkEntryReturn = struct_ARBulkEntryReturn # /opt/dockethead/include/ar.h: 6920

# /opt/dockethead/include/ar.h: 6926
class struct_ARBulkEntryReturnList(Structure):
    pass

struct_ARBulkEntryReturnList.__slots__ = [
    'numItems',
    'entryReturnList',
]
struct_ARBulkEntryReturnList._fields_ = [
    ('numItems', c_uint),
    ('entryReturnList', POINTER(ARBulkEntryReturn)),
]

ARBulkEntryReturnList = struct_ARBulkEntryReturnList # /opt/dockethead/include/ar.h: 6926

# /opt/dockethead/include/ar.h: 6933
class struct_AREntryBlockStruct(Structure):
    pass

struct_AREntryBlockStruct.__slots__ = [
    'blockSize',
    'entryBlock',
]
struct_AREntryBlockStruct._fields_ = [
    ('blockSize', c_uint),
    ('entryBlock', POINTER(c_ubyte)),
]

AREntryBlockStruct = struct_AREntryBlockStruct # /opt/dockethead/include/ar.h: 6933

# /opt/dockethead/include/ar.h: 6938
class struct_AREntryBlockList(Structure):
    pass

struct_AREntryBlockList.__slots__ = [
    'numItems',
    'entryBlockList',
]
struct_AREntryBlockList._fields_ = [
    ('numItems', c_uint),
    ('entryBlockList', POINTER(AREntryBlockStruct)),
]

AREntryBlockList = struct_AREntryBlockList # /opt/dockethead/include/ar.h: 6938

# /opt/dockethead/include/ar.h: 6970
class struct_ARImageDataStruct(Structure):
    pass

struct_ARImageDataStruct.__slots__ = [
    'numItems',
    'bytes',
]
struct_ARImageDataStruct._fields_ = [
    ('numItems', c_uint),
    ('bytes', POINTER(c_ubyte)),
]

ARImageDataStruct = struct_ARImageDataStruct # /opt/dockethead/include/ar.h: 6970

# /opt/dockethead/include/ar.h: 6977
class struct_ARImageDataList(Structure):
    pass

struct_ARImageDataList.__slots__ = [
    'numItems',
    'imageList',
]
struct_ARImageDataList._fields_ = [
    ('numItems', c_uint),
    ('imageList', POINTER(ARImageDataStruct)),
]

ARImageDataList = struct_ARImageDataList # /opt/dockethead/include/ar.h: 6977

# /opt/dockethead/include/ar.h: 6985
class struct_ARObjectChangeTimestamps(Structure):
    pass

struct_ARObjectChangeTimestamps.__slots__ = [
    'objectType',
    'createTime',
    'changeTime',
    'deleteTime',
]
struct_ARObjectChangeTimestamps._fields_ = [
    ('objectType', c_uint),
    ('createTime', ARTimestamp),
    ('changeTime', ARTimestamp),
    ('deleteTime', ARTimestamp),
]

ARObjectChangeTimestamps = struct_ARObjectChangeTimestamps # /opt/dockethead/include/ar.h: 6985

# /opt/dockethead/include/ar.h: 6991
class struct_ARObjectChangeTimestampList(Structure):
    pass

struct_ARObjectChangeTimestampList.__slots__ = [
    'numItems',
    'objectChanges',
]
struct_ARObjectChangeTimestampList._fields_ = [
    ('numItems', c_uint),
    ('objectChanges', POINTER(ARObjectChangeTimestamps)),
]

ARObjectChangeTimestampList = struct_ARObjectChangeTimestampList # /opt/dockethead/include/ar.h: 6991

# /opt/dockethead/include/ar.h: 7032
class struct_ARFilterContextStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7033
class struct_ARSchemaContextStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7019
class struct_ARWfdCurrentLocation(Structure):
    pass

struct_ARWfdCurrentLocation.__slots__ = [
    'ApiCall',
    'SchemaName',
    'Entrys',
    'Filter',
    'Stage',
    'ElsePath',
    'ActionNo',
    'ActionStr',
    'ActionDeferred',
    'filtContext',
    'schemaContext',
    'next',
]
struct_ARWfdCurrentLocation._fields_ = [
    ('ApiCall', String),
    ('SchemaName', String),
    ('Entrys', AREntryIdList),
    ('Filter', String),
    ('Stage', c_uint),
    ('ElsePath', ARBoolean),
    ('ActionNo', c_uint),
    ('ActionStr', String),
    ('ActionDeferred', ARBoolean),
    ('filtContext', POINTER(struct_ARFilterContextStruct)),
    ('schemaContext', POINTER(struct_ARSchemaContextStruct)),
    ('next', POINTER(struct_ARWfdCurrentLocation)),
]

ARWfdCurrentLocation = struct_ARWfdCurrentLocation # /opt/dockethead/include/ar.h: 7035

# /opt/dockethead/include/ar.h: 7047
class struct_ARWfdRmtBreakpoint(Structure):
    pass

struct_ARWfdRmtBreakpoint.__slots__ = [
    'id',
    'disable',
    'passcount',
    'bpQualifier',
    'filter',
    'schema',
    'stage',
    'actioNo',
    'elsePath',
]
struct_ARWfdRmtBreakpoint._fields_ = [
    ('id', c_uint),
    ('disable', ARBoolean),
    ('passcount', c_uint),
    ('bpQualifier', POINTER(struct_ARQualifierStruct)),
    ('filter', POINTER(ARNameType)),
    ('schema', POINTER(ARNameType)),
    ('stage', c_uint),
    ('actioNo', c_uint),
    ('elsePath', ARBoolean),
]

ARWfdRmtBreakpoint = struct_ARWfdRmtBreakpoint # /opt/dockethead/include/ar.h: 7047

# /opt/dockethead/include/ar.h: 7053
class struct_ARWfdRmtBreakpointList(Structure):
    pass

struct_ARWfdRmtBreakpointList.__slots__ = [
    'numItems',
    'bpList',
]
struct_ARWfdRmtBreakpointList._fields_ = [
    ('numItems', c_uint),
    ('bpList', POINTER(struct_ARWfdRmtBreakpoint)),
]

ARWfdRmtBreakpointList = struct_ARWfdRmtBreakpointList # /opt/dockethead/include/ar.h: 7053

# /opt/dockethead/include/ar.h: 7055
class struct_ARWfdBreakpointLink(Structure):
    pass

struct_ARWfdBreakpointLink.__slots__ = [
    'next',
    'timesPassed',
    'bp',
]
struct_ARWfdBreakpointLink._fields_ = [
    ('next', POINTER(struct_ARWfdBreakpointLink)),
    ('timesPassed', c_uint),
    ('bp', ARWfdRmtBreakpoint),
]

ARWfdBreakpointLink = struct_ARWfdBreakpointLink # /opt/dockethead/include/ar.h: 7062

# /opt/dockethead/include/ar.h: 7074
class struct_ARWfdUserContext(Structure):
    pass

struct_ARWfdUserContext.__slots__ = [
    'user',
    'notifyMech',
    'licenseList',
    'licenseType',
    'currentLicenseType',
    'doWorkflowFTS',
    'groupList',
    'adminFlag',
    'subadminFlag',
]
struct_ARWfdUserContext._fields_ = [
    ('user', ARAccessNameType),
    ('notifyMech', c_uint),
    ('licenseList', struct_ARUserLicenseList),
    ('licenseType', c_uint),
    ('currentLicenseType', c_uint),
    ('doWorkflowFTS', ARBoolean),
    ('groupList', struct_ARInternalIdList),
    ('adminFlag', ARBoolean),
    ('subadminFlag', ARBoolean),
]

ARWfdUserContext = struct_ARWfdUserContext # /opt/dockethead/include/ar.h: 7074

# /opt/dockethead/include/ar.h: 7090
class struct_ARMultiSchemaFieldIdStruct(Structure):
    pass

struct_ARMultiSchemaFieldIdStruct.__slots__ = [
    'queryFromAlias',
    'fieldId',
]
struct_ARMultiSchemaFieldIdStruct._fields_ = [
    ('queryFromAlias', ARNameType),
    ('fieldId', ARInternalId),
]

ARMultiSchemaFieldIdStruct = struct_ARMultiSchemaFieldIdStruct # /opt/dockethead/include/ar.h: 7090

# /opt/dockethead/include/ar.h: 7105
class struct_ARMultiSchemaFieldFuncStruct(Structure):
    pass

struct_ARMultiSchemaFieldFuncStruct.__slots__ = [
    'queryFromAlias',
    'fieldId',
    'funcId',
]
struct_ARMultiSchemaFieldFuncStruct._fields_ = [
    ('queryFromAlias', ARNameType),
    ('fieldId', ARInternalId),
    ('funcId', c_int),
]

ARMultiSchemaFieldFuncStruct = struct_ARMultiSchemaFieldFuncStruct # /opt/dockethead/include/ar.h: 7105

# /opt/dockethead/include/ar.h: 7110
class struct_ARMultiSchemaFieldIdList(Structure):
    pass

struct_ARMultiSchemaFieldIdList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaFieldIdList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaFieldIdStruct)),
]

ARMultiSchemaFieldIdList = struct_ARMultiSchemaFieldIdList # /opt/dockethead/include/ar.h: 7110

# /opt/dockethead/include/ar.h: 7115
class struct_ARMultiSchemaFieldFuncList(Structure):
    pass

struct_ARMultiSchemaFieldFuncList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaFieldFuncList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaFieldFuncStruct)),
]

ARMultiSchemaFieldFuncList = struct_ARMultiSchemaFieldFuncList # /opt/dockethead/include/ar.h: 7115

# /opt/dockethead/include/ar.h: 7121
class struct_ARMultiSchemaFuncCurrencyPartStruct(Structure):
    pass

struct_ARMultiSchemaFuncCurrencyPartStruct.__slots__ = [
    'fieldFunc',
    'partTag',
    'currencyCode',
]
struct_ARMultiSchemaFuncCurrencyPartStruct._fields_ = [
    ('fieldFunc', ARMultiSchemaFieldFuncStruct),
    ('partTag', c_uint),
    ('currencyCode', ARCurrencyCodeType),
]

ARMultiSchemaFuncCurrencyPartStruct = struct_ARMultiSchemaFuncCurrencyPartStruct # /opt/dockethead/include/ar.h: 7121

# /opt/dockethead/include/ar.h: 7127
class struct_ARMultiSchemaStatHistoryValue(Structure):
    pass

struct_ARMultiSchemaStatHistoryValue.__slots__ = [
    'queryFromAlias',
    'enumVal',
    'userOrTime',
]
struct_ARMultiSchemaStatHistoryValue._fields_ = [
    ('queryFromAlias', ARNameType),
    ('enumVal', c_ulong),
    ('userOrTime', c_uint),
]

ARMultiSchemaStatHistoryValue = struct_ARMultiSchemaStatHistoryValue # /opt/dockethead/include/ar.h: 7127

# /opt/dockethead/include/ar.h: 7134
class struct_ARMultiSchemaFuncStatHistoryValue(Structure):
    pass

struct_ARMultiSchemaFuncStatHistoryValue.__slots__ = [
    'queryFromAlias',
    'enumVal',
    'userOrTime',
    'funcId',
]
struct_ARMultiSchemaFuncStatHistoryValue._fields_ = [
    ('queryFromAlias', ARNameType),
    ('enumVal', c_ulong),
    ('userOrTime', c_uint),
    ('funcId', c_int),
]

ARMultiSchemaFuncStatHistoryValue = struct_ARMultiSchemaFuncStatHistoryValue # /opt/dockethead/include/ar.h: 7134

# /opt/dockethead/include/ar.h: 7186
class struct_ARMultiSchemaArithOpStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7322
class struct_ARMultiSchemaValueSetFuncQueryStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7143
class union_anon_27(Union):
    pass

union_anon_27.__slots__ = [
    'noval_',
    'fieldId',
    'value',
    'arithOp',
    'statHistory',
    'valueSet',
    'currencyField',
    'valueSetQuery',
]
union_anon_27._fields_ = [
    ('noval_', c_size_t),
    ('fieldId', ARMultiSchemaFieldIdStruct),
    ('value', ARValueStruct),
    ('arithOp', POINTER(struct_ARMultiSchemaArithOpStruct)),
    ('statHistory', ARMultiSchemaFuncStatHistoryValue),
    ('valueSet', ARValueList),
    ('currencyField', POINTER(ARMultiSchemaFuncCurrencyPartStruct)),
    ('valueSetQuery', POINTER(struct_ARMultiSchemaValueSetFuncQueryStruct)),
]

# /opt/dockethead/include/ar.h: 7154
class struct_ARMultiSchemaFieldValueOrArithStruct(Structure):
    pass

struct_ARMultiSchemaFieldValueOrArithStruct.__slots__ = [
    'tag',
    'u',
]
struct_ARMultiSchemaFieldValueOrArithStruct._fields_ = [
    ('tag', c_uint),
    ('u', union_anon_27),
]

ARMultiSchemaFieldValueOrArithStruct = struct_ARMultiSchemaFieldValueOrArithStruct # /opt/dockethead/include/ar.h: 7154

# /opt/dockethead/include/ar.h: 7192
class struct_ARMultiSchemaFuncArithOpStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7161
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'noval_',
    'fieldFunc',
    'value',
    'arithOp',
    'statHistory',
    'valueSet',
    'currencyField',
    'valueSetQuery',
]
union_anon_28._fields_ = [
    ('noval_', c_size_t),
    ('fieldFunc', ARMultiSchemaFieldFuncStruct),
    ('value', ARValueStruct),
    ('arithOp', POINTER(struct_ARMultiSchemaFuncArithOpStruct)),
    ('statHistory', ARMultiSchemaFuncStatHistoryValue),
    ('valueSet', ARValueList),
    ('currencyField', POINTER(ARMultiSchemaFuncCurrencyPartStruct)),
    ('valueSetQuery', POINTER(struct_ARMultiSchemaValueSetFuncQueryStruct)),
]

# /opt/dockethead/include/ar.h: 7171
class struct_ARMultiSchemaFieldFuncValueOrArithStruct(Structure):
    pass

struct_ARMultiSchemaFieldFuncValueOrArithStruct.__slots__ = [
    'tag',
    'u',
]
struct_ARMultiSchemaFieldFuncValueOrArithStruct._fields_ = [
    ('tag', c_uint),
    ('u', union_anon_28),
]

ARMultiSchemaFieldFuncValueOrArithStruct = struct_ARMultiSchemaFieldFuncValueOrArithStruct # /opt/dockethead/include/ar.h: 7171

# /opt/dockethead/include/ar.h: 7210
class struct_ARMultiSchemaQualifierStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7178
class struct_ARMultiSchemaAndOrStruct(Structure):
    pass

struct_ARMultiSchemaAndOrStruct.__slots__ = [
    'operandLeft',
    'operandRight',
]
struct_ARMultiSchemaAndOrStruct._fields_ = [
    ('operandLeft', POINTER(struct_ARMultiSchemaQualifierStruct)),
    ('operandRight', POINTER(struct_ARMultiSchemaQualifierStruct)),
]

ARMultiSchemaAndOrStruct = struct_ARMultiSchemaAndOrStruct # /opt/dockethead/include/ar.h: 7178

# /opt/dockethead/include/ar.h: 7220
class struct_ARMultiSchemaFuncQualifierStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7184
class struct_ARMultiSchemaFuncAndOrStruct(Structure):
    pass

struct_ARMultiSchemaFuncAndOrStruct.__slots__ = [
    'operandLeft',
    'operandRight',
]
struct_ARMultiSchemaFuncAndOrStruct._fields_ = [
    ('operandLeft', POINTER(struct_ARMultiSchemaFuncQualifierStruct)),
    ('operandRight', POINTER(struct_ARMultiSchemaFuncQualifierStruct)),
]

ARMultiSchemaFuncAndOrStruct = struct_ARMultiSchemaFuncAndOrStruct # /opt/dockethead/include/ar.h: 7184

struct_ARMultiSchemaArithOpStruct.__slots__ = [
    'operation',
    'operandLeft',
    'operandRight',
]
struct_ARMultiSchemaArithOpStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARMultiSchemaFieldValueOrArithStruct),
    ('operandRight', ARMultiSchemaFieldValueOrArithStruct),
]

ARMultiSchemaArithOpStruct = struct_ARMultiSchemaArithOpStruct # /opt/dockethead/include/ar.h: 7190

struct_ARMultiSchemaFuncArithOpStruct.__slots__ = [
    'operation',
    'operandLeft',
    'operandRight',
]
struct_ARMultiSchemaFuncArithOpStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARMultiSchemaFieldFuncValueOrArithStruct),
    ('operandRight', ARMultiSchemaFieldFuncValueOrArithStruct),
]

ARMultiSchemaFuncArithOpStruct = struct_ARMultiSchemaFuncArithOpStruct # /opt/dockethead/include/ar.h: 7196

# /opt/dockethead/include/ar.h: 7202
class struct_ARMultiSchemaRelOpStruct(Structure):
    pass

struct_ARMultiSchemaRelOpStruct.__slots__ = [
    'operation',
    'operandLeft',
    'operandRight',
]
struct_ARMultiSchemaRelOpStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARMultiSchemaFieldValueOrArithStruct),
    ('operandRight', ARMultiSchemaFieldValueOrArithStruct),
]

ARMultiSchemaRelOpStruct = struct_ARMultiSchemaRelOpStruct # /opt/dockethead/include/ar.h: 7202

# /opt/dockethead/include/ar.h: 7208
class struct_ARMultiSchemaFuncRelOpStruct(Structure):
    pass

struct_ARMultiSchemaFuncRelOpStruct.__slots__ = [
    'operation',
    'operandLeft',
    'operandRight',
]
struct_ARMultiSchemaFuncRelOpStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARMultiSchemaFieldFuncValueOrArithStruct),
    ('operandRight', ARMultiSchemaFieldFuncValueOrArithStruct),
]

ARMultiSchemaFuncRelOpStruct = struct_ARMultiSchemaFuncRelOpStruct # /opt/dockethead/include/ar.h: 7208

# /opt/dockethead/include/ar.h: 7212
class union_anon_29(Union):
    pass

union_anon_29.__slots__ = [
    'andor',
    'notQual',
    'relOp',
    'fieldId',
]
union_anon_29._fields_ = [
    ('andor', ARMultiSchemaAndOrStruct),
    ('notQual', POINTER(struct_ARMultiSchemaQualifierStruct)),
    ('relOp', POINTER(struct_ARMultiSchemaRelOpStruct)),
    ('fieldId', ARMultiSchemaFieldIdStruct),
]

struct_ARMultiSchemaQualifierStruct.__slots__ = [
    'operation',
    'u',
]
struct_ARMultiSchemaQualifierStruct._fields_ = [
    ('operation', c_uint),
    ('u', union_anon_29),
]

ARMultiSchemaQualifierStruct = struct_ARMultiSchemaQualifierStruct # /opt/dockethead/include/ar.h: 7218

# /opt/dockethead/include/ar.h: 7222
class union_anon_30(Union):
    pass

union_anon_30.__slots__ = [
    'andor',
    'notQual',
    'relOp',
    'fieldFunc',
]
union_anon_30._fields_ = [
    ('andor', ARMultiSchemaFuncAndOrStruct),
    ('notQual', POINTER(struct_ARMultiSchemaFuncQualifierStruct)),
    ('relOp', POINTER(struct_ARMultiSchemaFuncRelOpStruct)),
    ('fieldFunc', ARMultiSchemaFieldFuncStruct),
]

struct_ARMultiSchemaFuncQualifierStruct.__slots__ = [
    'operation',
    'u',
]
struct_ARMultiSchemaFuncQualifierStruct._fields_ = [
    ('operation', c_uint),
    ('u', union_anon_30),
]

ARMultiSchemaFuncQualifierStruct = struct_ARMultiSchemaFuncQualifierStruct # /opt/dockethead/include/ar.h: 7228

# /opt/dockethead/include/ar.h: 7302
class struct_ARMultiSchemaNestedQueryStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7282
class struct_ARMultiSchemaRecursiveQueryStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7242
class union_anon_31(Union):
    pass

union_anon_31.__slots__ = [
    'schemaName',
    'nestedQuery',
    'recursiveQuery',
]
union_anon_31._fields_ = [
    ('schemaName', ARNameType),
    ('nestedQuery', POINTER(struct_ARMultiSchemaNestedQueryStruct)),
    ('recursiveQuery', POINTER(struct_ARMultiSchemaRecursiveQueryStruct)),
]

# /opt/dockethead/include/ar.h: 7251
class struct_ARMultiSchemaQueryFromStruct(Structure):
    pass

struct_ARMultiSchemaQueryFromStruct.__slots__ = [
    'type',
    'u',
    'queryFromAlias',
    'joinType',
    'joinQual',
]
struct_ARMultiSchemaQueryFromStruct._fields_ = [
    ('type', c_uint),
    ('u', union_anon_31),
    ('queryFromAlias', ARNameType),
    ('joinType', c_uint),
    ('joinQual', POINTER(struct_ARMultiSchemaQualifierStruct)),
]

ARMultiSchemaQueryFromStruct = struct_ARMultiSchemaQueryFromStruct # /opt/dockethead/include/ar.h: 7251

# /opt/dockethead/include/ar.h: 7308
class struct_ARMultiSchemaNestedFuncQueryStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7291
class struct_ARMultiSchemaRecursiveFuncQueryStruct(Structure):
    pass

# /opt/dockethead/include/ar.h: 7255
class union_anon_32(Union):
    pass

union_anon_32.__slots__ = [
    'schemaName',
    'nestedQuery',
    'recursiveQuery',
]
union_anon_32._fields_ = [
    ('schemaName', ARNameType),
    ('nestedQuery', POINTER(struct_ARMultiSchemaNestedFuncQueryStruct)),
    ('recursiveQuery', POINTER(struct_ARMultiSchemaRecursiveFuncQueryStruct)),
]

# /opt/dockethead/include/ar.h: 7264
class struct_ARMultiSchemaFuncQueryFromStruct(Structure):
    pass

struct_ARMultiSchemaFuncQueryFromStruct.__slots__ = [
    'type',
    'u',
    'queryFromAlias',
    'joinType',
    'joinQual',
]
struct_ARMultiSchemaFuncQueryFromStruct._fields_ = [
    ('type', c_uint),
    ('u', union_anon_32),
    ('queryFromAlias', ARNameType),
    ('joinType', c_uint),
    ('joinQual', POINTER(struct_ARMultiSchemaQualifierStruct)),
]

ARMultiSchemaFuncQueryFromStruct = struct_ARMultiSchemaFuncQueryFromStruct # /opt/dockethead/include/ar.h: 7264

# /opt/dockethead/include/ar.h: 7269
class struct_ARMultiSchemaQueryFromList(Structure):
    pass

struct_ARMultiSchemaQueryFromList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaQueryFromList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaQueryFromStruct)),
]

ARMultiSchemaQueryFromList = struct_ARMultiSchemaQueryFromList # /opt/dockethead/include/ar.h: 7269

# /opt/dockethead/include/ar.h: 7274
class struct_ARMultiSchemaFuncQueryFromList(Structure):
    pass

struct_ARMultiSchemaFuncQueryFromList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaFuncQueryFromList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaFuncQueryFromStruct)),
]

ARMultiSchemaFuncQueryFromList = struct_ARMultiSchemaFuncQueryFromList # /opt/dockethead/include/ar.h: 7274

struct_ARMultiSchemaRecursiveQueryStruct.__slots__ = [
    'recursiveSchemaAlias',
    'queryFromList',
    'getListFields',
    'startQual',
    'recursionQual',
    'levelsToRetrieve',
]
struct_ARMultiSchemaRecursiveQueryStruct._fields_ = [
    ('recursiveSchemaAlias', ARNameType),
    ('queryFromList', ARMultiSchemaQueryFromList),
    ('getListFields', ARMultiSchemaFieldIdList),
    ('startQual', POINTER(ARMultiSchemaQualifierStruct)),
    ('recursionQual', POINTER(ARMultiSchemaQualifierStruct)),
    ('levelsToRetrieve', c_int),
]

ARMultiSchemaRecursiveQueryStruct = struct_ARMultiSchemaRecursiveQueryStruct # /opt/dockethead/include/ar.h: 7289

struct_ARMultiSchemaRecursiveFuncQueryStruct.__slots__ = [
    'recursiveSchemaAlias',
    'queryFromList',
    'getListFuncs',
    'startQual',
    'recursionQual',
    'levelsToRetrieve',
    'groupBy',
    'having',
]
struct_ARMultiSchemaRecursiveFuncQueryStruct._fields_ = [
    ('recursiveSchemaAlias', ARNameType),
    ('queryFromList', ARMultiSchemaFuncQueryFromList),
    ('getListFuncs', ARMultiSchemaFieldFuncList),
    ('startQual', POINTER(ARMultiSchemaQualifierStruct)),
    ('recursionQual', POINTER(ARMultiSchemaQualifierStruct)),
    ('levelsToRetrieve', c_int),
    ('groupBy', ARMultiSchemaFieldIdList),
    ('having', POINTER(ARMultiSchemaFuncQualifierStruct)),
]

ARMultiSchemaRecursiveFuncQueryStruct = struct_ARMultiSchemaRecursiveFuncQueryStruct # /opt/dockethead/include/ar.h: 7300

struct_ARMultiSchemaNestedQueryStruct.__slots__ = [
    'queryFromList',
    'getListFields',
    'qualifier',
]
struct_ARMultiSchemaNestedQueryStruct._fields_ = [
    ('queryFromList', ARMultiSchemaQueryFromList),
    ('getListFields', ARMultiSchemaFieldIdList),
    ('qualifier', POINTER(ARMultiSchemaQualifierStruct)),
]

ARMultiSchemaNestedQueryStruct = struct_ARMultiSchemaNestedQueryStruct # /opt/dockethead/include/ar.h: 7306

struct_ARMultiSchemaNestedFuncQueryStruct.__slots__ = [
    'queryFromList',
    'getListFuncs',
    'qualifier',
    'groupBy',
    'having',
]
struct_ARMultiSchemaNestedFuncQueryStruct._fields_ = [
    ('queryFromList', ARMultiSchemaFuncQueryFromList),
    ('getListFuncs', ARMultiSchemaFieldFuncList),
    ('qualifier', POINTER(ARMultiSchemaQualifierStruct)),
    ('groupBy', ARMultiSchemaFieldIdList),
    ('having', POINTER(ARMultiSchemaFuncQualifierStruct)),
]

ARMultiSchemaNestedFuncQueryStruct = struct_ARMultiSchemaNestedFuncQueryStruct # /opt/dockethead/include/ar.h: 7314

# /opt/dockethead/include/ar.h: 7320
class struct_ARMultiSchemaValueSetQueryStruct(Structure):
    pass

struct_ARMultiSchemaValueSetQueryStruct.__slots__ = [
    'queryFromList',
    'fieldId',
    'qualifier',
]
struct_ARMultiSchemaValueSetQueryStruct._fields_ = [
    ('queryFromList', ARMultiSchemaQueryFromList),
    ('fieldId', ARMultiSchemaFieldIdStruct),
    ('qualifier', POINTER(ARMultiSchemaQualifierStruct)),
]

ARMultiSchemaValueSetQueryStruct = struct_ARMultiSchemaValueSetQueryStruct # /opt/dockethead/include/ar.h: 7320

struct_ARMultiSchemaValueSetFuncQueryStruct.__slots__ = [
    'queryFromList',
    'fieldId',
    'qualifier',
    'groupBy',
    'having',
]
struct_ARMultiSchemaValueSetFuncQueryStruct._fields_ = [
    ('queryFromList', ARMultiSchemaFuncQueryFromList),
    ('fieldId', ARMultiSchemaFieldIdStruct),
    ('qualifier', POINTER(ARMultiSchemaQualifierStruct)),
    ('groupBy', ARMultiSchemaFieldIdList),
    ('having', POINTER(ARMultiSchemaFuncQualifierStruct)),
]

ARMultiSchemaValueSetFuncQueryStruct = struct_ARMultiSchemaValueSetFuncQueryStruct # /opt/dockethead/include/ar.h: 7328

# /opt/dockethead/include/ar.h: 7333
class struct_ARMultiSchemaSortStruct(Structure):
    pass

struct_ARMultiSchemaSortStruct.__slots__ = [
    'fieldId',
    'sortOrder',
]
struct_ARMultiSchemaSortStruct._fields_ = [
    ('fieldId', ARMultiSchemaFieldIdStruct),
    ('sortOrder', c_uint),
]

ARMultiSchemaSortStruct = struct_ARMultiSchemaSortStruct # /opt/dockethead/include/ar.h: 7333

# /opt/dockethead/include/ar.h: 7338
class struct_ARMultiSchemaSortList(Structure):
    pass

struct_ARMultiSchemaSortList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaSortList._fields_ = [
    ('numItems', c_int),
    ('listPtr', POINTER(ARMultiSchemaSortStruct)),
]

ARMultiSchemaSortList = struct_ARMultiSchemaSortList # /opt/dockethead/include/ar.h: 7338

# /opt/dockethead/include/ar.h: 7343
class struct_ARMultiSchemaFieldValueStruct(Structure):
    pass

struct_ARMultiSchemaFieldValueStruct.__slots__ = [
    'fieldId',
    'value',
]
struct_ARMultiSchemaFieldValueStruct._fields_ = [
    ('fieldId', ARMultiSchemaFieldIdStruct),
    ('value', ARValueStruct),
]

ARMultiSchemaFieldValueStruct = struct_ARMultiSchemaFieldValueStruct # /opt/dockethead/include/ar.h: 7343

# /opt/dockethead/include/ar.h: 7350
class struct_ARMultiSchemaFieldValueList(Structure):
    pass

struct_ARMultiSchemaFieldValueList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaFieldValueList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaFieldValueStruct)),
]

ARMultiSchemaFieldValueList = struct_ARMultiSchemaFieldValueList # /opt/dockethead/include/ar.h: 7350

# /opt/dockethead/include/ar.h: 7355
class struct_ARMultiSchemaFieldValueListList(Structure):
    pass

struct_ARMultiSchemaFieldValueListList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaFieldValueListList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaFieldValueList)),
]

ARMultiSchemaFieldValueListList = struct_ARMultiSchemaFieldValueListList # /opt/dockethead/include/ar.h: 7355

# /opt/dockethead/include/ar.h: 7360
class struct_ARMultiSchemaFieldFuncValueStruct(Structure):
    pass

struct_ARMultiSchemaFieldFuncValueStruct.__slots__ = [
    'fieldId',
    'value',
]
struct_ARMultiSchemaFieldFuncValueStruct._fields_ = [
    ('fieldId', ARMultiSchemaFieldFuncStruct),
    ('value', ARValueStruct),
]

ARMultiSchemaFieldFuncValueStruct = struct_ARMultiSchemaFieldFuncValueStruct # /opt/dockethead/include/ar.h: 7360

# /opt/dockethead/include/ar.h: 7365
class struct_ARMultiSchemaFieldFuncValueList(Structure):
    pass

struct_ARMultiSchemaFieldFuncValueList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaFieldFuncValueList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaFieldFuncValueStruct)),
]

ARMultiSchemaFieldFuncValueList = struct_ARMultiSchemaFieldFuncValueList # /opt/dockethead/include/ar.h: 7365

# /opt/dockethead/include/ar.h: 7370
class struct_ARMultiSchemaFieldFuncValueListList(Structure):
    pass

struct_ARMultiSchemaFieldFuncValueListList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARMultiSchemaFieldFuncValueListList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARMultiSchemaFieldFuncValueList)),
]

ARMultiSchemaFieldFuncValueListList = struct_ARMultiSchemaFieldFuncValueListList # /opt/dockethead/include/ar.h: 7370

# /opt/dockethead/include/ar.h: 7395
class struct_ARTaskCheckpointObj(Structure):
    pass

struct_ARTaskCheckpointObj.__slots__ = [
    'taskId',
    'checkpointId',
    'objName',
    'objType',
    'objOmlVersionGUID',
]
struct_ARTaskCheckpointObj._fields_ = [
    ('taskId', ARInternalId),
    ('checkpointId', ARInternalId),
    ('objName', ARNameType),
    ('objType', c_int),
    ('objOmlVersionGUID', String),
]

ARTaskCheckpointObj = struct_ARTaskCheckpointObj # /opt/dockethead/include/ar.h: 7395

# /opt/dockethead/include/ar.h: 7401
class struct_ARTaskCheckpointObjList(Structure):
    pass

struct_ARTaskCheckpointObjList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARTaskCheckpointObjList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARTaskCheckpointObj)),
]

ARTaskCheckpointObjList = struct_ARTaskCheckpointObjList # /opt/dockethead/include/ar.h: 7401

# /opt/dockethead/include/ar.h: 7411
class struct_ARTaskCheckpoint(Structure):
    pass

struct_ARTaskCheckpoint.__slots__ = [
    'taskId',
    'checkpointId',
    'checkpointName',
    'timestamp',
    'description',
    'objPropList',
    'cpObjNodeList',
]
struct_ARTaskCheckpoint._fields_ = [
    ('taskId', ARInternalId),
    ('checkpointId', ARInternalId),
    ('checkpointName', ARNameType),
    ('timestamp', ARTimestamp),
    ('description', ARTextString),
    ('objPropList', ARPropList),
    ('cpObjNodeList', ARTaskCheckpointObjList),
]

ARTaskCheckpoint = struct_ARTaskCheckpoint # /opt/dockethead/include/ar.h: 7411

# /opt/dockethead/include/ar.h: 7417
class struct_ARTaskCheckpointList(Structure):
    pass

struct_ARTaskCheckpointList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARTaskCheckpointList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARTaskCheckpoint)),
]

ARTaskCheckpointList = struct_ARTaskCheckpointList # /opt/dockethead/include/ar.h: 7417

# /opt/dockethead/include/ar.h: 7430
class struct_ARTask(Structure):
    pass

struct_ARTask.__slots__ = [
    'taskId',
    'taskName',
    'description',
    'owner',
    'lastChanged',
    'state',
    'timestamp',
    'objPropList',
    'baseline',
    'checkpointList',
]
struct_ARTask._fields_ = [
    ('taskId', ARInternalId),
    ('taskName', ARNameType),
    ('description', ARTextString),
    ('owner', ARAccessNameType),
    ('lastChanged', ARAccessNameType),
    ('state', c_int),
    ('timestamp', ARTimestamp),
    ('objPropList', ARPropList),
    ('baseline', ARTaskCheckpoint),
    ('checkpointList', ARTaskCheckpointList),
]

ARTask = struct_ARTask # /opt/dockethead/include/ar.h: 7430

# /opt/dockethead/include/ar.h: 7436
class struct_ARTaskList(Structure):
    pass

struct_ARTaskList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARTaskList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARTask)),
]

ARTaskList = struct_ARTaskList # /opt/dockethead/include/ar.h: 7436

# /opt/dockethead/include/ar.h: 7442
class struct_ARVercntlObject(Structure):
    pass

struct_ARVercntlObject.__slots__ = [
    'objName',
    'objType',
]
struct_ARVercntlObject._fields_ = [
    ('objName', ARNameType),
    ('objType', c_int),
]

ARVercntlObject = struct_ARVercntlObject # /opt/dockethead/include/ar.h: 7442

# /opt/dockethead/include/ar.h: 7449
class struct_ARVercntlObjectList(Structure):
    pass

struct_ARVercntlObjectList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARVercntlObjectList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARVercntlObject)),
]

ARVercntlObjectList = struct_ARVercntlObjectList # /opt/dockethead/include/ar.h: 7449

# /opt/dockethead/include/ar.h: 7460
class struct_ARTaskInfo(Structure):
    pass

struct_ARTaskInfo.__slots__ = [
    'taskId',
    'taskName',
    'description',
    'owner',
    'lastChanged',
    'state',
    'timestamp',
    'objPropList',
]
struct_ARTaskInfo._fields_ = [
    ('taskId', ARInternalId),
    ('taskName', ARNameType),
    ('description', ARTextString),
    ('owner', ARAccessNameType),
    ('lastChanged', ARAccessNameType),
    ('state', c_int),
    ('timestamp', ARTimestamp),
    ('objPropList', ARPropList),
]

ARTaskInfo = struct_ARTaskInfo # /opt/dockethead/include/ar.h: 7460

# /opt/dockethead/include/ar.h: 7467
class struct_ARTaskInfoList(Structure):
    pass

struct_ARTaskInfoList.__slots__ = [
    'numItems',
    'listPtr',
]
struct_ARTaskInfoList._fields_ = [
    ('numItems', c_uint),
    ('listPtr', POINTER(ARTaskInfo)),
]

ARTaskInfoList = struct_ARTaskInfoList # /opt/dockethead/include/ar.h: 7467

# /usr/include/limits.h: 82
try:
    INT_MAX = 2147483647
except:
    pass

# /opt/dockethead/include/artypes.h: 58
try:
    ARLONG32_MAX = INT_MAX
except:
    pass

# /opt/dockethead/include/artypes.h: 147
def ARL(z):
    return z

# /opt/dockethead/include/ar.h: 17
try:
    AR_SYSTEM_NAME = 'Action Request System'
except:
    pass

# /opt/dockethead/include/ar.h: 20
try:
    AR_HOME_CONFIGDIR = 'conf'
except:
    pass

# /opt/dockethead/include/ar.h: 36
try:
    AR_HOME_CONFIGFILE = 'ar.conf'
except:
    pass

# /opt/dockethead/include/ar.h: 38
try:
    AR_HOME_DB_CONFIGFILE = 'ardb.conf'
except:
    pass

# /opt/dockethead/include/ar.h: 40
try:
    AR_HOME_DEFAULT = '/usr/ar'
except:
    pass

# /opt/dockethead/include/ar.h: 42
try:
    AR_HOME_AUDIT_CONFIGFILE = 'araudit.conf'
except:
    pass

# /opt/dockethead/include/ar.h: 44
try:
    AR_MONITOR_CONFIGFILE = 'armonitor.conf'
except:
    pass

# /opt/dockethead/include/ar.h: 48
try:
    AR_ENV_CONFIGDIR = 'ARCONFIGDIR'
except:
    pass

# /opt/dockethead/include/ar.h: 50
try:
    AR_ENV_INSTALLDIR = 'ARINSTALLDIR'
except:
    pass

# /opt/dockethead/include/ar.h: 53
try:
    AR_ENV_MONITOR_CONFIG = 'ARMCONFIGFILE'
except:
    pass

# /opt/dockethead/include/ar.h: 55
try:
    AR_MONITOR_PID = 'armonitor.pid'
except:
    pass

# /opt/dockethead/include/ar.h: 57
try:
    AR_LOG_FILE = 'ar.log'
except:
    pass

# /opt/dockethead/include/ar.h: 59
try:
    AR_DIRECTORY_FILE = 'ar'
except:
    pass

# /opt/dockethead/include/ar.h: 61
try:
    AR_APPL_AUDIT_FILE = 'appl.aud'
except:
    pass

# /opt/dockethead/include/ar.h: 63
try:
    AR_APPL_VIOLATION_FILE = 'appl.vio'
except:
    pass

# /opt/dockethead/include/ar.h: 65
try:
    AR_DIRECTORY_AR_TAG = 'AR'
except:
    pass

# /opt/dockethead/include/ar.h: 67
try:
    AR_MAX_ACTIONS = 25
except:
    pass

# /opt/dockethead/include/ar.h: 68
try:
    AR_MAX_AL_MESSAGE_SIZE = 4095
except:
    pass

# /opt/dockethead/include/ar.h: 69
try:
    AR_MAX_AUTH_SIZE = 2047
except:
    pass

# /opt/dockethead/include/ar.h: 70
try:
    AR_MAX_AUTOMATION_SIZE = 2000
except:
    pass

# /opt/dockethead/include/ar.h: 71
try:
    AR_MAX_BUFFER_SIZE = 352
except:
    pass

# /opt/dockethead/include/ar.h: 72
try:
    AR_MAX_CMENU_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 73
try:
    AR_MAX_COMMAND_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 74
try:
    AR_MAX_COMMAND_SIZE_LONG = 4096
except:
    pass

# /opt/dockethead/include/ar.h: 75
try:
    AR_MAX_FORMAT_SIZE = 32
except:
    pass

# /opt/dockethead/include/ar.h: 76
try:
    AR_MAX_DDE_ITEM = 32767
except:
    pass

# /opt/dockethead/include/ar.h: 77
try:
    AR_MAX_DDE_NAME = 64
except:
    pass

# /opt/dockethead/include/ar.h: 78
try:
    AR_MAX_COM_NAME = 1024
except:
    pass

# /opt/dockethead/include/ar.h: 79
try:
    AR_MAX_COM_METHOD_NAME = 128
except:
    pass

# /opt/dockethead/include/ar.h: 80
try:
    AR_MAX_COM_ID_SIZE = 128
except:
    pass

# /opt/dockethead/include/ar.h: 81
try:
    AR_MAX_DEFAULT_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 82
try:
    AR_MAX_EMAIL_ADDR = 255
except:
    pass

# /opt/dockethead/include/ar.h: 83
try:
    AR_MAX_ENTRYID_SIZE = 15
except:
    pass

# /opt/dockethead/include/ar.h: 84
try:
    AR_MAX_GOTOGUIDE_LABEL_SIZE = 128
except:
    pass

# /opt/dockethead/include/ar.h: 85
try:
    AR_MAX_GROUPLIST_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 86
try:
    AR_MAX_GUID_SIZE = 30
except:
    pass

# /opt/dockethead/include/ar.h: 87
try:
    AR_MAX_GUID_PREFIX_SIZE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 88
try:
    AR_MAX_INDEX_BYTES = 255
except:
    pass

# /opt/dockethead/include/ar.h: 89
try:
    AR_MAX_INDEX_FIELDS = 16
except:
    pass

# /opt/dockethead/include/ar.h: 90
try:
    AR_MAX_LANG_SIZE = 15
except:
    pass

# /opt/dockethead/include/ar.h: 91
try:
    AR_MAX_LICENSE_NAME_SIZE = 50
except:
    pass

# /opt/dockethead/include/ar.h: 92
try:
    AR_MAX_LICENSE_KEY_SIZE = 30
except:
    pass

# /opt/dockethead/include/ar.h: 93
try:
    AR_MAX_LOCALE_SIZE = 64
except:
    pass

# /opt/dockethead/include/ar.h: 94
try:
    AR_MAX_MACRO_VALUE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 95
try:
    AR_MAX_MENU_ITEMS = 199
except:
    pass

# /opt/dockethead/include/ar.h: 97
try:
    AR_MAX_MENU_LEVELS = 15
except:
    pass

# /opt/dockethead/include/ar.h: 99
try:
    AR_MAX_LEVELS_DYNAMIC_MENU = 5
except:
    pass

# /opt/dockethead/include/ar.h: 100
try:
    AR_MAX_MESSAGE_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 101
try:
    AR_MAX_MULT_ENTRIES = 100
except:
    pass

# /opt/dockethead/include/ar.h: 103
try:
    AR_MAX_NAME_SIZE = 254
except:
    pass

# /opt/dockethead/include/ar.h: 104
try:
    AR_MAX_ACCESS_NAME_SIZE = 254
except:
    pass

# /opt/dockethead/include/ar.h: 106
try:
    AR_MAX_ACCESS_NAME_SIZE_63 = 30
except:
    pass

# /opt/dockethead/include/ar.h: 107
try:
    AR_MAX_PASSWORD_SIZE = 30
except:
    pass

# /opt/dockethead/include/ar.h: 108
try:
    AR_MAX_HASH_SIZE = 28
except:
    pass

# /opt/dockethead/include/ar.h: 109
try:
    AR_MAX_ENCRYPTED_PASSWORD_SIZE = 120
except:
    pass

# /opt/dockethead/include/ar.h: 110
try:
    AR_MAX_NAME_CHARACTERS = 80
except:
    pass

# /opt/dockethead/include/ar.h: 111
try:
    AR_MAX_NOTIFY_USER = 255
except:
    pass

# /opt/dockethead/include/ar.h: 112
try:
    AR_MAX_PATTERN_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 113
try:
    AR_MAX_RELATED_SIZE = 128
except:
    pass

# /opt/dockethead/include/ar.h: 114
try:
    AR_MAX_SCHEMAID_SIZE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 116
try:
    AR_MAX_SERVER_SIZE = 64
except:
    pass

# /opt/dockethead/include/ar.h: 117
try:
    AR_MAX_LINE_LENGTH = 2048
except:
    pass

# /opt/dockethead/include/ar.h: 118
try:
    AR_MAX_SDESC_SIZE = 254
except:
    pass

# /opt/dockethead/include/ar.h: 119
try:
    AR_MAX_SUBJECT_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 120
try:
    AR_MAX_HOSTID_SIZE = 100
except:
    pass

# /opt/dockethead/include/ar.h: 121
try:
    AR_MAX_TARGET_STRING_SIZE = 255
except:
    pass

# /opt/dockethead/include/ar.h: 123
try:
    AR_MAX_USER_GUID_SIZE = 128
except:
    pass

# /opt/dockethead/include/ar.h: 124
try:
    AR_MAX_WAIT_CONT_TITLE_SIZE = 64
except:
    pass

# /opt/dockethead/include/ar.h: 127
try:
    AR_MAX_FILENAME_SIZE = 12
except:
    pass

# /opt/dockethead/include/ar.h: 128
try:
    AR_MAX_FILENAME_BASE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 129
try:
    AR_MAX_FULL_FILENAME = 255
except:
    pass

# /opt/dockethead/include/ar.h: 132
try:
    AR_RESERV_OVERLAY_STRING = '__o'
except:
    pass

# /opt/dockethead/include/ar.h: 133
try:
    AR_RESERV_OVERLAY_CUSTOM_STRING = '__c'
except:
    pass

# /opt/dockethead/include/ar.h: 136
try:
    AR_ORIGINAL_OBJECT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 137
try:
    AR_OVERLAID_OBJECT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 138
try:
    AR_OVERLAY_OBJECT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 139
try:
    AR_CUSTOM_OBJECT = 4
except:
    pass

# /opt/dockethead/include/ar.h: 141
try:
    AR_MAX_CHAR_OVERLAID_OBJ_NAME = 244
except:
    pass

# /opt/dockethead/include/ar.h: 144
try:
    AR_OBJ_REL_OVERLAY_GROUP_BASE = '-1'
except:
    pass

# /opt/dockethead/include/ar.h: 145
try:
    AR_OBJ_REL_OVERLAY_GROUP_OVERLAID = '0'
except:
    pass

# /opt/dockethead/include/ar.h: 156
try:
    AR_OVERLAY_GROUP_TAG_NULL = (-2)
except:
    pass

# /opt/dockethead/include/ar.h: 157
try:
    AR_OVERLAY_GROUP_TAG_INVALID = (-1)
except:
    pass

# /opt/dockethead/include/ar.h: 158
try:
    AR_OVERLAY_GROUP_TAG_BASE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 164
try:
    AR_COMMIT_CLIENT_TRANSACTION = 1
except:
    pass

# /opt/dockethead/include/ar.h: 165
try:
    AR_ROLLBACK_CLIENT_TRANSACTION = 2
except:
    pass

# /opt/dockethead/include/ar.h: 168
try:
    MAX_CLIENT_MANAGED_TRANSACTIONS_TIMEOUT = 600
except:
    pass

# /opt/dockethead/include/ar.h: 169
try:
    DEFAULT_CLIENT_MANAGED_TRANSACTIONS_TIMEOUT = 60
except:
    pass

# /opt/dockethead/include/ar.h: 172
try:
    MAX_CONCURRENT_CLIENT_MANAGED_TRANSACTIONS = 100
except:
    pass

# /opt/dockethead/include/ar.h: 173
try:
    DEFAULT_NUM_CONCURRENT_CLIENT_MANAGED_TRANSACTIONS = 10
except:
    pass

# /opt/dockethead/include/ar.h: 177
try:
    AR_MAX_COLFLD_COLLENGTH = 255
except:
    pass

# /opt/dockethead/include/ar.h: 178
try:
    AR_MAX_SVR_EVENT_DETAILS = 255
except:
    pass

# /opt/dockethead/include/ar.h: 179
try:
    AR_MAX_SVR_EVENT_LIST = 255
except:
    pass

# /opt/dockethead/include/ar.h: 180
try:
    AR_MAX_TABLENAME_SIZE = 2047
except:
    pass

# /opt/dockethead/include/ar.h: 181
try:
    AR_MAX_TBLFLD_NUMCOLS = 255
except:
    pass

# /opt/dockethead/include/ar.h: 182
try:
    AR_MAX_TBLFLD_RETROWS = 9999
except:
    pass

# /opt/dockethead/include/ar.h: 189
try:
    AR_MAX_FLATFILE_LIMIT = 10000000
except:
    pass

# /opt/dockethead/include/ar.h: 190
try:
    AR_WARN_FLATFILE_LIMIT = 9000000
except:
    pass

# /opt/dockethead/include/ar.h: 193
try:
    AR_MAX_BLOB_SIZE = ARLONG32_MAX
except:
    pass

# /opt/dockethead/include/ar.h: 196
try:
    AR_MAX_FIELD_ID = ARLONG32_MAX
except:
    pass

# /opt/dockethead/include/ar.h: 199
try:
    AR_NO_LICENSE_DB_LIMIT = 2000000
except:
    pass

# /opt/dockethead/include/ar.h: 200
try:
    AR_NO_LICENSE_DB_COUNT = 2000
except:
    pass

# /opt/dockethead/include/ar.h: 202
try:
    AR_LICENSE_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 203
try:
    AR_LICENSE_TYPE_FIXED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 204
try:
    AR_LICENSE_TYPE_FLOATING = 2
except:
    pass

# /opt/dockethead/include/ar.h: 205
try:
    AR_LICENSE_TYPE_RESTRICTED_READ = 3
except:
    pass

# /opt/dockethead/include/ar.h: 207
try:
    AR_LICENSE_POOL_NON_RESERVED_POOL = (-1)
except:
    pass

# /opt/dockethead/include/ar.h: 209
try:
    AR_LICENSE_IMPORT_APPEND = 0
except:
    pass

# /opt/dockethead/include/ar.h: 210
try:
    AR_LICENSE_IMPORT_OVERWRITE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 212
try:
    AR_DEFAULT_INTERVAL = 300
except:
    pass

# /opt/dockethead/include/ar.h: 215
try:
    AR_CURRENT_API_VERSION = 20
except:
    pass

# /opt/dockethead/include/ar.h: 216
try:
    AR_MINIMUM_CMDB_API_VERSION = 3
except:
    pass

# /opt/dockethead/include/ar.h: 218
try:
    AR_CURRENT_CMDB_API_VERSION = 4
except:
    pass

# /opt/dockethead/include/ar.h: 220
try:
    AR_NATIVE_ENCRYPTION = '0'
except:
    pass

# /opt/dockethead/include/ar.h: 221
try:
    AR_UNICODE_ENCRYPTION = '1'
except:
    pass

# /opt/dockethead/include/ar.h: 223
try:
    AR_ENCRYPTION_VERSION_1 = '0'
except:
    pass

# /opt/dockethead/include/ar.h: 224
try:
    AR_ENCRYPTION_VERSION_2 = '1'
except:
    pass

# /opt/dockethead/include/ar.h: 225
try:
    AR_ENCRYPTION_VERSION_3 = '2'
except:
    pass

# /opt/dockethead/include/ar.h: 227
try:
    AR_SERVER_MIN_AUDIT_LOG_FILE_SIZE = 100000
except:
    pass

# /opt/dockethead/include/ar.h: 230
try:
    AR_MAX_DECIMAL_SIZE = 64
except:
    pass

# /opt/dockethead/include/ar.h: 231
try:
    AR_MAX_DECIMAL_FIELD_VALUE_LIMIT = '99999999999999999999999999.99'
except:
    pass

# /opt/dockethead/include/ar.h: 232
try:
    AR_MIN_DECIMAL_FIELD_VALUE_LIMIT = '-99999999999999999999999999.99'
except:
    pass

# /opt/dockethead/include/ar.h: 233
try:
    AR_MAX_CURRENCY_FIELD_VALUE_LIMIT = '99999999999999999999999999.99'
except:
    pass

# /opt/dockethead/include/ar.h: 234
try:
    AR_MIN_CURRENCY_FIELD_VALUE_LIMIT = '-99999999999999999999999999.99'
except:
    pass

# /opt/dockethead/include/ar.h: 235
try:
    AR_MAX_CURRENCY_CODE_SIZE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 236
try:
    AR_MAX_CURRENCY_RATIO_SIZE = 64
except:
    pass

# /opt/dockethead/include/ar.h: 237
try:
    AR_CURRENT_CURRENCY_RATIOS = 0
except:
    pass

# /opt/dockethead/include/ar.h: 239
try:
    AR_AUTH_CHAINING_MODE_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 240
try:
    AR_AUTH_CHAINING_MODE_ARS_THEN_AREA = 1
except:
    pass

# /opt/dockethead/include/ar.h: 241
try:
    AR_AUTH_CHAINING_MODE_AREA_THEN_ARS = 2
except:
    pass

# /opt/dockethead/include/ar.h: 242
try:
    AR_AUTH_CHAINING_MODE_ARS_OS_AREA = 3
except:
    pass

# /opt/dockethead/include/ar.h: 243
try:
    AR_AUTH_CHAINING_MODE_ARS_AREA_OS = 4
except:
    pass

# /opt/dockethead/include/ar.h: 244
try:
    AR_AUTH_CHAINING_MODE_MAX = 4
except:
    pass

# /opt/dockethead/include/ar.h: 252
try:
    FALSE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 255
try:
    False = 0
except:
    pass

# /opt/dockethead/include/ar.h: 258
try:
    TRUE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 261
try:
    True = 1
except:
    pass

# /opt/dockethead/include/ar.h: 265
try:
    AR_RETURN_OK = 0
except:
    pass

# /opt/dockethead/include/ar.h: 266
try:
    AR_RETURN_WARNING = 1
except:
    pass

# /opt/dockethead/include/ar.h: 267
try:
    AR_RETURN_ERROR = 2
except:
    pass

# /opt/dockethead/include/ar.h: 268
try:
    AR_RETURN_FATAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 270
try:
    AR_RETURN_BAD_STATUS = 4
except:
    pass

# /opt/dockethead/include/ar.h: 271
try:
    AR_RETURN_PROMPT = 5
except:
    pass

# /opt/dockethead/include/ar.h: 272
try:
    AR_RETURN_ACCESSIBLE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 273
try:
    AR_RETURN_TOOLTIP = 7
except:
    pass

# /opt/dockethead/include/ar.h: 297
try:
    ARTIMESTAMP_MAX = ARLONG32_MAX
except:
    pass

# /opt/dockethead/include/ar.h: 434
try:
    AR_BYTE_LIST_SELF_DEFINED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 436
try:
    AR_BYTE_LIST_WIN30_BITMAP = 1
except:
    pass

# /opt/dockethead/include/ar.h: 437
try:
    AR_BYTE_LIST_JPEG = 2
except:
    pass

# /opt/dockethead/include/ar.h: 438
try:
    AR_BYTE_LIST_TIFF = 3
except:
    pass

# /opt/dockethead/include/ar.h: 439
try:
    AR_BYTE_LIST_TARGA = 4
except:
    pass

# /opt/dockethead/include/ar.h: 440
try:
    AR_BYTE_LIST_PCX = 5
except:
    pass

# /opt/dockethead/include/ar.h: 441
try:
    AR_BYTE_LIST_LOCALIZED_FILE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 442
try:
    AR_BYTE_LIST_AUTH_STRING = 7
except:
    pass

# /opt/dockethead/include/ar.h: 443
try:
    AR_BYTE_LIST_FUNC_PTR = 8
except:
    pass

# /opt/dockethead/include/ar.h: 444
try:
    AR_BYTE_LIST_GIF = 9
except:
    pass

# /opt/dockethead/include/ar.h: 445
try:
    AR_BYTE_LIST_PNG = 10
except:
    pass

# /opt/dockethead/include/ar.h: 534
try:
    AR_DATA_TYPE_NULL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 535
try:
    AR_DATA_TYPE_KEYWORD = 1
except:
    pass

# /opt/dockethead/include/ar.h: 536
try:
    AR_DATA_TYPE_INTEGER = 2
except:
    pass

# /opt/dockethead/include/ar.h: 537
try:
    AR_DATA_TYPE_REAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 538
try:
    AR_DATA_TYPE_CHAR = 4
except:
    pass

# /opt/dockethead/include/ar.h: 539
try:
    AR_DATA_TYPE_DIARY = 5
except:
    pass

# /opt/dockethead/include/ar.h: 540
try:
    AR_DATA_TYPE_ENUM = 6
except:
    pass

# /opt/dockethead/include/ar.h: 541
try:
    AR_DATA_TYPE_TIME = 7
except:
    pass

# /opt/dockethead/include/ar.h: 542
try:
    AR_DATA_TYPE_BITMASK = 8
except:
    pass

# /opt/dockethead/include/ar.h: 543
try:
    AR_DATA_TYPE_BYTES = 9
except:
    pass

# /opt/dockethead/include/ar.h: 544
try:
    AR_DATA_TYPE_DECIMAL = 10
except:
    pass

# /opt/dockethead/include/ar.h: 545
try:
    AR_DATA_TYPE_ATTACH = 11
except:
    pass

# /opt/dockethead/include/ar.h: 546
try:
    AR_DATA_TYPE_CURRENCY = 12
except:
    pass

# /opt/dockethead/include/ar.h: 547
try:
    AR_DATA_TYPE_DATE = 13
except:
    pass

# /opt/dockethead/include/ar.h: 548
try:
    AR_DATA_TYPE_TIME_OF_DAY = 14
except:
    pass

# /opt/dockethead/include/ar.h: 550
try:
    AR_MAX_STD_DATA_TYPE = 14
except:
    pass

# /opt/dockethead/include/ar.h: 552
try:
    AR_DATA_TYPE_JOIN = 30
except:
    pass

# /opt/dockethead/include/ar.h: 553
try:
    AR_DATA_TYPE_TRIM = 31
except:
    pass

# /opt/dockethead/include/ar.h: 554
try:
    AR_DATA_TYPE_CONTROL = 32
except:
    pass

# /opt/dockethead/include/ar.h: 555
try:
    AR_DATA_TYPE_TABLE = 33
except:
    pass

# /opt/dockethead/include/ar.h: 556
try:
    AR_DATA_TYPE_COLUMN = 34
except:
    pass

# /opt/dockethead/include/ar.h: 557
try:
    AR_DATA_TYPE_PAGE = 35
except:
    pass

# /opt/dockethead/include/ar.h: 558
try:
    AR_DATA_TYPE_PAGE_HOLDER = 36
except:
    pass

# /opt/dockethead/include/ar.h: 559
try:
    AR_DATA_TYPE_ATTACH_POOL = 37
except:
    pass

# /opt/dockethead/include/ar.h: 561
try:
    AR_DATA_TYPE_ULONG = 40
except:
    pass

# /opt/dockethead/include/ar.h: 562
try:
    AR_DATA_TYPE_COORDS = 41
except:
    pass

# /opt/dockethead/include/ar.h: 563
try:
    AR_DATA_TYPE_VIEW = 42
except:
    pass

# /opt/dockethead/include/ar.h: 564
try:
    AR_DATA_TYPE_DISPLAY = 43
except:
    pass

# /opt/dockethead/include/ar.h: 566
try:
    AR_DATA_TYPE_MAX_TYPE = 43
except:
    pass

# /opt/dockethead/include/ar.h: 568
try:
    AR_FIELD_TYPE_DATA = 1
except:
    pass

# /opt/dockethead/include/ar.h: 569
try:
    AR_FIELD_TYPE_TRIM = 2
except:
    pass

# /opt/dockethead/include/ar.h: 570
try:
    AR_FIELD_TYPE_CONTROL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 571
try:
    AR_FIELD_TYPE_PAGE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 572
try:
    AR_FIELD_TYPE_PAGE_HOLDER = 16
except:
    pass

# /opt/dockethead/include/ar.h: 573
try:
    AR_FIELD_TYPE_TABLE = 32
except:
    pass

# /opt/dockethead/include/ar.h: 574
try:
    AR_FIELD_TYPE_COLUMN = 64
except:
    pass

# /opt/dockethead/include/ar.h: 575
try:
    AR_FIELD_TYPE_ATTACH = 128
except:
    pass

# /opt/dockethead/include/ar.h: 576
try:
    AR_FIELD_TYPE_ATTACH_POOL = 256
except:
    pass

# /opt/dockethead/include/ar.h: 578
try:
    AR_FIELD_TYPE_ALL = ((((((((AR_FIELD_TYPE_DATA | AR_FIELD_TYPE_TRIM) | AR_FIELD_TYPE_CONTROL) | AR_FIELD_TYPE_PAGE) | AR_FIELD_TYPE_PAGE_HOLDER) | AR_FIELD_TYPE_TABLE) | AR_FIELD_TYPE_COLUMN) | AR_FIELD_TYPE_ATTACH) | AR_FIELD_TYPE_ATTACH_POOL)
except:
    pass

# /opt/dockethead/include/ar.h: 584
try:
    AR_DEFAULT_VALUE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 590
try:
    AR_KEYWORD_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 591
try:
    AR_KEYWORD_USER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 592
try:
    AR_KEYWORD_TIMESTAMP = 2
except:
    pass

# /opt/dockethead/include/ar.h: 593
try:
    AR_KEYWORD_TIME_ONLY = 3
except:
    pass

# /opt/dockethead/include/ar.h: 595
try:
    AR_KEYWORD_DATE_ONLY = 4
except:
    pass

# /opt/dockethead/include/ar.h: 597
try:
    AR_KEYWORD_SCHEMA = 5
except:
    pass

# /opt/dockethead/include/ar.h: 598
try:
    AR_KEYWORD_SERVER = 6
except:
    pass

# /opt/dockethead/include/ar.h: 599
try:
    AR_KEYWORD_WEEKDAY = 7
except:
    pass

# /opt/dockethead/include/ar.h: 600
try:
    AR_KEYWORD_GROUPS = 8
except:
    pass

# /opt/dockethead/include/ar.h: 601
try:
    AR_KEYWORD_OPERATION = 9
except:
    pass

# /opt/dockethead/include/ar.h: 603
try:
    AR_KEYWORD_HARDWARE = 10
except:
    pass

# /opt/dockethead/include/ar.h: 604
try:
    AR_KEYWORD_OS = 11
except:
    pass

# /opt/dockethead/include/ar.h: 605
try:
    AR_KEYWORD_DATABASE = 12
except:
    pass

# /opt/dockethead/include/ar.h: 606
try:
    AR_KEYWORD_LASTID = 13
except:
    pass

# /opt/dockethead/include/ar.h: 608
try:
    AR_KEYWORD_LASTCOUNT = 14
except:
    pass

# /opt/dockethead/include/ar.h: 610
try:
    AR_KEYWORD_VERSION = 15
except:
    pass

# /opt/dockethead/include/ar.h: 611
try:
    AR_KEYWORD_VUI = 16
except:
    pass

# /opt/dockethead/include/ar.h: 612
try:
    AR_KEYWORD_GUIDETEXT = 17
except:
    pass

# /opt/dockethead/include/ar.h: 613
try:
    AR_KEYWORD_FIELDHELP = 18
except:
    pass

# /opt/dockethead/include/ar.h: 614
try:
    AR_KEYWORD_GUIDE = 19
except:
    pass

# /opt/dockethead/include/ar.h: 615
try:
    AR_KEYWORD_APPLICATION = 20
except:
    pass

# /opt/dockethead/include/ar.h: 616
try:
    AR_KEYWORD_LOCALE = 21
except:
    pass

# /opt/dockethead/include/ar.h: 617
try:
    AR_KEYWORD_CLIENT_TYPE = 22
except:
    pass

# /opt/dockethead/include/ar.h: 618
try:
    AR_KEYWORD_SCHEMA_ALIAS = 23
except:
    pass

# /opt/dockethead/include/ar.h: 619
try:
    AR_KEYWORD_ROWSELECTED = 24
except:
    pass

# /opt/dockethead/include/ar.h: 621
try:
    AR_KEYWORD_ROWCHANGED = 25
except:
    pass

# /opt/dockethead/include/ar.h: 623
try:
    AR_KEYWORD_BROWSER = 26
except:
    pass

# /opt/dockethead/include/ar.h: 624
try:
    AR_KEYWORD_VUI_TYPE = 27
except:
    pass

# /opt/dockethead/include/ar.h: 625
try:
    AR_KEYWORD_TCPPORT = 28
except:
    pass

# /opt/dockethead/include/ar.h: 626
try:
    AR_KEYWORD_HOMEURL = 29
except:
    pass

# /opt/dockethead/include/ar.h: 627
try:
    AR_KEYWORD_ROLES = 30
except:
    pass

# /opt/dockethead/include/ar.h: 628
try:
    AR_KEYWORD_EVENTTYPE = 31
except:
    pass

# /opt/dockethead/include/ar.h: 630
try:
    AR_KEYWORD_EVENTSRCWINID = 32
except:
    pass

# /opt/dockethead/include/ar.h: 632
try:
    AR_KEYWORD_CURRENTWINID = 33
except:
    pass

# /opt/dockethead/include/ar.h: 634
try:
    AR_KEYWORD_LASTOPENEDWINID = 34
except:
    pass

# /opt/dockethead/include/ar.h: 636
try:
    AR_KEYWORD_INBULKTRANS = 35
except:
    pass

# /opt/dockethead/include/ar.h: 638
try:
    AR_KEYWORD_FIELDID = 36
except:
    pass

# /opt/dockethead/include/ar.h: 640
try:
    AR_KEYWORD_FIELDNAME = 37
except:
    pass

# /opt/dockethead/include/ar.h: 642
try:
    AR_KEYWORD_FIELDLABEL = 38
except:
    pass

# /opt/dockethead/include/ar.h: 644
try:
    AR_KEYWORD_SERVERTIMESTAMP = 39
except:
    pass

# /opt/dockethead/include/ar.h: 646
try:
    AR_KEYWORD_GROUPIDS = 40
except:
    pass

# /opt/dockethead/include/ar.h: 648
try:
    AR_KEYWORD_EVENTDATA = 41
except:
    pass

# /opt/dockethead/include/ar.h: 650
try:
    AR_KEYWORD_ERRNO = 42
except:
    pass

# /opt/dockethead/include/ar.h: 652
try:
    AR_KEYWORD_ERRMSG = 43
except:
    pass

# /opt/dockethead/include/ar.h: 654
try:
    AR_KEYWORD_ERRAPPENDMSG = 44
except:
    pass

# /opt/dockethead/include/ar.h: 655
try:
    AR_KEYWORD_INCLNTMANAGEDTRANS = 45
except:
    pass

# /opt/dockethead/include/ar.h: 656
try:
    AR_KEYWORD_DRAGSRCFIELDID = 46
except:
    pass

# /opt/dockethead/include/ar.h: 657
try:
    AR_KEYWORD_DROPTGTFIELDID = 47
except:
    pass

# /opt/dockethead/include/ar.h: 658
try:
    AR_KEYWORD_SHIFT_KEY = 48
except:
    pass

# /opt/dockethead/include/ar.h: 659
try:
    AR_KEYWORD_CTRL_KEY = 49
except:
    pass

# /opt/dockethead/include/ar.h: 660
try:
    AR_KEYWORD_ALT_KEY = 50
except:
    pass

# /opt/dockethead/include/ar.h: 661
try:
    AR_KEYWORD_AUTHSTRING = 51
except:
    pass

# /opt/dockethead/include/ar.h: 662
try:
    AR_KEYWORD_ROWVISIBLE = 52
except:
    pass

# /opt/dockethead/include/ar.h: 664
try:
    AR_KEYWORD_NO = 53
except:
    pass

# /opt/dockethead/include/ar.h: 671
try:
    AR_MAX_KEYWORD_USED = AR_KEYWORD_NO
except:
    pass

# /opt/dockethead/include/ar.h: 673
try:
    AR_KEY_OPERATION_CREATE = 'CREATE'
except:
    pass

# /opt/dockethead/include/ar.h: 674
try:
    AR_KEY_OPERATION_DELETE = 'DELETE'
except:
    pass

# /opt/dockethead/include/ar.h: 675
try:
    AR_KEY_OPERATION_GET = 'GET'
except:
    pass

# /opt/dockethead/include/ar.h: 676
try:
    AR_KEY_OPERATION_GETLIST = 'GETLIST'
except:
    pass

# /opt/dockethead/include/ar.h: 677
try:
    AR_KEY_OPERATION_MERGE = 'MERGE'
except:
    pass

# /opt/dockethead/include/ar.h: 678
try:
    AR_KEY_OPERATION_SET = 'SET'
except:
    pass

# /opt/dockethead/include/ar.h: 679
try:
    AR_KEY_OPERATION_SET_ALL = 'SET ALL'
except:
    pass

# /opt/dockethead/include/ar.h: 680
try:
    AR_KEY_OPERATION_QUERY = 'QUERY'
except:
    pass

# /opt/dockethead/include/ar.h: 681
try:
    AR_KEY_OPERATION_GUIDE = 'GUIDE'
except:
    pass

# /opt/dockethead/include/ar.h: 682
try:
    AR_KEY_OPERATION_SERVICE = 'SERVICE'
except:
    pass

# /opt/dockethead/include/ar.h: 683
try:
    AR_KEY_OPERATION_ERRHANDLE = 'ERROR-HANDLER'
except:
    pass

# /opt/dockethead/include/ar.h: 685
try:
    AR_PATTERN_KEY_DIGIT = 101
except:
    pass

# /opt/dockethead/include/ar.h: 686
try:
    AR_PATTERN_KEY_ALPHA = 102
except:
    pass

# /opt/dockethead/include/ar.h: 687
try:
    AR_PATTERN_KEY_ALNUM = 103
except:
    pass

# /opt/dockethead/include/ar.h: 688
try:
    AR_PATTERN_KEY_PRINT = 104
except:
    pass

# /opt/dockethead/include/ar.h: 689
try:
    AR_PATTERN_KEY_UPPER = 105
except:
    pass

# /opt/dockethead/include/ar.h: 690
try:
    AR_PATTERN_KEY_LOWER = 106
except:
    pass

# /opt/dockethead/include/ar.h: 691
try:
    AR_PATTERN_KEY_MENU = 107
except:
    pass

# /opt/dockethead/include/ar.h: 709
try:
    AR_LOC_NULL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 710
try:
    AR_LOC_FILENAME = 1
except:
    pass

# /opt/dockethead/include/ar.h: 711
try:
    AR_LOC_BUFFER = 2
except:
    pass

# /opt/dockethead/include/ar.h: 841
try:
    AR_START_WITH_FIRST_ENTRY = 0
except:
    pass

# /opt/dockethead/include/ar.h: 844
try:
    AR_NO_MAX_LIST_RETRIEVE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 847
try:
    AR_RETRIEVE_ALL_ENTRIES = 999999999
except:
    pass

# /opt/dockethead/include/ar.h: 1011
try:
    AR_MERGE_ENTRY_DUP_ERROR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1012
try:
    AR_MERGE_ENTRY_DUP_NEW_ID = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1013
try:
    AR_MERGE_ENTRY_DUP_OVERWRITE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1014
try:
    AR_MERGE_ENTRY_DUP_MERGE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1015
try:
    AR_MERGE_ENTRY_GEN_NEW_ID = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1017
try:
    AR_MERGE_NO_REQUIRED_INCREMENT = 1024
except:
    pass

# /opt/dockethead/include/ar.h: 1019
try:
    AR_MERGE_NO_PATTERNS_INCREMENT = 2048
except:
    pass

# /opt/dockethead/include/ar.h: 1021
try:
    AR_MERGE_NO_WORKFLOW_FIRED = 4096
except:
    pass

# /opt/dockethead/include/ar.h: 1024
try:
    AR_MERGE_ENTRY_MULT_MATCH_ERROR = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1025
try:
    AR_MERGE_ENTRY_MULT_MATCH_USE_FIRST = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1033
try:
    AR_STAT_HISTORY_USER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1034
try:
    AR_STAT_HISTORY_TIME = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1043
try:
    AR_MAX_LOCAL_VARIABLES = 10
except:
    pass

# /opt/dockethead/include/ar.h: 1045
try:
    AR_QUERY_VALUE_MULTI_ERROR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1046
try:
    AR_QUERY_VALUE_MULTI_FIRST = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1047
try:
    AR_QUERY_VALUE_MULTI_SET = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1059
try:
    AR_CURRENCY_PART_FIELD = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1060
try:
    AR_CURRENCY_PART_VALUE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1061
try:
    AR_CURRENCY_PART_TYPE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1062
try:
    AR_CURRENCY_PART_DATE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1063
try:
    AR_CURRENCY_PART_FUNCTIONAL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1065
try:
    AR_CURRENCY_CODE_LEN = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1076
try:
    AR_FIELD = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1077
try:
    AR_VALUE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1078
try:
    AR_ARITHMETIC = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1079
try:
    AR_STAT_HISTORY = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1080
try:
    AR_VALUE_SET = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1081
try:
    AR_CURRENCY_FLD = 6
except:
    pass

# /opt/dockethead/include/ar.h: 1086
try:
    AR_FIELD_TRAN = 50
except:
    pass

# /opt/dockethead/include/ar.h: 1087
try:
    AR_FIELD_DB = 51
except:
    pass

# /opt/dockethead/include/ar.h: 1091
try:
    AR_LOCAL_VARIABLE = 52
except:
    pass

# /opt/dockethead/include/ar.h: 1092
try:
    AR_QUERY = 53
except:
    pass

# /opt/dockethead/include/ar.h: 1094
try:
    AR_CURRENCY_FLD_TRAN = 54
except:
    pass

# /opt/dockethead/include/ar.h: 1095
try:
    AR_CURRENCY_FLD_DB = 55
except:
    pass

# /opt/dockethead/include/ar.h: 1096
try:
    AR_CURRENCY_FLD_CURRENT = 56
except:
    pass

# /opt/dockethead/include/ar.h: 1098
try:
    AR_FIELD_CURRENT = 99
except:
    pass

# /opt/dockethead/include/ar.h: 1111
try:
    AR_FIELD_OFFSET = 12
except:
    pass

# /opt/dockethead/include/ar.h: 1113
try:
    AR_TEXT_OVERFLOW = (-3)
except:
    pass

# /opt/dockethead/include/ar.h: 1139
try:
    AR_ARITH_OP_ADD = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1140
try:
    AR_ARITH_OP_SUBTRACT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1141
try:
    AR_ARITH_OP_MULTIPLY = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1142
try:
    AR_ARITH_OP_DIVIDE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1143
try:
    AR_ARITH_OP_MODULO = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1144
try:
    AR_ARITH_OP_NEGATE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 1154
try:
    AR_REL_OP_EQUAL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1155
try:
    AR_REL_OP_GREATER = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1156
try:
    AR_REL_OP_GREATER_EQUAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1157
try:
    AR_REL_OP_LESS = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1158
try:
    AR_REL_OP_LESS_EQUAL = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1159
try:
    AR_REL_OP_NOT_EQUAL = 6
except:
    pass

# /opt/dockethead/include/ar.h: 1160
try:
    AR_REL_OP_LIKE = 7
except:
    pass

# /opt/dockethead/include/ar.h: 1161
try:
    AR_REL_OP_IN = 8
except:
    pass

# /opt/dockethead/include/ar.h: 1162
try:
    AR_REL_OP_NOT_IN = 9
except:
    pass

# /opt/dockethead/include/ar.h: 1172
try:
    AR_COND_OP_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1173
try:
    AR_COND_OP_AND = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1174
try:
    AR_COND_OP_OR = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1175
try:
    AR_COND_OP_NOT = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1176
try:
    AR_COND_OP_REL_OP = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1177
try:
    AR_COND_OP_FROM_FIELD = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1213
try:
    AR_SORT_ASCENDING = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1214
try:
    AR_SORT_DESCENDING = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1240
try:
    AR_STAT_OP_COUNT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1241
try:
    AR_STAT_OP_SUM = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1242
try:
    AR_STAT_OP_AVERAGE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1243
try:
    AR_STAT_OP_MINIMUM = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1244
try:
    AR_STAT_OP_MAXIMUM = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1327
try:
    AR_ARCHIVE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1328
try:
    AR_ARCHIVE_FORM = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1329
try:
    AR_ARCHIVE_DELETE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1330
try:
    AR_ARCHIVE_FILE_XML = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1331
try:
    AR_ARCHIVE_FILE_ARX = 8
except:
    pass

# /opt/dockethead/include/ar.h: 1332
try:
    AR_ARCHIVE_NO_ATTACHMENTS = 32
except:
    pass

# /opt/dockethead/include/ar.h: 1333
try:
    AR_ARCHIVE_NO_DIARY = 64
except:
    pass

# /opt/dockethead/include/ar.h: 1351
try:
    AR_AUDIT_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1352
try:
    AR_AUDIT_COPY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1353
try:
    AR_AUDIT_LOG = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1354
try:
    AR_AUDIT_LOG_SHADOW = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1356
try:
    AR_AUDIT_ONLY_CHNG_FLDS_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1357
try:
    AR_AUDIT_ONLY_CHNG_FLDS_YES = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1358
try:
    AR_AUDIT_ONLY_CHNG_FLDS_NO = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1360
try:
    AR_FIELD_OPTION_REQUIRED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1361
try:
    AR_FIELD_OPTION_OPTIONAL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1362
try:
    AR_FIELD_OPTION_SYSTEM = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1365
try:
    AR_FIELD_OPTION_DISPLAY = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1367
try:
    AR_FIELD_OPTION_FORCE_SYSTEM = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1369
try:
    AR_FIELD_OPEN_AT_CREATE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1370
try:
    AR_FIELD_PROTECTED_AT_CREATE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1372
try:
    AR_FIELD_BITOPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1373
try:
    AR_FIELD_BITOPTION_AUDIT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1374
try:
    AR_FIELD_BITOPTION_COPY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1376
try:
    AR_FIELD_BITOPTION_LOG_KEY1 = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1377
try:
    AR_FIELD_BITOPTION_LOG_KEY2 = 8
except:
    pass

# /opt/dockethead/include/ar.h: 1378
try:
    AR_FIELD_BITOPTION_LOG_KEY3 = 12
except:
    pass

# /opt/dockethead/include/ar.h: 1380
try:
    AR_FIELD_BITOPTION_AUDIT_MASK = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1381
try:
    AR_FIELD_BITOPTION_AUDIT_LOG_KEY_MASK = 12
except:
    pass

# /opt/dockethead/include/ar.h: 1384
try:
    AR_FIELD_BITOPTION_AUDIT_TO_OVERLAY_MASK = (AR_FIELD_BITOPTION_AUDIT_MASK | AR_FIELD_BITOPTION_AUDIT_LOG_KEY_MASK)
except:
    pass

# /opt/dockethead/include/ar.h: 1386
try:
    AR_DISPLAY_TAG_SQL = 'SQL'
except:
    pass

# /opt/dockethead/include/ar.h: 1450
try:
    AR_CACHE_DPROP_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1451
try:
    AR_CACHE_DPROP_VUI = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1452
try:
    AR_CACHE_DPROP_FIELD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1453
try:
    AR_CACHE_DPROP_ALL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1461
try:
    AR_DPROP_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1464
try:
    AR_DPROP_TRIM_TYPE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1465
try:
    AR_DVAL_TRIM_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1466
try:
    AR_DVAL_TRIM_LINE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1467
try:
    AR_DVAL_TRIM_SHAPE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1468
try:
    AR_DVAL_TRIM_TEXT = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1469
try:
    AR_DVAL_TRIM_IMAGE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1472
try:
    AR_DPROP_CNTL_TYPE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1473
try:
    AR_DVAL_CNTL_BUTTON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1474
try:
    AR_DVAL_CNTL_MENU = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1475
try:
    AR_DVAL_CNTL_TOOLBAR = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1476
try:
    AR_DVAL_CNTL_TAB_SWITCH = 8
except:
    pass

# /opt/dockethead/include/ar.h: 1477
try:
    AR_DVAL_CNTL_URL = 16
except:
    pass

# /opt/dockethead/include/ar.h: 1478
try:
    AR_DVAL_CNTL_CHART = 32
except:
    pass

# /opt/dockethead/include/ar.h: 1479
try:
    AR_DVAL_CNTL_METER = 64
except:
    pass

# /opt/dockethead/include/ar.h: 1480
try:
    AR_DVAL_CNTL_HORIZNAV = 128
except:
    pass

# /opt/dockethead/include/ar.h: 1481
try:
    AR_DVAL_CNTL_VERTICALNAV = 256
except:
    pass

# /opt/dockethead/include/ar.h: 1482
try:
    AR_DVAL_CNTL_NAV_ITEM = 512
except:
    pass

# /opt/dockethead/include/ar.h: 1485
try:
    AR_FIXED_POINT_PRECISION = 100
except:
    pass

# /opt/dockethead/include/ar.h: 1487
try:
    AR_DPROP_BBOX = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1489
try:
    AR_DPROP_VISIBLE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1490
try:
    AR_DPROP_ENABLE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1491
try:
    AR_DVAL_ENABLE_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1492
try:
    AR_DVAL_ENABLE_READ_ONLY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1493
try:
    AR_DVAL_ENABLE_READ_WRITE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1494
try:
    AR_DVAL_ENABLE_DISABLE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1495
try:
    AR_DPROP_HELP = 6
except:
    pass

# /opt/dockethead/include/ar.h: 1496
try:
    AR_DPROP_Z_ORDER = 7
except:
    pass

# /opt/dockethead/include/ar.h: 1497
try:
    AR_DPROP_COLOR_FILL = 8
except:
    pass

# /opt/dockethead/include/ar.h: 1498
try:
    AR_DVAL_COLOR_NONE = 'none'
except:
    pass

# /opt/dockethead/include/ar.h: 1499
try:
    AR_DVAL_COLOR_BG = 'bg'
except:
    pass

# /opt/dockethead/include/ar.h: 1500
try:
    AR_DVAL_COLOR_FG = 'fg'
except:
    pass

# /opt/dockethead/include/ar.h: 1501
try:
    AR_DVAL_COLOR_EDIT_BG = 'edit_bg'
except:
    pass

# /opt/dockethead/include/ar.h: 1502
try:
    AR_DVAL_COLOR_EDIT_FG = 'edit_fg'
except:
    pass

# /opt/dockethead/include/ar.h: 1503
try:
    AR_DVAL_COLOR_FOCUS = 'focus'
except:
    pass

# /opt/dockethead/include/ar.h: 1504
try:
    AR_DVAL_COLOR_INSET1 = 'inset1'
except:
    pass

# /opt/dockethead/include/ar.h: 1505
try:
    AR_DVAL_COLOR_INSET2 = 'inset2'
except:
    pass

# /opt/dockethead/include/ar.h: 1507
try:
    AR_DPROP_DEPTH_EFFECT = 9
except:
    pass

# /opt/dockethead/include/ar.h: 1508
try:
    AR_DVAL_DEPTH_EFFECT_FLAT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1509
try:
    AR_DVAL_DEPTH_EFFECT_RAISED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1510
try:
    AR_DVAL_DEPTH_EFFECT_SUNKEN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1511
try:
    AR_DVAL_DEPTH_EFFECT_FLOATING = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1512
try:
    AR_DVAL_DEPTH_EFFECT_ETCHED = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1513
try:
    AR_DPROP_DEPTH_AMOUNT = 10
except:
    pass

# /opt/dockethead/include/ar.h: 1514
try:
    AR_DPROP_COLOR_LINE = 11
except:
    pass

# /opt/dockethead/include/ar.h: 1515
try:
    AR_DPROP_COLOR_TEXT = 12
except:
    pass

# /opt/dockethead/include/ar.h: 1516
try:
    AR_DPROP_PROMPT = 13
except:
    pass

# /opt/dockethead/include/ar.h: 1518
try:
    AR_DPROP_HIDE_WEBHELP = 14
except:
    pass

# /opt/dockethead/include/ar.h: 1523
try:
    AR_DPROP_LABEL = 20
except:
    pass

# /opt/dockethead/include/ar.h: 1525
try:
    AR_DPROP_LABEL_BBOX = 21
except:
    pass

# /opt/dockethead/include/ar.h: 1526
try:
    AR_DPROP_LABEL_FONT_STYLE = 22
except:
    pass

# /opt/dockethead/include/ar.h: 1528
try:
    AR_DPROP_LABEL_FONT_SIZE = 23
except:
    pass

# /opt/dockethead/include/ar.h: 1529
try:
    AR_DPROP_LABEL_COLOR_TEXT = 24
except:
    pass

# /opt/dockethead/include/ar.h: 1531
try:
    AR_DPROP_LABEL_JUSTIFY = 25
except:
    pass

# /opt/dockethead/include/ar.h: 1532
try:
    AR_DVAL_JUSTIFY_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1533
try:
    AR_DVAL_JUSTIFY_LEFT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1534
try:
    AR_DVAL_JUSTIFY_CENTER = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1535
try:
    AR_DVAL_JUSTIFY_FILL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1536
try:
    AR_DVAL_JUSTIFY_RIGHT = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1537
try:
    AR_DVAL_JUSTIFY_TILE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1538
try:
    AR_DPROP_LABEL_ALIGN = 26
except:
    pass

# /opt/dockethead/include/ar.h: 1539
try:
    AR_DVAL_ALIGN_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1540
try:
    AR_DVAL_ALIGN_TOP = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1541
try:
    AR_DVAL_ALIGN_MIDDLE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1542
try:
    AR_DVAL_ALIGN_FILL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1543
try:
    AR_DVAL_ALIGN_BOTTOM = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1544
try:
    AR_DVAL_ALIGN_TILE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1545
try:
    AR_DPROP_LABEL_POS_SECTOR = 27
except:
    pass

# /opt/dockethead/include/ar.h: 1546
try:
    AR_DVAL_SECTOR_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1547
try:
    AR_DVAL_SECTOR_CENTER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1548
try:
    AR_DVAL_SECTOR_NORTH = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1549
try:
    AR_DVAL_SECTOR_EAST = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1550
try:
    AR_DVAL_SECTOR_SOUTH = 8
except:
    pass

# /opt/dockethead/include/ar.h: 1551
try:
    AR_DVAL_SECTOR_WEST = 16
except:
    pass

# /opt/dockethead/include/ar.h: 1552
try:
    AR_DPROP_LABEL_POS_JUSTIFY = 28
except:
    pass

# /opt/dockethead/include/ar.h: 1554
try:
    AR_DPROP_LABEL_POS_ALIGN = 29
except:
    pass

# /opt/dockethead/include/ar.h: 1556
try:
    AR_DPROP_LABEL_COLOR_FILL = 30
except:
    pass

# /opt/dockethead/include/ar.h: 1558
try:
    AR_DPROP_LABEL_COLOR_LINE = 31
except:
    pass

# /opt/dockethead/include/ar.h: 1562
try:
    AR_DPROP_COORDS = 40
except:
    pass

# /opt/dockethead/include/ar.h: 1564
try:
    AR_DPROP_LINE_WIDTH = 41
except:
    pass

# /opt/dockethead/include/ar.h: 1565
try:
    AR_DPROP_LINE_PATTERN = 42
except:
    pass

# /opt/dockethead/include/ar.h: 1569
try:
    AR_DPROP_JOINT_STYLE = 43
except:
    pass

# /opt/dockethead/include/ar.h: 1570
try:
    AR_DVAL_JOINT_EXTENDED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1571
try:
    AR_DVAL_JOINT_SHARP = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1572
try:
    AR_DVAL_JOINT_ROUNDED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1573
try:
    AR_DVAL_JOINT_SMOOTH = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1574
try:
    AR_DVAL_JOINT_MAX_SMOOTH = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1577
try:
    AR_DPROP_ENDCAP_START = 44
except:
    pass

# /opt/dockethead/include/ar.h: 1578
try:
    AR_DPROP_ENDCAP_END = 45
except:
    pass

# /opt/dockethead/include/ar.h: 1579
try:
    AR_DVAL_ENDCAP_ROUND = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1580
try:
    AR_DVAL_ENDCAP_FLUSH = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1581
try:
    AR_DVAL_ENDCAP_EXTENDED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1582
try:
    AR_DVAL_ENDCAP_ARROW1 = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1585
try:
    AR_DPROP_DATA_ROWS = 60
except:
    pass

# /opt/dockethead/include/ar.h: 1586
try:
    AR_DPROP_DATA_COLS = 61
except:
    pass

# /opt/dockethead/include/ar.h: 1589
try:
    AR_DPROP_DATA_SPIN = 62
except:
    pass

# /opt/dockethead/include/ar.h: 1591
try:
    AR_DPROP_DATA_MENU = 63
except:
    pass

# /opt/dockethead/include/ar.h: 1593
try:
    AR_DPROP_DATA_RADIO = 64
except:
    pass

# /opt/dockethead/include/ar.h: 1594
try:
    AR_DVAL_RADIO_DROPDOWN = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1595
try:
    AR_DVAL_RADIO_RADIO = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1596
try:
    AR_DVAL_RADIO_CHECKBOX = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1599
try:
    AR_DPROP_DATA_MENU_BBOX = 65
except:
    pass

# /opt/dockethead/include/ar.h: 1600
try:
    AR_DPROP_DATA_EXPAND_BBOX = 66
except:
    pass

# /opt/dockethead/include/ar.h: 1603
try:
    AR_DPROP_CHARFIELD_DISPLAY_TYPE = 67
except:
    pass

# /opt/dockethead/include/ar.h: 1604
try:
    AR_DVAL_CHARFIELD_EDIT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1605
try:
    AR_DVAL_CHARFIELD_DROPDOWN = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1606
try:
    AR_DVAL_CHARFIELD_MASKED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1607
try:
    AR_DVAL_CHARFIELD_FILE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1608
try:
    AR_DVAL_CHARFIELD_RICH_TEXT = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1609
try:
    AR_DVAL_CHARFIELD_RICH_TEXT_ADV = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1612
try:
    AR_DPROP_CHARFIELD_AUTO_COMPLETE = 68
except:
    pass

# /opt/dockethead/include/ar.h: 1613
try:
    AR_DVAL_AUTO_COMPLETE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1614
try:
    AR_DVAL_AUTO_COMPLETE_LEADING = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1615
try:
    AR_DVAL_AUTO_COMPLETE_ANYWHERE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1618
try:
    AR_DPROP_CHARFIELD_AUTO_COMPLETE_MATCH_BY = 69
except:
    pass

# /opt/dockethead/include/ar.h: 1619
try:
    AR_DVAL_AUTO_COMPLETE_MATCH_BY_VALUE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1620
try:
    AR_DVAL_AUTO_COMPLETE_MATCH_BY_LABEL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1623
try:
    AR_DPROP_ENABLE_CLEAR = 70
except:
    pass

# /opt/dockethead/include/ar.h: 1624
try:
    AR_DVAL_ENABLE_CLEAR_ALWAYS = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1625
try:
    AR_DVAL_ENABLE_CLEAR_SEARCH_ONLY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1628
try:
    AR_DPROP_TEXT = 80
except:
    pass

# /opt/dockethead/include/ar.h: 1629
try:
    AR_DPROP_TEXT_FONT_STYLE = 81
except:
    pass

# /opt/dockethead/include/ar.h: 1631
try:
    AR_DPROP_TEXT_FONT_SIZE = 82
except:
    pass

# /opt/dockethead/include/ar.h: 1634
try:
    AR_DPROP_HTML_TEXT = 83
except:
    pass

# /opt/dockethead/include/ar.h: 1635
try:
    AR_DPROP_HTML_TEXT_COLOR = 84
except:
    pass

# /opt/dockethead/include/ar.h: 1638
try:
    AR_DPROP_JUSTIFY = 90
except:
    pass

# /opt/dockethead/include/ar.h: 1640
try:
    AR_DPROP_ALIGN = 91
except:
    pass

# /opt/dockethead/include/ar.h: 1644
try:
    AR_DPROP_IMAGE = 100
except:
    pass

# /opt/dockethead/include/ar.h: 1647
try:
    AR_DPROP_PUSH_BUTTON_IMAGE = 101
except:
    pass

# /opt/dockethead/include/ar.h: 1651
try:
    AR_DPROP_BUTTON_TEXT = 110
except:
    pass

# /opt/dockethead/include/ar.h: 1652
try:
    AR_DPROP_BUTTON_2D = 111
except:
    pass

# /opt/dockethead/include/ar.h: 1654
try:
    AR_DPROP_BUTTON_IMAGE_POSITION = 112
except:
    pass

# /opt/dockethead/include/ar.h: 1655
try:
    AR_DVAL_IMAGE_CENTER = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1656
try:
    AR_DVAL_IMAGE_LEFT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1657
try:
    AR_DVAL_IMAGE_RIGHT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1658
try:
    AR_DVAL_IMAGE_ABOVE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1659
try:
    AR_DVAL_IMAGE_BELOW = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1660
try:
    AR_DPROP_BUTTON_SCALE_IMAGE = 113
except:
    pass

# /opt/dockethead/include/ar.h: 1662
try:
    AR_DPROP_BUTTON_MAINTAIN_RATIO = 114
except:
    pass

# /opt/dockethead/include/ar.h: 1666
try:
    AR_DPROP_MENU_TEXT = 120
except:
    pass

# /opt/dockethead/include/ar.h: 1667
try:
    AR_DPROP_MENU_POS = 121
except:
    pass

# /opt/dockethead/include/ar.h: 1669
try:
    AR_DPROP_MENU_MODE = 122
except:
    pass

# /opt/dockethead/include/ar.h: 1670
try:
    AR_DVAL_CNTL_ITEM = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1671
try:
    AR_DVAL_CNTL_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1672
try:
    AR_DVAL_CNTL_SEPARATOR = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1673
try:
    AR_DVAL_CNTL_CHOICE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1674
try:
    AR_DVAL_CNTL_DIALOG = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1675
try:
    AR_DVAL_CNTL_A_MENU = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1677
try:
    AR_DPROP_MENU_PARENT = 123
except:
    pass

# /opt/dockethead/include/ar.h: 1678
try:
    AR_DPROP_MENU_HELP = 124
except:
    pass

# /opt/dockethead/include/ar.h: 1681
try:
    AR_DPROP_TOOLTIP = 130
except:
    pass

# /opt/dockethead/include/ar.h: 1682
try:
    AR_DPROP_TOOLBAR_POS = 131
except:
    pass

# /opt/dockethead/include/ar.h: 1684
try:
    AR_DPROP_TOOLBAR_MODE = 132
except:
    pass

# /opt/dockethead/include/ar.h: 1686
try:
    AR_DPROP_TOOLBAR_TEXT = 133
except:
    pass

# /opt/dockethead/include/ar.h: 1689
try:
    AR_DPROP_TAB_MODE = 140
except:
    pass

# /opt/dockethead/include/ar.h: 1691
try:
    AR_DPROP_TAB_COORD = 141
except:
    pass

# /opt/dockethead/include/ar.h: 1696
try:
    AR_DPROP_TAB_TEXT = 142
except:
    pass

# /opt/dockethead/include/ar.h: 1697
try:
    AR_DPROP_TAB_ORDER = 143
except:
    pass

# /opt/dockethead/include/ar.h: 1700
try:
    AR_DPROP_DATETIME_POPUP = 144
except:
    pass

# /opt/dockethead/include/ar.h: 1701
try:
    AR_DVAL_DATETIME_BOTH = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1702
try:
    AR_DVAL_DATETIME_TIME = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1703
try:
    AR_DVAL_DATETIME_DATE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1706
try:
    AR_DPROP_BACKGROUND_MODE = 145
except:
    pass

# /opt/dockethead/include/ar.h: 1707
try:
    AR_DVAL_BKG_MODE_OPAQUE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1708
try:
    AR_DVAL_BKG_MODE_TRANSPARENT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1711
try:
    AR_DPROP_TAB_NEXT = 150
except:
    pass

# /opt/dockethead/include/ar.h: 1713
try:
    AR_DPROP_DATA_BBOX = 151
except:
    pass

# /opt/dockethead/include/ar.h: 1716
try:
    AR_DPROP_VIEW_GRID_BBOX = 160
except:
    pass

# /opt/dockethead/include/ar.h: 1718
try:
    AR_DPROP_VUI_DEFAULT = 161
except:
    pass

# /opt/dockethead/include/ar.h: 1721
try:
    AR_DPROP_PANE_LAYOUT = 162
except:
    pass

# /opt/dockethead/include/ar.h: 1723
try:
    AR_DPROP_DETAIL_PANE_VISIBILITY = 163
except:
    pass

# /opt/dockethead/include/ar.h: 1724
try:
    AR_DVAL_PANE_ALWAYS_HIDDEN = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1725
try:
    AR_DVAL_PANE_HIDDEN = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1726
try:
    AR_DVAL_PANE_VISIBLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1727
try:
    AR_DVAL_PANE_ALWAYS_VISIBLE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1729
try:
    AR_DPROP_PROMPT_PANE_VISIBILITY = 164
except:
    pass

# /opt/dockethead/include/ar.h: 1730
try:
    AR_DPROP_RESULT_PANE_VISIBILITY = 165
except:
    pass

# /opt/dockethead/include/ar.h: 1736
try:
    AR_DPROP_DETAIL_PANE_COLOR = 166
except:
    pass

# /opt/dockethead/include/ar.h: 1737
try:
    AR_DPROP_DETAIL_PANE_IMAGE = 167
except:
    pass

# /opt/dockethead/include/ar.h: 1739
try:
    AR_DPROP_IMAGE_ALIGN = 168
except:
    pass

# /opt/dockethead/include/ar.h: 1741
try:
    AR_DPROP_IMAGE_JUSTIFY = 169
except:
    pass

# /opt/dockethead/include/ar.h: 1745
try:
    AR_DPROP_DISPLAY_PARENT = 170
except:
    pass

# /opt/dockethead/include/ar.h: 1749
try:
    AR_DPROP_PAGE_ORDER = 180
except:
    pass

# /opt/dockethead/include/ar.h: 1751
try:
    AR_DPROP_PAGE_FIELD_TYPE = 181
except:
    pass

# /opt/dockethead/include/ar.h: 1752
try:
    AR_DVAL_PAGE_FIELD_NONEDITABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1753
try:
    AR_DVAL_PAGE_FIELD_EDITABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1755
try:
    AR_DPROP_TABLE_PANEL_BBOX = 182
except:
    pass

# /opt/dockethead/include/ar.h: 1759
try:
    AR_DPROP_PAGE_LABEL_DISPLAY = 190
except:
    pass

# /opt/dockethead/include/ar.h: 1762
try:
    AR_DVAL_PAGE_DISPLAY_TOP = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1763
try:
    AR_DVAL_PAGE_DISPLAY_BOTTOM = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1764
try:
    AR_DVAL_PAGE_DISPLAY_LEFT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1765
try:
    AR_DVAL_PAGE_DISPLAY_RIGHT = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1766
try:
    AR_DVAL_PAGE_DISPLAY_NONE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1769
try:
    AR_DPROP_PAGE_ARRANGEMENT = 191
except:
    pass

# /opt/dockethead/include/ar.h: 1772
try:
    AR_DVAL_PAGE_SCROLL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1773
try:
    AR_DVAL_PAGE_LAYER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1775
try:
    AR_DPROP_DEFAULT_PAGE = 192
except:
    pass

# /opt/dockethead/include/ar.h: 1779
try:
    AR_DPROP_TITLE_BAR_ICON_IMAGE = 200
except:
    pass

# /opt/dockethead/include/ar.h: 1785
try:
    AR_DPROP_DETAIL_PANE_WIDTH = 201
except:
    pass

# /opt/dockethead/include/ar.h: 1789
try:
    AR_DPROP_DETAIL_PANE_HEIGHT = 202
except:
    pass

# /opt/dockethead/include/ar.h: 1790
try:
    AR_DPROP_DETAIL_BANNER_VISIBILITY = 203
except:
    pass

# /opt/dockethead/include/ar.h: 1792
try:
    AR_DPROP_PROMPT_BANNER_VISIBILITY = 204
except:
    pass

# /opt/dockethead/include/ar.h: 1794
try:
    AR_DPROP_RESULT_BANNER_VISIBILITY = 205
except:
    pass

# /opt/dockethead/include/ar.h: 1796
try:
    AR_DPROP_ALIAS_SINGULAR = 206
except:
    pass

# /opt/dockethead/include/ar.h: 1797
try:
    AR_DPROP_ALIAS_PLURAL = 207
except:
    pass

# /opt/dockethead/include/ar.h: 1798
try:
    AR_DPROP_ALIAS_SHORT_SINGULAR = 208
except:
    pass

# /opt/dockethead/include/ar.h: 1800
try:
    AR_DPROP_ALIAS_SHORT_PLURAL = 209
except:
    pass

# /opt/dockethead/include/ar.h: 1802
try:
    AR_DPROP_ALIAS_ABBREV_SINGULAR = 210
except:
    pass

# /opt/dockethead/include/ar.h: 1803
try:
    AR_DPROP_ALIAS_ABBREV_PLURAL = 211
except:
    pass

# /opt/dockethead/include/ar.h: 1804
try:
    AR_DPROP_NAMED_SEARCHES = 212
except:
    pass

# /opt/dockethead/include/ar.h: 1807
try:
    AR_DPROP_MENU_ACCESS = 213
except:
    pass

# /opt/dockethead/include/ar.h: 1821
def AR_GET_MENU_ACCESS_ENABLED(x):
    return (x & 2) and (x & 1) or TRUE

# /opt/dockethead/include/ar.h: 1823
def AR_SET_MENU_ACCESS_ENABLED(x):
    return (x | 3)

# /opt/dockethead/include/ar.h: 1825
def AR_SET_MENU_ACCESS_DISABLED(x):
    return ((x | 2) & (~1))

# /opt/dockethead/include/ar.h: 1827
try:
    AR_DPROP_PANE_VISIBILITY_OPTION = 214
except:
    pass

# /opt/dockethead/include/ar.h: 1830
try:
    AR_DVAL_PANE_VISIBILITY_USER_CHOICE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1831
try:
    AR_DVAL_PANE_VISIBILITY_ADMIN = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1833
try:
    AR_DPROP_REQUEST_IDENTIFIER = 215
except:
    pass

# /opt/dockethead/include/ar.h: 1836
try:
    AR_DPROP_QUERY_LIST_COLOR = 216
except:
    pass

# /opt/dockethead/include/ar.h: 1841
try:
    AR_DPROP_COLUMN_WIDTH = 220
except:
    pass

# /opt/dockethead/include/ar.h: 1842
try:
    AR_DPROP_COLUMN_ORDER = 221
except:
    pass

# /opt/dockethead/include/ar.h: 1843
try:
    AR_DPROP_SORT_SEQ = 222
except:
    pass

# /opt/dockethead/include/ar.h: 1845
try:
    AR_DPROP_SORT_DIR = 223
except:
    pass

# /opt/dockethead/include/ar.h: 1847
try:
    AR_DVAL_SORT_DIR_ASCENDING = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1848
try:
    AR_DVAL_SORT_DIR_DESCENDING = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1850
try:
    AR_DPROP_DRILL_DOWN = 224
except:
    pass

# /opt/dockethead/include/ar.h: 1852
try:
    AR_DVAL_DRILL_DOWN_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1853
try:
    AR_DVAL_DRILL_DOWN_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1855
try:
    AR_DPROP_REFRESH = 225
except:
    pass

# /opt/dockethead/include/ar.h: 1856
try:
    AR_DVAL_REFRESH_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1857
try:
    AR_DVAL_REFRESH_TABLE_MAX = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1859
try:
    AR_DPROP_AUTO_REFRESH = 226
except:
    pass

# /opt/dockethead/include/ar.h: 1860
try:
    AR_DVAL_AUTO_REFRESH_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1861
try:
    AR_DVAL_AUTO_REFRESH_TABLE_MAX = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1863
try:
    AR_DPROP_AUTOFIT_COLUMNS = 227
except:
    pass

# /opt/dockethead/include/ar.h: 1865
try:
    AR_DVAL_AUTOFIT_COLUMNS_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1867
try:
    AR_DVAL_AUTOFIT_COLUMNS_SET = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1870
try:
    AR_DPROP_APPLY_DIRTY = 228
except:
    pass

# /opt/dockethead/include/ar.h: 1871
try:
    AR_DPROP_IMAGE_CACHE = 229
except:
    pass

# /opt/dockethead/include/ar.h: 1874
try:
    AR_DPROP_ENUM_LABELS = 230
except:
    pass

# /opt/dockethead/include/ar.h: 1876
try:
    AR_DPROP_MANAGE_EXPAND_BOX = 231
except:
    pass

# /opt/dockethead/include/ar.h: 1878
try:
    AR_DVAL_EXPAND_BOX_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1879
try:
    AR_DVAL_EXPAND_BOX_HIDE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1880
try:
    AR_DVAL_EXPAND_BOX_SHOW = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1882
try:
    AR_DPROP_ATTACH_ADD_LABEL = 232
except:
    pass

# /opt/dockethead/include/ar.h: 1884
try:
    AR_DPROP_ATTACH_DELETE_LABEL = 233
except:
    pass

# /opt/dockethead/include/ar.h: 1886
try:
    AR_DPROP_ATTACH_DISPLAY_LABEL = 234
except:
    pass

# /opt/dockethead/include/ar.h: 1888
try:
    AR_DPROP_ATTACH_SAVE_LABEL = 235
except:
    pass

# /opt/dockethead/include/ar.h: 1890
try:
    AR_DPROP_ATTACH_LABEL_TITLE = 236
except:
    pass

# /opt/dockethead/include/ar.h: 1892
try:
    AR_DPROP_ATTACH_FILENAME_TITLE = 237
except:
    pass

# /opt/dockethead/include/ar.h: 1894
try:
    AR_DPROP_ATTACH_FILESIZE_TITLE = 238
except:
    pass

# /opt/dockethead/include/ar.h: 1896
try:
    AR_DPROP_HIDE_PAGE_TABS_BORDERS = 239
except:
    pass

# /opt/dockethead/include/ar.h: 1898
try:
    AR_DPROP_DISPLAY_AS_TEXT_ONLY = 240
except:
    pass

# /opt/dockethead/include/ar.h: 1900
try:
    AR_DPROP_AR_OBJECT_NAME = 241
except:
    pass

# /opt/dockethead/include/ar.h: 1901
try:
    AR_DPROP_DISPLAY_FIELD_APP = 242
except:
    pass

# /opt/dockethead/include/ar.h: 1903
try:
    AR_DPROP_ZERO_SIZE_WHEN_HIDDEN = 243
except:
    pass

# /opt/dockethead/include/ar.h: 1905
try:
    AR_DPROP_ACCESSIBLE_HINT = 244
except:
    pass

# /opt/dockethead/include/ar.h: 1907
try:
    AR_DPROP_INITIAL_CURRENCY_TYPE = 245
except:
    pass

# /opt/dockethead/include/ar.h: 1909
try:
    AR_DPROP_AUTO_FIELD_COLPROP = 246
except:
    pass

# /opt/dockethead/include/ar.h: 1911
try:
    AR_DPROP_AUTO_FIELD_ROWNUM = 247
except:
    pass

# /opt/dockethead/include/ar.h: 1913
try:
    AR_DPROP_AUTO_FIELD_ROWPART = 248
except:
    pass

# /opt/dockethead/include/ar.h: 1915
try:
    AR_DPROP_AUTO_FIELD_ORDER = 249
except:
    pass

# /opt/dockethead/include/ar.h: 1917
try:
    AR_DPROP_AUTO_FIELD_TYPE = 250
except:
    pass

# /opt/dockethead/include/ar.h: 1918
try:
    AR_DVAL_AUTO_FIELD_REGULAR = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1919
try:
    AR_DVAL_AUTO_FIELD_NAV = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1920
try:
    AR_DVAL_AUTO_FIELD_ACTION = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1921
try:
    AR_DVAL_AUTO_FIELD_GROUPTITLE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 1922
try:
    AR_DVAL_AUTO_FIELD_PAGETITLE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 1923
try:
    AR_DVAL_AUTO_FIELD_APPTITLE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 1925
try:
    AR_DPROP_AUTO_LAYOUT = 251
except:
    pass

# /opt/dockethead/include/ar.h: 1926
try:
    AR_DVAL_AUTO_LAYOUT_OFF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1927
try:
    AR_DVAL_AUTO_LAYOUT_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1929
try:
    AR_DPROP_AUTO_LAYOUT_VUI_NAV = 252
except:
    pass

# /opt/dockethead/include/ar.h: 1930
try:
    AR_DVAL_AUTO_LAYOUT_VUI_NAV_OFF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1931
try:
    AR_DVAL_AUTO_LAYOUT_VUI_NAV_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1933
try:
    AR_DPROP_AUTO_LAYOUT_STYLE_SHEET = 253
except:
    pass

# /opt/dockethead/include/ar.h: 1935
try:
    AR_DPROP_AUTO_FIELD_NAVPROP = 254
except:
    pass

# /opt/dockethead/include/ar.h: 1936
try:
    AR_DVAL_AUTO_FIELD_LEVEL1 = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1937
try:
    AR_DVAL_AUTO_FIELD_LEVEL2 = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1938
try:
    AR_DVAL_AUTO_FIELD_LEVEL3 = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1940
try:
    AR_DPROP_AUTO_FIELD_SPACER = 255
except:
    pass

# /opt/dockethead/include/ar.h: 1941
try:
    AR_DVAL_AUTO_FIELD_SPACER_OFF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1942
try:
    AR_DVAL_AUTO_FIELD_SPACER_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1944
try:
    AR_DPROP_FORMACTION_FIELDS = 256
except:
    pass

# /opt/dockethead/include/ar.h: 1947
try:
    AR_DPROP_AUTO_SET_OVERLAP_FIELD = 257
except:
    pass

# /opt/dockethead/include/ar.h: 1950
try:
    AR_DPROP_AR_SERVER_NAME = 258
except:
    pass

# /opt/dockethead/include/ar.h: 1953
try:
    AR_DPROP_AUTO_FIELD_ALIGN = 259
except:
    pass

# /opt/dockethead/include/ar.h: 1954
try:
    AR_DVAL_AUTO_FIELD_ALIGN_LEFT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1955
try:
    AR_DVAL_AUTO_FIELD_ALIGN_RIGHT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1957
try:
    AR_DPROP_FORMACTION_PAGE_PROPERTIES = 260
except:
    pass

# /opt/dockethead/include/ar.h: 1959
try:
    AR_DPROP_FORMACTION_FLDS_EXCLUDE = 261
except:
    pass

# /opt/dockethead/include/ar.h: 1961
try:
    AR_DVAL_FORMACTION_FLDS_EXCLUDE_OFF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1962
try:
    AR_DVAL_FORMACTION_FLDS_EXCLUDE_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1964
try:
    AR_DPROP_AUTO_FIELD_NEW_COLUMN = 262
except:
    pass

# /opt/dockethead/include/ar.h: 1965
try:
    AR_DVAL_AUTO_FIELD_NEW_COLUMN_OFF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1966
try:
    AR_DVAL_AUTO_FIELD_NEW_COLUMN_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1968
try:
    AR_DPROP_AUTO_FIELD_NEW_SECTION = 263
except:
    pass

# /opt/dockethead/include/ar.h: 1969
try:
    AR_DVAL_AUTO_FIELD_NEW_SECTION_OFF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1970
try:
    AR_DVAL_AUTO_FIELD_NEW_SECTION_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1972
try:
    AR_DPROP_VUI_DEFAULT_PROCESS = 264
except:
    pass

# /opt/dockethead/include/ar.h: 1974
try:
    AR_DPROP_WEB_HEADER_CONTENT = 265
except:
    pass

# /opt/dockethead/include/ar.h: 1975
try:
    AR_DPROP_WEB_FOOTER_CONTENT = 266
except:
    pass

# /opt/dockethead/include/ar.h: 1977
try:
    AR_DPROP_PATH_TO_BKG_IMAGE = 267
except:
    pass

# /opt/dockethead/include/ar.h: 1979
try:
    AR_DPROP_WEB_TOOLBAR_VISIBILITY = 268
except:
    pass

# /opt/dockethead/include/ar.h: 1982
try:
    AR_DPROP_AR_GRAPH_PLUGIN_NAME = 269
except:
    pass

# /opt/dockethead/include/ar.h: 1985
try:
    AR_DPROP_EXPAND_COLLAPSE_TREE_LEVELS = 270
except:
    pass

# /opt/dockethead/include/ar.h: 1986
try:
    AR_DVAL_EXPAND_ALL_LEVELS = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1987
try:
    AR_DVAL_COLLAPSE_ALL_LEVELS = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1988
try:
    AR_DPROP_ATTACH_DESELECT_LABEL = 271
except:
    pass

# /opt/dockethead/include/ar.h: 1992
try:
    AR_DPROP_LAYOUT_POLICY = 272
except:
    pass

# /opt/dockethead/include/ar.h: 1993
try:
    AR_DVAL_LAYOUT_XY = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1994
try:
    AR_DVAL_LAYOUT_FILL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 1995
try:
    AR_DVAL_LAYOUT_FLOW = 2
except:
    pass

# /opt/dockethead/include/ar.h: 1997
try:
    AR_DPROP_PAGEHOLDER_DISPLAY_TYPE = 273
except:
    pass

# /opt/dockethead/include/ar.h: 1998
try:
    AR_DVAL_PAGEHOLDER_DISPLAY_TYPE_TABCTRL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 1999
try:
    AR_DVAL_PAGEHOLDER_DISPLAY_TYPE_STACKEDVIEW = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2000
try:
    AR_DVAL_PAGEHOLDER_DISPLAY_TYPE_SPLITTERVIEW = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2001
try:
    AR_DVAL_PAGEHOLDER_DISPLAY_TYPE_ACCORDION = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2003
try:
    AR_DPROP_ORIENTATION = 274
except:
    pass

# /opt/dockethead/include/ar.h: 2004
try:
    AR_DVAL_ORIENTATION_HORIZONTAL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2005
try:
    AR_DVAL_ORIENTATION_VERTICAL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2006
try:
    AR_DVAL_ORIENTATION_VERTICAL_UP = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2008
try:
    AR_DPROP_PAGEHOLDER_MARGIN_LEFT = 275
except:
    pass

# /opt/dockethead/include/ar.h: 2009
try:
    AR_DPROP_PAGEHOLDER_MARGIN_TOP = 276
except:
    pass

# /opt/dockethead/include/ar.h: 2010
try:
    AR_DPROP_PAGEHOLDER_MARGIN_RIGHT = 277
except:
    pass

# /opt/dockethead/include/ar.h: 2011
try:
    AR_DPROP_PAGEHOLDER_MARGIN_BOTTOM = 278
except:
    pass

# /opt/dockethead/include/ar.h: 2012
try:
    AR_DPROP_PAGEHOLDER_SPACING = 279
except:
    pass

# /opt/dockethead/include/ar.h: 2013
try:
    AR_DPROP_PAGEHOLDER_INIT_PAGE = 280
except:
    pass

# /opt/dockethead/include/ar.h: 2015
try:
    AR_DPROP_PAGE_HEADER_STATE = 281
except:
    pass

# /opt/dockethead/include/ar.h: 2016
try:
    AR_DVAL_PAGE_HEADER_HIDDEN = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2017
try:
    AR_DVAL_PAGE_HEADER_VISIBLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2019
try:
    AR_DPROP_PAGE_HEADER_COLOR = 282
except:
    pass

# /opt/dockethead/include/ar.h: 2020
try:
    AR_DPROP_PAGE_INITIAL_SIZE = 283
except:
    pass

# /opt/dockethead/include/ar.h: 2021
try:
    AR_DPROP_PAGE_MIN_SIZE = 284
except:
    pass

# /opt/dockethead/include/ar.h: 2022
try:
    AR_DPROP_PAGE_MAX_SIZE = 285
except:
    pass

# /opt/dockethead/include/ar.h: 2024
try:
    AR_DPROP_PAGE_BODY_STATE = 286
except:
    pass

# /opt/dockethead/include/ar.h: 2025
try:
    AR_DVAL_PAGE_BODY_COLLAPSE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2026
try:
    AR_DVAL_PAGE_BODY_EXPAND = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2028
try:
    AR_DPROP_LOCALIZATION_REQUIRED = 287
except:
    pass

# /opt/dockethead/include/ar.h: 2032
try:
    AR_DPROP_FIELD_HIGHLIGHT = 288
except:
    pass

# /opt/dockethead/include/ar.h: 2033
try:
    AR_DVAL_FIELD_HIGHLIGHT_DISABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2034
try:
    AR_DVAL_FIELD_HIGHLIGHT_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2036
try:
    AR_DPROP_FIELD_HIGHLIGHT_START_COLOR = 289
except:
    pass

# /opt/dockethead/include/ar.h: 2037
try:
    AR_DPROP_FIELD_HIGHLIGHT_END_COLOR = 290
except:
    pass

# /opt/dockethead/include/ar.h: 2040
try:
    AR_DPROP_FIELD_ROUNDED = 291
except:
    pass

# /opt/dockethead/include/ar.h: 2041
try:
    AR_DVAL_FIELD_ROUNDED_DISABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2042
try:
    AR_DVAL_FIELD_ROUNDED_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2045
try:
    AR_DPROP_FIELD_MIN_WIDTH = 292
except:
    pass

# /opt/dockethead/include/ar.h: 2046
try:
    AR_DPROP_FIELD_MAX_WIDTH = 293
except:
    pass

# /opt/dockethead/include/ar.h: 2047
try:
    AR_DPROP_FIELD_MIN_HEIGHT = 294
except:
    pass

# /opt/dockethead/include/ar.h: 2048
try:
    AR_DPROP_FIELD_MAX_HEIGHT = 295
except:
    pass

# /opt/dockethead/include/ar.h: 2050
try:
    AR_DPROP_COLOR_FILL_GRADIENT = 296
except:
    pass

# /opt/dockethead/include/ar.h: 2051
try:
    AR_DPROP_COLOR_FILL_GRADIENT_EFFECT = 297
except:
    pass

# /opt/dockethead/include/ar.h: 2052
try:
    AR_DVAL_GRADIENT_EFFECT_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2053
try:
    AR_DVAL_GRADIENT_EFFECT_LINEAR_HORIZONTAL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2054
try:
    AR_DVAL_GRADIENT_EFFECT_LINEAR_VERTICAL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2055
try:
    AR_DVAL_GRADIENT_EFFECT_REFLECTED_HORIZONTAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2056
try:
    AR_DVAL_GRADIENT_EFFECT_REFLECTED_VERTICAL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2058
try:
    AR_DPROP_COLOR_FILL_OPACITY = 298
except:
    pass

# /opt/dockethead/include/ar.h: 2061
try:
    AR_DPROP_FIELD_ROUNDED_TOP_RIGHT_RADIUS = 300
except:
    pass

# /opt/dockethead/include/ar.h: 2062
try:
    AR_DPROP_FIELD_ROUNDED_TOP_LEFT_RADIUS = 301
except:
    pass

# /opt/dockethead/include/ar.h: 2063
try:
    AR_DPROP_FIELD_ROUNDED_BOTTOM_RIGHT_RADIUS = 302
except:
    pass

# /opt/dockethead/include/ar.h: 2064
try:
    AR_DPROP_FIELD_ROUNDED_BOTTOM_LEFT_RADIUS = 303
except:
    pass

# /opt/dockethead/include/ar.h: 2067
try:
    AR_DPROP_PANELHOLDER_SPLITTER = 304
except:
    pass

# /opt/dockethead/include/ar.h: 2068
try:
    AR_DVAL_SPLITTER_HIDE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2069
try:
    AR_DVAL_SPLITTER_SHOW = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2070
try:
    AR_DVAL_SPLITTER_INVISIBLE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2074
try:
    AR_DPROP_COLOR_GRADIENT_HEADER = 305
except:
    pass

# /opt/dockethead/include/ar.h: 2075
try:
    AR_DPROP_COLOR_GRADIENT_EFFECT_HEADER = 306
except:
    pass

# /opt/dockethead/include/ar.h: 2076
try:
    AR_DVAL_GRADIENT_EFFECT_HEADER_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2077
try:
    AR_DVAL_GRADIENT_EFFECT_HEADER_LINEAR_HORIZONTAL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2078
try:
    AR_DVAL_GRADIENT_EFFECT_HEADER_LINEAR_VERTICAL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2079
try:
    AR_DVAL_GRADIENT_EFFECT_HEADER_REFLECTED_HORIZONTAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2080
try:
    AR_DVAL_GRADIENT_EFFECT_HEADER_REFLECTED_VERTICAL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2083
try:
    AR_DPROP_HIDE_PANELHOLDER_BORDERS = 307
except:
    pass

# /opt/dockethead/include/ar.h: 2085
try:
    AR_DPROP_PANEL_SLACK_ORDER = 308
except:
    pass

# /opt/dockethead/include/ar.h: 2086
try:
    AR_DPROP_PANEL_SLACK_DISTRIBUTION_ORDER = 308
except:
    pass

# /opt/dockethead/include/ar.h: 2087
try:
    AR_DPROP_PANEL_AVOID_WHITESPACE = 309
except:
    pass

# /opt/dockethead/include/ar.h: 2088
try:
    AR_DPROP_PANEL_FIT_TO_CONTENT = 309
except:
    pass

# /opt/dockethead/include/ar.h: 2090
try:
    AR_DPROP_ALIGNED = 310
except:
    pass

# /opt/dockethead/include/ar.h: 2091
try:
    AR_DVAL_ALIGNED_LEFT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2092
try:
    AR_DVAL_ALIGNED_RIGHT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2094
try:
    AR_DPROP_RIGHT_BBOX = 311
except:
    pass

# /opt/dockethead/include/ar.h: 2096
try:
    AR_DPROP_HEADER_HEIGHT = 312
except:
    pass

# /opt/dockethead/include/ar.h: 2097
try:
    AR_DPROP_NAV_ITEM_TEXT_COLOR = 313
except:
    pass

# /opt/dockethead/include/ar.h: 2100
try:
    AR_DPROP_FIELD_DRAGGABLE = 314
except:
    pass

# /opt/dockethead/include/ar.h: 2101
try:
    AR_DPROP_FIELD_DROPPABLE = 315
except:
    pass

# /opt/dockethead/include/ar.h: 2104
try:
    AR_DPROP_LOCALIZE_VIEW = 316
except:
    pass

# /opt/dockethead/include/ar.h: 2105
try:
    AR_DVAL_LOCALIZE_VIEW_SKIP = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2106
try:
    AR_DVAL_LOCALIZE_VIEW_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2108
try:
    AR_DPROP_LOCALIZE_FIELD = 317
except:
    pass

# /opt/dockethead/include/ar.h: 2109
try:
    AR_DVAL_LOCALIZE_FIELD_SKIP = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2110
try:
    AR_DVAL_LOCALIZE_FIELD_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2112
try:
    AR_DPROP_FLOW_LAYOUT_VERT_SPACE = 318
except:
    pass

# /opt/dockethead/include/ar.h: 2114
try:
    AR_DPROP_PANEL_MARGIN_LEFT = 319
except:
    pass

# /opt/dockethead/include/ar.h: 2115
try:
    AR_DPROP_PANEL_MARGIN_TOP = 320
except:
    pass

# /opt/dockethead/include/ar.h: 2116
try:
    AR_DPROP_PANEL_MARGIN_RIGHT = 321
except:
    pass

# /opt/dockethead/include/ar.h: 2117
try:
    AR_DPROP_PANEL_MARGIN_BOTTOM = 322
except:
    pass

# /opt/dockethead/include/ar.h: 2118
try:
    AR_DPROP_AUTO_RESIZE = 323
except:
    pass

# /opt/dockethead/include/ar.h: 2119
try:
    AR_DVAL_RESIZE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2120
try:
    AR_DVAL_RESIZE_VERT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2121
try:
    AR_DVAL_RESIZE_HORZ = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2122
try:
    AR_DVAL_RESIZE_BOTH = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2124
try:
    AR_DPROP_FIELD_FLOAT_STYLE = 324
except:
    pass

# /opt/dockethead/include/ar.h: 2125
try:
    AR_DVAL_FLOAT_STYLE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2126
try:
    AR_DVAL_FLOAT_STYLE_MODELESS = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2127
try:
    AR_DVAL_FLOAT_STYLE_DIALOG = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2128
try:
    AR_DVAL_FLOAT_STYLE_TOOLTIP = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2130
try:
    AR_DPROP_FIELD_FLOAT_EFFECT = 325
except:
    pass

# /opt/dockethead/include/ar.h: 2131
try:
    AR_DVAL_FLOAT_EFFECT_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2132
try:
    AR_DVAL_FLOAT_EFFECT_APPEAR_DISAPPEAR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2133
try:
    AR_DVAL_FLOAT_EFFECT_GROW_SHRINK = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2134
try:
    AR_DVAL_FLOAT_EFFECT_FADEIN_FADEOUT = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2136
try:
    AR_DPROP_PANELHOLDER_SHRINKTOFIT = 326
except:
    pass

# /opt/dockethead/include/ar.h: 2137
try:
    AR_DPROP_PANEL_BORDER_THICKNESS = 327
except:
    pass

# /opt/dockethead/include/ar.h: 2138
try:
    AR_DPROP_AUTO_COMPLETE_AFTER_KEYSTROKES = 328
except:
    pass

# /opt/dockethead/include/ar.h: 2139
try:
    AR_DPROP_AUTO_COMPLETE_HIDE_MENU_BUTTON = 329
except:
    pass

# /opt/dockethead/include/ar.h: 2141
try:
    AR_DPROP_ROW_LABEL = 330
except:
    pass

# /opt/dockethead/include/ar.h: 2142
try:
    AR_DPROP_ROW_LABEL_PLURAL = 331
except:
    pass

# /opt/dockethead/include/ar.h: 2146
try:
    AR_DPROP_TABLE_COLUMN_HEADER_ALIGNMENT = 332
except:
    pass

# /opt/dockethead/include/ar.h: 2147
try:
    AR_DPROP_TABLE_COLUMN_DATA_ALIGNMENT = 333
except:
    pass

# /opt/dockethead/include/ar.h: 2148
try:
    AR_DVAL_TABLE_COLUMN_ALIGNMENT_RIGHT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2149
try:
    AR_DVAL_TABLE_COLUMN_ALIGNMENT_CENTER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2150
try:
    AR_DVAL_TABLE_COLUMN_ALIGNMENT_LEFT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2152
try:
    AR_DPROP_MOUSEOVER_EFFECT = 334
except:
    pass

# /opt/dockethead/include/ar.h: 2153
try:
    AR_DVAL_MOUSEOVER_EFFECT_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2154
try:
    AR_DVAL_MOUSEOVER_EFFECT_CURSOR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2155
try:
    AR_DVAL_MOUSEOVER_EFFECT_HIGHLIGHT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2157
try:
    AR_DPROP_DVF_INLINE = 335
except:
    pass

# /opt/dockethead/include/ar.h: 2158
try:
    AR_DPROP_EXTERNAL_LINK_BUTTON = 336
except:
    pass

# /opt/dockethead/include/ar.h: 2163
try:
    AR_DPROP_PREFIX_NEW = 900
except:
    pass

# /opt/dockethead/include/ar.h: 2164
try:
    AR_DPROP_PREFIX_SEARCH = 901
except:
    pass

# /opt/dockethead/include/ar.h: 2165
try:
    AR_DPROP_PREFIX_MODIFY = 902
except:
    pass

# /opt/dockethead/include/ar.h: 2166
try:
    AR_DPROP_PREFIX_MODIFY_ALL = 903
except:
    pass

# /opt/dockethead/include/ar.h: 2167
try:
    AR_DPROP_PREFIX_DISPLAY = 904
except:
    pass

# /opt/dockethead/include/ar.h: 2168
try:
    AR_DPROP_PREFIX_MATCHING_REQ = 905
except:
    pass

# /opt/dockethead/include/ar.h: 2169
try:
    AR_DPROP_PREFIX_NO_MATCHING_REQ = 906
except:
    pass

# /opt/dockethead/include/ar.h: 2171
try:
    AR_DPROP_PREFIX_MINval = 900
except:
    pass

# /opt/dockethead/include/ar.h: 2172
try:
    AR_DPROP_PREFIX_MAXval = 906
except:
    pass

# /opt/dockethead/include/ar.h: 2177
try:
    AR_DPROP_TABLE_DISPLAY_TYPE = 5001
except:
    pass

# /opt/dockethead/include/ar.h: 2178
try:
    AR_DVAL_TABLE_DISPLAY_TABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2179
try:
    AR_DVAL_TABLE_DISPLAY_RESULTS_LIST = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2180
try:
    AR_DVAL_TABLE_DISPLAY_NOTIFICATION = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2181
try:
    AR_DVAL_TABLE_DISPLAY_SINGLE_TABLE_TREE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2182
try:
    AR_DVAL_TABLE_DISPLAY_MULTI_TABLE_TREE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2183
try:
    AR_DVAL_TABLE_DISPLAY_PAGE_ARRAY = 5
except:
    pass

# /opt/dockethead/include/ar.h: 2185
try:
    AR_DPROP_TABLE_SELINIT = 5003
except:
    pass

# /opt/dockethead/include/ar.h: 2187
try:
    AR_DVAL_TABLE_SELINIT_SELFIRE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2188
try:
    AR_DVAL_TABLE_SELINIT_SELNOFIRE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2189
try:
    AR_DVAL_TABLE_SELINIT_NOSEL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2191
try:
    AR_DPROP_TABLE_SELREFRESH = 5004
except:
    pass

# /opt/dockethead/include/ar.h: 2193
try:
    AR_DVAL_TABLE_SELREFRESH_RETFIRE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2194
try:
    AR_DVAL_TABLE_SELREFRESH_RETNOFIRE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2195
try:
    AR_DVAL_TABLE_SELREFRESH_FIRSTFIRE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2196
try:
    AR_DVAL_TABLE_SELREFRESH_FIRSTNOFIRE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2197
try:
    AR_DVAL_TABLE_SELREFRESH_NOSEL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2199
try:
    AR_DPROP_TABLE_CHUNK_SIZE = 5005
except:
    pass

# /opt/dockethead/include/ar.h: 2200
try:
    AR_DPROP_TABLE_CHUNK_NEXT = 5006
except:
    pass

# /opt/dockethead/include/ar.h: 2201
try:
    AR_DPROP_TABLE_CHUNK_PREV = 5007
except:
    pass

# /opt/dockethead/include/ar.h: 2202
try:
    AR_DPROP_TABLE_NOT_REFRESHED = 5008
except:
    pass

# /opt/dockethead/include/ar.h: 2204
try:
    AR_DPROP_TABLE_ENTRIES_RETURNED = 5009
except:
    pass

# /opt/dockethead/include/ar.h: 2206
try:
    AR_DPROP_TABLE_AUTOREFRESH = 5010
except:
    pass

# /opt/dockethead/include/ar.h: 2207
try:
    AR_DPROP_TABLE_DRILL_COL = 5011
except:
    pass

# /opt/dockethead/include/ar.h: 2210
try:
    AR_DPROP_TABLE_SELROWS_DISABLE = 5012
except:
    pass

# /opt/dockethead/include/ar.h: 2211
try:
    AR_DVAL_TABLE_SELROWS_MULTI_SELECT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2212
try:
    AR_DVAL_TABLE_SELROWS_DISABLE_YES = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2213
try:
    AR_DVAL_TABLE_SELROWS_SINGLE_SELECT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2214
try:
    AR_DVAL_TABLE_SELROWS_DISABLE_NO = AR_DVAL_TABLE_SELROWS_MULTI_SELECT
except:
    pass

# /opt/dockethead/include/ar.h: 2216
try:
    AR_DPROP_TABLE_SELECT_ALL = 5013
except:
    pass

# /opt/dockethead/include/ar.h: 2217
try:
    AR_DPROP_TABLE_DESELECT_ALL = 5014
except:
    pass

# /opt/dockethead/include/ar.h: 2218
try:
    AR_DPROP_TABLE_REFRESH = 5015
except:
    pass

# /opt/dockethead/include/ar.h: 2219
try:
    AR_DPROP_TABLE_REPORT = 5016
except:
    pass

# /opt/dockethead/include/ar.h: 2220
try:
    AR_DPROP_TABLE_DELETE = 5017
except:
    pass

# /opt/dockethead/include/ar.h: 2221
try:
    AR_DPROP_TABLE_READ = 5018
except:
    pass

# /opt/dockethead/include/ar.h: 2222
try:
    AR_DPROP_TABLE_UNREAD = 5019
except:
    pass

# /opt/dockethead/include/ar.h: 2223
try:
    AR_DPROP_TABLE_SELECTIONCOLUMN_LABEL = 5020
except:
    pass

# /opt/dockethead/include/ar.h: 2225
try:
    AR_DPROP_TABLE_COL_DISPLAY_TYPE = 5021
except:
    pass

# /opt/dockethead/include/ar.h: 2226
try:
    AR_DVAL_TABLE_COL_DISPLAY_NONEDITABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2227
try:
    AR_DVAL_TABLE_COL_DISPLAY_EDITABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2228
try:
    AR_DVAL_TABLE_COL_DISPLAY_HTML = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2229
try:
    AR_DVAL_TABLE_COL_DISPLAY_PAGE_DATA = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2230
try:
    AR_DVAL_TABLE_COL_DISPLAY_DROPDOWN_MENU = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2232
try:
    AR_DPROP_TABLE_COL_INITVAL = 5022
except:
    pass

# /opt/dockethead/include/ar.h: 2234
try:
    AR_DPROP_FIXED_TABLE_HEADERS = 5023
except:
    pass

# /opt/dockethead/include/ar.h: 2235
try:
    AR_DVAL_FIXED_TABLE_HEADERS_DISABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2236
try:
    AR_DVAL_FIXED_TABLE_HEADERS_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2238
try:
    AR_DPROP_VIEWFIELD_SCROLLBARS = 5024
except:
    pass

# /opt/dockethead/include/ar.h: 2239
try:
    AR_DVAL_VIEWFIELD_SCROLLBARS_AUTO = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2240
try:
    AR_DVAL_VIEWFIELD_SCROLLBARS_ON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2241
try:
    AR_DVAL_VIEWFIELD_SCROLLBARS_HIDDEN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2243
try:
    AR_DPROP_VIEWFIELD_BORDERS = 5025
except:
    pass

# /opt/dockethead/include/ar.h: 2244
try:
    AR_DVAL_VIEWFIELD_BORDERS_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2245
try:
    AR_DVAL_VIEWFIELD_BORDERS_NONE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2246
try:
    AR_DVAL_VIEWFIELD_BORDERS_ENABLE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2248
try:
    AR_DPROP_ENTRYPOINT_LABEL_DEFAULT_NEW = 5026
except:
    pass

# /opt/dockethead/include/ar.h: 2249
try:
    AR_DPROP_ENTRYPOINT_LABEL_DEFAULT_SEARCH = 5027
except:
    pass

# /opt/dockethead/include/ar.h: 2251
try:
    AR_DPROP_TABLE_COL_WRAP_TEXT = 5058
except:
    pass

# /opt/dockethead/include/ar.h: 2252
try:
    AR_DVAL_TABLE_COL_WRAP_TEXT_DISABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2253
try:
    AR_DVAL_TABLE_COL_WRAP_TEXT_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2255
try:
    AR_DPROP_TABLE_PREFERENCES = 5060
except:
    pass

# /opt/dockethead/include/ar.h: 2257
try:
    AR_DPROP_FIELD_CUSTOMSTYLE = 5061
except:
    pass

# /opt/dockethead/include/ar.h: 2259
try:
    AR_DPROP_TABLE_TREE_CUSTOM_NULL_VALUE = 5062
except:
    pass

# /opt/dockethead/include/ar.h: 2261
try:
    AR_DPROP_NAVBAR_INITIAL_SELECTED_ITEM = 5063
except:
    pass

# /opt/dockethead/include/ar.h: 2264
try:
    AR_DPROP_NAVBAR_WORKFLOW_ON_SELECTED_ITEM = 5064
except:
    pass

# /opt/dockethead/include/ar.h: 2266
try:
    AR_DVAL_NAVBAR_SELITEM_NOFIRE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2267
try:
    AR_DVAL_NAVBAR_SELITEM_FIRE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2269
try:
    AR_DPROP_NAVBAR_SELECT_ITEM_ON_CLICK = 5065
except:
    pass

# /opt/dockethead/include/ar.h: 2271
try:
    AR_DPROP_BUTTON_ALT_TEXT = 5066
except:
    pass

# /opt/dockethead/include/ar.h: 2274
try:
    AR_DPROP_TABLE_USE_LOCALE = 5067
except:
    pass

# /opt/dockethead/include/ar.h: 2277
try:
    AR_DPROP_QUERY_LIST_BKG_COLOR = 5068
except:
    pass

# /opt/dockethead/include/ar.h: 2281
try:
    AR_DPROP_AUTO_MAXIMIZE_WINDOW = 5069
except:
    pass

# /opt/dockethead/include/ar.h: 2283
try:
    AR_DVAL_AUTO_MAXIMIZE_WINDOW_DISABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2284
try:
    AR_DVAL_AUTO_MAXIMIZE_WINDOW_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2286
try:
    AR_DPROP_VIEW_RTL = 5070
except:
    pass

# /opt/dockethead/include/ar.h: 2287
try:
    AR_DVAL_VIEW_RTL_DISABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2288
try:
    AR_DVAL_VIEW_RTL_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2292
try:
    AR_DPROP_TABLE_PAGE_ARRAY_LEFT_MARGIN = 5100
except:
    pass

# /opt/dockethead/include/ar.h: 2293
try:
    AR_DPROP_TABLE_PAGE_ARRAY_RIGHT_MARGIN = 5101
except:
    pass

# /opt/dockethead/include/ar.h: 2294
try:
    AR_DPROP_TABLE_PAGE_ARRAY_TOP_MARGIN = 5102
except:
    pass

# /opt/dockethead/include/ar.h: 2295
try:
    AR_DPROP_TABLE_PAGE_ARRAY_BOTTOM_MARGIN = 5103
except:
    pass

# /opt/dockethead/include/ar.h: 2297
try:
    AR_DPROP_TABLE_PAGE_VISIBLE_COLUMNS = 5104
except:
    pass

# /opt/dockethead/include/ar.h: 2302
try:
    AR_DPROP_TABLE_PAGE_ARRAY_HOR_SPACE = 5109
except:
    pass

# /opt/dockethead/include/ar.h: 2303
try:
    AR_DPROP_TABLE_PAGE_ARRAY_VER_SPACE = 5110
except:
    pass

# /opt/dockethead/include/ar.h: 2308
try:
    AR_DPROP_FORM_LOCK_ALLVUI = 5111
except:
    pass

# /opt/dockethead/include/ar.h: 2309
try:
    AR_DPROP_VUI_LOCK_VUI = 5112
except:
    pass

# /opt/dockethead/include/ar.h: 2333
try:
    AR_DPROP_TABLE_ROOT_NODE_IMAGE = 5113
except:
    pass

# /opt/dockethead/include/ar.h: 2334
try:
    AR_DPROP_TABLE_ROOT_NODE_ALT_TEXT = 5114
except:
    pass

# /opt/dockethead/include/ar.h: 2335
try:
    AR_DPROP_TABLE_COL_IMAGE_LIST = 5115
except:
    pass

# /opt/dockethead/include/ar.h: 2337
try:
    AR_DPROP_SHOWURL = 5116
except:
    pass

# /opt/dockethead/include/ar.h: 2338
try:
    AR_DPROP_NAVIGATION_MODE = 5117
except:
    pass

# /opt/dockethead/include/ar.h: 2340
try:
    AR_DVAL_NAV_EXPANDABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2341
try:
    AR_DVAL_NAV_FLYOUT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2343
try:
    AR_DPROP_TABLE_CELL_BKG_COLOR = 5118
except:
    pass

# /opt/dockethead/include/ar.h: 2344
try:
    AR_DPROP_TABLE_COL_ENABLE_SORT = 5119
except:
    pass

# /opt/dockethead/include/ar.h: 2345
try:
    AR_DVAL_TABLE_COL_SORT_DISABLED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2346
try:
    AR_DVAL_TABLE_COL_SORT_ENABLED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2348
try:
    AR_DPROP_APPLIST_MODE = 5120
except:
    pass

# /opt/dockethead/include/ar.h: 2349
try:
    AR_DVAL_APP_TRADITIONAL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2350
try:
    AR_DVAL_APP_FLYOUT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2352
try:
    AR_DPROP_TABLE_COLUMN_CHECKBOX = 5121
except:
    pass

# /opt/dockethead/include/ar.h: 2353
try:
    AR_DVAL_TABLE_COLUMN_CHECKBOX_DISABLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2354
try:
    AR_DVAL_TABLE_COLUMN_CHECKBOX_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2359
try:
    AR_DPROP_SKIN_STYLE = 5200
except:
    pass

# /opt/dockethead/include/ar.h: 2360
try:
    AR_DPROP_ATTACH_FIELD_IMAGE_CACHE = 5201
except:
    pass

# /opt/dockethead/include/ar.h: 2364
try:
    AR_DPROP_LOCALIZE_FIELD_DATA = 5202
except:
    pass

# /opt/dockethead/include/ar.h: 2366
try:
    AR_DPROP_FIELD_PROCESS_ENTRY_MODE = 5203
except:
    pass

# /opt/dockethead/include/ar.h: 2367
try:
    AR_DVAL_FIELD_PROCESS_NOT_REQUIRED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2368
try:
    AR_DVAL_FIELD_PROCESS_REQUIRED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2371
try:
    AR_DPROP_SORT_GROUP = 5204
except:
    pass

# /opt/dockethead/include/ar.h: 2377
try:
    AR_DPROP_SORT_AGGREGATION_TYPE = 5205
except:
    pass

# /opt/dockethead/include/ar.h: 2378
try:
    AR_DVAL_SORT_AGGREGATION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2379
try:
    AR_DVAL_SORT_AGGREGATION_COUNT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2382
try:
    AR_DPROP_TABLE_HDRFTR_GRADTYPE = 5206
except:
    pass

# /opt/dockethead/include/ar.h: 2385
try:
    AR_DPROP_TABLE_COLUMN_HEADER_TEXT_COLOR = 5207
except:
    pass

# /opt/dockethead/include/ar.h: 2388
try:
    AR_DPROP_TABLE_HDRFTR_GRADCOLOR = 5208
except:
    pass

# /opt/dockethead/include/ar.h: 2391
try:
    AR_DPROP_TABLE_HDRFTR_GRADBKGCOLOR = 5209
except:
    pass

# /opt/dockethead/include/ar.h: 2394
try:
    AR_DPROP_VIEW_BORDER_COLOR = 5210
except:
    pass

# /opt/dockethead/include/ar.h: 2397
try:
    AR_DPROP_VERTNAV_SUBLEVELTWO_COLOR = 5211
except:
    pass

# /opt/dockethead/include/ar.h: 2399
try:
    AR_DPROP_TABLE_CONTENT_CLIPPED = 5212
except:
    pass

# /opt/dockethead/include/ar.h: 2400
try:
    AR_DVAL_TABLE_CONTENT_NOT_CLIPPED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2401
try:
    AR_DVAL_TABLE_CONTENT_CLIPPED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2404
try:
    AR_DPROP_COL_HEADBKG_GRADTYPE = 5213
except:
    pass

# /opt/dockethead/include/ar.h: 2407
try:
    AR_DPROP_COL_HEADBKG_GRADCOLOR = 5214
except:
    pass

# /opt/dockethead/include/ar.h: 2410
try:
    AR_DPROP_COL_HEADBKG_GRADBKGCOLOR = 5215
except:
    pass

# /opt/dockethead/include/ar.h: 2413
try:
    AR_DPROP_DROP_SHADOW = 5216
except:
    pass

# /opt/dockethead/include/ar.h: 2414
try:
    AR_DVAL_DROP_SHADOW_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2415
try:
    AR_DVAL_DROP_SHADOW_NORTH_WEST = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2418
try:
    AR_DPROP_ATTACH_FTRGRAD_COLOR = 5217
except:
    pass

# /opt/dockethead/include/ar.h: 2421
try:
    AR_DPROP_ATTACH_FTRGRADBKG_COLOR = 5218
except:
    pass

# /opt/dockethead/include/ar.h: 2424
try:
    AR_DPROP_ATTACH_FTRGRAD_TYPE = 5219
except:
    pass

# /opt/dockethead/include/ar.h: 2427
try:
    AR_DPROP_ATTACH_COLGRAD_COLOR = 5220
except:
    pass

# /opt/dockethead/include/ar.h: 2430
try:
    AR_DPROP_ATTACH_COLGRADBKG_COLOR = 5221
except:
    pass

# /opt/dockethead/include/ar.h: 2433
try:
    AR_DPROP_ATTACH_COLGRAD_TYPE = 5222
except:
    pass

# /opt/dockethead/include/ar.h: 2436
try:
    AR_DPROP_ATTACH_COLHDRTXT_COLOR = 5223
except:
    pass

# /opt/dockethead/include/ar.h: 2439
try:
    AR_DPROP_MENU_BOX = 5224
except:
    pass

# /opt/dockethead/include/ar.h: 2442
try:
    AR_DPROP_CHARFIELD_BORDER = 5225
except:
    pass

# /opt/dockethead/include/ar.h: 2445
try:
    AR_DPROP_DISABLED_IMAGE = 5226
except:
    pass

# /opt/dockethead/include/ar.h: 2448
try:
    AR_DPROP_APPLIST_TOP_BKG_COLOR = 5227
except:
    pass

# /opt/dockethead/include/ar.h: 2451
try:
    AR_DPROP_APPLIST_SUB_EVEN_LVL_BKG_COLOR = 5228
except:
    pass

# /opt/dockethead/include/ar.h: 2454
try:
    AR_DPROP_APPLIST_SUB_ODD_LVL_BKG_COLOR = 5229
except:
    pass

# /opt/dockethead/include/ar.h: 2457
try:
    AR_DPROP_COLUMN_INITIAL_STATE = 5230
except:
    pass

# /opt/dockethead/include/ar.h: 2458
try:
    AR_DVAL_COLUMN_INITIAL_STATE_REMOVED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2459
try:
    AR_DVAL_COLUMN_INITIAL_STATE_SHOWN = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2472
try:
    AR_OPROP_RESERVED = 60000
except:
    pass

# /opt/dockethead/include/ar.h: 2474
try:
    AR_OPROP_VENDOR_NAME = 60001
except:
    pass

# /opt/dockethead/include/ar.h: 2476
try:
    AR_OPROP_VENDOR_PRODUCT = 60002
except:
    pass

# /opt/dockethead/include/ar.h: 2477
try:
    AR_OPROP_VENDOR_VERSION = 60003
except:
    pass

# /opt/dockethead/include/ar.h: 2478
try:
    AR_OPROP_GUID = 60004
except:
    pass

# /opt/dockethead/include/ar.h: 2480
try:
    AR_OPROP_COPYRIGHT = 60005
except:
    pass

# /opt/dockethead/include/ar.h: 2481
try:
    AR_OPROP_SCC_LOCKED_BY = 60006
except:
    pass

# /opt/dockethead/include/ar.h: 2485
try:
    AR_OPROP_SCC_VERSION = 60007
except:
    pass

# /opt/dockethead/include/ar.h: 2486
try:
    AR_OPROP_SCC_TIMESTAMP = 60008
except:
    pass

# /opt/dockethead/include/ar.h: 2487
try:
    AR_OPROP_SCC_USER = 60009
except:
    pass

# /opt/dockethead/include/ar.h: 2488
try:
    AR_OPROP_SCC_LOCATION = 60010
except:
    pass

# /opt/dockethead/include/ar.h: 2489
try:
    AR_OPROP_SCC_DATA_LOCKED_BY = 60011
except:
    pass

# /opt/dockethead/include/ar.h: 2493
try:
    AR_OPROP_SCC_DATA_VERSION = 60012
except:
    pass

# /opt/dockethead/include/ar.h: 2494
try:
    AR_OPROP_SCC_DATA_TIMESTAMP = 60013
except:
    pass

# /opt/dockethead/include/ar.h: 2495
try:
    AR_OPROP_SCC_DATA_USER = 60014
except:
    pass

# /opt/dockethead/include/ar.h: 2496
try:
    AR_OPROP_SCC_DATA_LOCATION = 60015
except:
    pass

# /opt/dockethead/include/ar.h: 2497
try:
    AR_OPROP_WINDOW_OPEN_IF_SAMPLE_SERVER_SCHEMA = 60016
except:
    pass

# /opt/dockethead/include/ar.h: 2501
try:
    AR_OPROP_WINDOW_OPEN_ELSE_SAMPLE_SERVER_SCHEMA = 60017
except:
    pass

# /opt/dockethead/include/ar.h: 2505
try:
    AR_OPROP_FORM_NAME_WEB_ALIAS = 60018
except:
    pass

# /opt/dockethead/include/ar.h: 2510
try:
    AR_OPROP_VIEW_LABEL_WEB_ALIAS = 60019
except:
    pass

# /opt/dockethead/include/ar.h: 2515
try:
    AR_OPROP_APP_WEB_ALIAS = 60020
except:
    pass

# /opt/dockethead/include/ar.h: 2519
try:
    AR_OPROP_INTERVAL_VALUE = 60021
except:
    pass

# /opt/dockethead/include/ar.h: 2524
try:
    AR_OPROP_INTEGRITY_KEY = 60022
except:
    pass

# /opt/dockethead/include/ar.h: 2527
try:
    AR_OPROP_NEXT_ID_BLOCK_SIZE = 60023
except:
    pass

# /opt/dockethead/include/ar.h: 2531
try:
    AR_OPROP_POOL_NUMBER = 60024
except:
    pass

# /opt/dockethead/include/ar.h: 2534
try:
    AR_OPROP_CORE_FIELDS_OPTION_MASK = 60025
except:
    pass

# /opt/dockethead/include/ar.h: 2538
try:
    AR_CORE_FIELDS_OPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2539
try:
    AR_CORE_FIELDS_OPTION_DISABLE_STATUS_HISTORY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2541
try:
    AR_OPROP_FT_SCAN_TIME_MONTH_MASK = 60030
except:
    pass

# /opt/dockethead/include/ar.h: 2542
try:
    AR_OPROP_FT_SCAN_TIME_WEEKDAY_MASK = 60031
except:
    pass

# /opt/dockethead/include/ar.h: 2543
try:
    AR_OPROP_FT_SCAN_TIME_HOUR_MASK = 60032
except:
    pass

# /opt/dockethead/include/ar.h: 2544
try:
    AR_OPROP_FT_SCAN_TIME_MINUTE = 60033
except:
    pass

# /opt/dockethead/include/ar.h: 2545
try:
    AR_OPROP_FT_SCAN_TIME_INTERVAL = 60034
except:
    pass

# /opt/dockethead/include/ar.h: 2547
try:
    AR_OPROP_GUIDE_PARAMETERS = 60035
except:
    pass

# /opt/dockethead/include/ar.h: 2551
try:
    AR_OPROP_CACHE_DISP_PROP = 60036
except:
    pass

# /opt/dockethead/include/ar.h: 2554
try:
    AR_OPROP_TRANSACTION_HANDLE_ID = 60037
except:
    pass

# /opt/dockethead/include/ar.h: 2558
try:
    AR_OPROP_MAX_VENDOR_TEMP_TABLES = 60038
except:
    pass

# /opt/dockethead/include/ar.h: 2560
try:
    AR_OPROP_STATIC_PERMISSION_INHERITED = 60039
except:
    pass

# /opt/dockethead/include/ar.h: 2564
try:
    AR_OPROP_DYNAMIC_PERMISSION_INHERITED = 60040
except:
    pass

# /opt/dockethead/include/ar.h: 2569
try:
    AR_OPROP_MFS_OPTION_MASK = 60045
except:
    pass

# /opt/dockethead/include/ar.h: 2573
try:
    AR_MULTI_FORM_SEARCH_OPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2574
try:
    AR_MULTI_FORM_SEARCH_OPTION_EXCLUDE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2576
try:
    AR_OPROP_FORM_ALLOW_DELETE = 60046
except:
    pass

# /opt/dockethead/include/ar.h: 2577
try:
    AR_OPROP_TABLE_PERSIST_DIRTY_ROWS = 60047
except:
    pass

# /opt/dockethead/include/ar.h: 2579
try:
    AR_OPROP_MFS_WEIGHTED_RELEVANCY_FIELDS = 60048
except:
    pass

# /opt/dockethead/include/ar.h: 2585
try:
    AR_MFS_WEIGHTED_RELEVANCY_TITLE_FIELD_TAG = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2586
try:
    AR_MFS_WEIGHTED_RELEVANCY_ENVIRONMENT_FIELD_TAG = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2587
try:
    AR_MFS_WEIGHTED_RELEVANCY_KEYWORDS_FIELD_TAG = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2589
try:
    AR_OPROP_APP_INTEGRATION_WORKFLOW = 60049
except:
    pass

# /opt/dockethead/include/ar.h: 2591
try:
    AR_OPROP_LOCALIZE_FORM_VIEWS = 60050
except:
    pass

# /opt/dockethead/include/ar.h: 2592
try:
    AR_LOCALIZE_FORM_VIEWS_SKIP = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2593
try:
    AR_LOCALIZE_FORM_VIEWS_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2594
try:
    AR_LOCALIZE_FORM_VIEWS_ALIASES = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2595
try:
    AR_OPROP_LOCALIZE_FORM_DATA = 60051
except:
    pass

# /opt/dockethead/include/ar.h: 2596
try:
    AR_LOCALIZE_FORM_DATA_SKIP = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2597
try:
    AR_LOCALIZE_FORM_DATA_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2598
try:
    AR_OPROP_LOCALIZE_FIELD_DATA = 60052
except:
    pass

# /opt/dockethead/include/ar.h: 2599
try:
    AR_LOCALIZE_FIELD_DATA_SKIP = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2600
try:
    AR_LOCALIZE_FIELD_DATA_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2602
try:
    AR_OPROP_FT_MFS_CATEGORY_NAME = 60055
except:
    pass

# /opt/dockethead/include/ar.h: 2605
try:
    AR_OPROP_FT_MFS_INDEX_TABLE_FIELD = 60056
except:
    pass

# /opt/dockethead/include/ar.h: 2606
try:
    AR_FT_MFS_INDEX_TABLE_FIELD_OPTION_NO = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2607
try:
    AR_FT_MFS_INDEX_TABLE_FIELD_OPTION_YES = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2609
try:
    AR_OPROP_OBJECT_MODE = 60057
except:
    pass

# /opt/dockethead/include/ar.h: 2613
try:
    AR_CUSTOMIZE_MODE_OBJECT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2614
try:
    AR_FULL_MODE_OBJECT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2616
try:
    AR_OPROP_OVERLAY_GROUP = 60058
except:
    pass

# /opt/dockethead/include/ar.h: 2617
try:
    AR_OPROP_OVERLAY_DESIGN_GROUP = 60059
except:
    pass

# /opt/dockethead/include/ar.h: 2618
try:
    AR_OPROP_OVERLAY_PROP = 60060
except:
    pass

# /opt/dockethead/include/ar.h: 2622
try:
    AR_OVERLAY_CLIENT_MODE_BASE = '-1'
except:
    pass

# /opt/dockethead/include/ar.h: 2623
try:
    AR_OVERLAY_CLIENT_MODE_FULL = '-2'
except:
    pass

# /opt/dockethead/include/ar.h: 2625
try:
    AR_OPROP_DRILL_DOWN_IN_WEB_REPORTS = 60062
except:
    pass

# /opt/dockethead/include/ar.h: 2626
try:
    AR_PROHIBIT_DRILL_DOWN_IN_WEB_REPORTS = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2627
try:
    AR_ALLOW_DRILL_DOWN_IN_WEB_REPORTS = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2629
try:
    AR_OPROP_FT_STRIP_TAGS = 60063
except:
    pass

# /opt/dockethead/include/ar.h: 2631
try:
    AR_FT_STRIP_TAGS_OPTION_NO = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2632
try:
    AR_FT_STRIP_TAGS_OPTION_YES = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2638
try:
    AR_OPROP_DISPLAY_FORM_SINGLETON = 60064
except:
    pass

# /opt/dockethead/include/ar.h: 2639
try:
    AR_OPEN_FORM_MULTIPLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2640
try:
    AR_OPEN_FORM_SINGLETON = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2642
try:
    AR_OPROP_FT_FILTER_SEARCH = 60065
except:
    pass

# /opt/dockethead/include/ar.h: 2644
try:
    AR_FT_FILTER_SEARCH_OPTION_NO = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2645
try:
    AR_FT_FILTER_SEARCH_OPTION_YES = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2650
try:
    AR_OPROP_FORM_TAG_NAME = 60066
except:
    pass

# /opt/dockethead/include/ar.h: 2654
try:
    AR_OPROP_VUI_OVERLAY_CHANGED_FIELD_LIST = 60067
except:
    pass

# /opt/dockethead/include/ar.h: 2656
try:
    AR_OPROP_GRANULAR_OVERLAY_MODE = 60068
except:
    pass

# /opt/dockethead/include/ar.h: 2664
try:
    AR_GRANULAR_OVERLAY_FULL_MODE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2667
try:
    AR_GRANULAR_OVERLAY_ONLY_MODE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2671
try:
    AR_OPROP_OVERLAY_EXTEND_MASK = 60069
except:
    pass

# /opt/dockethead/include/ar.h: 2673
try:
    AR_OPROP_OVERLAY_INHERIT_MASK = 60070
except:
    pass

# /opt/dockethead/include/ar.h: 2676
try:
    AR_GRANULAR_UNSET = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2677
try:
    AR_GRANULAR_PERMISSIONS = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2678
try:
    AR_GRANULAR_FORM_LIST = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2679
try:
    AR_GRANULAR_INDEX = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2680
try:
    AR_GRANULAR_OTHER = 8
except:
    pass

# /opt/dockethead/include/ar.h: 2682
try:
    AR_GRANULAR_ACTLINK_SHELL = ((AR_GRANULAR_PERMISSIONS | AR_GRANULAR_FORM_LIST) | AR_GRANULAR_OTHER)
except:
    pass

# /opt/dockethead/include/ar.h: 2683
try:
    AR_GRANULAR_FIELD_SHELL = (AR_GRANULAR_PERMISSIONS | AR_GRANULAR_OTHER)
except:
    pass

# /opt/dockethead/include/ar.h: 2684
try:
    AR_GRANULAR_FILTER_SHELL = (AR_GRANULAR_FORM_LIST | AR_GRANULAR_OTHER)
except:
    pass

# /opt/dockethead/include/ar.h: 2685
try:
    AR_GRANULAR_ESCALATION_SHELL = (AR_GRANULAR_FORM_LIST | AR_GRANULAR_OTHER)
except:
    pass

# /opt/dockethead/include/ar.h: 2686
try:
    AR_GRANULAR_SCHEMA_SHELL = ((AR_GRANULAR_PERMISSIONS | AR_GRANULAR_INDEX) | AR_GRANULAR_OTHER)
except:
    pass

# /opt/dockethead/include/ar.h: 2688
try:
    AR_GRANULAR_RESERVE1 = (1 << 31)
except:
    pass

# /opt/dockethead/include/ar.h: 2689
try:
    AR_GRANULAR_RESERVE2 = (1 << 30)
except:
    pass

# /opt/dockethead/include/ar.h: 2698
try:
    AR_SMOPROP_MIN = 90000
except:
    pass

# /opt/dockethead/include/ar.h: 2699
try:
    AR_SMOPROP_MAX = 119999
except:
    pass

# /opt/dockethead/include/ar.h: 2701
try:
    AR_SMOPROP_NONE = 90000
except:
    pass

# /opt/dockethead/include/ar.h: 2702
try:
    AR_SMOPROP_OBJECT_VERSION = 90001
except:
    pass

# /opt/dockethead/include/ar.h: 2703
try:
    AR_SMOPROP_APP_OWNER = 90002
except:
    pass

# /opt/dockethead/include/ar.h: 2704
try:
    AR_SMOPROP_OBJECT_LOCK_TYPE = 90003
except:
    pass

# /opt/dockethead/include/ar.h: 2706
try:
    AR_SMOPROP_OBJECT_LOCK_KEY = 90004
except:
    pass

# /opt/dockethead/include/ar.h: 2707
try:
    AR_SMOPROP_ENTRYPOINT_DEFAULT_NEW_ORDER = 90005
except:
    pass

# /opt/dockethead/include/ar.h: 2709
try:
    AR_SMOPROP_ENTRYPOINT_DEFAULT_SEARCH_ORDER = 90006
except:
    pass

# /opt/dockethead/include/ar.h: 2711
try:
    AR_SMOPROP_NO_APP_STATS_LOGGING = 90007
except:
    pass

# /opt/dockethead/include/ar.h: 2714
try:
    AR_SMOPROP_APP_LIC_VERSION = 90008
except:
    pass

# /opt/dockethead/include/ar.h: 2715
try:
    AR_SMOPROP_APP_LIC_DESCRIPTOR = 90009
except:
    pass

# /opt/dockethead/include/ar.h: 2716
try:
    AR_SMOPROP_APP_LIC_USER_LICENSABLE = 90010
except:
    pass

# /opt/dockethead/include/ar.h: 2717
try:
    AR_SMOPROP_APP_ACCESS_POINT = 90011
except:
    pass

# /opt/dockethead/include/ar.h: 2721
try:
    AR_SMOPROP_APP_BSM_TAG = 90012
except:
    pass

# /opt/dockethead/include/ar.h: 2726
try:
    AR_SMOPROP_PRIMARY_FIELDSET = 90013
except:
    pass

# /opt/dockethead/include/ar.h: 2729
try:
    AR_SMOPROP_FILTER_GET_DATA_AS_USER = 90014
except:
    pass

# /opt/dockethead/include/ar.h: 2730
try:
    AR_FILTER_GET_DATA_AS_ADMIN = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2731
try:
    AR_FILTER_GET_DATA_AS_USER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2734
try:
    AR_SMOPROP_OVERLAY_PROPERTY = 90015
except:
    pass

# /opt/dockethead/include/ar.h: 2736
try:
    AR_SMOPROP_OVERLAY_GROUP = 90016
except:
    pass

# /opt/dockethead/include/ar.h: 2743
try:
    AR_CURRENT_SERVER_TAG = '@'
except:
    pass

# /opt/dockethead/include/ar.h: 2745
try:
    AR_CURRENT_SCHEMA_TAG = '@'
except:
    pass

# /opt/dockethead/include/ar.h: 2747
try:
    AR_CURRENT_SCREEN_TAG = '*'
except:
    pass

# /opt/dockethead/include/ar.h: 2748
try:
    AR_CURRENT_TRAN_TAG = '*'
except:
    pass

# /opt/dockethead/include/ar.h: 2750
try:
    AR_REP_SCHEMA_TAG = '&'
except:
    pass

# /opt/dockethead/include/ar.h: 2754
try:
    AR_NO_MATCH_ERROR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2755
try:
    AR_NO_MATCH_SET_NULL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2757
try:
    AR_NO_MATCH_NO_ACTION = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2759
try:
    AR_NO_MATCH_SUBMIT = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2762
try:
    AR_MULTI_MATCH_ERROR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2763
try:
    AR_MULTI_MATCH_SET_NULL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2765
try:
    AR_MULTI_MATCH_USE_FIRST = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2766
try:
    AR_MULTI_MATCH_PICKLIST = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2768
try:
    AR_MULTI_MATCH_MODIFY_ALL = 5
except:
    pass

# /opt/dockethead/include/ar.h: 2770
try:
    AR_MULTI_MATCH_NO_ACTION = 6
except:
    pass

# /opt/dockethead/include/ar.h: 2772
try:
    AR_MULTI_MATCH_USE_LOCALE = 7
except:
    pass

# /opt/dockethead/include/ar.h: 2797
try:
    AR_DDE_EXECUTE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2798
try:
    AR_DDE_POKE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2799
try:
    AR_DDE_REQUEST = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2823
try:
    AR_COM_PARM_NULL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2824
try:
    AR_COM_PARM_FIELDID = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2825
try:
    AR_COM_PARM_VALUE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2831
try:
    AR_COM_METHOD_NULL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2832
try:
    AR_COM_METHOD_FIELDID = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2897
try:
    AR_ASSIGN_SQL_SCHEMA_NAME = '_SQL_'
except:
    pass

# /opt/dockethead/include/ar.h: 2899
try:
    AR_ASSIGN_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 2900
try:
    AR_ASSIGN_TYPE_VALUE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2901
try:
    AR_ASSIGN_TYPE_FIELD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2902
try:
    AR_ASSIGN_TYPE_PROCESS = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2903
try:
    AR_ASSIGN_TYPE_ARITH = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2904
try:
    AR_ASSIGN_TYPE_FUNCTION = 5
except:
    pass

# /opt/dockethead/include/ar.h: 2905
try:
    AR_ASSIGN_TYPE_DDE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 2906
try:
    AR_ASSIGN_TYPE_SQL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 2907
try:
    AR_ASSIGN_TYPE_FILTER_API = 8
except:
    pass

# /opt/dockethead/include/ar.h: 2964
try:
    AR_FUNCTION_DATE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 2965
try:
    AR_FUNCTION_TIME = 2
except:
    pass

# /opt/dockethead/include/ar.h: 2966
try:
    AR_FUNCTION_MONTH = 3
except:
    pass

# /opt/dockethead/include/ar.h: 2967
try:
    AR_FUNCTION_DAY = 4
except:
    pass

# /opt/dockethead/include/ar.h: 2968
try:
    AR_FUNCTION_YEAR = 5
except:
    pass

# /opt/dockethead/include/ar.h: 2969
try:
    AR_FUNCTION_WEEKDAY = 6
except:
    pass

# /opt/dockethead/include/ar.h: 2970
try:
    AR_FUNCTION_HOUR = 7
except:
    pass

# /opt/dockethead/include/ar.h: 2971
try:
    AR_FUNCTION_MINUTE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 2972
try:
    AR_FUNCTION_SECOND = 9
except:
    pass

# /opt/dockethead/include/ar.h: 2973
try:
    AR_FUNCTION_TRUNC = 10
except:
    pass

# /opt/dockethead/include/ar.h: 2974
try:
    AR_FUNCTION_ROUND = 11
except:
    pass

# /opt/dockethead/include/ar.h: 2975
try:
    AR_FUNCTION_CONVERT = 12
except:
    pass

# /opt/dockethead/include/ar.h: 2978
try:
    AR_FUNCTION_LENGTH = 13
except:
    pass

# /opt/dockethead/include/ar.h: 2979
try:
    AR_FUNCTION_UPPER = 14
except:
    pass

# /opt/dockethead/include/ar.h: 2980
try:
    AR_FUNCTION_LOWER = 15
except:
    pass

# /opt/dockethead/include/ar.h: 2981
try:
    AR_FUNCTION_SUBSTR = 16
except:
    pass

# /opt/dockethead/include/ar.h: 2984
try:
    AR_FUNCTION_LEFT = 17
except:
    pass

# /opt/dockethead/include/ar.h: 2985
try:
    AR_FUNCTION_RIGHT = 18
except:
    pass

# /opt/dockethead/include/ar.h: 2986
try:
    AR_FUNCTION_LTRIM = 19
except:
    pass

# /opt/dockethead/include/ar.h: 2987
try:
    AR_FUNCTION_RTRIM = 20
except:
    pass

# /opt/dockethead/include/ar.h: 2988
try:
    AR_FUNCTION_LPAD = 21
except:
    pass

# /opt/dockethead/include/ar.h: 2990
try:
    AR_FUNCTION_RPAD = 22
except:
    pass

# /opt/dockethead/include/ar.h: 2992
try:
    AR_FUNCTION_REPLACE = 23
except:
    pass

# /opt/dockethead/include/ar.h: 2994
try:
    AR_FUNCTION_STRSTR = 24
except:
    pass

# /opt/dockethead/include/ar.h: 2996
try:
    AR_FUNCTION_MIN = 25
except:
    pass

# /opt/dockethead/include/ar.h: 2997
try:
    AR_FUNCTION_MAX = 26
except:
    pass

# /opt/dockethead/include/ar.h: 2999
try:
    AR_FUNCTION_COLSUM = 27
except:
    pass

# /opt/dockethead/include/ar.h: 3000
try:
    AR_FUNCTION_COLCOUNT = 28
except:
    pass

# /opt/dockethead/include/ar.h: 3002
try:
    AR_FUNCTION_COLAVG = 29
except:
    pass

# /opt/dockethead/include/ar.h: 3004
try:
    AR_FUNCTION_COLMIN = 30
except:
    pass

# /opt/dockethead/include/ar.h: 3005
try:
    AR_FUNCTION_COLMAX = 31
except:
    pass

# /opt/dockethead/include/ar.h: 3006
try:
    AR_FUNCTION_DATEADD = 32
except:
    pass

# /opt/dockethead/include/ar.h: 3007
try:
    AR_FUNCTION_DATEDIFF = 33
except:
    pass

# /opt/dockethead/include/ar.h: 3008
try:
    AR_FUNCTION_DATENAME = 34
except:
    pass

# /opt/dockethead/include/ar.h: 3009
try:
    AR_FUNCTION_DATENUM = 35
except:
    pass

# /opt/dockethead/include/ar.h: 3010
try:
    AR_FUNCTION_CURRCONVERT = 36
except:
    pass

# /opt/dockethead/include/ar.h: 3011
try:
    AR_FUNCTION_CURRSETDATE = 37
except:
    pass

# /opt/dockethead/include/ar.h: 3012
try:
    AR_FUNCTION_CURRSETTYPE = 38
except:
    pass

# /opt/dockethead/include/ar.h: 3013
try:
    AR_FUNCTION_CURRSETVALUE = 39
except:
    pass

# /opt/dockethead/include/ar.h: 3014
try:
    AR_FUNCTION_LENGTHC = 40
except:
    pass

# /opt/dockethead/include/ar.h: 3015
try:
    AR_FUNCTION_LEFTC = 41
except:
    pass

# /opt/dockethead/include/ar.h: 3016
try:
    AR_FUNCTION_RIGHTC = 42
except:
    pass

# /opt/dockethead/include/ar.h: 3017
try:
    AR_FUNCTION_LPADC = 43
except:
    pass

# /opt/dockethead/include/ar.h: 3019
try:
    AR_FUNCTION_RPADC = 44
except:
    pass

# /opt/dockethead/include/ar.h: 3021
try:
    AR_FUNCTION_STRSTRC = 45
except:
    pass

# /opt/dockethead/include/ar.h: 3023
try:
    AR_FUNCTION_SUBSTRC = 46
except:
    pass

# /opt/dockethead/include/ar.h: 3027
try:
    AR_FUNCTION_ENCRYPT = 47
except:
    pass

# /opt/dockethead/include/ar.h: 3030
try:
    AR_FUNCTION_DECRYPT = 48
except:
    pass

# /opt/dockethead/include/ar.h: 3032
try:
    AR_FUNCTION_HOVER = 49
except:
    pass

# /opt/dockethead/include/ar.h: 3034
try:
    AR_FUNCTION_TEMPLATE = 50
except:
    pass

# /opt/dockethead/include/ar.h: 3038
try:
    AR_FUNCTION_SELECTEDROWCOUNT = 51
except:
    pass

# /opt/dockethead/include/ar.h: 3039
try:
    AR_FUNCTION_DROPPEDROWINDEX = 52
except:
    pass

# /opt/dockethead/include/ar.h: 3040
try:
    AR_FUNCTION_DROPPEDCOLUMNINDEX = 53
except:
    pass

# /opt/dockethead/include/ar.h: 3041
try:
    AR_FUNCTION_MAPGET = 54
except:
    pass

# /opt/dockethead/include/ar.h: 3042
try:
    AR_FUNCTION_LISTGET = 55
except:
    pass

# /opt/dockethead/include/ar.h: 3043
try:
    AR_FUNCTION_LISTSIZE = 56
except:
    pass

# /opt/dockethead/include/ar.h: 3044
try:
    AR_FUNCTION_STRIPHTML = 57
except:
    pass

# /opt/dockethead/include/ar.h: 3045
try:
    AR_FUNCTION_VISIBLEROWS = 58
except:
    pass

# /opt/dockethead/include/ar.h: 3046
try:
    AR_MAX_FUNCTION_USED = 58
except:
    pass

# /opt/dockethead/include/ar.h: 3058
try:
    AR_ORDER_MAX = 1000
except:
    pass

# /opt/dockethead/include/ar.h: 3061
try:
    AR_OPERATION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3062
try:
    AR_OPERATION_GET = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3063
try:
    AR_OPERATION_SET = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3064
try:
    AR_OPERATION_CREATE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3065
try:
    AR_OPERATION_DELETE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 3066
try:
    AR_OPERATION_MERGE = 16
except:
    pass

# /opt/dockethead/include/ar.h: 3067
try:
    AR_OPERATION_GUIDE = 32
except:
    pass

# /opt/dockethead/include/ar.h: 3068
try:
    AR_OPERATION_SERVICE = 64
except:
    pass

# /opt/dockethead/include/ar.h: 3070
try:
    AR_NOTIFY_BEHAVIOR_SEND_MULTIPLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3072
try:
    AR_NOTIFY_PERMISSION_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3091
try:
    AR_NOTIFY_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3092
try:
    AR_NOTIFY_VIA_NOTIFIER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3093
try:
    AR_NOTIFY_VIA_EMAIL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3094
try:
    AR_NOTIFY_VIA_DEFAULT = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3096
try:
    AR_NOTIFY_VIA_XREF = 99
except:
    pass

# /opt/dockethead/include/ar.h: 3099
try:
    AR_NOTIFY_PRIORITY_MAX = 10
except:
    pass

# /opt/dockethead/include/ar.h: 3101
try:
    AR_FILTER_FIELD_IDS_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3102
try:
    AR_FILTER_FIELD_IDS_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3103
try:
    AR_FILTER_FIELD_IDS_LIST = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3104
try:
    AR_FILTER_FIELD_IDS_CHANGED = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3183
try:
    AR_GOTO_FIELD_XREF = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3184
try:
    AR_GOTO_ABSOLUTE_ORDER = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3185
try:
    AR_GOTO_OFFSET_FORWARD = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3186
try:
    AR_GOTO_OFFSET_BACKWARD = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3209
try:
    AR_CALL_GUIDE_FORM_HIDDEN = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3211
try:
    AR_CALL_GUIDE_LOOP_SELECTED_ONLY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3214
try:
    AR_CALL_GUIDE_LOOP_ALL_ROWS_VISIBLE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3217
try:
    AR_CALL_GUIDE_MODE_MAX = 7
except:
    pass

# /opt/dockethead/include/ar.h: 3243
try:
    AR_FILTER_ACTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3244
try:
    AR_FILTER_ACTION_NOTIFY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3245
try:
    AR_FILTER_ACTION_MESSAGE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3246
try:
    AR_FILTER_ACTION_LOG = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3247
try:
    AR_FILTER_ACTION_FIELDS = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3248
try:
    AR_FILTER_ACTION_PROCESS = 5
except:
    pass

# /opt/dockethead/include/ar.h: 3249
try:
    AR_FILTER_ACTION_FIELDP = 6
except:
    pass

# /opt/dockethead/include/ar.h: 3250
try:
    AR_FILTER_ACTION_SQL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 3251
try:
    AR_FILTER_ACTION_GOTOACTION = 8
except:
    pass

# /opt/dockethead/include/ar.h: 3252
try:
    AR_FILTER_ACTION_CALLGUIDE = 9
except:
    pass

# /opt/dockethead/include/ar.h: 3253
try:
    AR_FILTER_ACTION_EXITGUIDE = 10
except:
    pass

# /opt/dockethead/include/ar.h: 3254
try:
    AR_FILTER_ACTION_GOTOGUIDELABEL = 11
except:
    pass

# /opt/dockethead/include/ar.h: 3255
try:
    AR_FILTER_ACTION_SERVICE = 12
except:
    pass

# /opt/dockethead/include/ar.h: 3256
try:
    AR_FILTER_LAST_ACTION = AR_FILTER_ACTION_SERVICE
except:
    pass

# /opt/dockethead/include/ar.h: 3258
try:
    AR_ERRHANDLER_ENABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3298
try:
    AR_EXECUTE_ON_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3299
try:
    AR_EXECUTE_ON_BUTTON = (1 << 0)
except:
    pass

# /opt/dockethead/include/ar.h: 3300
try:
    AR_EXECUTE_ON_RETURN = (1 << 1)
except:
    pass

# /opt/dockethead/include/ar.h: 3301
try:
    AR_EXECUTE_ON_SUBMIT = (1 << 2)
except:
    pass

# /opt/dockethead/include/ar.h: 3302
try:
    AR_EXECUTE_ON_MODIFY = (1 << 3)
except:
    pass

# /opt/dockethead/include/ar.h: 3303
try:
    AR_EXECUTE_ON_DISPLAY = (1 << 4)
except:
    pass

# /opt/dockethead/include/ar.h: 3304
try:
    AR_EXECUTE_ON_MODIFY_ALL = (1 << 5)
except:
    pass

# /opt/dockethead/include/ar.h: 3305
try:
    AR_EXECUTE_ON_MENU_OPEN = (1 << 6)
except:
    pass

# /opt/dockethead/include/ar.h: 3306
try:
    AR_EXECUTE_ON_MENU_CHOICE = (1 << 7)
except:
    pass

# /opt/dockethead/include/ar.h: 3307
try:
    AR_EXECUTE_ON_LOSE_FOCUS = (1 << 8)
except:
    pass

# /opt/dockethead/include/ar.h: 3308
try:
    AR_EXECUTE_ON_SET_DEFAULT = (1 << 9)
except:
    pass

# /opt/dockethead/include/ar.h: 3309
try:
    AR_EXECUTE_ON_QUERY = (1 << 10)
except:
    pass

# /opt/dockethead/include/ar.h: 3310
try:
    AR_EXECUTE_ON_AFTER_MODIFY = (1 << 11)
except:
    pass

# /opt/dockethead/include/ar.h: 3311
try:
    AR_EXECUTE_ON_AFTER_SUBMIT = (1 << 12)
except:
    pass

# /opt/dockethead/include/ar.h: 3312
try:
    AR_EXECUTE_ON_GAIN_FOCUS = (1 << 13)
except:
    pass

# /opt/dockethead/include/ar.h: 3313
try:
    AR_EXECUTE_ON_WINDOW_OPEN = (1 << 14)
except:
    pass

# /opt/dockethead/include/ar.h: 3314
try:
    AR_EXECUTE_ON_WINDOW_CLOSE = (1 << 15)
except:
    pass

# /opt/dockethead/include/ar.h: 3315
try:
    AR_EXECUTE_ON_UNDISPLAY = (1 << 16)
except:
    pass

# /opt/dockethead/include/ar.h: 3316
try:
    AR_EXECUTE_ON_COPY_SUBMIT = (1 << 17)
except:
    pass

# /opt/dockethead/include/ar.h: 3317
try:
    AR_EXECUTE_ON_LOADED = (1 << 18)
except:
    pass

# /opt/dockethead/include/ar.h: 3318
try:
    AR_EXECUTE_ON_INTERVAL = (1 << 19)
except:
    pass

# /opt/dockethead/include/ar.h: 3319
try:
    AR_EXECUTE_ON_EVENT = (1 << 20)
except:
    pass

# /opt/dockethead/include/ar.h: 3320
try:
    AR_EXECUTE_ON_MASK_EXP_V10 = ((AR_EXECUTE_ON_EVENT * 2) - 1)
except:
    pass

# /opt/dockethead/include/ar.h: 3322
try:
    AR_EXECUTE_ON_TABLE_CONTENT_CHANGE = (1 << 21)
except:
    pass

# /opt/dockethead/include/ar.h: 3323
try:
    AR_EXECUTE_ON_HOVER_FIELD_LABEL = (1 << 22)
except:
    pass

# /opt/dockethead/include/ar.h: 3324
try:
    AR_EXECUTE_ON_HOVER_FIELD_DATA = (1 << 23)
except:
    pass

# /opt/dockethead/include/ar.h: 3325
try:
    AR_EXECUTE_ON_HOVER_FIELD = (1 << 24)
except:
    pass

# /opt/dockethead/include/ar.h: 3327
try:
    AR_EXECUTE_ON_PAGE_EXPAND = (1 << 25)
except:
    pass

# /opt/dockethead/include/ar.h: 3328
try:
    AR_EXECUTE_ON_PAGE_COLLAPSE = (1 << 26)
except:
    pass

# /opt/dockethead/include/ar.h: 3329
try:
    AR_EXECUTE_ON_DRAG = (1 << 27)
except:
    pass

# /opt/dockethead/include/ar.h: 3330
try:
    AR_EXECUTE_ON_DROP = (1 << 28)
except:
    pass

# /opt/dockethead/include/ar.h: 3332
try:
    AR_EXECUTE_ON_MASK_MAX = ((AR_EXECUTE_ON_DROP * 2) - 1)
except:
    pass

# /opt/dockethead/include/ar.h: 3335
try:
    AR_EXECUTE_ON_MASK_FOCUS_FIELD = ((((((((((((AR_EXECUTE_ON_RETURN | AR_EXECUTE_ON_MENU_CHOICE) | AR_EXECUTE_ON_MENU_OPEN) | AR_EXECUTE_ON_LOSE_FOCUS) | AR_EXECUTE_ON_GAIN_FOCUS) | AR_EXECUTE_ON_TABLE_CONTENT_CHANGE) | AR_EXECUTE_ON_HOVER_FIELD_LABEL) | AR_EXECUTE_ON_HOVER_FIELD_DATA) | AR_EXECUTE_ON_HOVER_FIELD) | AR_EXECUTE_ON_PAGE_EXPAND) | AR_EXECUTE_ON_PAGE_COLLAPSE) | AR_EXECUTE_ON_DRAG) | AR_EXECUTE_ON_DROP)
except:
    pass

# /opt/dockethead/include/ar.h: 3368
try:
    AR_FIELD_CHAR_OPTION_REFERENCE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3370
try:
    AR_FOCUS_UNCHANGED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3371
try:
    AR_FOCUS_SET_TO_FIELD = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3373
try:
    AR_ACCESS_OPTION_UNCHANGED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3374
try:
    AR_ACCESS_OPTION_READ_ONLY = AR_DVAL_ENABLE_READ_ONLY
except:
    pass

# /opt/dockethead/include/ar.h: 3375
try:
    AR_ACCESS_OPTION_READ_WRITE = AR_DVAL_ENABLE_READ_WRITE
except:
    pass

# /opt/dockethead/include/ar.h: 3376
try:
    AR_ACCESS_OPTION_DISABLE = AR_DVAL_ENABLE_DISABLE
except:
    pass

# /opt/dockethead/include/ar.h: 3427
try:
    AR_ACTIVE_LINK_ACTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3428
try:
    AR_ACTIVE_LINK_ACTION_MACRO = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3429
try:
    AR_ACTIVE_LINK_ACTION_FIELDS = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3430
try:
    AR_ACTIVE_LINK_ACTION_PROCESS = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3431
try:
    AR_ACTIVE_LINK_ACTION_MESSAGE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3432
try:
    AR_ACTIVE_LINK_ACTION_SET_CHAR = 5
except:
    pass

# /opt/dockethead/include/ar.h: 3433
try:
    AR_ACTIVE_LINK_ACTION_DDE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 3434
try:
    AR_ACTIVE_LINK_ACTION_FIELDP = 7
except:
    pass

# /opt/dockethead/include/ar.h: 3435
try:
    AR_ACTIVE_LINK_ACTION_SQL = 8
except:
    pass

# /opt/dockethead/include/ar.h: 3436
try:
    AR_ACTIVE_LINK_ACTION_AUTO = 9
except:
    pass

# /opt/dockethead/include/ar.h: 3437
try:
    AR_ACTIVE_LINK_ACTION_OPENDLG = 10
except:
    pass

# /opt/dockethead/include/ar.h: 3438
try:
    AR_ACTIVE_LINK_ACTION_COMMITC = 11
except:
    pass

# /opt/dockethead/include/ar.h: 3439
try:
    AR_ACTIVE_LINK_ACTION_CLOSEWND = 12
except:
    pass

# /opt/dockethead/include/ar.h: 3440
try:
    AR_ACTIVE_LINK_ACTION_CALLGUIDE = 13
except:
    pass

# /opt/dockethead/include/ar.h: 3441
try:
    AR_ACTIVE_LINK_ACTION_EXITGUIDE = 14
except:
    pass

# /opt/dockethead/include/ar.h: 3442
try:
    AR_ACTIVE_LINK_ACTION_GOTOGUIDELABEL = 15
except:
    pass

# /opt/dockethead/include/ar.h: 3443
try:
    AR_ACTIVE_LINK_ACTION_WAIT = 16
except:
    pass

# /opt/dockethead/include/ar.h: 3444
try:
    AR_ACTIVE_LINK_ACTION_GOTOACTION = 17
except:
    pass

# /opt/dockethead/include/ar.h: 3445
try:
    AR_ACTIVE_LINK_ACTION_SERVICE = 18
except:
    pass

# /opt/dockethead/include/ar.h: 3447
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DLG = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3448
try:
    AR_ACTIVE_LINK_ACTION_OPEN_SEARCH = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3449
try:
    AR_ACTIVE_LINK_ACTION_OPEN_SUBMIT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3450
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY_LST = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3451
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY_DETAIL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3452
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY_SPLIT = 5
except:
    pass

# /opt/dockethead/include/ar.h: 3453
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DSPLY_LST = 6
except:
    pass

# /opt/dockethead/include/ar.h: 3454
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DSPLY_DETAIL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 3455
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DSPLY_SPLIT = 8
except:
    pass

# /opt/dockethead/include/ar.h: 3456
try:
    AR_ACTIVE_LINK_ACTION_OPEN_REPORT = 9
except:
    pass

# /opt/dockethead/include/ar.h: 3457
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY = 10
except:
    pass

# /opt/dockethead/include/ar.h: 3458
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DSPLY = 11
except:
    pass

# /opt/dockethead/include/ar.h: 3459
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY_DIRECT = 12
except:
    pass

# /opt/dockethead/include/ar.h: 3463
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY_DIRECT_LST = 13
except:
    pass

# /opt/dockethead/include/ar.h: 3464
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY_DIRECT_DETAIL = 14
except:
    pass

# /opt/dockethead/include/ar.h: 3465
try:
    AR_ACTIVE_LINK_ACTION_OPEN_MODIFY_DIRECT_SPLIT = 15
except:
    pass

# /opt/dockethead/include/ar.h: 3467
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DISPLAY_DIRECT = 16
except:
    pass

# /opt/dockethead/include/ar.h: 3468
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DISPLAY_DIRECT_LST = 17
except:
    pass

# /opt/dockethead/include/ar.h: 3469
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DISPLAY_DIRECT_DETAIL = 18
except:
    pass

# /opt/dockethead/include/ar.h: 3470
try:
    AR_ACTIVE_LINK_ACTION_OPEN_DISPLAY_DIRECT_SPLIT = 19
except:
    pass

# /opt/dockethead/include/ar.h: 3471
try:
    AR_ACTIVE_LINK_ACTION_OPEN_POPUP = 20
except:
    pass

# /opt/dockethead/include/ar.h: 3476
try:
    AR_REPORT_ATTR_LAYOUT = (ARL (1))
except:
    pass

# /opt/dockethead/include/ar.h: 3477
try:
    AR_REPORT_ATTR_IDLIST = (ARL (2))
except:
    pass

# /opt/dockethead/include/ar.h: 3478
try:
    AR_REPORT_ATTR_NAME = (ARL (3))
except:
    pass

# /opt/dockethead/include/ar.h: 3479
try:
    AR_REPORT_ATTR_TITLE = (ARL (4))
except:
    pass

# /opt/dockethead/include/ar.h: 3480
try:
    AR_REPORT_ATTR_HEADER = (ARL (5))
except:
    pass

# /opt/dockethead/include/ar.h: 3481
try:
    AR_REPORT_ATTR_FOOTER = (ARL (6))
except:
    pass

# /opt/dockethead/include/ar.h: 3482
try:
    AR_REPORT_ATTR_LINES = (ARL (7))
except:
    pass

# /opt/dockethead/include/ar.h: 3483
try:
    AR_REPORT_ATTR_TOP = (ARL (8))
except:
    pass

# /opt/dockethead/include/ar.h: 3484
try:
    AR_REPORT_ATTR_BOTTOM = (ARL (9))
except:
    pass

# /opt/dockethead/include/ar.h: 3485
try:
    AR_REPORT_ATTR_CHARS = (ARL (10))
except:
    pass

# /opt/dockethead/include/ar.h: 3486
try:
    AR_REPORT_ATTR_LEFT = (ARL (11))
except:
    pass

# /opt/dockethead/include/ar.h: 3487
try:
    AR_REPORT_ATTR_RIGHT = (ARL (12))
except:
    pass

# /opt/dockethead/include/ar.h: 3488
try:
    AR_REPORT_ATTR_COL_SEP = (ARL (13))
except:
    pass

# /opt/dockethead/include/ar.h: 3489
try:
    AR_REPORT_ATTR_ONE_REC_PER_PAGE = (ARL (14))
except:
    pass

# /opt/dockethead/include/ar.h: 3490
try:
    AR_REPORT_ATTR_COMPRESSED = (ARL (15))
except:
    pass

# /opt/dockethead/include/ar.h: 3491
try:
    AR_REPORT_ATTR_TITLE_SEP_CHAR = (ARL (16))
except:
    pass

# /opt/dockethead/include/ar.h: 3492
try:
    AR_REPORT_REC_SEP = (ARL (17))
except:
    pass

# /opt/dockethead/include/ar.h: 3493
try:
    AR_REPORT_LONG_FIELD_FORMAT = (ARL (18))
except:
    pass

# /opt/dockethead/include/ar.h: 3494
try:
    AR_REPORT_COL_TITLE_PER = (ARL (19))
except:
    pass

# /opt/dockethead/include/ar.h: 3495
try:
    AR_REPORT_ATTR_PAGE_BREAKS = (ARL (20))
except:
    pass

# /opt/dockethead/include/ar.h: 3496
try:
    AR_REPORT_ATTR_TYPE = (ARL (21))
except:
    pass

# /opt/dockethead/include/ar.h: 3497
try:
    AR_REPORT_ATTR_FILENAME = (ARL (22))
except:
    pass

# /opt/dockethead/include/ar.h: 3498
try:
    AR_REPORT_ATTR_PRINT_ORIENT = (ARL (23))
except:
    pass

# /opt/dockethead/include/ar.h: 3499
try:
    AR_REPORT_ATTR_SCHEMANAME = (ARL (24))
except:
    pass

# /opt/dockethead/include/ar.h: 3500
try:
    AR_REPORT_ATTR_SERVERNAME = (ARL (25))
except:
    pass

# /opt/dockethead/include/ar.h: 3501
try:
    AR_REPORT_ATTR_QUERY = (ARL (26))
except:
    pass

# /opt/dockethead/include/ar.h: 3502
try:
    AR_REPORT_ATTR_ENTRYIDS = (ARL (27))
except:
    pass

# /opt/dockethead/include/ar.h: 3503
try:
    AR_REPORT_ATTR_QUERY_OVERRIDE = (ARL (28))
except:
    pass

# /opt/dockethead/include/ar.h: 3504
try:
    AR_REPORT_ATTR_OPERATION = (ARL (29))
except:
    pass

# /opt/dockethead/include/ar.h: 3505
try:
    AR_REPORT_ATTR_LOCATION = (ARL (30))
except:
    pass

# /opt/dockethead/include/ar.h: 3506
try:
    AR_REPORT_ATTR_CHAR_ENCODING = (ARL (31))
except:
    pass

# /opt/dockethead/include/ar.h: 3507
try:
    AR_REPORT_ATTR_INLINE_FORM = (ARL (32))
except:
    pass

# /opt/dockethead/include/ar.h: 3509
try:
    AR_REPORT_LOCATION_EMBEDDED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3510
try:
    AR_REPORT_LOCATION_LOCAL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3511
try:
    AR_REPORT_LOCATION_REPORTING_FORM = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3512
try:
    AR_REPORT_LOCATION_FIELD = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3556
try:
    AR_PERMISSIONS_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3558
try:
    AR_PERMISSIONS_VISIBLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3559
try:
    AR_PERMISSIONS_HIDDEN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3561
try:
    AR_PERMISSIONS_VIEW = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3562
try:
    AR_PERMISSIONS_CHANGE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3592
try:
    AR_GROUP_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3593
try:
    AR_GROUP_TYPE_VIEW = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3594
try:
    AR_GROUP_TYPE_CHANGE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3596
try:
    AR_GROUP_CATEGORY_REGULAR = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3597
try:
    AR_GROUP_CATEGORY_DYNAMIC = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3598
try:
    AR_GROUP_CATEGORY_COMPUTED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3600
try:
    AR_GROUP_PARENT_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3638
try:
    AR_LICENSE_TAG_WRITE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3639
try:
    AR_LICENSE_TAG_FULL_TEXT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3640
try:
    AR_LICENSE_TAG_RESERVED1 = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3641
try:
    AR_LICENSE_TAG_APP = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3643
try:
    AR_LICENSE_TAG_WRITE_INDEX = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3644
try:
    AR_LICENSE_TAG_RESV_INDEX = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3645
try:
    AR_LICENSE_TAG_NUM_INDEXES = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3739
try:
    AR_USER_LIST_MYSELF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3740
try:
    AR_USER_LIST_REGISTERED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3741
try:
    AR_USER_LIST_CURRENT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3742
try:
    AR_USER_LIST_INVALID = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3743
try:
    AR_USER_LIST_APPLICATION = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3772
try:
    AR_LOCK_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3773
try:
    AR_LOCK_TYPE_READONLY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3775
try:
    AR_LOCK_TYPE_HIDDEN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3777
try:
    AR_LOCK_TYPE_MIN = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3778
try:
    AR_LOCK_TYPE_MAX = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3787
try:
    AR_PRECISION_NONE = (-1)
except:
    pass

# /opt/dockethead/include/ar.h: 3797
try:
    AR_MENU_APPEND = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3798
try:
    AR_MENU_OVERWRITE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3801
try:
    AR_QBE_MATCH_ANYWHERE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3802
try:
    AR_QBE_MATCH_LEADING = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3803
try:
    AR_QBE_MATCH_EQUAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3806
try:
    AR_FULLTEXT_OPTIONS_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3807
try:
    AR_FULLTEXT_OPTIONS_INDEXED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3808
try:
    AR_FULLTEXT_OPTIONS_LITERAL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3809
try:
    AR_FULLTEXT_OPTIONS_EXCLUDE_FIELD_BASED = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3811
try:
    AR_COREFIELD_LENGTH_FACTOR = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3813
try:
    AR_LENGTH_UNIT_BYTE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3814
try:
    AR_LENGTH_UNIT_CHAR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3816
try:
    AR_STORE_OPT_DEF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3817
try:
    AR_STORE_OPT_INROW = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3818
try:
    AR_STORE_OPT_OUTROW = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3845
try:
    AR_ENUM_STYLE_REGULAR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3846
try:
    AR_ENUM_STYLE_CUSTOM = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3847
try:
    AR_ENUM_STYLE_QUERY = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3885
try:
    AR_ATTACH_FIELD_TYPE_EMBED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3886
try:
    AR_ATTACH_FIELD_TYPE_LINK = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3914
try:
    COLUMN_LIMIT_DATASOURCE_DATA_FIELD = 0
except:
    pass

# /opt/dockethead/include/ar.h: 3915
try:
    COLUMN_LIMIT_DATASOURCE_DISPLAY_FIELD = 1
except:
    pass

# /opt/dockethead/include/ar.h: 3916
try:
    COLUMN_LIMIT_DATASOURCE_CONTROL_FIELD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 3917
try:
    COLUMN_LIMIT_DATASOURCE_TRIM_FIELD = 3
except:
    pass

# /opt/dockethead/include/ar.h: 3918
try:
    COLUMN_LIMIT_DATASOURCE_VIEW_FIELD = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3919
try:
    COLUMN_LIMIT_DATASOURCE_MAX = 4
except:
    pass

# /opt/dockethead/include/ar.h: 3960
try:
    AR_MAX_FUNC_CURRENCY_LIMIT_TEXT_SIZE = 20
except:
    pass

# /opt/dockethead/include/ar.h: 3989
try:
    AR_FIELD_LIMIT_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4028
try:
    AR_MENU_REFRESH_CONNECT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4029
try:
    AR_MENU_REFRESH_OPEN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4030
try:
    AR_MENU_REFRESH_INTERVAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 4032
try:
    AR_MENU_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4033
try:
    AR_MENU_TYPE_VALUE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4034
try:
    AR_MENU_TYPE_MENU = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4062
try:
    AR_MENU_FILE_SERVER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4063
try:
    AR_MENU_FILE_CLIENT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4098
try:
    AR_CHAR_MENU_DD_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4099
try:
    AR_CHAR_MENU_DD_FORM = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4100
try:
    AR_CHAR_MENU_DD_FIELD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4117
try:
    AR_CHAR_MENU_DD_DB_NAME = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4118
try:
    AR_CHAR_MENU_DD_LOCAL_NAME = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4119
try:
    AR_CHAR_MENU_DD_ID = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4122
try:
    AR_CHAR_MENU_DD_FORMAT_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4123
try:
    AR_CHAR_MENU_DD_FORMAT_ID = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4124
try:
    AR_CHAR_MENU_DD_FORMAT_NAME = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4125
try:
    AR_CHAR_MENU_DD_FORMAT_QUOTES = 3
except:
    pass

# /opt/dockethead/include/ar.h: 4126
try:
    AR_CHAR_MENU_DD_FORMAT_DOLLARS = 4
except:
    pass

# /opt/dockethead/include/ar.h: 4127
try:
    AR_CHAR_MENU_DD_FORMAT_ID_NAME = 5
except:
    pass

# /opt/dockethead/include/ar.h: 4128
try:
    AR_CHAR_MENU_DD_FORMAT_NAMEL = 6
except:
    pass

# /opt/dockethead/include/ar.h: 4129
try:
    AR_CHAR_MENU_DD_FORMAT_QUOTESL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 4130
try:
    AR_CHAR_MENU_DD_FORMAT_DOLLARSL = 8
except:
    pass

# /opt/dockethead/include/ar.h: 4131
try:
    AR_CHAR_MENU_DD_FORMAT_ID_L = 9
except:
    pass

# /opt/dockethead/include/ar.h: 4132
try:
    AR_CHAR_MENU_DD_FORMAT_NAME_L = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4133
try:
    AR_CHAR_MENU_DD_FORMAT_L_NAME = 11
except:
    pass

# /opt/dockethead/include/ar.h: 4149
try:
    AR_CHAR_MENU_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4150
try:
    AR_CHAR_MENU_LIST = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4151
try:
    AR_CHAR_MENU_QUERY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4152
try:
    AR_CHAR_MENU_FILE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 4153
try:
    AR_CHAR_MENU_SQL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 4154
try:
    AR_CHAR_MENU_SS = 5
except:
    pass

# /opt/dockethead/include/ar.h: 4155
try:
    AR_CHAR_MENU_DATA_DICTIONARY = 6
except:
    pass

# /opt/dockethead/include/ar.h: 4179
try:
    AR_STRUCT_XML_OFFSET = (1 << 30)
except:
    pass

# /opt/dockethead/include/ar.h: 4180
try:
    AR_STRUCT_SUPPRESS_NONSTRUCTURAL_CHANGE_TAG = (1 << 29)
except:
    pass

# /opt/dockethead/include/ar.h: 4184
try:
    AR_EXPORT_FORMAT_AR_DEF = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4185
try:
    AR_EXPORT_FORMAT_XML = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4187
try:
    AR_STRUCT_ITEM_SCHEMA = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4188
try:
    AR_STRUCT_ITEM_SCHEMA_DEFN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4189
try:
    AR_STRUCT_ITEM_SCHEMA_VIEW = 3
except:
    pass

# /opt/dockethead/include/ar.h: 4190
try:
    AR_STRUCT_ITEM_SCHEMA_MAIL = 4
except:
    pass

# /opt/dockethead/include/ar.h: 4191
try:
    AR_STRUCT_ITEM_FILTER = 5
except:
    pass

# /opt/dockethead/include/ar.h: 4192
try:
    AR_STRUCT_ITEM_ACTIVE_LINK = 6
except:
    pass

# /opt/dockethead/include/ar.h: 4193
try:
    AR_STRUCT_ITEM_ADMIN_EXT = 7
except:
    pass

# /opt/dockethead/include/ar.h: 4194
try:
    AR_STRUCT_ITEM_CHAR_MENU = 8
except:
    pass

# /opt/dockethead/include/ar.h: 4195
try:
    AR_STRUCT_ITEM_ESCALATION = 9
except:
    pass

# /opt/dockethead/include/ar.h: 4196
try:
    AR_STRUCT_ITEM_DIST_MAP = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4197
try:
    AR_STRUCT_ITEM_SCHEMA_VIEW_MIN = 11
except:
    pass

# /opt/dockethead/include/ar.h: 4198
try:
    AR_STRUCT_ITEM_CONTAINER = 12
except:
    pass

# /opt/dockethead/include/ar.h: 4199
try:
    AR_STRUCT_ITEM_DIST_POOL = 13
except:
    pass

# /opt/dockethead/include/ar.h: 4200
try:
    AR_STRUCT_ITEM_VUI = 14
except:
    pass

# /opt/dockethead/include/ar.h: 4201
try:
    AR_STRUCT_ITEM_FIELD = 15
except:
    pass

# /opt/dockethead/include/ar.h: 4202
try:
    AR_STRUCT_ITEM_APP = 16
except:
    pass

# /opt/dockethead/include/ar.h: 4203
try:
    AR_STRUCT_ITEM_IMAGE = 17
except:
    pass

# /opt/dockethead/include/ar.h: 4204
try:
    AR_STRUCT_ITEM_LOCALE_VUI = 18
except:
    pass

# /opt/dockethead/include/ar.h: 4205
try:
    AR_STRUCT_ITEM_TASK = 19
except:
    pass

# /opt/dockethead/include/ar.h: 4207
try:
    AR_STRUCT_ITEM_SCHEMA_DATA = 30
except:
    pass

# /opt/dockethead/include/ar.h: 4208
try:
    AR_STRUCT_ITEM_LOCK_BLOCK = 31
except:
    pass

# /opt/dockethead/include/ar.h: 4211
try:
    AR_STRUCT_ITEM_SCHEMA_VIEW_2 = 103
except:
    pass

# /opt/dockethead/include/ar.h: 4213
try:
    AR_STRUCT_ITEM_LOCALE_VUI_DATA = 104
except:
    pass

# /opt/dockethead/include/ar.h: 4214
try:
    AR_STRUCT_ITEM_LOCALE_APP_DATA = 105
except:
    pass

# /opt/dockethead/include/ar.h: 4215
try:
    AR_STRUCT_ITEM_PLACEHOLDER = 106
except:
    pass

# /opt/dockethead/include/ar.h: 4218
try:
    AR_VERCNTL_OBJ_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4219
try:
    AR_VERCNTL_OBJ_TYPE_ACTIVE_LINK = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4220
try:
    AR_VERCNTL_OBJ_TYPE_MENU = 20
except:
    pass

# /opt/dockethead/include/ar.h: 4221
try:
    AR_VERCNTL_OBJ_TYPE_CONTAINER = 30
except:
    pass

# /opt/dockethead/include/ar.h: 4222
try:
    AR_VERCNTL_OBJ_TYPE_ESCALATION = 40
except:
    pass

# /opt/dockethead/include/ar.h: 4223
try:
    AR_VERCNTL_OBJ_TYPE_FILTER = 50
except:
    pass

# /opt/dockethead/include/ar.h: 4224
try:
    AR_VERCNTL_OBJ_TYPE_FORM = 60
except:
    pass

# /opt/dockethead/include/ar.h: 4225
try:
    AR_VERCNTL_OBJ_TYPE_IMAGE = 70
except:
    pass

# /opt/dockethead/include/ar.h: 4228
try:
    AR_VERCNTL_OBJ_SUBTYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4229
try:
    AR_VERCNTL_OBJ_SUBTYPE_CONTAINER_ACTIVELINK_GUIDE = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4230
try:
    AR_VERCNTL_OBJ_SUBTYPE_CONTAINER_APPLICATION = 20
except:
    pass

# /opt/dockethead/include/ar.h: 4231
try:
    AR_VERCNTL_OBJ_SUBTYPE_CONTAINER_FILTER_GUIDE = 30
except:
    pass

# /opt/dockethead/include/ar.h: 4232
try:
    AR_VERCNTL_OBJ_SUBTYPE_CONTAINER_PACKINGLIST = 40
except:
    pass

# /opt/dockethead/include/ar.h: 4233
try:
    AR_VERCNTL_OBJ_SUBTYPE_CONTAINER_WEBSERVICE = 50
except:
    pass

# /opt/dockethead/include/ar.h: 4236
try:
    AR_VERCNTL_OBJ_RESERVATION_MODE_DISABLED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4237
try:
    AR_VERCNTL_OBJ_RESERVATION_MODE_ENFORCED = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4238
try:
    AR_VERCNTL_OBJ_RESERVATION_MODE_DEFAULT = AR_VERCNTL_OBJ_RESERVATION_MODE_DISABLED
except:
    pass

# /opt/dockethead/include/ar.h: 4241
try:
    AR_VERCNTL_OBJ_MOD_LOG_MODE_DISABLED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4242
try:
    AR_VERCNTL_OBJ_MOD_LOG_MODE_ENABLED = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4243
try:
    AR_VERCNTL_OBJ_MOD_LOG_MODE_DEFAULT = AR_VERCNTL_OBJ_MOD_LOG_MODE_DISABLED
except:
    pass

# /opt/dockethead/include/ar.h: 4246
try:
    AR_VERCNTL_OBJ_MOD_LOG_DEFINITION_FILES_SAVE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4247
try:
    AR_VERCNTL_OBJ_MOD_LOG_DEFINITION_FILES_DONOT_SAVE = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4248
try:
    AR_VERCNTL_OBJ_MOD_LOG_DEFINITION_FILES_DEFAULT = AR_VERCNTL_OBJ_MOD_LOG_DEFINITION_FILES_SAVE
except:
    pass

# /opt/dockethead/include/ar.h: 4252
try:
    AR_STRUCT_ITEM_XML_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4253
try:
    AR_STRUCT_ITEM_XML_SCHEMA = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_SCHEMA)
except:
    pass

# /opt/dockethead/include/ar.h: 4254
try:
    AR_STRUCT_ITEM_XML_FILTER = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_FILTER)
except:
    pass

# /opt/dockethead/include/ar.h: 4255
try:
    AR_STRUCT_ITEM_XML_ACTIVE_LINK = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_ACTIVE_LINK)
except:
    pass

# /opt/dockethead/include/ar.h: 4256
try:
    AR_STRUCT_ITEM_XML_CHAR_MENU = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_CHAR_MENU)
except:
    pass

# /opt/dockethead/include/ar.h: 4257
try:
    AR_STRUCT_ITEM_XML_ESCALATION = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_ESCALATION)
except:
    pass

# /opt/dockethead/include/ar.h: 4258
try:
    AR_STRUCT_ITEM_XML_DIST_MAP = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_DIST_MAP)
except:
    pass

# /opt/dockethead/include/ar.h: 4259
try:
    AR_STRUCT_ITEM_XML_CONTAINER = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_CONTAINER)
except:
    pass

# /opt/dockethead/include/ar.h: 4260
try:
    AR_STRUCT_ITEM_XML_DIST_POOL = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_DIST_POOL)
except:
    pass

# /opt/dockethead/include/ar.h: 4261
try:
    AR_STRUCT_ITEM_XML_VUI = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_VUI)
except:
    pass

# /opt/dockethead/include/ar.h: 4262
try:
    AR_STRUCT_ITEM_XML_FIELD = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_FIELD)
except:
    pass

# /opt/dockethead/include/ar.h: 4263
try:
    AR_STRUCT_ITEM_XML_APP = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_APP)
except:
    pass

# /opt/dockethead/include/ar.h: 4264
try:
    AR_STRUCT_ITEM_XML_SCHEMA_DATA = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_SCHEMA_DATA)
except:
    pass

# /opt/dockethead/include/ar.h: 4265
try:
    AR_STRUCT_ITEM_XML_LOCK_BLOCK = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_LOCK_BLOCK)
except:
    pass

# /opt/dockethead/include/ar.h: 4266
try:
    AR_STRUCT_ITEM_XML_IMAGE = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_IMAGE)
except:
    pass

# /opt/dockethead/include/ar.h: 4267
try:
    AR_STRUCT_ITEM_XML_LOCALE_VUI = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_LOCALE_VUI)
except:
    pass

# /opt/dockethead/include/ar.h: 4268
try:
    AR_STRUCT_ITEM_XML_TASK = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_TASK)
except:
    pass

# /opt/dockethead/include/ar.h: 4269
try:
    AR_STRUCT_ITEM_XML_LOCALE_VUI_DATA = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_LOCALE_VUI_DATA)
except:
    pass

# /opt/dockethead/include/ar.h: 4270
try:
    AR_STRUCT_ITEM_XML_LOCALE_APP_DATA = (AR_STRUCT_XML_OFFSET | AR_STRUCT_ITEM_LOCALE_APP_DATA)
except:
    pass

# /opt/dockethead/include/ar.h: 4273
try:
    AR_CACHE_ADMINONLYCREATE_EVENT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4274
try:
    AR_CACHE_ADMINONLYPUBLIC_EVENT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4275
try:
    AR_CACHE_FREE_EVENT = 3
except:
    pass

# /opt/dockethead/include/ar.h: 4276
try:
    AR_CACHE_GROUPCHANGEPUBLIC_EVENT = 4
except:
    pass

# /opt/dockethead/include/ar.h: 4278
try:
    AR_CACHE_EVENT_MAX = 4
except:
    pass

# /opt/dockethead/include/ar.h: 4281
try:
    AR_GCE_OPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4282
try:
    AR_GCE_OPTION_NEXT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4289
try:
    EXPORT_OPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4290
try:
    EXPORT_VUI_MINIMUM = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4292
try:
    AR_OPT_NO_IMPORT = (-1)
except:
    pass

# /opt/dockethead/include/ar.h: 4304
try:
    AR_IMPORT_OPT_CREATE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4305
try:
    AR_IMPORT_OPT_OVERWRITE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4312
try:
    AR_IMPORT_OPT_HANDLE_CONFLICT_ERROR = 16
except:
    pass

# /opt/dockethead/include/ar.h: 4313
try:
    AR_IMPORT_OPT_HANDLE_CONFLICT_OVERWRITE = 32
except:
    pass

# /opt/dockethead/include/ar.h: 4314
try:
    AR_IMPORT_OPT_HANDLE_CONFLICT_NO_ACTION = 48
except:
    pass

# /opt/dockethead/include/ar.h: 4316
try:
    AR_IMPORT_OPT_NOT_DELETE_FIELD = 64
except:
    pass

# /opt/dockethead/include/ar.h: 4317
try:
    AR_IMPORT_OPT_DATA_REJECT_FOR_DUP = 128
except:
    pass

# /opt/dockethead/include/ar.h: 4318
try:
    AR_IMPORT_OPT_DATA_NEWID_FOR_DUP = 256
except:
    pass

# /opt/dockethead/include/ar.h: 4319
try:
    AR_IMPORT_OPT_DATA_OVERWRITE_FOR_DUP = 512
except:
    pass

# /opt/dockethead/include/ar.h: 4320
try:
    AR_IMPORT_OPT_DATA_MERGE_FOR_DUP = 1024
except:
    pass

# /opt/dockethead/include/ar.h: 4321
try:
    AR_IMPORT_OPT_DATA_NEWID_FOR_ALL = 2048
except:
    pass

# /opt/dockethead/include/ar.h: 4322
try:
    AR_IMPORT_OPT_NOT_DELETE_VUI = 4096
except:
    pass

# /opt/dockethead/include/ar.h: 4323
try:
    AR_IMPORT_OPT_NOT_OVERWRITE_PERMISSION = 8192
except:
    pass

# /opt/dockethead/include/ar.h: 4324
try:
    AR_IMPORT_OPT_WORKFLOW_PRESERVE_DEFN = 16384
except:
    pass

# /opt/dockethead/include/ar.h: 4327
try:
    AR_IMPORT_OPT_WORKFLOW_MERGE_ATTACHLIST = 32768
except:
    pass

# /opt/dockethead/include/ar.h: 4328
try:
    AR_IMPORT_OPT_PRESERVE_HISTORY = 65536
except:
    pass

# /opt/dockethead/include/ar.h: 4329
try:
    AR_IMPORT_OPT_PRESERVE_INDEX = 131072
except:
    pass

# /opt/dockethead/include/ar.h: 4330
try:
    AR_IMPORT_OPT_PRESERVE_VUI_NAMESPACE = 262144
except:
    pass

# /opt/dockethead/include/ar.h: 4332
try:
    AR_IMPORT_OPT_PRESERVE_EXTRA_APP_FORMS = 524288
except:
    pass

# /opt/dockethead/include/ar.h: 4333
try:
    AR_IMPORT_OPT_WITH_APP_OWNER = 1048576
except:
    pass

# /opt/dockethead/include/ar.h: 4335
try:
    AR_IMPORT_OPT_WORKFLOW_PRESERVE_ATTACHLIST = 2097152
except:
    pass

# /opt/dockethead/include/ar.h: 4337
try:
    AR_IMPORT_OPT_WORKFLOW_REMOVE_ATTACHLIST = 4194304
except:
    pass

# /opt/dockethead/include/ar.h: 4339
try:
    AR_IMPORT_OPT_OVERWRITE_FULL_TEXT_OPTION = 8388608
except:
    pass

# /opt/dockethead/include/ar.h: 4340
try:
    AR_IMPORT_OPT_OVERWRITE_DISP_PROPS = 16777216
except:
    pass

# /opt/dockethead/include/ar.h: 4341
try:
    AR_IMPORT_OPT_CREATE_NEW_ONLY = 33554432
except:
    pass

# /opt/dockethead/include/ar.h: 4343
try:
    AR_IMPORT_OPT_BASIC_MASK = 15
except:
    pass

# /opt/dockethead/include/ar.h: 4347
try:
    AR_IMPORT_OPT_HANDLE_CONFLICT_MASK = 48
except:
    pass

# /opt/dockethead/include/ar.h: 4352
try:
    AR_DISABLE_KEYWORD_VALIDATION = (1 << 0)
except:
    pass

# /opt/dockethead/include/ar.h: 4353
try:
    AR_DISABLE_PATTERN_MATCHING = (1 << 1)
except:
    pass

# /opt/dockethead/include/ar.h: 4355
try:
    AR_EXPORT_DEFAULT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 4356
try:
    AR_EXPORT_SHARED_WORKFLOW = (1 << 0)
except:
    pass

# /opt/dockethead/include/ar.h: 4357
try:
    AR_EXPORT_DEFAULT_LOCALE = (1 << 1)
except:
    pass

# /opt/dockethead/include/ar.h: 4358
try:
    AR_EXPORT_SELECTED_LOCALES = (1 << 2)
except:
    pass

# /opt/dockethead/include/ar.h: 4359
try:
    AR_EXPORT_APP_INTEGRATION_WORKFLOW = (1 << 3)
except:
    pass

# /opt/dockethead/include/ar.h: 4360
try:
    AR_EXPORT_LOCALE_ONLY = (1 << 4)
except:
    pass

# /opt/dockethead/include/ar.h: 4361
try:
    AR_EXPORT_APPLICATION = (1 << 5)
except:
    pass

# /opt/dockethead/include/ar.h: 4362
try:
    AR_EXPORT_OVERLAY = (1 << 6)
except:
    pass

# /opt/dockethead/include/ar.h: 4375
try:
    AR_SETFIELD_OPT_PRESERVE_UNLISTED_DISPLAY_INSTANCES = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4386
try:
    AR_SETFIELD_OPT_DELETE_LISTED_DISPLAY_INSTANCES = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4390
try:
    AR_SETFIELD_OPT_PRESERVE_DELETE_BITS = 3
except:
    pass

# /opt/dockethead/include/ar.h: 4408
try:
    AR_SERVER_INFO_DB_TYPE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 4409
try:
    AR_SERVER_INFO_SERVER_LICENSE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 4410
try:
    AR_SERVER_INFO_FIXED_LICENSE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 4411
try:
    AR_SERVER_INFO_VERSION = 4
except:
    pass

# /opt/dockethead/include/ar.h: 4412
try:
    AR_SERVER_INFO_ALLOW_GUESTS = 5
except:
    pass

# /opt/dockethead/include/ar.h: 4413
try:
    AR_SERVER_INFO_USE_ETC_PASSWD = 6
except:
    pass

# /opt/dockethead/include/ar.h: 4414
try:
    AR_SERVER_INFO_XREF_PASSWORDS = 7
except:
    pass

# /opt/dockethead/include/ar.h: 4416
try:
    AR_SERVER_INFO_DEBUG_MODE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 4417
try:
    AR_SERVER_INFO_DB_NAME = 9
except:
    pass

# /opt/dockethead/include/ar.h: 4418
try:
    AR_SERVER_INFO_DB_PASSWORD = 10
except:
    pass

# /opt/dockethead/include/ar.h: 4419
try:
    AR_SERVER_INFO_HARDWARE = 11
except:
    pass

# /opt/dockethead/include/ar.h: 4420
try:
    AR_SERVER_INFO_OS = 12
except:
    pass

# /opt/dockethead/include/ar.h: 4421
try:
    AR_SERVER_INFO_SERVER_DIR = 13
except:
    pass

# /opt/dockethead/include/ar.h: 4422
try:
    AR_SERVER_INFO_DBHOME_DIR = 14
except:
    pass

# /opt/dockethead/include/ar.h: 4423
try:
    AR_SERVER_INFO_SET_PROC_TIME = 15
except:
    pass

# /opt/dockethead/include/ar.h: 4425
try:
    AR_SERVER_INFO_EMAIL_FROM = 16
except:
    pass

# /opt/dockethead/include/ar.h: 4426
try:
    AR_SERVER_INFO_SQL_LOG_FILE = 17
except:
    pass

# /opt/dockethead/include/ar.h: 4427
try:
    AR_SERVER_INFO_FLOAT_LICENSE = 18
except:
    pass

# /opt/dockethead/include/ar.h: 4428
try:
    AR_SERVER_INFO_FLOAT_TIMEOUT = 19
except:
    pass

# /opt/dockethead/include/ar.h: 4430
try:
    AR_SERVER_INFO_UNQUAL_QUERIES = 20
except:
    pass

# /opt/dockethead/include/ar.h: 4431
try:
    AR_SERVER_INFO_FILTER_LOG_FILE = 21
except:
    pass

# /opt/dockethead/include/ar.h: 4432
try:
    AR_SERVER_INFO_USER_LOG_FILE = 22
except:
    pass

# /opt/dockethead/include/ar.h: 4433
try:
    AR_SERVER_INFO_REM_SERV_ID = 23
except:
    pass

# /opt/dockethead/include/ar.h: 4434
try:
    AR_SERVER_INFO_MULTI_SERVER = 24
except:
    pass

# /opt/dockethead/include/ar.h: 4435
try:
    AR_SERVER_INFO_EMBEDDED_SQL = 25
except:
    pass

# /opt/dockethead/include/ar.h: 4436
try:
    AR_SERVER_INFO_MAX_SCHEMAS = 26
except:
    pass

# /opt/dockethead/include/ar.h: 4438
try:
    AR_SERVER_INFO_DB_VERSION = 27
except:
    pass

# /opt/dockethead/include/ar.h: 4439
try:
    AR_SERVER_INFO_MAX_ENTRIES = 28
except:
    pass

# /opt/dockethead/include/ar.h: 4441
try:
    AR_SERVER_INFO_MAX_F_DAEMONS = 29
except:
    pass

# /opt/dockethead/include/ar.h: 4443
try:
    AR_SERVER_INFO_MAX_L_DAEMONS = 30
except:
    pass

# /opt/dockethead/include/ar.h: 4445
try:
    AR_SERVER_INFO_ESCALATION_LOG_FILE = 31
except:
    pass

# /opt/dockethead/include/ar.h: 4447
try:
    AR_SERVER_INFO_ESCL_DAEMON = 32
except:
    pass

# /opt/dockethead/include/ar.h: 4448
try:
    AR_SERVER_INFO_SUBMITTER_MODE = 33
except:
    pass

# /opt/dockethead/include/ar.h: 4449
try:
    AR_SERVER_INFO_API_LOG_FILE = 34
except:
    pass

# /opt/dockethead/include/ar.h: 4450
try:
    AR_SERVER_INFO_FTEXT_FIXED = 35
except:
    pass

# /opt/dockethead/include/ar.h: 4451
try:
    AR_SERVER_INFO_FTEXT_FLOAT = 36
except:
    pass

# /opt/dockethead/include/ar.h: 4452
try:
    AR_SERVER_INFO_FTEXT_TIMEOUT = 37
except:
    pass

# /opt/dockethead/include/ar.h: 4454
try:
    AR_SERVER_INFO_RESERV1_A = 38
except:
    pass

# /opt/dockethead/include/ar.h: 4455
try:
    AR_SERVER_INFO_RESERV1_B = 39
except:
    pass

# /opt/dockethead/include/ar.h: 4456
try:
    AR_SERVER_INFO_RESERV1_C = 40
except:
    pass

# /opt/dockethead/include/ar.h: 4457
try:
    AR_SERVER_INFO_SERVER_IDENT = 41
except:
    pass

# /opt/dockethead/include/ar.h: 4459
try:
    AR_SERVER_INFO_DS_SVR_LICENSE = 42
except:
    pass

# /opt/dockethead/include/ar.h: 4460
try:
    AR_SERVER_INFO_DS_MAPPING = 43
except:
    pass

# /opt/dockethead/include/ar.h: 4462
try:
    AR_SERVER_INFO_DS_PENDING = 44
except:
    pass

# /opt/dockethead/include/ar.h: 4464
try:
    AR_SERVER_INFO_DS_RPC_SOCKET = 45
except:
    pass

# /opt/dockethead/include/ar.h: 4465
try:
    AR_SERVER_INFO_DS_LOG_FILE = 46
except:
    pass

# /opt/dockethead/include/ar.h: 4466
try:
    AR_SERVER_INFO_SUPPRESS_WARN = 47
except:
    pass

# /opt/dockethead/include/ar.h: 4468
try:
    AR_SERVER_INFO_HOSTNAME = 48
except:
    pass

# /opt/dockethead/include/ar.h: 4469
try:
    AR_SERVER_INFO_FULL_HOSTNAME = 49
except:
    pass

# /opt/dockethead/include/ar.h: 4470
try:
    AR_SERVER_INFO_SAVE_LOGIN = 50
except:
    pass

# /opt/dockethead/include/ar.h: 4472
try:
    AR_SERVER_INFO_U_CACHE_CHANGE = 51
except:
    pass

# /opt/dockethead/include/ar.h: 4473
try:
    AR_SERVER_INFO_G_CACHE_CHANGE = 52
except:
    pass

# /opt/dockethead/include/ar.h: 4474
try:
    AR_SERVER_INFO_STRUCT_CHANGE = 53
except:
    pass

# /opt/dockethead/include/ar.h: 4476
try:
    AR_SERVER_INFO_CASE_SENSITIVE = 54
except:
    pass

# /opt/dockethead/include/ar.h: 4477
try:
    AR_SERVER_INFO_SERVER_LANG = 55
except:
    pass

# /opt/dockethead/include/ar.h: 4478
try:
    AR_SERVER_INFO_ADMIN_ONLY = 56
except:
    pass

# /opt/dockethead/include/ar.h: 4479
try:
    AR_SERVER_INFO_CACHE_LOG_FILE = 57
except:
    pass

# /opt/dockethead/include/ar.h: 4480
try:
    AR_SERVER_INFO_FLASH_DAEMON = 58
except:
    pass

# /opt/dockethead/include/ar.h: 4481
try:
    AR_SERVER_INFO_THREAD_LOG_FILE = 59
except:
    pass

# /opt/dockethead/include/ar.h: 4482
try:
    AR_SERVER_INFO_ADMIN_TCP_PORT = 60
except:
    pass

# /opt/dockethead/include/ar.h: 4483
try:
    AR_SERVER_INFO_ESCL_TCP_PORT = 61
except:
    pass

# /opt/dockethead/include/ar.h: 4484
try:
    AR_SERVER_INFO_FAST_TCP_PORT = 62
except:
    pass

# /opt/dockethead/include/ar.h: 4485
try:
    AR_SERVER_INFO_LIST_TCP_PORT = 63
except:
    pass

# /opt/dockethead/include/ar.h: 4486
try:
    AR_SERVER_INFO_FLASH_TCP_PORT = 64
except:
    pass

# /opt/dockethead/include/ar.h: 4487
try:
    AR_SERVER_INFO_TCD_TCP_PORT = 65
except:
    pass

# /opt/dockethead/include/ar.h: 4488
try:
    AR_SERVER_INFO_DSO_DEST_PORT = 66
except:
    pass

# /opt/dockethead/include/ar.h: 4489
try:
    AR_SERVER_INFO_INFORMIX_DBN = 67
except:
    pass

# /opt/dockethead/include/ar.h: 4490
try:
    AR_SERVER_INFO_INFORMIX_TBC = 68
except:
    pass

# /opt/dockethead/include/ar.h: 4491
try:
    AR_SERVER_INFO_INGRES_VNODE = 69
except:
    pass

# /opt/dockethead/include/ar.h: 4492
try:
    AR_SERVER_INFO_ORACLE_SID = 70
except:
    pass

# /opt/dockethead/include/ar.h: 4493
try:
    AR_SERVER_INFO_ORACLE_TWO_T = 71
except:
    pass

# /opt/dockethead/include/ar.h: 4494
try:
    AR_SERVER_INFO_SYBASE_CHARSET = 72
except:
    pass

# /opt/dockethead/include/ar.h: 4495
try:
    AR_SERVER_INFO_SYBASE_SERV = 73
except:
    pass

# /opt/dockethead/include/ar.h: 4496
try:
    AR_SERVER_INFO_SHARED_MEM = 74
except:
    pass

# /opt/dockethead/include/ar.h: 4497
try:
    AR_SERVER_INFO_SHARED_CACHE = 75
except:
    pass

# /opt/dockethead/include/ar.h: 4498
try:
    AR_SERVER_INFO_CACHE_SEG_SIZE = 76
except:
    pass

# /opt/dockethead/include/ar.h: 4499
try:
    AR_SERVER_INFO_DB_USER = 77
except:
    pass

# /opt/dockethead/include/ar.h: 4500
try:
    AR_SERVER_INFO_NFY_TCP_PORT = 78
except:
    pass

# /opt/dockethead/include/ar.h: 4501
try:
    AR_SERVER_INFO_FILT_MAX_TOTAL = 79
except:
    pass

# /opt/dockethead/include/ar.h: 4502
try:
    AR_SERVER_INFO_FILT_MAX_STACK = 80
except:
    pass

# /opt/dockethead/include/ar.h: 4503
try:
    AR_SERVER_INFO_DEFAULT_ORDER_BY = 81
except:
    pass

# /opt/dockethead/include/ar.h: 4504
try:
    AR_SERVER_INFO_DELAYED_CACHE = 82
except:
    pass

# /opt/dockethead/include/ar.h: 4505
try:
    AR_SERVER_INFO_DSO_MERGE_STYLE = 83
except:
    pass

# /opt/dockethead/include/ar.h: 4506
try:
    AR_SERVER_INFO_EMAIL_LINE_LEN = 84
except:
    pass

# /opt/dockethead/include/ar.h: 4507
try:
    AR_SERVER_INFO_EMAIL_SYSTEM = 85
except:
    pass

# /opt/dockethead/include/ar.h: 4508
try:
    AR_SERVER_INFO_INFORMIX_RELAY_MOD = 86
except:
    pass

# /opt/dockethead/include/ar.h: 4509
try:
    AR_SERVER_INFO_PS_RPC_SOCKET = 87
except:
    pass

# /opt/dockethead/include/ar.h: 4510
try:
    AR_SERVER_INFO_REGISTER_PORTMAPPER = 88
except:
    pass

# /opt/dockethead/include/ar.h: 4511
try:
    AR_SERVER_INFO_SERVER_NAME = 89
except:
    pass

# /opt/dockethead/include/ar.h: 4512
try:
    AR_SERVER_INFO_DBCONF = 90
except:
    pass

# /opt/dockethead/include/ar.h: 4513
try:
    AR_SERVER_INFO_APPL_PENDING = 91
except:
    pass

# /opt/dockethead/include/ar.h: 4515
try:
    AR_SERVER_INFO_AP_RPC_SOCKET = 92
except:
    pass

# /opt/dockethead/include/ar.h: 4516
try:
    AR_SERVER_INFO_AP_LOG_FILE = 93
except:
    pass

# /opt/dockethead/include/ar.h: 4517
try:
    AR_SERVER_INFO_AP_DEFN_CHECK = 94
except:
    pass

# /opt/dockethead/include/ar.h: 4519
try:
    AR_SERVER_INFO_MAX_LOG_FILE_SIZE = 95
except:
    pass

# /opt/dockethead/include/ar.h: 4520
try:
    AR_SERVER_INFO_CLUSTERED_INDEX = 96
except:
    pass

# /opt/dockethead/include/ar.h: 4522
try:
    AR_SERVER_INFO_ACTLINK_DIR = 97
except:
    pass

# /opt/dockethead/include/ar.h: 4524
try:
    AR_SERVER_INFO_ACTLINK_SHELL = 98
except:
    pass

# /opt/dockethead/include/ar.h: 4526
try:
    AR_SERVER_INFO_USER_CACHE_UTILS = 99
except:
    pass

# /opt/dockethead/include/ar.h: 4528
try:
    AR_SERVER_INFO_EMAIL_TIMEOUT = 100
except:
    pass

# /opt/dockethead/include/ar.h: 4529
try:
    AR_SERVER_INFO_EXPORT_VERSION = 101
except:
    pass

# /opt/dockethead/include/ar.h: 4530
try:
    AR_SERVER_INFO_ENCRYPT_AL_SQL = 102
except:
    pass

# /opt/dockethead/include/ar.h: 4532
try:
    AR_SERVER_INFO_SCC_ENABLED = 103
except:
    pass

# /opt/dockethead/include/ar.h: 4533
try:
    AR_SERVER_INFO_SCC_PROVIDER_NAME = 104
except:
    pass

# /opt/dockethead/include/ar.h: 4534
try:
    AR_SERVER_INFO_SCC_TARGET_DIR = 105
except:
    pass

# /opt/dockethead/include/ar.h: 4535
try:
    AR_SERVER_INFO_SCC_COMMENT_CHECKIN = 106
except:
    pass

# /opt/dockethead/include/ar.h: 4537
try:
    AR_SERVER_INFO_SCC_COMMENT_CHECKOUT = 107
except:
    pass

# /opt/dockethead/include/ar.h: 4539
try:
    AR_SERVER_INFO_SCC_INTEGRATION_MODE = 108
except:
    pass

# /opt/dockethead/include/ar.h: 4541
try:
    AR_SERVER_INFO_EA_RPC_SOCKET = 109
except:
    pass

# /opt/dockethead/include/ar.h: 4543
try:
    AR_SERVER_INFO_EA_RPC_TIMEOUT = 110
except:
    pass

# /opt/dockethead/include/ar.h: 4546
try:
    AR_SERVER_INFO_USER_INFO_LISTS = 111
except:
    pass

# /opt/dockethead/include/ar.h: 4548
try:
    AR_SERVER_INFO_USER_INST_TIMEOUT = 112
except:
    pass

# /opt/dockethead/include/ar.h: 4551
try:
    AR_SERVER_INFO_DEBUG_GROUPID = 113
except:
    pass

# /opt/dockethead/include/ar.h: 4555
try:
    AR_SERVER_INFO_APPLICATION_AUDIT = 114
except:
    pass

# /opt/dockethead/include/ar.h: 4557
try:
    AR_SERVER_INFO_EA_SYNC_TIMEOUT = 115
except:
    pass

# /opt/dockethead/include/ar.h: 4560
try:
    AR_SERVER_INFO_SERVER_TIME = 116
except:
    pass

# /opt/dockethead/include/ar.h: 4561
try:
    AR_SERVER_INFO_SVR_SEC_CACHE = 117
except:
    pass

# /opt/dockethead/include/ar.h: 4563
try:
    AR_SERVER_INFO_LOGFILE_APPEND = 118
except:
    pass

# /opt/dockethead/include/ar.h: 4565
try:
    AR_SERVER_INFO_MINIMUM_API_VER = 119
except:
    pass

# /opt/dockethead/include/ar.h: 4568
try:
    AR_SERVER_INFO_MAX_AUDIT_LOG_FILE_SIZE = 120
except:
    pass

# /opt/dockethead/include/ar.h: 4570
try:
    AR_SERVER_INFO_CANCEL_QUERY = 121
except:
    pass

# /opt/dockethead/include/ar.h: 4571
try:
    AR_SERVER_INFO_MULT_ASSIGN_GROUPS = 122
except:
    pass

# /opt/dockethead/include/ar.h: 4572
try:
    AR_SERVER_INFO_ARFORK_LOG_FILE = 123
except:
    pass

# /opt/dockethead/include/ar.h: 4573
try:
    AR_SERVER_INFO_DSO_PLACEHOLDER_MODE = 124
except:
    pass

# /opt/dockethead/include/ar.h: 4575
try:
    AR_SERVER_INFO_DSO_POLLING_INTERVAL = 125
except:
    pass

# /opt/dockethead/include/ar.h: 4576
try:
    AR_SERVER_INFO_DSO_SOURCE_SERVER = 126
except:
    pass

# /opt/dockethead/include/ar.h: 4577
try:
    AR_SERVER_INFO_DS_POOL = 127
except:
    pass

# /opt/dockethead/include/ar.h: 4579
try:
    AR_SERVER_INFO_DSO_TIMEOUT_NORMAL = 128
except:
    pass

# /opt/dockethead/include/ar.h: 4582
try:
    AR_SERVER_INFO_ENC_PUB_KEY = 129
except:
    pass

# /opt/dockethead/include/ar.h: 4583
try:
    AR_SERVER_INFO_ENC_PUB_KEY_EXP = 130
except:
    pass

# /opt/dockethead/include/ar.h: 4586
try:
    AR_SERVER_INFO_ENC_DATA_KEY_EXP = 131
except:
    pass

# /opt/dockethead/include/ar.h: 4588
try:
    AR_SERVER_INFO_ENC_DATA_ENCR_ALG = 132
except:
    pass

# /opt/dockethead/include/ar.h: 4590
try:
    AR_SERVER_INFO_ENC_SEC_POLICY = 133
except:
    pass

# /opt/dockethead/include/ar.h: 4591
try:
    AR_SERVER_INFO_ENC_SESS_H_ENTRIES = 134
except:
    pass

# /opt/dockethead/include/ar.h: 4593
try:
    AR_SERVER_INFO_DSO_TARGET_CONNECTION = 135
except:
    pass

# /opt/dockethead/include/ar.h: 4595
try:
    AR_SERVER_INFO_PREFERENCE_PRIORITY = 136
except:
    pass

# /opt/dockethead/include/ar.h: 4597
try:
    AR_SERVER_INFO_ORACLE_QUERY_ON_CLOB = 137
except:
    pass

# /opt/dockethead/include/ar.h: 4599
try:
    AR_SERVER_INFO_MESSAGE_CAT_SCHEMA = 138
except:
    pass

# /opt/dockethead/include/ar.h: 4601
try:
    AR_SERVER_INFO_ALERT_SCHEMA = 139
except:
    pass

# /opt/dockethead/include/ar.h: 4603
try:
    AR_SERVER_INFO_LOCALIZED_SERVER = 140
except:
    pass

# /opt/dockethead/include/ar.h: 4605
try:
    AR_SERVER_INFO_SVR_EVENT_LIST = 141
except:
    pass

# /opt/dockethead/include/ar.h: 4607
try:
    AR_SERVER_INFO_DISABLE_ADMIN_OPERATIONS = 142
except:
    pass

# /opt/dockethead/include/ar.h: 4609
try:
    AR_SERVER_INFO_DISABLE_ESCALATIONS = 143
except:
    pass

# /opt/dockethead/include/ar.h: 4611
try:
    AR_SERVER_INFO_ALERT_LOG_FILE = 144
except:
    pass

# /opt/dockethead/include/ar.h: 4613
try:
    AR_SERVER_INFO_DISABLE_ALERTS = 145
except:
    pass

# /opt/dockethead/include/ar.h: 4615
try:
    AR_SERVER_INFO_CHECK_ALERT_USERS = 146
except:
    pass

# /opt/dockethead/include/ar.h: 4617
try:
    AR_SERVER_INFO_ALERT_SEND_TIMEOUT = 147
except:
    pass

# /opt/dockethead/include/ar.h: 4619
try:
    AR_SERVER_INFO_ALERT_OUTBOUND_PORT = 148
except:
    pass

# /opt/dockethead/include/ar.h: 4620
try:
    AR_SERVER_INFO_ALERT_SOURCE_AR = 149
except:
    pass

# /opt/dockethead/include/ar.h: 4621
try:
    AR_SERVER_INFO_ALERT_SOURCE_FB = 150
except:
    pass

# /opt/dockethead/include/ar.h: 4622
try:
    AR_SERVER_INFO_DSO_USER_PASSWD = 151
except:
    pass

# /opt/dockethead/include/ar.h: 4623
try:
    AR_SERVER_INFO_DSO_TARGET_PASSWD = 152
except:
    pass

# /opt/dockethead/include/ar.h: 4624
try:
    AR_SERVER_INFO_APP_SERVICE_PASSWD = 153
except:
    pass

# /opt/dockethead/include/ar.h: 4626
try:
    AR_SERVER_INFO_MID_TIER_PASSWD = 154
except:
    pass

# /opt/dockethead/include/ar.h: 4627
try:
    AR_SERVER_INFO_PLUGIN_LOG_FILE = 155
except:
    pass

# /opt/dockethead/include/ar.h: 4629
try:
    AR_SERVER_INFO_SVR_STATS_REC_MODE = 156
except:
    pass

# /opt/dockethead/include/ar.h: 4631
try:
    AR_SERVER_INFO_SVR_STATS_REC_INTERVAL = 157
except:
    pass

# /opt/dockethead/include/ar.h: 4633
try:
    AR_SERVER_INFO_DEFAULT_WEB_PATH = 158
except:
    pass

# /opt/dockethead/include/ar.h: 4635
try:
    AR_SERVER_INFO_FILTER_API_RPC_TIMEOUT = 159
except:
    pass

# /opt/dockethead/include/ar.h: 4637
try:
    AR_SERVER_INFO_DISABLED_CLIENT = 160
except:
    pass

# /opt/dockethead/include/ar.h: 4639
try:
    AR_SERVER_INFO_PLUGIN_PASSWD = 161
except:
    pass

# /opt/dockethead/include/ar.h: 4640
try:
    AR_SERVER_INFO_PLUGIN_ALIAS = 162
except:
    pass

# /opt/dockethead/include/ar.h: 4641
try:
    AR_SERVER_INFO_PLUGIN_TARGET_PASSWD = 163
except:
    pass

# /opt/dockethead/include/ar.h: 4643
try:
    AR_SERVER_INFO_REM_WKFLW_PASSWD = 164
except:
    pass

# /opt/dockethead/include/ar.h: 4644
try:
    AR_SERVER_INFO_REM_WKFLW_TARGET_PASSWD = 165
except:
    pass

# /opt/dockethead/include/ar.h: 4646
try:
    AR_SERVER_INFO_EXPORT_SVR_OPS = 166
except:
    pass

# /opt/dockethead/include/ar.h: 4648
try:
    AR_SERVER_INFO_INIT_FORM = 167
except:
    pass

# /opt/dockethead/include/ar.h: 4650
try:
    AR_SERVER_INFO_ENC_PUB_KEY_ALG = 168
except:
    pass

# /opt/dockethead/include/ar.h: 4652
try:
    AR_SERVER_INFO_IP_NAMES = 169
except:
    pass

# /opt/dockethead/include/ar.h: 4654
try:
    AR_SERVER_INFO_DSO_CACHE_CHK_INTERVAL = 170
except:
    pass

# /opt/dockethead/include/ar.h: 4656
try:
    AR_SERVER_INFO_DSO_MARK_PENDING_RETRY = 171
except:
    pass

# /opt/dockethead/include/ar.h: 4658
try:
    AR_SERVER_INFO_DSO_RPCPROG_NUM = 172
except:
    pass

# /opt/dockethead/include/ar.h: 4660
try:
    AR_SERVER_INFO_DELAY_RECACHE_TIME = 173
except:
    pass

# /opt/dockethead/include/ar.h: 4663
try:
    AR_SERVER_INFO_DFLT_ALLOW_CURRENCIES = 174
except:
    pass

# /opt/dockethead/include/ar.h: 4665
try:
    AR_SERVER_INFO_CURRENCY_INTERVAL = 175
except:
    pass

# /opt/dockethead/include/ar.h: 4667
try:
    AR_SERVER_INFO_ORACLE_CURSOR_SHARE = 176
except:
    pass

# /opt/dockethead/include/ar.h: 4669
try:
    AR_SERVER_INFO_DB2_DB_ALIAS = 177
except:
    pass

# /opt/dockethead/include/ar.h: 4670
try:
    AR_SERVER_INFO_DB2_SERVER = 178
except:
    pass

# /opt/dockethead/include/ar.h: 4671
try:
    AR_SERVER_INFO_DFLT_FUNC_CURRENCIES = 179
except:
    pass

# /opt/dockethead/include/ar.h: 4673
try:
    AR_SERVER_INFO_EMAIL_IMPORT_FORM = 180
except:
    pass

# /opt/dockethead/include/ar.h: 4676
try:
    AR_SERVER_INFO_EMAIL_AIX_USE_OLD_EMAIL = 181
except:
    pass

# /opt/dockethead/include/ar.h: 4678
try:
    AR_SERVER_INFO_TWO_DIGIT_YEAR_CUTOFF = 182
except:
    pass

# /opt/dockethead/include/ar.h: 4679
try:
    AR_SERVER_INFO_ALLOW_BACKQUOTE_IN_PROCESS = 183
except:
    pass

# /opt/dockethead/include/ar.h: 4681
try:
    AR_SERVER_INFO_DB_CONNECTION_RETRIES = 184
except:
    pass

# /opt/dockethead/include/ar.h: 4682
try:
    AR_SERVER_INFO_DB_CHAR_SET = 185
except:
    pass

# /opt/dockethead/include/ar.h: 4684
try:
    AR_SERVER_INFO_CURR_PART_VALUE_STR = 186
except:
    pass

# /opt/dockethead/include/ar.h: 4685
try:
    AR_SERVER_INFO_CURR_PART_TYPE_STR = 187
except:
    pass

# /opt/dockethead/include/ar.h: 4686
try:
    AR_SERVER_INFO_CURR_PART_DATE_STR = 188
except:
    pass

# /opt/dockethead/include/ar.h: 4687
try:
    AR_SERVER_INFO_HOMEPAGE_FORM = 189
except:
    pass

# /opt/dockethead/include/ar.h: 4688
try:
    AR_SERVER_INFO_DISABLE_FTS_INDEXER = 190
except:
    pass

# /opt/dockethead/include/ar.h: 4690
try:
    AR_SERVER_INFO_DISABLE_ARCHIVE = 191
except:
    pass

# /opt/dockethead/include/ar.h: 4692
try:
    AR_SERVER_INFO_SERVERGROUP_MEMBER = 192
except:
    pass

# /opt/dockethead/include/ar.h: 4694
try:
    AR_SERVER_INFO_SERVERGROUP_LOG_FILE = 193
except:
    pass

# /opt/dockethead/include/ar.h: 4696
try:
    AR_SERVER_INFO_FLUSH_LOG_LINES = 194
except:
    pass

# /opt/dockethead/include/ar.h: 4698
try:
    AR_SERVER_INFO_SERVERGROUP_INTERVAL = 195
except:
    pass

# /opt/dockethead/include/ar.h: 4700
try:
    AR_SERVER_INFO_JAVA_VM_OPTIONS = 196
except:
    pass

# /opt/dockethead/include/ar.h: 4701
try:
    AR_SERVER_INFO_PER_THREAD_LOGS = 197
except:
    pass

# /opt/dockethead/include/ar.h: 4703
try:
    AR_SERVER_INFO_CONFIG_FILE = 198
except:
    pass

# /opt/dockethead/include/ar.h: 4704
try:
    AR_SERVER_INFO_SSTABLE_CHUNK_SIZE = 199
except:
    pass

# /opt/dockethead/include/ar.h: 4706
try:
    AR_SERVER_INFO_SG_EMAIL_STATE = 200
except:
    pass

# /opt/dockethead/include/ar.h: 4710
try:
    AR_SERVER_INFO_SG_FLASHBOARDS_STATE = 201
except:
    pass

# /opt/dockethead/include/ar.h: 4714
try:
    AR_SERVER_INFO_SERVERGROUP_NAME = 202
except:
    pass

# /opt/dockethead/include/ar.h: 4716
try:
    AR_SERVER_INFO_SG_ADMIN_SERVER_NAME = 203
except:
    pass

# /opt/dockethead/include/ar.h: 4718
try:
    AR_SERVER_INFO_LOCKED_WKFLW_LOG_MODE = 204
except:
    pass

# /opt/dockethead/include/ar.h: 4722
try:
    AR_SERVER_INFO_ROLE_CHANGE = 205
except:
    pass

# /opt/dockethead/include/ar.h: 4723
try:
    AR_SERVER_INFO_SG_ADMIN_SERVER_PORT = 206
except:
    pass

# /opt/dockethead/include/ar.h: 4725
try:
    AR_SERVER_INFO_PLUGIN_LOOPBACK_RPC = 207
except:
    pass

# /opt/dockethead/include/ar.h: 4727
try:
    AR_SERVER_INFO_CACHE_MODE = 208
except:
    pass

# /opt/dockethead/include/ar.h: 4728
try:
    AR_SERVER_INFO_DB_FREESPACE = 209
except:
    pass

# /opt/dockethead/include/ar.h: 4730
try:
    AR_SERVER_INFO_GENERAL_AUTH_ERR = 210
except:
    pass

# /opt/dockethead/include/ar.h: 4732
try:
    AR_SERVER_INFO_AUTH_CHAINING_MODE = 211
except:
    pass

# /opt/dockethead/include/ar.h: 4737
try:
    AR_SERVER_INFO_RPC_NON_BLOCKING_IO = 212
except:
    pass

# /opt/dockethead/include/ar.h: 4739
try:
    AR_SERVER_INFO_SYS_LOGGING_OPTIONS = 213
except:
    pass

# /opt/dockethead/include/ar.h: 4741
try:
    AR_SERVER_INFO_EXT_AUTH_CAPABILITIES = 214
except:
    pass

# /opt/dockethead/include/ar.h: 4746
try:
    AR_SERVER_INFO_DSO_ERROR_RETRY = 215
except:
    pass

# /opt/dockethead/include/ar.h: 4750
try:
    AR_SERVER_INFO_PREF_SERVER_OPTION = 216
except:
    pass

# /opt/dockethead/include/ar.h: 4753
try:
    AR_SERVER_INFO_FTINDEXER_LOG_FILE = 217
except:
    pass

# /opt/dockethead/include/ar.h: 4755
try:
    AR_SERVER_INFO_EXCEPTION_OPTION = 218
except:
    pass

# /opt/dockethead/include/ar.h: 4758
try:
    AR_SERVER_INFO_ERROR_EXCEPTION_LIST = 219
except:
    pass

# /opt/dockethead/include/ar.h: 4760
try:
    AR_SERVER_INFO_DSO_MAX_QUERY_SIZE = 220
except:
    pass

# /opt/dockethead/include/ar.h: 4762
try:
    AR_SERVER_INFO_ADMIN_OP_TRACKING = 221
except:
    pass

# /opt/dockethead/include/ar.h: 4766
try:
    AR_SERVER_INFO_ADMIN_OP_PROGRESS = 222
except:
    pass

# /opt/dockethead/include/ar.h: 4771
try:
    AR_SERVER_INFO_PLUGIN_DEFAULT_TIMEOUT = 223
except:
    pass

# /opt/dockethead/include/ar.h: 4773
try:
    AR_SERVER_INFO_EA_IGNORE_EXCESS_GROUPS = 224
except:
    pass

# /opt/dockethead/include/ar.h: 4777
try:
    AR_SERVER_INFO_EA_GROUP_MAPPING = 225
except:
    pass

# /opt/dockethead/include/ar.h: 4779
try:
    AR_SERVER_INFO_PLUGIN_LOG_LEVEL = 226
except:
    pass

# /opt/dockethead/include/ar.h: 4781
try:
    AR_SERVER_INFO_FT_THRESHOLD_LOW = 227
except:
    pass

# /opt/dockethead/include/ar.h: 4783
try:
    AR_SERVER_INFO_FT_THRESHOLD_HIGH = 228
except:
    pass

# /opt/dockethead/include/ar.h: 4785
try:
    AR_SERVER_INFO_NOTIFY_WEB_PATH = 229
except:
    pass

# /opt/dockethead/include/ar.h: 4787
try:
    AR_SERVER_INFO_DISABLE_NON_UNICODE_CLIENTS = 230
except:
    pass

# /opt/dockethead/include/ar.h: 4788
try:
    AR_SERVER_INFO_FT_COLLECTION_DIR = 231
except:
    pass

# /opt/dockethead/include/ar.h: 4790
try:
    AR_SERVER_INFO_FT_CONFIGURATION_DIR = 232
except:
    pass

# /opt/dockethead/include/ar.h: 4792
try:
    AR_SERVER_INFO_FT_TEMP_DIR = 233
except:
    pass

# /opt/dockethead/include/ar.h: 4794
try:
    AR_SERVER_INFO_FT_REINDEX = 234
except:
    pass

# /opt/dockethead/include/ar.h: 4796
try:
    AR_SERVER_INFO_FT_DISABLE_SEARCH = 235
except:
    pass

# /opt/dockethead/include/ar.h: 4800
try:
    AR_SERVER_INFO_FT_CASE_SENSITIVITY = 236
except:
    pass

# /opt/dockethead/include/ar.h: 4804
try:
    AR_SERVER_INFO_FT_SEARCH_MATCH_OP = 237
except:
    pass

# /opt/dockethead/include/ar.h: 4810
try:
    AR_SERVER_INFO_FT_STOP_WORDS = 238
except:
    pass

# /opt/dockethead/include/ar.h: 4812
try:
    AR_SERVER_INFO_FT_RECOVERY_INTERVAL = 239
except:
    pass

# /opt/dockethead/include/ar.h: 4815
try:
    AR_SERVER_INFO_FT_OPTIMIZE_THRESHOLD = 240
except:
    pass

# /opt/dockethead/include/ar.h: 4818
try:
    AR_SERVER_INFO_MAX_PASSWORD_ATTEMPTS = 241
except:
    pass

# /opt/dockethead/include/ar.h: 4821
try:
    AR_SERVER_INFO_GUESTS_RESTRICT_READ = 242
except:
    pass

# /opt/dockethead/include/ar.h: 4825
try:
    AR_SERVER_INFO_ORACLE_CLOB_STORE_INROW = 243
except:
    pass

# /opt/dockethead/include/ar.h: 4829
try:
    AR_SERVER_INFO_NEXT_ID_BLOCK_SIZE = 244
except:
    pass

# /opt/dockethead/include/ar.h: 4830
try:
    AR_SERVER_INFO_NEXT_ID_COMMIT = 245
except:
    pass

# /opt/dockethead/include/ar.h: 4832
try:
    AR_SERVER_INFO_RPC_CLIENT_XDR_LIMIT = 246
except:
    pass

# /opt/dockethead/include/ar.h: 4834
try:
    AR_SERVER_INFO_CACHE_DISP_PROP = 247
except:
    pass

# /opt/dockethead/include/ar.h: 4840
try:
    AR_SERVER_INFO_USE_CON_NAME_IN_STATS = 248
except:
    pass

# /opt/dockethead/include/ar.h: 4844
try:
    AR_SERVER_INFO_DB_MAX_ATTACH_SIZE = 249
except:
    pass

# /opt/dockethead/include/ar.h: 4846
try:
    AR_SERVER_INFO_DB_MAX_TEXT_SIZE = 250
except:
    pass

# /opt/dockethead/include/ar.h: 4854
try:
    AR_SERVER_INFO_GUID_PREFIX = 251
except:
    pass

# /opt/dockethead/include/ar.h: 4856
try:
    AR_SERVER_INFO_MULTIPLE_ARSYSTEM_SERVERS = 252
except:
    pass

# /opt/dockethead/include/ar.h: 4860
try:
    AR_SERVER_INFO_ORACLE_BULK_FETCH_COUNT = 253
except:
    pass

# /opt/dockethead/include/ar.h: 4863
try:
    AR_SERVER_INFO_MINIMUM_CMDB_API_VER = 254
except:
    pass

# /opt/dockethead/include/ar.h: 4866
try:
    AR_SERVER_INFO_PLUGIN_PORT = 255
except:
    pass

# /opt/dockethead/include/ar.h: 4867
try:
    AR_SERVER_INFO_PLUGIN_LIST = 256
except:
    pass

# /opt/dockethead/include/ar.h: 4869
try:
    AR_SERVER_INFO_PLUGIN_PATH_LIST = 257
except:
    pass

# /opt/dockethead/include/ar.h: 4871
try:
    AR_SERVER_INFO_SHARED_LIB = 258
except:
    pass

# /opt/dockethead/include/ar.h: 4873
try:
    AR_SERVER_INFO_SHARED_LIB_PATH = 259
except:
    pass

# /opt/dockethead/include/ar.h: 4875
try:
    AR_SERVER_INFO_CMDB_INSTALL_DIR = 260
except:
    pass

# /opt/dockethead/include/ar.h: 4877
try:
    AR_SERVER_INFO_RE_LOG_DIR = 261
except:
    pass

# /opt/dockethead/include/ar.h: 4879
try:
    AR_SERVER_INFO_LOG_TO_FORM = 262
except:
    pass

# /opt/dockethead/include/ar.h: 4881
try:
    AR_SERVER_INFO_SQL_LOG_FORM = 263
except:
    pass

# /opt/dockethead/include/ar.h: 4882
try:
    AR_SERVER_INFO_API_LOG_FORM = 264
except:
    pass

# /opt/dockethead/include/ar.h: 4883
try:
    AR_SERVER_INFO_ESCL_LOG_FORM = 265
except:
    pass

# /opt/dockethead/include/ar.h: 4884
try:
    AR_SERVER_INFO_FILTER_LOG_FORM = 266
except:
    pass

# /opt/dockethead/include/ar.h: 4885
try:
    AR_SERVER_INFO_USER_LOG_FORM = 267
except:
    pass

# /opt/dockethead/include/ar.h: 4886
try:
    AR_SERVER_INFO_ALERT_LOG_FORM = 268
except:
    pass

# /opt/dockethead/include/ar.h: 4887
try:
    AR_SERVER_INFO_SVRGRP_LOG_FORM = 269
except:
    pass

# /opt/dockethead/include/ar.h: 4888
try:
    AR_SERVER_INFO_FTINDX_LOG_FORM = 270
except:
    pass

# /opt/dockethead/include/ar.h: 4889
try:
    AR_SERVER_INFO_THREAD_LOG_FORM = 271
except:
    pass

# /opt/dockethead/include/ar.h: 4891
try:
    AR_SERVER_INFO_FIPS_SERVER_MODE = 272
except:
    pass

# /opt/dockethead/include/ar.h: 4892
try:
    AR_SERVER_INFO_FIPS_CLIENT_MODE = 273
except:
    pass

# /opt/dockethead/include/ar.h: 4893
try:
    AR_SERVER_INFO_FIPS_STATUS = 274
except:
    pass

# /opt/dockethead/include/ar.h: 4894
try:
    AR_SERVER_INFO_ENC_LEVEL = 275
except:
    pass

# /opt/dockethead/include/ar.h: 4895
try:
    AR_SERVER_INFO_ENC_ALGORITHM = 276
except:
    pass

# /opt/dockethead/include/ar.h: 4896
try:
    AR_SERVER_INFO_FIPS_MODE_INDEX = 277
except:
    pass

# /opt/dockethead/include/ar.h: 4897
try:
    AR_SERVER_INFO_FIPS_DUAL_MODE_INDEX = 278
except:
    pass

# /opt/dockethead/include/ar.h: 4898
try:
    AR_SERVER_INFO_ENC_LEVEL_INDEX = 279
except:
    pass

# /opt/dockethead/include/ar.h: 4899
try:
    AR_SERVER_INFO_DSO_MAIN_POLL_INTERVAL = 280
except:
    pass

# /opt/dockethead/include/ar.h: 4900
try:
    AR_SERVER_INFO_RECORD_OBJECT_RELS = 281
except:
    pass

# /opt/dockethead/include/ar.h: 4903
try:
    AR_SERVER_INFO_LICENSE_USAGE = 282
except:
    pass

# /opt/dockethead/include/ar.h: 4905
try:
    AR_SERVER_INFO_COMMON_LOG_FORM = 283
except:
    pass

# /opt/dockethead/include/ar.h: 4906
try:
    AR_SERVER_INFO_LOG_FORM_SELECTED = 284
except:
    pass

# /opt/dockethead/include/ar.h: 4909
try:
    AR_SERVER_INFO_MAX_CLIENT_MANAGED_TRANSACTIONS = 285
except:
    pass

# /opt/dockethead/include/ar.h: 4910
try:
    AR_SERVER_INFO_CLIENT_MANAGED_TRANSACTION_TIMEOUT = 286
except:
    pass

# /opt/dockethead/include/ar.h: 4913
try:
    AR_SERVER_INFO_OBJ_RESERVATION_MODE = 287
except:
    pass

# /opt/dockethead/include/ar.h: 4914
try:
    AR_SERVER_INFO_NEW_ENC_PUB_KEY_EXP = 288
except:
    pass

# /opt/dockethead/include/ar.h: 4915
try:
    AR_SERVER_INFO_NEW_ENC_DATA_KEY_EXP = 289
except:
    pass

# /opt/dockethead/include/ar.h: 4916
try:
    AR_SERVER_INFO_NEW_ENC_DATA_ALG = 290
except:
    pass

# /opt/dockethead/include/ar.h: 4917
try:
    AR_SERVER_INFO_NEW_ENC_SEC_POLICY = 291
except:
    pass

# /opt/dockethead/include/ar.h: 4918
try:
    AR_SERVER_INFO_NEW_FIPS_SERVER_MODE = 292
except:
    pass

# /opt/dockethead/include/ar.h: 4919
try:
    AR_SERVER_INFO_NEW_ENC_LEVEL = 293
except:
    pass

# /opt/dockethead/include/ar.h: 4920
try:
    AR_SERVER_INFO_NEW_ENC_ALGORITHM = 294
except:
    pass

# /opt/dockethead/include/ar.h: 4921
try:
    AR_SERVER_INFO_NEW_FIPS_MODE_INDEX = 295
except:
    pass

# /opt/dockethead/include/ar.h: 4922
try:
    AR_SERVER_INFO_NEW_ENC_LEVEL_INDEX = 296
except:
    pass

# /opt/dockethead/include/ar.h: 4923
try:
    AR_SERVER_INFO_NEW_ENC_PUB_KEY = 297
except:
    pass

# /opt/dockethead/include/ar.h: 4924
try:
    AR_SERVER_INFO_CUR_ENC_PUB_KEY = 298
except:
    pass

# /opt/dockethead/include/ar.h: 4925
try:
    AR_SERVER_INFO_NEW_ENC_PUB_KEY_INDEX = 299
except:
    pass

# /opt/dockethead/include/ar.h: 4927
try:
    AR_SERVER_INFO_CURRENT_ENC_SEC_POLICY = 300
except:
    pass

# /opt/dockethead/include/ar.h: 4928
try:
    AR_SERVER_INFO_ENC_LIBRARY_LEVEL = 301
except:
    pass

# /opt/dockethead/include/ar.h: 4929
try:
    AR_SERVER_INFO_NEW_FIPS_ALG = 302
except:
    pass

# /opt/dockethead/include/ar.h: 4930
try:
    AR_SERVER_INFO_FIPS_ALG = 303
except:
    pass

# /opt/dockethead/include/ar.h: 4931
try:
    AR_SERVER_INFO_FIPS_PUB_KEY = 304
except:
    pass

# /opt/dockethead/include/ar.h: 4932
try:
    AR_SERVER_INFO_WFD_QUEUES = 305
except:
    pass

# /opt/dockethead/include/ar.h: 4933
try:
    AR_SERVER_INFO_VERCNTL_OBJ_MOD_LOG_MODE = 306
except:
    pass

# /opt/dockethead/include/ar.h: 4934
try:
    AR_SERVER_INFO_MAX_RECURSION_LEVEL = 307
except:
    pass

# /opt/dockethead/include/ar.h: 4935
try:
    AR_SERVER_INFO_FT_SERVER_NAME = 308
except:
    pass

# /opt/dockethead/include/ar.h: 4936
try:
    AR_SERVER_INFO_FT_SERVER_PORT = 309
except:
    pass

# /opt/dockethead/include/ar.h: 4937
try:
    AR_SERVER_INFO_DISABLE_AUDIT_ONLY_CHANGED_FIELDS = 310
except:
    pass

# /opt/dockethead/include/ar.h: 4939
try:
    AR_SERVER_INFO_VERCNTL_OBJ_MOD_LOG_SAVE_DEF = 311
except:
    pass

# /opt/dockethead/include/ar.h: 4940
try:
    AR_SERVER_INFO_SG_AIE_STATE = 312
except:
    pass

# /opt/dockethead/include/ar.h: 4944
try:
    AR_SERVER_INFO_MAX_VENDOR_TEMP_TABLES = 313
except:
    pass

# /opt/dockethead/include/ar.h: 4946
try:
    AR_SERVER_INFO_DSO_LOG_LEVEL = 314
except:
    pass

# /opt/dockethead/include/ar.h: 4947
try:
    AR_SERVER_INFO_DS_PENDING_ERR = 315
except:
    pass

# /opt/dockethead/include/ar.h: 4948
try:
    AR_SERVER_INFO_REGISTRY_LOCATION = 316
except:
    pass

# /opt/dockethead/include/ar.h: 4949
try:
    AR_SERVER_INFO_REGISTRY_USER = 317
except:
    pass

# /opt/dockethead/include/ar.h: 4950
try:
    AR_SERVER_INFO_REGISTRY_PASSWORD = 318
except:
    pass

# /opt/dockethead/include/ar.h: 4951
try:
    AR_SERVER_INFO_DSO_LOG_ERR_FORM = 319
except:
    pass

# /opt/dockethead/include/ar.h: 4953
try:
    AR_SERVER_INFO_ARSIGNALD_LOG_FILE = 320
except:
    pass

# /opt/dockethead/include/ar.h: 4954
try:
    AR_SERVER_INFO_FIRE_ESCALATIONS = 321
except:
    pass

# /opt/dockethead/include/ar.h: 4955
try:
    AR_SERVER_INFO_PRELOAD_NUM_THREADS = 322
except:
    pass

# /opt/dockethead/include/ar.h: 4956
try:
    AR_SERVER_INFO_PRELOAD_NUM_SCHEMA_SEGS = 323
except:
    pass

# /opt/dockethead/include/ar.h: 4957
try:
    AR_SERVER_INFO_PRELOAD_THREAD_INIT_ONLY = 324
except:
    pass

# /opt/dockethead/include/ar.h: 4959
try:
    AR_SERVER_INFO_REG_ENDPOINT_CACHE_FLUSH = 325
except:
    pass

# /opt/dockethead/include/ar.h: 4961
try:
    AR_SERVER_INFO_CREATE_WKFLW_PLACEHOLDER = 326
except:
    pass

# /opt/dockethead/include/ar.h: 4971
try:
    AR_SERVER_INFO_MFS_TITLE_FIELD_WEIGHT = 327
except:
    pass

# /opt/dockethead/include/ar.h: 4972
try:
    AR_SERVER_INFO_MFS_ENVIRONMENT_FIELD_WEIGHT = 328
except:
    pass

# /opt/dockethead/include/ar.h: 4973
try:
    AR_SERVER_INFO_MFS_KEYWORDS_FIELD_WEIGHT = 329
except:
    pass

# /opt/dockethead/include/ar.h: 4974
try:
    AR_SERVER_INFO_COPY_CACHE_LOGGING = 330
except:
    pass

# /opt/dockethead/include/ar.h: 4975
try:
    AR_SERVER_INFO_DSO_SUPPRESS_NO_SUCH_ENTRY_FOR_DELETE = 331
except:
    pass

# /opt/dockethead/include/ar.h: 4977
try:
    AR_SERVER_INFO_USE_FTS_IN_WORKFLOW = 332
except:
    pass

# /opt/dockethead/include/ar.h: 4981
try:
    AR_SERVER_INFO_MAX_ATTACH_SIZE = 333
except:
    pass

# /opt/dockethead/include/ar.h: 4983
try:
    AR_SERVER_INFO_DISABLE_ARSIGNALS = 334
except:
    pass

# /opt/dockethead/include/ar.h: 4984
try:
    AR_SERVER_INFO_FT_SEARCH_THRESHOLD = 335
except:
    pass

# /opt/dockethead/include/ar.h: 4987
try:
    AR_SERVER_INFO_REQ_FIELD_IDENTIFIER = 336
except:
    pass

# /opt/dockethead/include/ar.h: 4988
try:
    AR_SERVER_INFO_REQ_FIELD_IDENTIFIER_LOCATION = 337
except:
    pass

# /opt/dockethead/include/ar.h: 4990
try:
    AR_SERVER_INFO_FT_SIGNAL_DELAY = 338
except:
    pass

# /opt/dockethead/include/ar.h: 4993
try:
    AR_SERVER_INFO_ATRIUM_SSO_AUTHENTICATION = 339
except:
    pass

# /opt/dockethead/include/ar.h: 4995
try:
    AR_SERVER_INFO_OVERLAY_MODE = 340
except:
    pass

# /opt/dockethead/include/ar.h: 4996
try:
    AR_SERVER_INFO_FT_FORM_REINDEX = 341
except:
    pass

# /opt/dockethead/include/ar.h: 4999
try:
    AR_SERVER_INFO_DS_LOGICAL_MAPPING = 342
except:
    pass

# /opt/dockethead/include/ar.h: 5000
try:
    AR_SERVER_INFO_DB_CONNECTION_TIMEOUT = 343
except:
    pass

# /opt/dockethead/include/ar.h: 5001
try:
    AR_SERVER_INFO_ATRIUMSSO_LOCATION = 344
except:
    pass

# /opt/dockethead/include/ar.h: 5002
try:
    AR_SERVER_INFO_ATRIUMSSO_USER = 345
except:
    pass

# /opt/dockethead/include/ar.h: 5003
try:
    AR_SERVER_INFO_ATRIUMSSO_PASSWORD = 346
except:
    pass

# /opt/dockethead/include/ar.h: 5004
try:
    AR_SERVER_INFO_SUPPRESS_DOMAIN_IN_URL = 347
except:
    pass

# /opt/dockethead/include/ar.h: 5005
try:
    AR_SERVER_INFO_RESTART_PLUGIN = 348
except:
    pass

# /opt/dockethead/include/ar.h: 5006
try:
    AR_SERVER_INFO_USE_PROMPT_BAR_FOR = 349
except:
    pass

# /opt/dockethead/include/ar.h: 5007
try:
    AR_SERVER_INFO_ATRIUMSSO_KEYSTORE_PATH = 350
except:
    pass

# /opt/dockethead/include/ar.h: 5008
try:
    AR_SERVER_INFO_ATRIUMSSO_KEYSTORE_PASSWORD = 351
except:
    pass

# /opt/dockethead/include/ar.h: 5009
try:
    AR_SERVER_INFO_MAX_LOG_HISTORY = 352
except:
    pass

# /opt/dockethead/include/ar.h: 5010
try:
    AR_SERVER_INFO_SUPRESS_LOGOFF_SIGNALS = 353
except:
    pass

# /opt/dockethead/include/ar.h: 5011
try:
    AR_SERVER_INFO_DB_FUNCTIONAL_INDEX = 354
except:
    pass

# /opt/dockethead/include/ar.h: 5014
try:
    AR_SERVER_INFO_UPGRADE_MODE = 355
except:
    pass

# /opt/dockethead/include/ar.h: 5015
try:
    AR_SERVER_INFO_UPGRADE_RESERVED = 356
except:
    pass

# /opt/dockethead/include/ar.h: 5016
try:
    AR_SERVER_INFO_UPGRADE_ADMIN_USER = 357
except:
    pass

# /opt/dockethead/include/ar.h: 5017
try:
    AR_SERVER_INFO_UPGRADE_DUAL_DATA_FORMS = 358
except:
    pass

# /opt/dockethead/include/ar.h: 5021
try:
    AR_SERVER_INFO_API_MONITORING_UPDATE_INTERVAL = 380
except:
    pass

# /opt/dockethead/include/ar.h: 5022
try:
    AR_SERVER_INFO_API_RECORDING_CLIENT_TYPE = 381
except:
    pass

# /opt/dockethead/include/ar.h: 5023
try:
    AR_SERVER_INFO_API_RECORDING_ENABLE = 382
except:
    pass

# /opt/dockethead/include/ar.h: 5026
try:
    AR_SERVER_INFO_OBJ_RESERVATION_REPOSITORY_TYPE = 383
except:
    pass

# /opt/dockethead/include/ar.h: 5030
try:
    AR_SERVER_INFO_STATS_APISQL_CONTROL = 384
except:
    pass

# /opt/dockethead/include/ar.h: 5031
try:
    AR_SERVER_INFO_STATS_APISQL_MAX_SAVED = 386
except:
    pass

# /opt/dockethead/include/ar.h: 5032
try:
    AR_SERVER_INFO_STATS_APISQL_INTERVAL = 387
except:
    pass

# /opt/dockethead/include/ar.h: 5033
try:
    AR_SERVER_INFO_STATS_APISQL_MIN_TIME = 388
except:
    pass

# /opt/dockethead/include/ar.h: 5034
try:
    AR_SERVER_INFO_STATS_GET_INCOMPLETE_API = 389
except:
    pass

# /opt/dockethead/include/ar.h: 5035
try:
    AR_SERVER_INFO_STATS_GET_LONGEST_API = 390
except:
    pass

# /opt/dockethead/include/ar.h: 5036
try:
    AR_SERVER_INFO_STATS_GET_INCOMPLETE_SQL = 391
except:
    pass

# /opt/dockethead/include/ar.h: 5037
try:
    AR_SERVER_INFO_STATS_GET_LONGEST_SQL = 392
except:
    pass

# /opt/dockethead/include/ar.h: 5039
try:
    AR_SERVER_INFO_ATTACH_EXT_FILTER = 393
except:
    pass

# /opt/dockethead/include/ar.h: 5040
try:
    AR_SERVER_INFO_ATTACH_EXT_LIST = 394
except:
    pass

# /opt/dockethead/include/ar.h: 5041
try:
    AR_SERVER_INFO_ATTACH_EXCEPTION_LIST = 395
except:
    pass

# /opt/dockethead/include/ar.h: 5042
try:
    AR_SERVER_INFO_ATTACH_DISPLAY_FILTER = 396
except:
    pass

# /opt/dockethead/include/ar.h: 5043
try:
    AR_SERVER_INFO_ATTACH_DISPLAY_LIST = 397
except:
    pass

# /opt/dockethead/include/ar.h: 5044
try:
    AR_SERVER_INFO_ATTACH_VALIDATION_PLUGIN_NAME = 398
except:
    pass

# /opt/dockethead/include/ar.h: 5045
try:
    AR_SERVER_INFO_ATTACH_SYSTEM_EXCEPTION_LIST = 401
except:
    pass

# /opt/dockethead/include/ar.h: 5047
try:
    AR_MAX_SERVER_INFO_USED = 401
except:
    pass

# /opt/dockethead/include/ar.h: 5050
try:
    TRACK_LICENSE_USAGE_DISABLED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5051
try:
    TRACK_LICENSE_USAGE_WRITE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5052
try:
    TRACK_LICENSE_USAGE_ALL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5055
try:
    NORMAL_TO_INPROCESS_UPGRADE_MODE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5056
try:
    INPROCESS_TO_COMPLETE_UPGRADE_MODE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5057
try:
    COMPLETE_TO_NORMAL_UPGRADE_MODE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5059
try:
    ROLLBACK_INPROCESS_TO_NORMAL_UPGRADE_MODE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5061
try:
    UPGRADE_MODE_NORMAL_OPERATION = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5062
try:
    UPGRADE_MODE_INPROCESS = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5063
try:
    UPGRADE_MODE_COMPLETED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5065
try:
    AR_DEBUG_SERVER_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5066
try:
    AR_DEBUG_SERVER_SQL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5067
try:
    AR_DEBUG_SERVER_FILTER = (1 << 1)
except:
    pass

# /opt/dockethead/include/ar.h: 5068
try:
    AR_DEBUG_SERVER_USER = (1 << 2)
except:
    pass

# /opt/dockethead/include/ar.h: 5069
try:
    AR_DEBUG_SERVER_ESCALATION = (1 << 3)
except:
    pass

# /opt/dockethead/include/ar.h: 5070
try:
    AR_DEBUG_SERVER_API = (1 << 4)
except:
    pass

# /opt/dockethead/include/ar.h: 5071
try:
    AR_DEBUG_THREAD = (1 << 5)
except:
    pass

# /opt/dockethead/include/ar.h: 5072
try:
    AR_DEBUG_SERVER_ALERT = (1 << 6)
except:
    pass

# /opt/dockethead/include/ar.h: 5073
try:
    AR_DEBUG_SERVER_ARFORK = (1 << 7)
except:
    pass

# /opt/dockethead/include/ar.h: 5074
try:
    AR_DEBUG_SERVER_SERVGROUP = (1 << 8)
except:
    pass

# /opt/dockethead/include/ar.h: 5075
try:
    AR_DEBUG_SERVER_FTINDEXER = (1 << 9)
except:
    pass

# /opt/dockethead/include/ar.h: 5076
try:
    AR_DEBUG_SERVER_DISTRIB = (1 << 15)
except:
    pass

# /opt/dockethead/include/ar.h: 5077
try:
    AR_DEBUG_SERVER_APPROVAL = (1 << 16)
except:
    pass

# /opt/dockethead/include/ar.h: 5078
try:
    AR_DEBUG_SERVER_PLUGIN = (1 << 17)
except:
    pass

# /opt/dockethead/include/ar.h: 5079
try:
    AR_DEBUG_SERVER_EXTLOG = (1 << 18)
except:
    pass

# /opt/dockethead/include/ar.h: 5080
try:
    AR_DEBUG_SERVER_CHECKDB = (1 << 19)
except:
    pass

# /opt/dockethead/include/ar.h: 5081
try:
    AR_DEBUG_SERVER_ARSIGNALD = (1 << 20)
except:
    pass

# /opt/dockethead/include/ar.h: 5083
try:
    NUM_DEBUG_FLAGS = 15
except:
    pass

# /opt/dockethead/include/ar.h: 5101
try:
    NUM_SERVER_DEBUG_TYPES = 9
except:
    pass

# /opt/dockethead/include/ar.h: 5105
try:
    PER_THREAD_LOG_TYPES = ((((((AR_DEBUG_SERVER_SQL | AR_DEBUG_SERVER_FILTER) | AR_DEBUG_SERVER_USER) | AR_DEBUG_SERVER_ESCALATION) | AR_DEBUG_SERVER_API) | AR_DEBUG_SERVER_ALERT) | AR_DEBUG_SERVER_FTINDEXER)
except:
    pass

# /opt/dockethead/include/ar.h: 5114
try:
    AR_LOG_TO_FORM_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5115
try:
    AR_LOG_TO_FORM_SQL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5116
try:
    AR_LOG_TO_FORM_FILTER = (1 << 1)
except:
    pass

# /opt/dockethead/include/ar.h: 5117
try:
    AR_LOG_TO_FORM_USER = (1 << 2)
except:
    pass

# /opt/dockethead/include/ar.h: 5118
try:
    AR_LOG_TO_FORM_ESCALATION = (1 << 3)
except:
    pass

# /opt/dockethead/include/ar.h: 5119
try:
    AR_LOG_TO_FORM_API = (1 << 4)
except:
    pass

# /opt/dockethead/include/ar.h: 5120
try:
    AR_LOG_TO_FORM_THREAD = (1 << 5)
except:
    pass

# /opt/dockethead/include/ar.h: 5121
try:
    AR_LOG_TO_FORM_ALERT = (1 << 6)
except:
    pass

# /opt/dockethead/include/ar.h: 5122
try:
    AR_LOG_TO_FORM_SERVGROUP = (1 << 8)
except:
    pass

# /opt/dockethead/include/ar.h: 5123
try:
    AR_LOG_TO_FORM_FTINDEXER = (1 << 9)
except:
    pass

# /opt/dockethead/include/ar.h: 5127
try:
    AR_PLUGIN_LOG_OFF = 10000
except:
    pass

# /opt/dockethead/include/ar.h: 5128
try:
    AR_PLUGIN_LOG_SEVERE = 1000
except:
    pass

# /opt/dockethead/include/ar.h: 5129
try:
    AR_PLUGIN_LOG_WARNING = 900
except:
    pass

# /opt/dockethead/include/ar.h: 5130
try:
    AR_PLUGIN_LOG_INFO = 800
except:
    pass

# /opt/dockethead/include/ar.h: 5131
try:
    AR_PLUGIN_LOG_CONFIG = 700
except:
    pass

# /opt/dockethead/include/ar.h: 5132
try:
    AR_PLUGIN_LOG_FINE = 600
except:
    pass

# /opt/dockethead/include/ar.h: 5133
try:
    AR_PLUGIN_LOG_FINER = 500
except:
    pass

# /opt/dockethead/include/ar.h: 5134
try:
    AR_PLUGIN_LOG_FINEST = 400
except:
    pass

# /opt/dockethead/include/ar.h: 5135
try:
    AR_PLUGIN_LOG_ALL = 100
except:
    pass

# /opt/dockethead/include/ar.h: 5137
try:
    AR_SUBMITTER_MODE_LOCKED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5138
try:
    AR_SUBMITTER_MODE_CHANGEABLE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5140
try:
    AR_SAVE_LOGIN_USER_OPTION = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5141
try:
    AR_SAVE_LOGIN_ADMIN_SAVE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5142
try:
    AR_SAVE_LOGIN_ADMIN_NO_SAVE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5144
try:
    AR_SYS_MSG_DISP_NOTE_AND_WARN = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5145
try:
    AR_SYS_MSG_DISP_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5146
try:
    AR_SYS_MSG_DISP_NONE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5148
try:
    AR_CASE_SENSITIVE_UNKNOWN = (-1)
except:
    pass

# /opt/dockethead/include/ar.h: 5149
try:
    AR_CASE_SENSITIVE_YES = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5150
try:
    AR_CASE_SENSITIVE_NO = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5153
try:
    AR_PREF_SERVER_USER_OPTION = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5154
try:
    AR_PREF_SERVER_USE_THIS_SERVER = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5155
try:
    AR_PREF_SERVER_USE_NOT_THIS_SERVER = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5163
try:
    AR_SERVER_STAT_START_TIME = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5164
try:
    AR_SERVER_STAT_BAD_PASSWORD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5165
try:
    AR_SERVER_STAT_NO_WRITE_TOKEN = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5167
try:
    AR_SERVER_STAT_NO_FULL_TOKEN = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5169
try:
    AR_SERVER_STAT_CURRENT_USERS = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5170
try:
    AR_SERVER_STAT_WRITE_FIXED = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5171
try:
    AR_SERVER_STAT_WRITE_FLOATING = 7
except:
    pass

# /opt/dockethead/include/ar.h: 5172
try:
    AR_SERVER_STAT_WRITE_READ = 8
except:
    pass

# /opt/dockethead/include/ar.h: 5173
try:
    AR_SERVER_STAT_FULL_FIXED = 9
except:
    pass

# /opt/dockethead/include/ar.h: 5174
try:
    AR_SERVER_STAT_FULL_FLOATING = 10
except:
    pass

# /opt/dockethead/include/ar.h: 5175
try:
    AR_SERVER_STAT_FULL_NONE = 11
except:
    pass

# /opt/dockethead/include/ar.h: 5176
try:
    AR_SERVER_STAT_API_REQUESTS = 12
except:
    pass

# /opt/dockethead/include/ar.h: 5177
try:
    AR_SERVER_STAT_API_TIME = 13
except:
    pass

# /opt/dockethead/include/ar.h: 5178
try:
    AR_SERVER_STAT_ENTRY_TIME = 14
except:
    pass

# /opt/dockethead/include/ar.h: 5179
try:
    AR_SERVER_STAT_RESTRUCT_TIME = 15
except:
    pass

# /opt/dockethead/include/ar.h: 5180
try:
    AR_SERVER_STAT_OTHER_TIME = 16
except:
    pass

# /opt/dockethead/include/ar.h: 5182
try:
    AR_SERVER_STAT_CACHE_TIME = 17
except:
    pass

# /opt/dockethead/include/ar.h: 5184
try:
    AR_SERVER_STAT_GET_E_COUNT = 18
except:
    pass

# /opt/dockethead/include/ar.h: 5185
try:
    AR_SERVER_STAT_GET_E_TIME = 19
except:
    pass

# /opt/dockethead/include/ar.h: 5186
try:
    AR_SERVER_STAT_SET_E_COUNT = 20
except:
    pass

# /opt/dockethead/include/ar.h: 5187
try:
    AR_SERVER_STAT_SET_E_TIME = 21
except:
    pass

# /opt/dockethead/include/ar.h: 5188
try:
    AR_SERVER_STAT_CREATE_E_COUNT = 22
except:
    pass

# /opt/dockethead/include/ar.h: 5189
try:
    AR_SERVER_STAT_CREATE_E_TIME = 23
except:
    pass

# /opt/dockethead/include/ar.h: 5190
try:
    AR_SERVER_STAT_DELETE_E_COUNT = 24
except:
    pass

# /opt/dockethead/include/ar.h: 5191
try:
    AR_SERVER_STAT_DELETE_E_TIME = 25
except:
    pass

# /opt/dockethead/include/ar.h: 5192
try:
    AR_SERVER_STAT_MERGE_E_COUNT = 26
except:
    pass

# /opt/dockethead/include/ar.h: 5193
try:
    AR_SERVER_STAT_MERGE_E_TIME = 27
except:
    pass

# /opt/dockethead/include/ar.h: 5194
try:
    AR_SERVER_STAT_GETLIST_E_COUNT = 28
except:
    pass

# /opt/dockethead/include/ar.h: 5195
try:
    AR_SERVER_STAT_GETLIST_E_TIME = 29
except:
    pass

# /opt/dockethead/include/ar.h: 5196
try:
    AR_SERVER_STAT_E_STATS_COUNT = 30
except:
    pass

# /opt/dockethead/include/ar.h: 5197
try:
    AR_SERVER_STAT_E_STATS_TIME = 31
except:
    pass

# /opt/dockethead/include/ar.h: 5198
try:
    AR_SERVER_STAT_FILTER_PASSED = 32
except:
    pass

# /opt/dockethead/include/ar.h: 5199
try:
    AR_SERVER_STAT_FILTER_FAILED = 33
except:
    pass

# /opt/dockethead/include/ar.h: 5201
try:
    AR_SERVER_STAT_FILTER_DISABLE = 34
except:
    pass

# /opt/dockethead/include/ar.h: 5203
try:
    AR_SERVER_STAT_FILTER_NOTIFY = 35
except:
    pass

# /opt/dockethead/include/ar.h: 5204
try:
    AR_SERVER_STAT_FILTER_MESSAGE = 36
except:
    pass

# /opt/dockethead/include/ar.h: 5205
try:
    AR_SERVER_STAT_FILTER_LOG = 37
except:
    pass

# /opt/dockethead/include/ar.h: 5206
try:
    AR_SERVER_STAT_FILTER_FIELDS = 38
except:
    pass

# /opt/dockethead/include/ar.h: 5207
try:
    AR_SERVER_STAT_FILTER_PROCESS = 39
except:
    pass

# /opt/dockethead/include/ar.h: 5208
try:
    AR_SERVER_STAT_FILTER_TIME = 40
except:
    pass

# /opt/dockethead/include/ar.h: 5210
try:
    AR_SERVER_STAT_ESCL_PASSED = 41
except:
    pass

# /opt/dockethead/include/ar.h: 5211
try:
    AR_SERVER_STAT_ESCL_FAILED = 42
except:
    pass

# /opt/dockethead/include/ar.h: 5213
try:
    AR_SERVER_STAT_ESCL_DISABLE = 43
except:
    pass

# /opt/dockethead/include/ar.h: 5215
try:
    AR_SERVER_STAT_ESCL_NOTIFY = 44
except:
    pass

# /opt/dockethead/include/ar.h: 5216
try:
    AR_SERVER_STAT_ESCL_LOG = 45
except:
    pass

# /opt/dockethead/include/ar.h: 5217
try:
    AR_SERVER_STAT_ESCL_FIELDS = 46
except:
    pass

# /opt/dockethead/include/ar.h: 5218
try:
    AR_SERVER_STAT_ESCL_PROCESS = 47
except:
    pass

# /opt/dockethead/include/ar.h: 5219
try:
    AR_SERVER_STAT_ESCL_TIME = 48
except:
    pass

# /opt/dockethead/include/ar.h: 5221
try:
    AR_SERVER_STAT_TIMES_BLOCKED = 49
except:
    pass

# /opt/dockethead/include/ar.h: 5223
try:
    AR_SERVER_STAT_NUMBER_BLOCKED = 50
except:
    pass

# /opt/dockethead/include/ar.h: 5225
try:
    AR_SERVER_STAT_CPU = 51
except:
    pass

# /opt/dockethead/include/ar.h: 5227
try:
    AR_SERVER_STAT_SQL_DB_COUNT = 52
except:
    pass

# /opt/dockethead/include/ar.h: 5228
try:
    AR_SERVER_STAT_SQL_DB_TIME = 53
except:
    pass

# /opt/dockethead/include/ar.h: 5229
try:
    AR_SERVER_STAT_FTS_SRCH_COUNT = 54
except:
    pass

# /opt/dockethead/include/ar.h: 5230
try:
    AR_SERVER_STAT_FTS_SRCH_TIME = 55
except:
    pass

# /opt/dockethead/include/ar.h: 5231
try:
    AR_SERVER_STAT_SINCE_START = 56
except:
    pass

# /opt/dockethead/include/ar.h: 5232
try:
    AR_SERVER_STAT_IDLE_TIME = 57
except:
    pass

# /opt/dockethead/include/ar.h: 5233
try:
    AR_SERVER_STAT_NET_RESP_TIME = 58
except:
    pass

# /opt/dockethead/include/ar.h: 5235
try:
    AR_SERVER_STAT_FILTER_FIELDP = 59
except:
    pass

# /opt/dockethead/include/ar.h: 5236
try:
    AR_SERVER_STAT_ESCL_FIELDP = 60
except:
    pass

# /opt/dockethead/include/ar.h: 5237
try:
    AR_SERVER_STAT_FILTER_SQL = 61
except:
    pass

# /opt/dockethead/include/ar.h: 5238
try:
    AR_SERVER_STAT_ESCL_SQL = 62
except:
    pass

# /opt/dockethead/include/ar.h: 5239
try:
    AR_SERVER_STAT_NUM_THREADS = 63
except:
    pass

# /opt/dockethead/include/ar.h: 5240
try:
    AR_SERVER_STAT_FILTER_GOTO_ACTION = 64
except:
    pass

# /opt/dockethead/include/ar.h: 5241
try:
    AR_SERVER_STAT_FILTER_CALL_GUIDE = 65
except:
    pass

# /opt/dockethead/include/ar.h: 5242
try:
    AR_SERVER_STAT_FILTER_EXIT_GUIDE = 66
except:
    pass

# /opt/dockethead/include/ar.h: 5243
try:
    AR_SERVER_STAT_FILTER_GOTO_GUIDE_LB = 67
except:
    pass

# /opt/dockethead/include/ar.h: 5245
try:
    AR_SERVER_STAT_FILTER_FIELDS_SQL = 68
except:
    pass

# /opt/dockethead/include/ar.h: 5247
try:
    AR_SERVER_STAT_FILTER_FIELDS_PROCESS = 69
except:
    pass

# /opt/dockethead/include/ar.h: 5249
try:
    AR_SERVER_STAT_FILTER_FIELDS_FLTAPI = 70
except:
    pass

# /opt/dockethead/include/ar.h: 5251
try:
    AR_SERVER_STAT_ESCL_FIELDS_SQL = 71
except:
    pass

# /opt/dockethead/include/ar.h: 5253
try:
    AR_SERVER_STAT_ESCL_FIELDS_PROCESS = 72
except:
    pass

# /opt/dockethead/include/ar.h: 5255
try:
    AR_SERVER_STAT_ESCL_FIELDS_FLTAPI = 73
except:
    pass

# /opt/dockethead/include/ar.h: 5257
try:
    AR_SERVER_STAT_WRITE_RESTRICTED_READ = 74
except:
    pass

# /opt/dockethead/include/ar.h: 5259
try:
    AR_SERVER_STAT_NUM_CACHES = 75
except:
    pass

# /opt/dockethead/include/ar.h: 5260
try:
    AR_SERVER_STAT_MAX_CACHES = 76
except:
    pass

# /opt/dockethead/include/ar.h: 5262
try:
    AR_MAX_SERVER_STAT_USED = 76
except:
    pass

# /opt/dockethead/include/ar.h: 5287
try:
    AR_FULLTEXT_REINDEX = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5293
try:
    AR_FULL_TEXT_SEARCH_CASE_SENSITIVE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5294
try:
    AR_FULL_TEXT_SEARCH_CASE_INSENSITIVE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5296
try:
    AR_FULL_TEXT_DISABLE_SEARCHING = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5297
try:
    AR_FULL_TEXT_ENABLE_SEARCHING = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5299
try:
    AR_FULLTEXT_FTS_MATCH_FORCE_L_T_WILD = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5301
try:
    AR_FULLTEXT_FTS_MATCH_FORCE_T_WILD = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5302
try:
    AR_FULLTEXT_FTS_MATCH_IGNORE_L_WILD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5303
try:
    AR_FULLTEXT_FTS_MATCH_REMOVE_WILD = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5304
try:
    AR_FULLTEXT_FTS_MATCH_UNCHANGED = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5306
try:
    AR_FULL_TEXT_FORM_REINDEX_SEPARATOR = '\\f'
except:
    pass

# /opt/dockethead/include/ar.h: 5311
try:
    AR_FULLTEXTINFO_COLLECTION_DIR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5312
try:
    AR_FULLTEXTINFO_STOPWORD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5313
try:
    AR_FULLTEXTINFO_REINDEX = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5314
try:
    AR_FULLTEXTINFO_CASE_SENSITIVE_SRCH = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5315
try:
    AR_FULLTEXTINFO_STATE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5316
try:
    AR_FULLTEXTINFO_FTS_MATCH_OP = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5317
try:
    AR_FULLTEXTINFO_HOMEDIR = 7
except:
    pass

# /opt/dockethead/include/ar.h: 5318
try:
    AR_FULLTEXTINFO_DEBUG = 8
except:
    pass

# /opt/dockethead/include/ar.h: 5319
try:
    AR_FULLTEXTINFO_TEMP_DIR = 9
except:
    pass

# /opt/dockethead/include/ar.h: 5321
try:
    AR_MAX_FULLTEXT_INFO_USED = 9
except:
    pass

# /opt/dockethead/include/ar.h: 5324
try:
    AR_CASE_SENSITIVE_SEARCH = AR_FULL_TEXT_SEARCH_CASE_SENSITIVE
except:
    pass

# /opt/dockethead/include/ar.h: 5325
try:
    AR_CASE_INSENSITIVE_SEARCH = AR_FULL_TEXT_SEARCH_CASE_INSENSITIVE
except:
    pass

# /opt/dockethead/include/ar.h: 5328
try:
    AR_FULLTEXT_STATE_OFF = AR_FULL_TEXT_DISABLE_SEARCHING
except:
    pass

# /opt/dockethead/include/ar.h: 5329
try:
    AR_FULLTEXT_STATE_ON = AR_FULL_TEXT_ENABLE_SEARCHING
except:
    pass

# /opt/dockethead/include/ar.h: 5398
def AR_DAY(x, y):
    return ((x >> y) & 1)

# /opt/dockethead/include/ar.h: 5399
def AR_HOUR(x, y):
    return ((x >> y) & 1)

# /opt/dockethead/include/ar.h: 5400
def AR_SETDAY(x):
    return (1 << x)

# /opt/dockethead/include/ar.h: 5401
def AR_SETHOUR(x):
    return (1 << x)

# /opt/dockethead/include/ar.h: 5402
try:
    AR_HOUR_A_DAY = 24
except:
    pass

# /opt/dockethead/include/ar.h: 5403
try:
    AR_TIMEMARK_ALL = (-1)
except:
    pass

# /opt/dockethead/include/ar.h: 5404
try:
    AR_TIMEMARK_NOTFOUND = (-1)
except:
    pass

# /opt/dockethead/include/ar.h: 5405
try:
    AR_TIMEMARK_END_OF_MONTH = 31
except:
    pass

# /opt/dockethead/include/ar.h: 5408
try:
    AR_ESCALATION_TYPE_INTERVAL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5409
try:
    AR_ESCALATION_TYPE_TIMEMARK = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5430
try:
    AR_LONGVALUE_TYPE_HELPTEXT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5431
try:
    AR_LONGVALUE_TYPE_CHANGEDIARY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5434
try:
    AR_FIELD_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5435
try:
    AR_FIELD_REGULAR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5436
try:
    AR_FIELD_JOIN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5437
try:
    AR_FIELD_VIEW = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5438
try:
    AR_FIELD_VENDOR = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5439
try:
    AR_FIELD_INHERITANCE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5441
try:
    AR_FIELD_CLEAN_DELETE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5444
try:
    AR_FIELD_DATA_DELETE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5446
try:
    AR_FIELD_FORCE_DELETE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5450
try:
    AR_FIELD_MAPPING_PRIMARY = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5451
try:
    AR_FIELD_MAPPING_SECONDARY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5516
try:
    AR_SCHEMA_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5517
try:
    AR_SCHEMA_REGULAR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5518
try:
    AR_SCHEMA_JOIN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5519
try:
    AR_SCHEMA_VIEW = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5520
try:
    AR_SCHEMA_DIALOG = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5521
try:
    AR_SCHEMA_VENDOR = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5522
try:
    AR_SCHEMA_PLACEHOLDER = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5523
try:
    AR_SCHEMA_MAX_SCHEMA_TYPE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5525
try:
    AR_LIST_SCHEMA_ALL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5526
try:
    AR_LIST_SCHEMA_REGULAR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5527
try:
    AR_LIST_SCHEMA_JOIN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5528
try:
    AR_LIST_SCHEMA_VIEW = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5529
try:
    AR_LIST_SCHEMA_UPLINK = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5531
try:
    AR_LIST_SCHEMA_DOWNLINK = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5533
try:
    AR_LIST_SCHEMA_DIALOG = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5534
try:
    AR_LIST_SCHEMA_ALL_WITH_DATA = 7
except:
    pass

# /opt/dockethead/include/ar.h: 5536
try:
    AR_LIST_SCHEMA_VENDOR = 8
except:
    pass

# /opt/dockethead/include/ar.h: 5537
try:
    AR_LIST_SCHEMA_ALLOWED_IN_MFSEARCH = 9
except:
    pass

# /opt/dockethead/include/ar.h: 5540
try:
    AR_HIDDEN_INCREMENT = 1024
except:
    pass

# /opt/dockethead/include/ar.h: 5543
try:
    AR_JOIN_LEVEL_ORDER = 2048
except:
    pass

# /opt/dockethead/include/ar.h: 5546
try:
    AR_ATTRIB_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5548
try:
    AR_ATTRIB_VISIBLE = AR_ATTRIB_NONE
except:
    pass

# /opt/dockethead/include/ar.h: 5549
try:
    AR_ATTRIB_HIDDEN = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5552
try:
    AR_JOIN_OPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5553
try:
    AR_JOIN_OPTION_OUTER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5556
try:
    AR_JOIN_SETOPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5558
try:
    AR_JOIN_SETOPTION_REF = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5560
try:
    ARI_WF_DEFERRED_CREATE_MODE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5563
try:
    ARI_WF_SETOPTION_OW = 1024
except:
    pass

# /opt/dockethead/include/ar.h: 5567
try:
    AR_JOIN_DELOPTION_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5570
try:
    AR_JOIN_DELOPTION_FORCE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5576
try:
    AR_DEFAULT_DELETE_OPTION = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5579
try:
    AR_SCHEMA_CLEAN_DELETE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5584
try:
    AR_SCHEMA_DATA_DELETE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5586
try:
    AR_SCHEMA_FORCE_DELETE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5589
try:
    AR_LOCK_BLOCK_DELETE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5592
try:
    AR_SCHEMA_SHADOW_DELETE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 5596
try:
    AR_SCHEMA_SET_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5598
try:
    AR_SCHEMA_SET_DELETE_FIELDS_WITH_MAPPING = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5602
try:
    AR_SCHEMA_SET_DELETE_CONFLICTING_FIELDS = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5693
try:
    AR_SUPPORT_FILE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5694
try:
    AR_SUPPORT_FILE_EXTERNAL_REPORT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5733
try:
    AR_DISPLAY_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5734
try:
    AR_DISPLAY_TYPE_TEXT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5735
try:
    AR_DISPLAY_TYPE_NUMTEXT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5736
try:
    AR_DISPLAY_TYPE_CHECKBOX = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5737
try:
    AR_DISPLAY_TYPE_CHOICE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5738
try:
    AR_DISPLAY_TYPE_BUTTON = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5739
try:
    AR_DISPLAY_TYPE_TRIM = 7
except:
    pass

# /opt/dockethead/include/ar.h: 5741
try:
    AR_DISPLAY_OPT_VISIBLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5742
try:
    AR_DISPLAY_OPT_HIDDEN = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5745
try:
    AR_DISPLAY_LABEL_LEFT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5746
try:
    AR_DISPLAY_LABEL_TOP = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5773
try:
    ARCON_ALL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5774
try:
    ARCON_GUIDE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5775
try:
    ARCON_APP = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5776
try:
    ARCON_PACK = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5777
try:
    ARCON_FILTER_GUIDE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5778
try:
    ARCON_WEBSERVICE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5779
try:
    ARCON_LAST_RESERVED = 65535
except:
    pass

# /opt/dockethead/include/ar.h: 5782
try:
    ARREF_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5783
try:
    ARREF_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5784
try:
    ARREF_SCHEMA = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5785
try:
    ARREF_FILTER = 3
except:
    pass

# /opt/dockethead/include/ar.h: 5786
try:
    ARREF_ESCALATION = 4
except:
    pass

# /opt/dockethead/include/ar.h: 5787
try:
    ARREF_ACTLINK = 5
except:
    pass

# /opt/dockethead/include/ar.h: 5788
try:
    ARREF_CONTAINER = 6
except:
    pass

# /opt/dockethead/include/ar.h: 5789
try:
    ARREF_CHAR_MENU = 7
except:
    pass

# /opt/dockethead/include/ar.h: 5790
try:
    ARREF_IMAGE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 5791
try:
    ARREF_TASK = 9
except:
    pass

# /opt/dockethead/include/ar.h: 5792
try:
    ARREF_LAST_SERVER_OBJ = 32767
except:
    pass

# /opt/dockethead/include/ar.h: 5796
try:
    ARREF_ICON = 32768
except:
    pass

# /opt/dockethead/include/ar.h: 5797
try:
    ARREF_SMALL_ICON = 32769
except:
    pass

# /opt/dockethead/include/ar.h: 5798
try:
    ARREF_MAXIMIZE_FORMS = 32770
except:
    pass

# /opt/dockethead/include/ar.h: 5800
try:
    ARREF_APPLICATION_FORMS = 32771
except:
    pass

# /opt/dockethead/include/ar.h: 5804
try:
    ARREF_ABOUT_BOX_IMAGE = 32772
except:
    pass

# /opt/dockethead/include/ar.h: 5805
try:
    ARREF_ABOUT_BOX_FORM = 32773
except:
    pass

# /opt/dockethead/include/ar.h: 5807
try:
    ARREF_NULL_STRING = 32774
except:
    pass

# /opt/dockethead/include/ar.h: 5808
try:
    ARREF_APPLICATION_HELP_EXT = 32775
except:
    pass

# /opt/dockethead/include/ar.h: 5810
try:
    ARREF_APPLICATION_HELP_FILE = 32776
except:
    pass

# /opt/dockethead/include/ar.h: 5812
try:
    ARREF_APPLICATION_PRIMARY_FORM = 32777
except:
    pass

# /opt/dockethead/include/ar.h: 5814
try:
    ARREF_APPLICATION_FORM_VUI = 32778
except:
    pass

# /opt/dockethead/include/ar.h: 5816
try:
    ARREF_APPLICATION_DISABLE_BEGIN_TASK = 32779
except:
    pass

# /opt/dockethead/include/ar.h: 5819
try:
    ARREF_APPLICATION_HELP_INDEX_EXT = 32780
except:
    pass

# /opt/dockethead/include/ar.h: 5822
try:
    ARREF_APPLICATION_HELP_INDEX_FILE = 32781
except:
    pass

# /opt/dockethead/include/ar.h: 5825
try:
    ARREF_APPLICATION_HELP_FILE_NAME = 32782
except:
    pass

# /opt/dockethead/include/ar.h: 5828
try:
    ARREF_PACKINGLIST_GUIDE = 32783
except:
    pass

# /opt/dockethead/include/ar.h: 5830
try:
    ARREF_PACKINGLIST_APP = 32784
except:
    pass

# /opt/dockethead/include/ar.h: 5832
try:
    ARREF_PACKINGLIST_PACK = 32785
except:
    pass

# /opt/dockethead/include/ar.h: 5834
try:
    ARREF_GROUP_DATA = 32786
except:
    pass

# /opt/dockethead/include/ar.h: 5837
try:
    ARREF_DISTMAPPING_DATA = 32787
except:
    pass

# /opt/dockethead/include/ar.h: 5840
try:
    ARREF_APPLICATION_HAS_EXT_HELP = 32788
except:
    pass

# /opt/dockethead/include/ar.h: 5842
try:
    ARREF_APPLICATION_SUPPORT_FILES = 32789
except:
    pass

# /opt/dockethead/include/ar.h: 5844
try:
    ARREF_PACKINGLIST_DSOPOOL = 32792
except:
    pass

# /opt/dockethead/include/ar.h: 5847
try:
    ARREF_PACKINGLIST_FILTER_GUIDE = 32793
except:
    pass

# /opt/dockethead/include/ar.h: 5849
try:
    ARREF_FLASH_BOARD_DEF = 32794
except:
    pass

# /opt/dockethead/include/ar.h: 5850
try:
    ARREF_FLASH_DATA_SOURCE_DEF = 32795
except:
    pass

# /opt/dockethead/include/ar.h: 5851
try:
    ARREF_FLASH_VARIABLE_DEF = 32796
except:
    pass

# /opt/dockethead/include/ar.h: 5852
try:
    ARREF_WS_PROPERTIES = 32797
except:
    pass

# /opt/dockethead/include/ar.h: 5854
try:
    ARREF_WS_OPERATION = 32798
except:
    pass

# /opt/dockethead/include/ar.h: 5857
try:
    ARREF_WS_ARXML_MAPPING = 32799
except:
    pass

# /opt/dockethead/include/ar.h: 5860
try:
    ARREF_WS_WSDL = 32800
except:
    pass

# /opt/dockethead/include/ar.h: 5861
try:
    ARREF_PACKINGLIST_WEBSERVICE = 32801
except:
    pass

# /opt/dockethead/include/ar.h: 5863
try:
    ARREF_WS_PUBLISHING_LOC = 32802
except:
    pass

# /opt/dockethead/include/ar.h: 5865
try:
    ARREF_APPLICATION_HELP_FILE_NAME2 = 32803
except:
    pass

# /opt/dockethead/include/ar.h: 5868
try:
    ARREF_APPLICATION_HELP_EXT2 = 32804
except:
    pass

# /opt/dockethead/include/ar.h: 5870
try:
    ARREF_APPLICATION_HELP_FILE2 = 32805
except:
    pass

# /opt/dockethead/include/ar.h: 5872
try:
    ARREF_APPLICATION_HELP_INDEX_EXT2 = 32806
except:
    pass

# /opt/dockethead/include/ar.h: 5875
try:
    ARREF_APPLICATION_HELP_INDEX_FILE2 = 32807
except:
    pass

# /opt/dockethead/include/ar.h: 5878
try:
    ARREF_APPLICATION_HELP_FILE_NAME3 = 32808
except:
    pass

# /opt/dockethead/include/ar.h: 5881
try:
    ARREF_APPLICATION_HELP_EXT3 = 32809
except:
    pass

# /opt/dockethead/include/ar.h: 5883
try:
    ARREF_APPLICATION_HELP_FILE3 = 32810
except:
    pass

# /opt/dockethead/include/ar.h: 5885
try:
    ARREF_APPLICATION_HELP_INDEX_EXT3 = 32811
except:
    pass

# /opt/dockethead/include/ar.h: 5888
try:
    ARREF_APPLICATION_HELP_INDEX_FILE3 = 32812
except:
    pass

# /opt/dockethead/include/ar.h: 5891
try:
    ARREF_APPLICATION_HELP_FILE_NAME4 = 32813
except:
    pass

# /opt/dockethead/include/ar.h: 5894
try:
    ARREF_APPLICATION_HELP_EXT4 = 32814
except:
    pass

# /opt/dockethead/include/ar.h: 5896
try:
    ARREF_APPLICATION_HELP_FILE4 = 32815
except:
    pass

# /opt/dockethead/include/ar.h: 5898
try:
    ARREF_APPLICATION_HELP_INDEX_EXT4 = 32816
except:
    pass

# /opt/dockethead/include/ar.h: 5901
try:
    ARREF_APPLICATION_HELP_INDEX_FILE4 = 32817
except:
    pass

# /opt/dockethead/include/ar.h: 5904
try:
    ARREF_APPLICATION_HELP_FILE_NAME5 = 32818
except:
    pass

# /opt/dockethead/include/ar.h: 5907
try:
    ARREF_APPLICATION_HELP_EXT5 = 32819
except:
    pass

# /opt/dockethead/include/ar.h: 5909
try:
    ARREF_APPLICATION_HELP_FILE5 = 32820
except:
    pass

# /opt/dockethead/include/ar.h: 5911
try:
    ARREF_APPLICATION_HELP_INDEX_EXT5 = 32821
except:
    pass

# /opt/dockethead/include/ar.h: 5914
try:
    ARREF_APPLICATION_HELP_INDEX_FILE5 = 32822
except:
    pass

# /opt/dockethead/include/ar.h: 5917
try:
    ARREF_APPLICATION_HELP_LABEL = 32823
except:
    pass

# /opt/dockethead/include/ar.h: 5919
try:
    ARREF_APPLICATION_HELP_LABEL2 = 32824
except:
    pass

# /opt/dockethead/include/ar.h: 5921
try:
    ARREF_APPLICATION_HELP_LABEL3 = 32825
except:
    pass

# /opt/dockethead/include/ar.h: 5923
try:
    ARREF_APPLICATION_HELP_LABEL4 = 32826
except:
    pass

# /opt/dockethead/include/ar.h: 5925
try:
    ARREF_APPLICATION_HELP_LABEL5 = 32827
except:
    pass

# /opt/dockethead/include/ar.h: 5927
try:
    ARREF_WS_XML_SCHEMA_LOC = 32828
except:
    pass

# /opt/dockethead/include/ar.h: 5929
try:
    ARREF_ENTRYPOINT_ORDER = 32829
except:
    pass

# /opt/dockethead/include/ar.h: 5931
try:
    ARREF_ENTRYPOINT_START_ACTLINK = 32830
except:
    pass

# /opt/dockethead/include/ar.h: 5933
try:
    ARREF_APP_AUTOLAYOUT_SS = 32831
except:
    pass

# /opt/dockethead/include/ar.h: 5935
try:
    ARREF_APP_FORMACTION_FIELDS = 32832
except:
    pass

# /opt/dockethead/include/ar.h: 5936
try:
    ARREF_ENCAPSULATED_APP_DATA = 32833
except:
    pass

# /opt/dockethead/include/ar.h: 5938
try:
    ARREF_APP_DEFAULT_OBJ_PERMS = 32835
except:
    pass

# /opt/dockethead/include/ar.h: 5940
try:
    ARREF_APP_ADD_FORMACTION_FIELDS = 32836
except:
    pass

# /opt/dockethead/include/ar.h: 5941
try:
    ARREF_APP_FORMACTION_RESULTS_LIST_FIXED_HEADER = 32837
except:
    pass

# /opt/dockethead/include/ar.h: 5942
try:
    ARREF_APP_FORMACTION_PAGE_PROPERTIES = 32838
except:
    pass

# /opt/dockethead/include/ar.h: 5943
try:
    ARREF_APP_OBJECT_VERSION = 32839
except:
    pass

# /opt/dockethead/include/ar.h: 5944
try:
    ARREF_APP_PACKING_LISTS = 32840
except:
    pass

# /opt/dockethead/include/ar.h: 5945
try:
    ARREF_APP_DATA_MERGE_IMP_QUAL = 32841
except:
    pass

# /opt/dockethead/include/ar.h: 5947
try:
    ARREF_APP_DATA_MERGE_IMP_OPTION = 32842
except:
    pass

# /opt/dockethead/include/ar.h: 5950
try:
    ARREF_LAST_RESERVED = 65535
except:
    pass

# /opt/dockethead/include/ar.h: 5955
try:
    ARREF_DATA_ARSREF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5956
try:
    ARREF_DATA_EXTREF = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5959
try:
    ARCONOWNER_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 5960
try:
    ARCONOWNER_ALL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 5961
try:
    ARCONOWNER_SCHEMA = 2
except:
    pass

# /opt/dockethead/include/ar.h: 5965
try:
    ARMAX_CON_LABEL_LEN = 255
except:
    pass

# /opt/dockethead/include/ar.h: 5966
try:
    ARMAX_CON_DESCRIPTION_LEN = 2000
except:
    pass

# /opt/dockethead/include/ar.h: 5967
try:
    ARMAX_CON_TASK_NAME_LEN = 1024
except:
    pass

# /opt/dockethead/include/ar.h: 5968
try:
    ARMAX_CON_OML_LABEL_LEN = 1024
except:
    pass

# /opt/dockethead/include/ar.h: 6084
try:
    AR_SIGNAL_CONFIG_CHANGED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6085
try:
    AR_SIGNAL_GROUP_CACHE_CHANGED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6086
try:
    AR_SIGNAL_LICENSE_CHANGED = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6087
try:
    AR_SIGNAL_ALERT_USER_CHANGED = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6088
try:
    AR_SIGNAL_DSO_SIGNAL = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6089
try:
    AR_SIGNAL_USER_CACHE_CHANGED = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6090
try:
    AR_SIGNAL_APPLICATION_SIGNAL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6091
try:
    AR_SIGNAL_ARCHIVE_CHANGED = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6092
try:
    AR_SIGNAL_ESCALATION_CHANGED = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6093
try:
    AR_SIGNAL_RECACHE = 10
except:
    pass

# /opt/dockethead/include/ar.h: 6094
try:
    AR_SIGNAL_COMPUTED_GROUP_CHANGED = 11
except:
    pass

# /opt/dockethead/include/ar.h: 6095
try:
    AR_SIGNAL_DYNAMIC_PERM_CHANGED = 12
except:
    pass

# /opt/dockethead/include/ar.h: 6096
try:
    AR_SIGNAL_FULL_TEXT_PENDING = 13
except:
    pass

# /opt/dockethead/include/ar.h: 6097
try:
    AR_SIGNAL_INSTALL_SIGNAL = 14
except:
    pass

# /opt/dockethead/include/ar.h: 6098
try:
    AR_SIGNAL_SRVSTAT_SIGNAL = 15
except:
    pass

# /opt/dockethead/include/ar.h: 6099
try:
    AR_SIGNAL_FULL_TEXT_REINDEXING_SYNC = 16
except:
    pass

# /opt/dockethead/include/ar.h: 6117
try:
    AR_WRITE_TO_FILE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6118
try:
    AR_WRITE_TO_STATUS_LIST = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6120
try:
    AR_WORKFLOW_CONN_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6121
try:
    AR_WORKFLOW_CONN_SCHEMA_LIST = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6165
try:
    AR_ENC_SEC_POLICY_ENCRYPT_ALLOWED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6166
try:
    AR_ENC_SEC_POLICY_ENCRYPT_REQUIRED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6167
try:
    AR_ENC_SEC_POLICY_ENCRYPT_DISALLOWED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6170
try:
    AR_LOCAL_TEXT_SYSTEM_MESSAGE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6171
try:
    AR_LOCAL_TEXT_ACT_LINK_MESSAGE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6172
try:
    AR_LOCAL_TEXT_FILTER_MESSAGE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6173
try:
    AR_LOCAL_TEXT_ACT_LINK_HELP = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6174
try:
    AR_LOCAL_TEXT_FORM_HELP = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6175
try:
    AR_LOCAL_TEXT_FIELD_HELP = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6176
try:
    AR_LOCAL_TEXT_CONTAIN_DESC = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6177
try:
    AR_LOCAL_TEXT_LIST_MENU_DEFN = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6178
try:
    AR_LOCAL_TEXT_EXTERN_REPORT = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6179
try:
    AR_LOCAL_TEXT_CONTAINER_LABEL = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6180
try:
    AR_LOCAL_TEXT_CONTAINER_HELP = 10
except:
    pass

# /opt/dockethead/include/ar.h: 6181
try:
    AR_LOCAL_TEXT_APPLICATION_HELP = 11
except:
    pass

# /opt/dockethead/include/ar.h: 6182
try:
    AR_LOCAL_TEXT_APPLICATION_ABOUT = 12
except:
    pass

# /opt/dockethead/include/ar.h: 6183
try:
    AR_LOCAL_TEXT_APPLICATION_HELP_INDEX = 13
except:
    pass

# /opt/dockethead/include/ar.h: 6184
try:
    AR_LOCAL_TEXT_FLASHBRD_MESSAGE = 14
except:
    pass

# /opt/dockethead/include/ar.h: 6185
try:
    AR_LOCAL_TEXT_FLASHBRD_LABEL = 15
except:
    pass

# /opt/dockethead/include/ar.h: 6187
try:
    AR_LOCAL_TEXT_ACTIVE_MESSAGE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6188
try:
    AR_LOCAL_TEXT_INACTIVE_MESSAGE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6190
try:
    AR_LOCAL_TEXT_RETURN_TYPE_MSG_TEXT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6191
try:
    AR_LOCAL_TEXT_RETURN_TYPE_BIN_ATTACH = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6193
try:
    IFELSE_IF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6194
try:
    IFELSE_ELSE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6197
try:
    AR_ALERT_SOURCE_GP = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6198
try:
    AR_ALERT_SOURCE_AR = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6199
try:
    AR_ALERT_SOURCE_FIRST = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6200
try:
    AR_ALERT_SOURCE_CHECK = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6201
try:
    AR_ALERT_SOURCE_FB = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6203
try:
    AR_ALERT_ACK = 'ack'
except:
    pass

# /opt/dockethead/include/ar.h: 6204
try:
    AR_ALERT_USER_BROADCAST = '*'
except:
    pass

# /opt/dockethead/include/ar.h: 6206
try:
    AR_ALERT_STRING_SEP = '\\\\'
except:
    pass

# /opt/dockethead/include/ar.h: 6209
try:
    AR_SVR_EVENT_CHG_SCHEMA = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6210
try:
    AR_SVR_EVENT_CHG_FIELD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6211
try:
    AR_SVR_EVENT_CHG_CHARMENU = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6212
try:
    AR_SVR_EVENT_CHG_FILTER = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6213
try:
    AR_SVR_EVENT_CHG_IMPORT = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6214
try:
    AR_SVR_EVENT_CHG_ACTLINK = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6215
try:
    AR_SVR_EVENT_CHG_ESCAL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6216
try:
    AR_SVR_EVENT_CHG_VUI = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6217
try:
    AR_SVR_EVENT_CHG_CONTAINER = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6218
try:
    AR_SVR_EVENT_CHG_USERS = 10
except:
    pass

# /opt/dockethead/include/ar.h: 6219
try:
    AR_SVR_EVENT_CHG_GROUPS = 11
except:
    pass

# /opt/dockethead/include/ar.h: 6220
try:
    AR_SVR_EVENT_CHG_SVR_SETTINGS = 12
except:
    pass

# /opt/dockethead/include/ar.h: 6221
try:
    AR_SVR_EVENT_CHG_ALERT_USERS = 13
except:
    pass

# /opt/dockethead/include/ar.h: 6222
try:
    AR_SVR_EVENT_ARCHIVE_DONE = 14
except:
    pass

# /opt/dockethead/include/ar.h: 6223
try:
    AR_SVR_EVENT_SERVGROUP_ACTION = 15
except:
    pass

# /opt/dockethead/include/ar.h: 6224
try:
    AR_SVR_EVENT_CHG_LICENSES = 16
except:
    pass

# /opt/dockethead/include/ar.h: 6225
try:
    AR_SVR_EVENT_DYNAMIC_PERM = 17
except:
    pass

# /opt/dockethead/include/ar.h: 6226
try:
    AR_SVR_EVENT_CHG_IMAGE = 18
except:
    pass

# /opt/dockethead/include/ar.h: 6228
try:
    AR_MAX_SVR_EVENT_USED = 18
except:
    pass

# /opt/dockethead/include/ar.h: 6231
try:
    AR_MAX_SVR_EVENT_TYPE_STR = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6234
try:
    AR_SVR_EVENT_USER_ADDED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6235
try:
    AR_SVR_EVENT_USER_MODIFIED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6236
try:
    AR_SVR_EVENT_USER_DELETED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6239
try:
    AR_SVR_EVENT_GROUP_ADDED = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6240
try:
    AR_SVR_EVENT_GROUP_MODIFIED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6241
try:
    AR_SVR_EVENT_GROUP_DELETED = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6242
try:
    AR_SVR_EVENT_COMPGROUP_ADDED = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6243
try:
    AR_SVR_EVENT_COMPGROUP_MODIFIED = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6244
try:
    AR_SVR_EVENT_COMPGROUP_DELETED = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6245
try:
    AR_SVR_EVENT_APPLICATION_ADDED = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6246
try:
    AR_SVR_EVENT_APPLICATION_MODIFIED = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6247
try:
    AR_SVR_EVENT_APPLICATION_DELETED = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6248
try:
    AR_SVR_EVENT_ROLE_ADDED = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6249
try:
    AR_SVR_EVENT_ROLE_MODIFIED = 10
except:
    pass

# /opt/dockethead/include/ar.h: 6250
try:
    AR_SVR_EVENT_ROLE_DELETED = 11
except:
    pass

# /opt/dockethead/include/ar.h: 6253
try:
    AR_SVR_EVENT_ARCHIVE_FORM = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6254
try:
    AR_SVR_EVENT_ARCHIVE_DELETE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6255
try:
    AR_SVR_EVENT_ARCHIVE_FORM_DELETE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6256
try:
    AR_SVR_EVENT_ARCHIVE_XML = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6257
try:
    AR_SVR_EVENT_ARCHIVE_ARX = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6260
try:
    AR_SVR_EVENT_SERVGROUP_FAILOVER = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6261
try:
    AR_SVR_EVENT_SERVGROUP_RELINQUISH = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6262
try:
    AR_SVR_EVENT_SERVGROUP_TAKEOVER = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6275
try:
    AR_SVR_EVENT_IMPORT_SET_OBJECT = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6276
try:
    AR_SVR_EVENT_IMPORT_CREATE_OBJECT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6279
try:
    AR_SVR_EVENT_DYN_PERMISSION_START = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6280
try:
    AR_SVR_EVENT_DYN_PERMISSION_END = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6376
try:
    AR_SVR_STATS_RECMODE_OFF = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6377
try:
    AR_SVR_STATS_RECMODE_CUMUL_ONLY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6378
try:
    AR_SVR_STATS_RECMODE_CUMUL_QUEUE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6382
try:
    AR_DSO_UPDATE_IMMEDIATELY = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6383
try:
    AR_DSO_UPDATE_HOURLY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6384
try:
    AR_DSO_UPDATE_DAILY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6385
try:
    AR_DSO_UPDATE_ON_RETURN = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6386
try:
    AR_DSO_UPDATE_NO_UPDATE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6388
try:
    AR_DSO_TRANSFER_DATA_ONLY = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6389
try:
    AR_DSO_TRANSFER_OWNERSHIP = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6390
try:
    AR_DSO_TRANSFER_COPY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6391
try:
    AR_DSO_TRANSFER_COPY_DELETE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6393
try:
    AR_DSO_TRANSFER_DUP_ERROR = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6394
try:
    AR_DSO_TRANSFER_DUP_OVERWRITE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6395
try:
    AR_DSO_TRANSFER_DUP_CREATE_NEW = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6397
try:
    AR_DSO_MAP_BY_FIELD_IDS = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6398
try:
    AR_DSO_MAP_BY_CUSTOM = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6399
try:
    AR_DSO_MAP_BY_FIELD_NAMES = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6401
try:
    AR_DSO_ERROR_RETRY_STANDARD = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6402
try:
    AR_DSO_ERROR_RETRY_NO_RETRY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6403
try:
    AR_DSO_ERROR_RETRY_ALL_RETRY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6404
try:
    AR_DSO_ERROR_RETRY_STANDARD_DB = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6407
try:
    AR_VUI_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6408
try:
    AR_VUI_TYPE_WINDOWS = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6409
try:
    AR_VUI_TYPE_STANDARD = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6410
try:
    AR_VUI_TYPE_WEB = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6411
try:
    AR_VUI_TYPE_WEB_ABS_POS = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6412
try:
    AR_VUI_TYPE_WIRELESS = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6413
try:
    AR_VUI_TYPE_WEB_AUTOGEN = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6414
try:
    AR_VUI_TYPE_WEB_ABS_POS_AUTOGEN = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6415
try:
    AR_VUI_TYPE_DEFAULT = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6416
try:
    AR_VUI_TYPE_SELECT = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6419
try:
    AR_CLIENT_TYPE_UNKNOWN = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6420
try:
    AR_CLIENT_TYPE_PRE_50 = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6421
try:
    AR_CLIENT_TYPE_WAT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6422
try:
    AR_CLIENT_TYPE_WUT = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6423
try:
    AR_CLIENT_TYPE_WIP = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6424
try:
    AR_CLIENT_TYPE_DSO = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6425
try:
    AR_CLIENT_TYPE_ODBC = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6426
try:
    AR_CLIENT_TYPE_APPROVAL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6427
try:
    AR_CLIENT_TYPE_WEB_SERVER = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6428
try:
    AR_CLIENT_TYPE_MID_TIER = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6429
try:
    AR_CLIENT_TYPE_PALM_PILOT = 10
except:
    pass

# /opt/dockethead/include/ar.h: 6430
try:
    AR_CLIENT_TYPE_FLASHBOARDS = 11
except:
    pass

# /opt/dockethead/include/ar.h: 6431
try:
    AR_CLIENT_TYPE_FLASHBOARDS_MID_TIER = 12
except:
    pass

# /opt/dockethead/include/ar.h: 6432
try:
    AR_CLIENT_TYPE_EIE = 13
except:
    pass

# /opt/dockethead/include/ar.h: 6434
try:
    AR_CLIENT_TYPE_RELOAD = 14
except:
    pass

# /opt/dockethead/include/ar.h: 6435
try:
    AR_CLIENT_TYPE_CACHE = 15
except:
    pass

# /opt/dockethead/include/ar.h: 6436
try:
    AR_CLIENT_TYPE_DIST = 16
except:
    pass

# /opt/dockethead/include/ar.h: 6437
try:
    AR_CLIENT_TYPE_RUN_MACRO = 17
except:
    pass

# /opt/dockethead/include/ar.h: 6438
try:
    AR_CLIENT_TYPE_MAIL = 18
except:
    pass

# /opt/dockethead/include/ar.h: 6439
try:
    AR_CLIENT_TYPE_IMPORT_CMD = 19
except:
    pass

# /opt/dockethead/include/ar.h: 6440
try:
    AR_CLIENT_TYPE_REPORT_PLUGIN = 20
except:
    pass

# /opt/dockethead/include/ar.h: 6441
try:
    AR_CLIENT_TYPE_ALERT = 21
except:
    pass

# /opt/dockethead/include/ar.h: 6442
try:
    AR_CLIENT_TYPE_MAIL_DAEMON = 22
except:
    pass

# /opt/dockethead/include/ar.h: 6443
try:
    AR_CLIENT_TYPE_SIGNAL = 23
except:
    pass

# /opt/dockethead/include/ar.h: 6444
try:
    AR_CLIENT_TYPE_DEBUGGER = 24
except:
    pass

# /opt/dockethead/include/ar.h: 6445
try:
    AR_CLIENT_TYPE_OBJSTR = 25
except:
    pass

# /opt/dockethead/include/ar.h: 6446
try:
    AR_CLIENT_TYPE_OBJSTR_SYNC = 26
except:
    pass

# /opt/dockethead/include/ar.h: 6447
try:
    AR_CLIENT_TYPE_SERVER_ADMIN_PLUGIN = 27
except:
    pass

# /opt/dockethead/include/ar.h: 6448
try:
    AR_CLIENT_TYPE_SIM_PUBLISHING_SERVER = 28
except:
    pass

# /opt/dockethead/include/ar.h: 6449
try:
    AR_CLIENT_TYPE_SIM_SME = 29
except:
    pass

# /opt/dockethead/include/ar.h: 6450
try:
    AR_CLIENT_TYPE_CMDB_ENGINE = 30
except:
    pass

# /opt/dockethead/include/ar.h: 6451
try:
    AR_CLIENT_TYPE_CMDB_DRIVER = 31
except:
    pass

# /opt/dockethead/include/ar.h: 6452
try:
    AR_CLIENT_TYPE_RECON_ENGINE = 32
except:
    pass

# /opt/dockethead/include/ar.h: 6453
try:
    AR_CLIENT_TYPE_ASSIGNMENT_ENGINE = 33
except:
    pass

# /opt/dockethead/include/ar.h: 6454
try:
    AR_CLIENT_TYPE_WEBSERVICE = 34
except:
    pass

# /opt/dockethead/include/ar.h: 6455
try:
    AR_CLIENT_TYPE_NORMALIZATION_ENGINE = 35
except:
    pass

# /opt/dockethead/include/ar.h: 6456
try:
    AR_CLIENT_TYPE_DEVELOPER_STUDIO = 36
except:
    pass

# /opt/dockethead/include/ar.h: 6457
try:
    AR_CLIENT_TYPE_FT_TEXT_READER = 37
except:
    pass

# /opt/dockethead/include/ar.h: 6458
try:
    AR_CLIENT_TYPE_ATRIUMSSO = 38
except:
    pass

# /opt/dockethead/include/ar.h: 6459
try:
    AR_CLIENT_TYPE_MIGRATOR = 39
except:
    pass

# /opt/dockethead/include/ar.h: 6460
try:
    AR_CLIENT_TYPE_UDM = 40
except:
    pass

# /opt/dockethead/include/ar.h: 6461
try:
    AR_CLIENT_TYPE_RKM_OPERATIONS = 41
except:
    pass

# /opt/dockethead/include/ar.h: 6462
try:
    AR_CLIENT_TYPE_RKM_FORM_PERMISSIONS = 42
except:
    pass

# /opt/dockethead/include/ar.h: 6463
try:
    AR_CLIENT_TYPE_RKM_DOCUMENT_MIGRATOR = 43
except:
    pass

# /opt/dockethead/include/ar.h: 6464
try:
    AR_CLIENT_TYPE_RKM_FILE_SYSTEM = 44
except:
    pass

# /opt/dockethead/include/ar.h: 6465
try:
    AR_CLIENT_TYPE_RKM_FILE_SYSTEM_SYNC = 45
except:
    pass

# /opt/dockethead/include/ar.h: 6466
try:
    AR_CLIENT_TYPE_RKM_GROUP = 46
except:
    pass

# /opt/dockethead/include/ar.h: 6467
try:
    AR_CLIENT_TYPE_RKM_REGISTRATION = 47
except:
    pass

# /opt/dockethead/include/ar.h: 6468
try:
    AR_CLIENT_TYPE_ASSET_SWLM_RULE_ENGINE = 48
except:
    pass

# /opt/dockethead/include/ar.h: 6469
try:
    AR_CLIENT_TYPE_ASSET_SOFTWARE_USAGE = 49
except:
    pass

# /opt/dockethead/include/ar.h: 6470
try:
    AR_CLIENT_TYPE_ASSET_RLE_CONFIG = 50
except:
    pass

# /opt/dockethead/include/ar.h: 6471
try:
    AR_CLIENT_TYPE_ASSET_CHARGE_BACK = 51
except:
    pass

# /opt/dockethead/include/ar.h: 6472
try:
    AR_CLIENT_TYPE_ITSM_COMMON = 52
except:
    pass

# /opt/dockethead/include/ar.h: 6473
try:
    AR_CLIENT_TYPE_ITSM_CAI = 53
except:
    pass

# /opt/dockethead/include/ar.h: 6474
try:
    AR_CLIENT_TYPE_ITSM_UTILITY = 54
except:
    pass

# /opt/dockethead/include/ar.h: 6475
try:
    AR_CLIENT_TYPE_ITSM_APPQUERY = 55
except:
    pass

# /opt/dockethead/include/ar.h: 6476
try:
    AR_CLIENT_TYPE_ITSM_NEXT_ID = 56
except:
    pass

# /opt/dockethead/include/ar.h: 6477
try:
    AR_CLIENT_TYPE_ATRIUM_INTEGRATOR = 57
except:
    pass

# /opt/dockethead/include/ar.h: 6478
try:
    AR_CLIENT_TYPE_ADDM = 58
except:
    pass

# /opt/dockethead/include/ar.h: 6479
try:
    AR_CLIENT_TYPE_BPPM = 59
except:
    pass

# /opt/dockethead/include/ar.h: 6480
try:
    AR_CLIENT_TYPE_ODA = 60
except:
    pass

# /opt/dockethead/include/ar.h: 6481
try:
    AR_CLIENT_TYPE_MYIT = 61
except:
    pass

# /opt/dockethead/include/ar.h: 6483
try:
    AR_CLIENT_TYPE_END_OF_PRODUCT = 3999
except:
    pass

# /opt/dockethead/include/ar.h: 6485
try:
    AR_CLIENT_TYPE_UNPRODUCTIZED_START = 4000
except:
    pass

# /opt/dockethead/include/ar.h: 6486
try:
    AR_CLIENT_TYPE_DRIVER = 4000
except:
    pass

# /opt/dockethead/include/ar.h: 6487
try:
    AR_CLIENT_TYPE_DISPATCHER = 4001
except:
    pass

# /opt/dockethead/include/ar.h: 6489
try:
    AR_CLIENT_TYPE_HELP = 4002
except:
    pass

# /opt/dockethead/include/ar.h: 6490
try:
    AR_CLIENT_TYPE_JANITOR = 4003
except:
    pass

# /opt/dockethead/include/ar.h: 6491
try:
    AR_CLIENT_TYPE_MENU = 4004
except:
    pass

# /opt/dockethead/include/ar.h: 6492
try:
    AR_CLIENT_TYPE_STRUCT = 4005
except:
    pass

# /opt/dockethead/include/ar.h: 6493
try:
    AR_CLIENT_TYPE_TEXT = 4006
except:
    pass

# /opt/dockethead/include/ar.h: 6494
try:
    AR_CLIENT_TYPE_SQLED = 4007
except:
    pass

# /opt/dockethead/include/ar.h: 6495
try:
    AR_CLIENT_TYPE_CHANGE_SEL = 4008
except:
    pass

# /opt/dockethead/include/ar.h: 6496
try:
    AR_CLIENT_TYPE_CHANGE_ID = 4009
except:
    pass

# /opt/dockethead/include/ar.h: 6497
try:
    AR_CLIENT_TYPE_LABEL = 4010
except:
    pass

# /opt/dockethead/include/ar.h: 6498
try:
    AR_CLIENT_TYPE_INSTALLER = 4011
except:
    pass

# /opt/dockethead/include/ar.h: 6499
try:
    AR_CLIENT_TYPE_RIK = 4012
except:
    pass

# /opt/dockethead/include/ar.h: 6501
try:
    AR_CLIENT_TYPE_END_OF_RESERVED_RANGE = 5000
except:
    pass

# /opt/dockethead/include/ar.h: 6504
try:
    AR_SESS_CHUNK_RESPONSE_SIZE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6505
try:
    AR_SESS_TIMEOUT_NORMAL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6506
try:
    AR_SESS_TIMEOUT_LONG = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6507
try:
    AR_SESS_TIMEOUT_XLONG = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6508
try:
    AR_SESS_LOCK_TO_SOCKET_NUMBER = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6509
try:
    AR_SESS_POOLED = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6510
try:
    AR_SESS_CLIENT_TYPE = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6511
try:
    AR_SESS_VUI_TYPE = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6512
try:
    AR_SESS_OVERRIDE_PREV_IP = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6514
try:
    AR_SESS_API_CMD_LOG = 10
except:
    pass

# /opt/dockethead/include/ar.h: 6515
try:
    AR_SESS_API_RES_LOG = 11
except:
    pass

# /opt/dockethead/include/ar.h: 6517
try:
    AR_SESS_CONTROL_PROP_DESIGN_OVERLAYGROUP = 12
except:
    pass

# /opt/dockethead/include/ar.h: 6520
try:
    AR_SESS_CONTROL_PROP_API_OVERLAYGROUP = 13
except:
    pass

# /opt/dockethead/include/ar.h: 6524
try:
    AR_SESS_CONTROL_PROP_GRANULAR_OVERLAY_RETRIEVE_MODE = 14
except:
    pass

# /opt/dockethead/include/ar.h: 6528
try:
    AR_XML_DOC_CHAR_STR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6529
try:
    AR_XML_DOC_FILE_NAME = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6530
try:
    AR_XML_DOC_URL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6531
try:
    AR_XML_DOC_FILE_HANDLE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6571
try:
    AR_ENC_ECC_163 = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6572
try:
    AR_ENC_ECC_239 = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6573
try:
    AR_ENC_ECC_571 = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6574
try:
    AR_ENC_RMOD_512 = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6575
try:
    AR_ENC_RMOD_1024 = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6576
try:
    AR_ENC_RMOD_2048 = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6580
try:
    AR_ENC_DES_SINGLE_KEY_CBC = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6581
try:
    AR_ENC_RC4_KEY_LEN_128 = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6582
try:
    AR_ENC_RC4_KEY_LEN_2048 = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6583
try:
    AR_ENC_RC4_KEY_LEN_64 = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6584
try:
    AR_ENC_RC4_KEY_LEN_56 = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6586
try:
    AR_ENC_AES_KEY_LEN_128 = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6587
try:
    AR_ENC_AES_KEY_LEN_256 = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6588
try:
    AR_ENC_AES_FIPS_KEY_LEN_128 = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6589
try:
    AR_ENC_AES_FIPS_KEY_LEN_256 = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6592
try:
    ENABLE_FIPS_MODE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6593
try:
    ENABLE_FIPS_DUAL_MODE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6595
try:
    FIPS_SERVER_MODE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6596
try:
    FIPS_CLIENT_MODE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6597
try:
    FIPS_STATUS = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6598
try:
    DATA_ENCRYPTION = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6599
try:
    DATA_ALGORITHM = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6600
try:
    FIPS_DUAL_MODE = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6601
try:
    SECURITY_POLICY = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6602
try:
    DATAKEY_INTERVAL = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6603
try:
    PUBLIC_KEY_ALGORITHM = 9
except:
    pass

# /opt/dockethead/include/ar.h: 6604
try:
    PUBLIC_KEY_INTERVAL = 10
except:
    pass

# /opt/dockethead/include/ar.h: 6605
try:
    NEW_FIPS_SERVER_MODE = 11
except:
    pass

# /opt/dockethead/include/ar.h: 6606
try:
    NEW_DATA_ENCRYPTION = 12
except:
    pass

# /opt/dockethead/include/ar.h: 6607
try:
    NEW_DATA_ALGORITHM = 13
except:
    pass

# /opt/dockethead/include/ar.h: 6608
try:
    NEW_SECURITY_POLICY = 14
except:
    pass

# /opt/dockethead/include/ar.h: 6609
try:
    NEW_DATAKEY_INTERVAL = 15
except:
    pass

# /opt/dockethead/include/ar.h: 6610
try:
    NEW_PUBLIC_KEY_ALGORITHM = 16
except:
    pass

# /opt/dockethead/include/ar.h: 6611
try:
    NEW_PUBLIC_KEY_INTERVAL = 17
except:
    pass

# /opt/dockethead/include/ar.h: 6612
try:
    DATA_ENCRYPTION_LEVEL = 18
except:
    pass

# /opt/dockethead/include/ar.h: 6613
try:
    LIBRARY_ENCRYPTION_LEVEL = 19
except:
    pass

# /opt/dockethead/include/ar.h: 6614
try:
    NEW_FIPS_DATA_ALGORITHM = 20
except:
    pass

# /opt/dockethead/include/ar.h: 6625
try:
    AR_DATEPARTS_YEAR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6626
try:
    AR_DATEPARTS_MONTH = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6627
try:
    AR_DATEPARTS_DAY = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6628
try:
    AR_DATEPARTS_WEEK = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6629
try:
    AR_DATEPARTS_WEEKDAY = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6636
try:
    AR_TWO_DIGIT_YEAR_CUTOFF_INCREMENT = 29
except:
    pass

# /opt/dockethead/include/ar.h: 6679
try:
    AR_ENTRYPOINT_BROWSER_TYPE_IE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6680
try:
    AR_ENTRYPOINT_BROWSER_TYPE_NN4 = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6681
try:
    AR_ENTRYPOINT_BROWSER_TYPE_NN6 = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6682
try:
    AR_ENTRYPOINT_BROWSER_TYPE_NN7 = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6685
try:
    AR_ENTRYPOINT_TYPE_AL_GUIDE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6686
try:
    AR_ENTRYPOINT_TYPE_DEFAULT_SEARCH = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6687
try:
    AR_ENTRYPOINT_TYPE_DEFAULT_NEW = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6690
try:
    AR_XML_FORM_MAP_TYPE_EMBEDDED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6691
try:
    AR_XML_FORM_MAP_TYPE_REFERENCE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6693
try:
    AR_XML_VALINFO_USERNAME = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6694
try:
    AR_XML_VALINFO_PASSWORD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6695
try:
    AR_XML_VALINFO_UT_PASSWORD_TYPE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6879
try:
    AR_APP_TYPE_LOCAL = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6880
try:
    AR_APP_TYPE_DISTRIBUTABLE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6884
try:
    AR_BULK_ENTRY_CREATE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6885
try:
    AR_BULK_ENTRY_SET = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6886
try:
    AR_BULK_ENTRY_DELETE = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6887
try:
    AR_BULK_ENTRY_MERGE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6888
try:
    AR_BULK_ENTRY_XMLCREATE = 5
except:
    pass

# /opt/dockethead/include/ar.h: 6889
try:
    AR_BULK_ENTRY_XMLSET = 6
except:
    pass

# /opt/dockethead/include/ar.h: 6890
try:
    AR_BULK_ENTRY_XMLDELETE = 7
except:
    pass

# /opt/dockethead/include/ar.h: 6892
try:
    AR_BULK_ENTRY_ACTION_SEND = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6893
try:
    AR_BULK_ENTRY_ACTION_CANCEL = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6942
try:
    AR_SYSTEM_LOGGING_OPTION_NONE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6946
try:
    AR_EXT_AUTH_DATA_NO_EMAIL_ADDR = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6947
try:
    AR_EXT_AUTH_DATA_NO_NOTIFY_MECH = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6948
try:
    AR_EXT_AUTH_DATA_NO_GROUP_IDS = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6949
try:
    AR_EXT_AUTH_DATA_NO_LICENSE_INFO = 8
except:
    pass

# /opt/dockethead/include/ar.h: 6950
try:
    AR_EXT_AUTH_DATA_NO_NOTIF_VALIDATION = 16
except:
    pass

# /opt/dockethead/include/ar.h: 6954
try:
    AR_EXCEPTION_DIAG_INCLUDE_ALL = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6955
try:
    AR_EXCEPTION_DIAG_EXCLUDE_STACK = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6958
try:
    AR_AUDIT_FORCE_DISABLE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6960
try:
    AR_AUDIT_ALLOW_MOVE = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6962
try:
    AR_AUDIT_UPDATE_ONLY = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6994
try:
    WFD_IDLE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 6995
try:
    WFD_RUNNING = 1
except:
    pass

# /opt/dockethead/include/ar.h: 6996
try:
    WFD_BEFORE_API = 2
except:
    pass

# /opt/dockethead/include/ar.h: 6997
try:
    WFD_BEFORE_QUAL = 3
except:
    pass

# /opt/dockethead/include/ar.h: 6998
try:
    WFD_PHASE_1 = 4
except:
    pass

# /opt/dockethead/include/ar.h: 6999
try:
    WFD_PHASE_2 = 5
except:
    pass

# /opt/dockethead/include/ar.h: 7000
try:
    WFD_PHASE_3 = 6
except:
    pass

# /opt/dockethead/include/ar.h: 7001
try:
    WFD_ESCL = 7
except:
    pass

# /opt/dockethead/include/ar.h: 7002
try:
    WFD_BEFORE_CMDB = 8
except:
    pass

# /opt/dockethead/include/ar.h: 7003
try:
    WFD_AFTER_API = 9
except:
    pass

# /opt/dockethead/include/ar.h: 7006
try:
    WFD_EXECUTE_STEP = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7007
try:
    WFD_EXECUTE_RUN = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7008
try:
    WFD_EXECUTE_RESV_1 = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7009
try:
    WFD_EXECUTE_RESV_2 = 3
except:
    pass

# /opt/dockethead/include/ar.h: 7012
try:
    WFD_EXEC_NOTHING = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7013
try:
    WFD_EXEC_STEPPED = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7014
try:
    WFD_EXEC_BRK_POINT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7015
try:
    WFD_EXEC_USER_BRK = 3
except:
    pass

# /opt/dockethead/include/ar.h: 7016
try:
    WFD_EXEC_CONTINUE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 7017
try:
    WFD_EXEC_QUERY = 5
except:
    pass

# /opt/dockethead/include/ar.h: 7078
try:
    AR_CHECKDB_TYPE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7079
try:
    AR_CHECKDB_ASSIGN_SHORT_LONG = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7080
try:
    AR_CHECKDB_PROP_SHORT_LONG = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7081
try:
    AR_CHECKDB_QUERY_SHORT_LONG = 3
except:
    pass

# /opt/dockethead/include/ar.h: 7083
try:
    AR_REC_QRY_PARENT_ALIAS = 'parent'
except:
    pass

# /opt/dockethead/include/ar.h: 7084
try:
    AR_SQL_MS_ALIAS_PREFIX = 'J'
except:
    pass

# /opt/dockethead/include/ar.h: 7093
try:
    AR_MULTI_SCHEMA_FUNC_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7094
try:
    AR_MULTI_SCHEMA_FUNC_COUNT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7095
try:
    AR_MULTI_SCHEMA_FUNC_SUM = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7096
try:
    AR_MULTI_SCHEMA_FUNC_AVG = 3
except:
    pass

# /opt/dockethead/include/ar.h: 7097
try:
    AR_MULTI_SCHEMA_FUNC_MIN = 4
except:
    pass

# /opt/dockethead/include/ar.h: 7098
try:
    AR_MULTI_SCHEMA_FUNC_MAX = 5
except:
    pass

# /opt/dockethead/include/ar.h: 7099
try:
    AR_MULTI_SCHEMA_FUNC_LAST = 5
except:
    pass

# /opt/dockethead/include/ar.h: 7136
try:
    AR_VALUE_SET_QUERY = 7
except:
    pass

# /opt/dockethead/include/ar.h: 7231
try:
    AR_MULTI_SCHEMA_SCHEMA_NAME = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7232
try:
    AR_MULTI_SCHEMA_NESTED_QUERY = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7233
try:
    AR_MULTI_SCHEMA_RECURSIVE_QUERY = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7236
try:
    AR_MULTI_SCHEMA_JOIN_INNER = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7237
try:
    AR_MULTI_SCHEMA_JOIN_LEFT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7238
try:
    AR_MULTI_SCHEMA_JOIN_RIGHT = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7277
try:
    AR_MAX_RECURSION_LEVEL_DEFAULT = 25
except:
    pass

# /opt/dockethead/include/ar.h: 7280
try:
    AR_MAX_VENDOR_TEMP_TABLES_DEFAULT = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7373
try:
    AR_TASK_STATE_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7374
try:
    AR_TASK_STATE_OPEN = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7375
try:
    AR_TASK_STATE_COMMIT = 4
except:
    pass

# /opt/dockethead/include/ar.h: 7376
try:
    AR_TASK_STATE_ROllEDBACK = 8
except:
    pass

# /opt/dockethead/include/ar.h: 7377
try:
    AR_TASK_STATE_OPEN_MASK = AR_TASK_STATE_OPEN
except:
    pass

# /opt/dockethead/include/ar.h: 7378
try:
    AR_TASK_STATE_COMPLETE_MASK = (AR_TASK_STATE_COMMIT | AR_TASK_STATE_ROllEDBACK)
except:
    pass

# /opt/dockethead/include/ar.h: 7380
try:
    AR_TASK_NODE_OP_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7381
try:
    AR_TASK_NODE_OP_CHANGE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7382
try:
    AR_TASK_NODE_OP_ADD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7383
try:
    AR_TASK_NODE_OP_REMOVE = 4
except:
    pass

# /opt/dockethead/include/ar.h: 7384
try:
    AR_TASK_OBJ_OP_NONE = 0
except:
    pass

# /opt/dockethead/include/ar.h: 7385
try:
    AR_TASK_OBJ_OP_CHANGE = 1
except:
    pass

# /opt/dockethead/include/ar.h: 7386
try:
    AR_TASK_OBJ_OP_ADD = 2
except:
    pass

# /opt/dockethead/include/ar.h: 7387
try:
    AR_TASK_OBJ_OP_REMOVE = 4
except:
    pass

ARTextString = struct_ARTextString # /opt/dockethead/include/ar.h: 319

AREntryIdList = struct_AREntryIdList # /opt/dockethead/include/ar.h: 327

ARInternalIdList = struct_ARInternalIdList # /opt/dockethead/include/ar.h: 335

ARInternalIdListList = struct_ARInternalIdListList # /opt/dockethead/include/ar.h: 343

ARLocaleList = struct_ARLocaleList # /opt/dockethead/include/ar.h: 351

ARNameList = struct_ARNameList # /opt/dockethead/include/ar.h: 359

ARNamePtrList = struct_ARNamePtrList # /opt/dockethead/include/ar.h: 367

ARFileNameList = struct_ARFileNameList # /opt/dockethead/include/ar.h: 372

ARAccessNameList = struct_ARAccessNameList # /opt/dockethead/include/ar.h: 379

ARAccessNamePtrList = struct_ARAccessNamePtrList # /opt/dockethead/include/ar.h: 387

ARPasswordList = struct_ARPasswordList # /opt/dockethead/include/ar.h: 393

ARServerNameList = struct_ARServerNameList # /opt/dockethead/include/ar.h: 400

ARTextStringList = struct_ARTextStringList # /opt/dockethead/include/ar.h: 408

ARTimestampList = struct_ARTimestampList # /opt/dockethead/include/ar.h: 416

ARUnsignedIntList = struct_ARUnsignedIntList # /opt/dockethead/include/ar.h: 424

ARUnsignedIntPtrList = struct_ARUnsignedIntPtrList # /opt/dockethead/include/ar.h: 432

ARByteList = struct_ARByteList # /opt/dockethead/include/ar.h: 454

ARLocalizationInfo = struct_ARLocalizationInfo # /opt/dockethead/include/ar.h: 465

ARControlStruct = struct_ARControlStruct # /opt/dockethead/include/ar.h: 495

ARStatusStruct = struct_ARStatusStruct # /opt/dockethead/include/ar.h: 505

ARStatusList = struct_ARStatusList # /opt/dockethead/include/ar.h: 513

ARStatusListList = struct_ARStatusListList # /opt/dockethead/include/ar.h: 521

ARMessageStruct = struct_ARMessageStruct # /opt/dockethead/include/ar.h: 531

ARCoordStruct = struct_ARCoordStruct # /opt/dockethead/include/ar.h: 699

ARCoordList = struct_ARCoordList # /opt/dockethead/include/ar.h: 706

ARBufStruct = struct_ARBufStruct # /opt/dockethead/include/ar.h: 719

ARLocStruct = struct_ARLocStruct # /opt/dockethead/include/ar.h: 731

ARAttachStruct = struct_ARAttachStruct # /opt/dockethead/include/ar.h: 741

ARFuncCurrencyStruct = struct_ARFuncCurrencyStruct # /opt/dockethead/include/ar.h: 749

ARFuncCurrencyList = struct_ARFuncCurrencyList # /opt/dockethead/include/ar.h: 757

ARCurrencyStruct = struct_ARCurrencyStruct # /opt/dockethead/include/ar.h: 767

ARCurrencyList = struct_ARCurrencyList # /opt/dockethead/include/ar.h: 774

ARValueStruct = struct_ARValueStruct # /opt/dockethead/include/ar.h: 814

ARValueList = struct_ARValueList # /opt/dockethead/include/ar.h: 822

ARValuePtrList = struct_ARValuePtrList # /opt/dockethead/include/ar.h: 830

ARValueListList = struct_ARValueListList # /opt/dockethead/include/ar.h: 838

AREntryListFieldStruct = struct_AREntryListFieldStruct # /opt/dockethead/include/ar.h: 856

AREntryListFieldList = struct_AREntryListFieldList # /opt/dockethead/include/ar.h: 863

AREntryListFieldListList = struct_AREntryListFieldListList # /opt/dockethead/include/ar.h: 871

AREntryListStruct = struct_AREntryListStruct # /opt/dockethead/include/ar.h: 882

AREntryFuncListStruct = struct_AREntryFuncListStruct # /opt/dockethead/include/ar.h: 893

AREntryListList = struct_AREntryListList # /opt/dockethead/include/ar.h: 900

AREntryFuncListList = struct_AREntryFuncListList # /opt/dockethead/include/ar.h: 907

AREntryIdListList = struct_AREntryIdListList # /opt/dockethead/include/ar.h: 914

ARFieldValueStruct = struct_ARFieldValueStruct # /opt/dockethead/include/ar.h: 922

ARFieldValueList = struct_ARFieldValueList # /opt/dockethead/include/ar.h: 930

AREntryListFieldValueStruct = struct_AREntryListFieldValueStruct # /opt/dockethead/include/ar.h: 941

AREntryListFieldValueList = struct_AREntryListFieldValueList # /opt/dockethead/include/ar.h: 949

ARFieldFuncValueStruct = struct_ARFieldFuncValueStruct # /opt/dockethead/include/ar.h: 957

ARFieldFuncValueList = struct_ARFieldFuncValueList # /opt/dockethead/include/ar.h: 965

AREntryListFieldFuncValueStruct = struct_AREntryListFieldFuncValueStruct # /opt/dockethead/include/ar.h: 972

AREntryListFieldFuncValueList = struct_AREntryListFieldFuncValueList # /opt/dockethead/include/ar.h: 980

ARBooleanList = struct_ARBooleanList # /opt/dockethead/include/ar.h: 987

ARBooleanListList = struct_ARBooleanListList # /opt/dockethead/include/ar.h: 995

ARFieldValueListList = struct_ARFieldValueListList # /opt/dockethead/include/ar.h: 1002

ARFieldFuncValueListList = struct_ARFieldFuncValueListList # /opt/dockethead/include/ar.h: 1009

ARQualifierStruct = struct_ARQualifierStruct # /opt/dockethead/include/ar.h: 1189

ARStatHistoryValue = struct_ARStatHistoryValue # /opt/dockethead/include/ar.h: 1041

ARQueryValueStruct = struct_ARQueryValueStruct # /opt/dockethead/include/ar.h: 1057

ARCurrencyPartStruct = struct_ARCurrencyPartStruct # /opt/dockethead/include/ar.h: 1073

ARArithOpStruct = struct_ARArithOpStruct # /opt/dockethead/include/ar.h: 1146

ARFieldValueOrArithStruct = struct_ARFieldValueOrArithStruct # /opt/dockethead/include/ar.h: 1137

ARRelOpStruct = struct_ARRelOpStruct # /opt/dockethead/include/ar.h: 1170

ARAndOrStruct = struct_ARAndOrStruct # /opt/dockethead/include/ar.h: 1183

ARQualifierList = struct_ARQualifierList # /opt/dockethead/include/ar.h: 1211

ARSortStruct = struct_ARSortStruct # /opt/dockethead/include/ar.h: 1221

ARSortList = struct_ARSortList # /opt/dockethead/include/ar.h: 1229

ARSortListList = struct_ARSortListList # /opt/dockethead/include/ar.h: 1237

ARStatisticsResultStruct = struct_ARStatisticsResultStruct # /opt/dockethead/include/ar.h: 1251

ARStatisticsResultList = struct_ARStatisticsResultList # /opt/dockethead/include/ar.h: 1259

ARIndexStruct = struct_ARIndexStruct # /opt/dockethead/include/ar.h: 1270

ARIndexList = struct_ARIndexList # /opt/dockethead/include/ar.h: 1278

ARIndexListList = struct_ARIndexListList # /opt/dockethead/include/ar.h: 1286

ARDayStruct = struct_ARDayStruct # /opt/dockethead/include/ar.h: 1301

ARArchiveInfoStruct = struct_ARArchiveInfoStruct # /opt/dockethead/include/ar.h: 1317

ARArchiveInfoList = struct_ARArchiveInfoList # /opt/dockethead/include/ar.h: 1325

ARAuditInfoStruct = struct_ARAuditInfoStruct # /opt/dockethead/include/ar.h: 1343

ARAuditInfoList = struct_ARAuditInfoList # /opt/dockethead/include/ar.h: 1349

ARPropStruct = struct_ARPropStruct # /opt/dockethead/include/ar.h: 1393

ARPropList = struct_ARPropList # /opt/dockethead/include/ar.h: 1401

ARPropListList = struct_ARPropListList # /opt/dockethead/include/ar.h: 1409

ARDisplayInstanceStruct = struct_ARDisplayInstanceStruct # /opt/dockethead/include/ar.h: 1417

ARDisplayInstanceList = struct_ARDisplayInstanceList # /opt/dockethead/include/ar.h: 1428

ARDisplayInstanceListList = struct_ARDisplayInstanceListList # /opt/dockethead/include/ar.h: 1436

ARDisplayInstanceListPtrList = struct_ARDisplayInstanceListPtrList # /opt/dockethead/include/ar.h: 1444

ARAssignFieldStruct = struct_ARAssignFieldStruct # /opt/dockethead/include/ar.h: 2795

ARDDEStruct = struct_ARDDEStruct # /opt/dockethead/include/ar.h: 2810

ARAssignSQLStruct = struct_ARAssignSQLStruct # /opt/dockethead/include/ar.h: 2820

ARCOMValueStruct = struct_ARCOMValueStruct # /opt/dockethead/include/ar.h: 2847

ARCOMMethodParmStruct = struct_ARCOMMethodParmStruct # /opt/dockethead/include/ar.h: 2856

ARCOMMethodParmList = struct_ARCOMMethodParmList # /opt/dockethead/include/ar.h: 2864

ARCOMMethodStruct = struct_ARCOMMethodStruct # /opt/dockethead/include/ar.h: 2875

ARCOMMethodList = struct_ARCOMMethodList # /opt/dockethead/include/ar.h: 2883

ARAutomationStruct = struct_ARAutomationStruct # /opt/dockethead/include/ar.h: 2894

ARArithOpAssignStruct = struct_ARArithOpAssignStruct # /opt/dockethead/include/ar.h: 2955

ARFunctionAssignStruct = struct_ARFunctionAssignStruct # /opt/dockethead/include/ar.h: 3048

ARAssignFilterApiStruct = struct_ARAssignFilterApiStruct # /opt/dockethead/include/ar.h: 2928

ARAssignStruct = struct_ARAssignStruct # /opt/dockethead/include/ar.h: 2925

ARFieldAssignStruct = struct_ARFieldAssignStruct # /opt/dockethead/include/ar.h: 2944

ARFieldAssignList = struct_ARFieldAssignList # /opt/dockethead/include/ar.h: 2952

ARFilterActionNotifyAdvanced = struct_ARFilterActionNotifyAdvanced # /opt/dockethead/include/ar.h: 3089

ARFilterActionNotify = struct_ARFilterActionNotify # /opt/dockethead/include/ar.h: 3120

ARFilterStatusStruct = struct_ARFilterStatusStruct # /opt/dockethead/include/ar.h: 3129

ARPushFieldsStruct = struct_ARPushFieldsStruct # /opt/dockethead/include/ar.h: 3137

ARPushFieldsList = struct_ARPushFieldsList # /opt/dockethead/include/ar.h: 3145

ARPushFieldsActionStruct = struct_ARPushFieldsActionStruct # /opt/dockethead/include/ar.h: 3154

ARSetFieldsActionStruct = struct_ARSetFieldsActionStruct # /opt/dockethead/include/ar.h: 3163

ARSQLStruct = struct_ARSQLStruct # /opt/dockethead/include/ar.h: 3170

AROverlaidStruct = struct_AROverlaidStruct # /opt/dockethead/include/ar.h: 3180

ARGotoActionStruct = struct_ARGotoActionStruct # /opt/dockethead/include/ar.h: 3193

ARCallGuideStruct = struct_ARCallGuideStruct # /opt/dockethead/include/ar.h: 3207

ARExitGuideStruct = struct_ARExitGuideStruct # /opt/dockethead/include/ar.h: 3223

ARGotoGuideLabelStruct = struct_ARGotoGuideLabelStruct # /opt/dockethead/include/ar.h: 3229

ARSvcActionStruct = struct_ARSvcActionStruct # /opt/dockethead/include/ar.h: 3240

ARFilterActionStruct = struct_ARFilterActionStruct # /opt/dockethead/include/ar.h: 3279

ARFilterActionList = struct_ARFilterActionList # /opt/dockethead/include/ar.h: 3286

ARFilterActionListList = struct_ARFilterActionListList # /opt/dockethead/include/ar.h: 3294

ARMacroParmStruct = struct_ARMacroParmStruct # /opt/dockethead/include/ar.h: 3348

ARMacroParmList = struct_ARMacroParmList # /opt/dockethead/include/ar.h: 3355

ARActiveLinkMacroStruct = struct_ARActiveLinkMacroStruct # /opt/dockethead/include/ar.h: 3363

ARFieldCharacteristics = struct_ARFieldCharacteristics # /opt/dockethead/include/ar.h: 3387

AROpenDlgStruct = struct_AROpenDlgStruct # /opt/dockethead/include/ar.h: 3406

ARCommitChangesStruct = struct_ARCommitChangesStruct # /opt/dockethead/include/ar.h: 3412

ARCloseWndStruct = struct_ARCloseWndStruct # /opt/dockethead/include/ar.h: 3418

ARWaitStruct = struct_ARWaitStruct # /opt/dockethead/include/ar.h: 3424

ARActiveLinkActionStruct = struct_ARActiveLinkActionStruct # /opt/dockethead/include/ar.h: 3539

ARActiveLinkActionList = struct_ARActiveLinkActionList # /opt/dockethead/include/ar.h: 3546

ARActiveLinkActionListList = struct_ARActiveLinkActionListList # /opt/dockethead/include/ar.h: 3554

ARPermissionStruct = struct_ARPermissionStruct # /opt/dockethead/include/ar.h: 3569

ARPermissionList = struct_ARPermissionList # /opt/dockethead/include/ar.h: 3576

ARPermissionListList = struct_ARPermissionListList # /opt/dockethead/include/ar.h: 3583

ARPermissionListPtrList = struct_ARPermissionListPtrList # /opt/dockethead/include/ar.h: 3590

ARGroupInfoStruct = struct_ARGroupInfoStruct # /opt/dockethead/include/ar.h: 3612

ARGroupInfoList = struct_ARGroupInfoList # /opt/dockethead/include/ar.h: 3619

ARRoleInfoStruct = struct_ARRoleInfoStruct # /opt/dockethead/include/ar.h: 3628

ARRoleInfoList = struct_ARRoleInfoList # /opt/dockethead/include/ar.h: 3636

ARUserLicenseStruct = struct_ARUserLicenseStruct # /opt/dockethead/include/ar.h: 3655

ARUserLicenseList = struct_ARUserLicenseList # /opt/dockethead/include/ar.h: 3663

ARAppLicensePoolList = struct_ARAppLicensePoolList # /opt/dockethead/include/ar.h: 3671

ARLicenseNameList = struct_ARLicenseNameList # /opt/dockethead/include/ar.h: 3678

ARLicenseDateStruct = struct_ARLicenseDateStruct # /opt/dockethead/include/ar.h: 3687

ARLicenseInfoStruct = struct_ARLicenseInfoStruct # /opt/dockethead/include/ar.h: 3703

ARLicenseInfoList = struct_ARLicenseInfoList # /opt/dockethead/include/ar.h: 3711

ARLicenseValidStruct = struct_ARLicenseValidStruct # /opt/dockethead/include/ar.h: 3721

ARLicenseValidList = struct_ARLicenseValidList # /opt/dockethead/include/ar.h: 3729

ARHostIDTypeList = struct_ARHostIDTypeList # /opt/dockethead/include/ar.h: 3737

ARUserInfoStruct = struct_ARUserInfoStruct # /opt/dockethead/include/ar.h: 3754

ARUserInfoList = struct_ARUserInfoList # /opt/dockethead/include/ar.h: 3761

ARWorkflowLockStruct = struct_ARWorkflowLockStruct # /opt/dockethead/include/ar.h: 3770

ARIntegerLimitsStruct = struct_ARIntegerLimitsStruct # /opt/dockethead/include/ar.h: 3785

ARRealLimitsStruct = struct_ARRealLimitsStruct # /opt/dockethead/include/ar.h: 3795

ARCharLimitsStruct = struct_ARCharLimitsStruct # /opt/dockethead/include/ar.h: 3837

ARDiaryLimitsStruct = struct_ARDiaryLimitsStruct # /opt/dockethead/include/ar.h: 3843

AREnumItemStruct = struct_AREnumItemStruct # /opt/dockethead/include/ar.h: 3854

AREnumItemList = struct_AREnumItemList # /opt/dockethead/include/ar.h: 3861

AREnumQueryStruct = struct_AREnumQueryStruct # /opt/dockethead/include/ar.h: 3871

AREnumLimitsStruct = struct_AREnumLimitsStruct # /opt/dockethead/include/ar.h: 3883

ARAttachLimitsStruct = struct_ARAttachLimitsStruct # /opt/dockethead/include/ar.h: 3894

ARTableLimitsStruct = struct_ARTableLimitsStruct # /opt/dockethead/include/ar.h: 3911

ARColumnLimitsStruct = struct_ARColumnLimitsStruct # /opt/dockethead/include/ar.h: 3931

ARDecimalLimitsStruct = struct_ARDecimalLimitsStruct # /opt/dockethead/include/ar.h: 3939

ARViewLimits = struct_ARViewLimits # /opt/dockethead/include/ar.h: 3945

ARDisplayLimits = struct_ARDisplayLimits # /opt/dockethead/include/ar.h: 3951

ARDateLimitsStruct = struct_ARDateLimitsStruct # /opt/dockethead/include/ar.h: 3958

ARCurrencyDetailStruct = struct_ARCurrencyDetailStruct # /opt/dockethead/include/ar.h: 3968

ARCurrencyDetailList = struct_ARCurrencyDetailList # /opt/dockethead/include/ar.h: 3976

ARCurrencyLimitsStruct = struct_ARCurrencyLimitsStruct # /opt/dockethead/include/ar.h: 3987

ARFieldLimitStruct = struct_ARFieldLimitStruct # /opt/dockethead/include/ar.h: 4013

ARFieldLimitList = struct_ARFieldLimitList # /opt/dockethead/include/ar.h: 4019

ARFieldLimitPtrList = struct_ARFieldLimitPtrList # /opt/dockethead/include/ar.h: 4025

ARCharMenuStruct = struct_ARCharMenuStruct # /opt/dockethead/include/ar.h: 4157

ARCharMenuItemStruct = struct_ARCharMenuItemStruct # /opt/dockethead/include/ar.h: 4046

ARCharMenuQueryStruct = struct_ARCharMenuQueryStruct # /opt/dockethead/include/ar.h: 4060

ARCharMenuFileStruct = struct_ARCharMenuFileStruct # /opt/dockethead/include/ar.h: 4069

ARCharMenuSQLStruct = struct_ARCharMenuSQLStruct # /opt/dockethead/include/ar.h: 4078

ARCharMenuList = struct_ARCharMenuList # /opt/dockethead/include/ar.h: 4085

ARCharMenuSSStruct = struct_ARCharMenuSSStruct # /opt/dockethead/include/ar.h: 4096

ARCharMenuDDFormStruct = struct_ARCharMenuDDFormStruct # /opt/dockethead/include/ar.h: 4107

ARCharMenuDDFieldStruct = struct_ARCharMenuDDFieldStruct # /opt/dockethead/include/ar.h: 4114

ARCharMenuDDStruct = struct_ARCharMenuDDStruct # /opt/dockethead/include/ar.h: 4147

ARCharMenuStructList = struct_ARCharMenuStructList # /opt/dockethead/include/ar.h: 4176

ARStructItemStruct = struct_ARStructItemStruct # /opt/dockethead/include/ar.h: 4398

ARStructItemList = struct_ARStructItemList # /opt/dockethead/include/ar.h: 4405

ARServerInfoRequestList = struct_ARServerInfoRequestList # /opt/dockethead/include/ar.h: 5269

ARServerInfoStruct = struct_ARServerInfoStruct # /opt/dockethead/include/ar.h: 5276

ARServerInfoList = struct_ARServerInfoList # /opt/dockethead/include/ar.h: 5283

ARFullTextInfoRequestList = struct_ARFullTextInfoRequestList # /opt/dockethead/include/ar.h: 5337

ARFullTextInfoStruct = struct_ARFullTextInfoStruct # /opt/dockethead/include/ar.h: 5350

ARFullTextInfoList = struct_ARFullTextInfoList # /opt/dockethead/include/ar.h: 5357

ARStatusHistoryStruct = struct_ARStatusHistoryStruct # /opt/dockethead/include/ar.h: 5369

ARStatusHistoryList = struct_ARStatusHistoryList # /opt/dockethead/include/ar.h: 5376

ARDiaryStruct = struct_ARDiaryStruct # /opt/dockethead/include/ar.h: 5384

ARDiaryList = struct_ARDiaryList # /opt/dockethead/include/ar.h: 5391

AREscalationTmStruct = struct_AREscalationTmStruct # /opt/dockethead/include/ar.h: 5420

AREscalationTmList = struct_AREscalationTmList # /opt/dockethead/include/ar.h: 5427

ARJoinMappingStruct = struct_ARJoinMappingStruct # /opt/dockethead/include/ar.h: 5458

ARViewMappingStruct = struct_ARViewMappingStruct # /opt/dockethead/include/ar.h: 5464

ARVendorMappingStruct = struct_ARVendorMappingStruct # /opt/dockethead/include/ar.h: 5470

ARInheritanceMappingStruct = struct_ARInheritanceMappingStruct # /opt/dockethead/include/ar.h: 5486

ARFieldMappingStruct = struct_ARFieldMappingStruct # /opt/dockethead/include/ar.h: 5500

ARFieldMappingList = struct_ARFieldMappingList # /opt/dockethead/include/ar.h: 5507

ARFieldMappingPtrList = struct_ARFieldMappingPtrList # /opt/dockethead/include/ar.h: 5514

ARJoinSchema = struct_ARJoinSchema # /opt/dockethead/include/ar.h: 5615

ARViewSchema = struct_ARViewSchema # /opt/dockethead/include/ar.h: 5621

ARVendorSchema = struct_ARVendorSchema # /opt/dockethead/include/ar.h: 5629

ARCompoundSchema = struct_ARCompoundSchema # /opt/dockethead/include/ar.h: 5641

ARCompoundSchemaList = struct_ARCompoundSchemaList # /opt/dockethead/include/ar.h: 5648

ARDataMappingInfoStruct = struct_ARDataMappingInfoStruct # /opt/dockethead/include/ar.h: 5660

ARDataMappingInfoList = struct_ARDataMappingInfoList # /opt/dockethead/include/ar.h: 5667

ARSchemaInheritanceStruct = struct_ARSchemaInheritanceStruct # /opt/dockethead/include/ar.h: 5676

ARSchemaInheritanceList = struct_ARSchemaInheritanceList # /opt/dockethead/include/ar.h: 5683

ARSchemaInheritanceListList = struct_ARSchemaInheritanceListList # /opt/dockethead/include/ar.h: 5690

ARSupportFileInfoStruct = struct_ARSupportFileInfoStruct # /opt/dockethead/include/ar.h: 5704

ARSupportFileInfoList = struct_ARSupportFileInfoList # /opt/dockethead/include/ar.h: 5711

ARStatisticsStruct = struct_ARStatisticsStruct # /opt/dockethead/include/ar.h: 5720

ARStatisticsList = struct_ARStatisticsList # /opt/dockethead/include/ar.h: 5727

ARDisplayStruct = struct_ARDisplayStruct # /opt/dockethead/include/ar.h: 5762

ARDisplayList = struct_ARDisplayList # /opt/dockethead/include/ar.h: 5769

ARContainerOwnerObj = struct_ARContainerOwnerObj # /opt/dockethead/include/ar.h: 5976

ARContainerOwnerObjList = struct_ARContainerOwnerObjList # /opt/dockethead/include/ar.h: 5983

ARContainerOwnerObjListList = struct_ARContainerOwnerObjListList # /opt/dockethead/include/ar.h: 5990

ARContainerOwnerObjId = struct_ARContainerOwnerObjId # /opt/dockethead/include/ar.h: 5997

ARContainerOwnerObjIdList = struct_ARContainerOwnerObjIdList # /opt/dockethead/include/ar.h: 6004

ARExtReferenceStruct = struct_ARExtReferenceStruct # /opt/dockethead/include/ar.h: 6014

ARReferenceUnion = struct_ARReferenceUnion # /opt/dockethead/include/ar.h: 6028

ARReferenceStruct = struct_ARReferenceStruct # /opt/dockethead/include/ar.h: 6037

ARReferenceList = struct_ARReferenceList # /opt/dockethead/include/ar.h: 6044

ARReferenceListList = struct_ARReferenceListList # /opt/dockethead/include/ar.h: 6051

ARReferenceTypeList = struct_ARReferenceTypeList # /opt/dockethead/include/ar.h: 6058

ARContainerInfo = struct_ARContainerInfo # /opt/dockethead/include/ar.h: 6067

ARContainerInfoList = struct_ARContainerInfoList # /opt/dockethead/include/ar.h: 6074

ARContainerTypeList = struct_ARContainerTypeList # /opt/dockethead/include/ar.h: 6081

ARSignalStruct = struct_ARSignalStruct # /opt/dockethead/include/ar.h: 6106

ARSignalList = struct_ARSignalList # /opt/dockethead/include/ar.h: 6113

ARWorkflowConnectStruct = struct_ARWorkflowConnectStruct # /opt/dockethead/include/ar.h: 6131

ARWorkflowConnectList = struct_ARWorkflowConnectList # /opt/dockethead/include/ar.h: 6138

ARLocalizedRequestStruct = struct_ARLocalizedRequestStruct # /opt/dockethead/include/ar.h: 6155

ARLocalizedRequestList = struct_ARLocalizedRequestList # /opt/dockethead/include/ar.h: 6162

ARConfigSvrEvents = struct_ARConfigSvrEvents # /opt/dockethead/include/ar.h: 6286

ARFieldInfoStruct = struct_ARFieldInfoStruct # /opt/dockethead/include/ar.h: 6309

ARFieldInfoList = struct_ARFieldInfoList # /opt/dockethead/include/ar.h: 6316

ARExportFieldInfoStruct = struct_ARExportFieldInfoStruct # /opt/dockethead/include/ar.h: 6342

ARExportFieldInfoList = struct_ARExportFieldInfoList # /opt/dockethead/include/ar.h: 6349

ARVuiInfoStruct = struct_ARVuiInfoStruct # /opt/dockethead/include/ar.h: 6365

ARVuiInfoList = struct_ARVuiInfoList # /opt/dockethead/include/ar.h: 6372

ARXMLInputDoc = struct_ARXMLInputDoc # /opt/dockethead/include/ar.h: 6543

ARXMLOutputDoc = struct_ARXMLOutputDoc # /opt/dockethead/include/ar.h: 6555

ARXMLParsedStream = struct_ARXMLParsedStream # /opt/dockethead/include/ar.h: 6561

ARXMLParserHandle = struct_ARXMLParserHandle # /opt/dockethead/include/ar.h: 6567

ARDateStruct = struct_ARDateStruct # /opt/dockethead/include/ar.h: 6623

ARComplexEntryGetIn = struct_ARComplexEntryGetIn # /opt/dockethead/include/ar.h: 6713

ARComplexEntryGetOut = struct_ARComplexEntryGetOut # /opt/dockethead/include/ar.h: 6741

ARComplexEntryCreate = struct_ARComplexEntryCreate # /opt/dockethead/include/ar.h: 6758

ARComplexEntrySet = struct_ARComplexEntrySet # /opt/dockethead/include/ar.h: 6780

ARComplexEntryService = struct_ARComplexEntryService # /opt/dockethead/include/ar.h: 6810

ARComplexEntryServiceOut = struct_ARComplexEntryServiceOut # /opt/dockethead/include/ar.h: 6828

ARComplexEntryGetInList = struct_ARComplexEntryGetInList # /opt/dockethead/include/ar.h: 6710

ARComplexEntryGetOutList = struct_ARComplexEntryGetOutList # /opt/dockethead/include/ar.h: 6738

ARComplexEntryCreateList = struct_ARComplexEntryCreateList # /opt/dockethead/include/ar.h: 6756

ARComplexEntrySetList = struct_ARComplexEntrySetList # /opt/dockethead/include/ar.h: 6778

ARComplexEntryOptions = struct_ARComplexEntryOptions # /opt/dockethead/include/ar.h: 6802

ARComplexEntryServiceList = struct_ARComplexEntryServiceList # /opt/dockethead/include/ar.h: 6808

ARComplexEntryServiceOutList = struct_ARComplexEntryServiceOutList # /opt/dockethead/include/ar.h: 6826

ARXMLValueInfoStruct = struct_ARXMLValueInfoStruct # /opt/dockethead/include/ar.h: 6841

ARXMLValueInfoList = struct_ARXMLValueInfoList # /opt/dockethead/include/ar.h: 6848

ARObjectInfoStruct = struct_ARObjectInfoStruct # /opt/dockethead/include/ar.h: 6865

ARObjectInfoList = struct_ARObjectInfoList # /opt/dockethead/include/ar.h: 6863

AREntryReturn = struct_AREntryReturn # /opt/dockethead/include/ar.h: 6899

ARXMLEntryReturn = struct_ARXMLEntryReturn # /opt/dockethead/include/ar.h: 6905

ARBulkEntryReturn = struct_ARBulkEntryReturn # /opt/dockethead/include/ar.h: 6920

ARBulkEntryReturnList = struct_ARBulkEntryReturnList # /opt/dockethead/include/ar.h: 6926

AREntryBlockStruct = struct_AREntryBlockStruct # /opt/dockethead/include/ar.h: 6933

AREntryBlockList = struct_AREntryBlockList # /opt/dockethead/include/ar.h: 6938

ARImageDataStruct = struct_ARImageDataStruct # /opt/dockethead/include/ar.h: 6970

ARImageDataList = struct_ARImageDataList # /opt/dockethead/include/ar.h: 6977

ARObjectChangeTimestamps = struct_ARObjectChangeTimestamps # /opt/dockethead/include/ar.h: 6985

ARObjectChangeTimestampList = struct_ARObjectChangeTimestampList # /opt/dockethead/include/ar.h: 6991

ARFilterContextStruct = struct_ARFilterContextStruct # /opt/dockethead/include/ar.h: 7032

ARSchemaContextStruct = struct_ARSchemaContextStruct # /opt/dockethead/include/ar.h: 7033

ARWfdCurrentLocation = struct_ARWfdCurrentLocation # /opt/dockethead/include/ar.h: 7019

ARWfdRmtBreakpoint = struct_ARWfdRmtBreakpoint # /opt/dockethead/include/ar.h: 7047

ARWfdRmtBreakpointList = struct_ARWfdRmtBreakpointList # /opt/dockethead/include/ar.h: 7053

ARWfdBreakpointLink = struct_ARWfdBreakpointLink # /opt/dockethead/include/ar.h: 7055

ARWfdUserContext = struct_ARWfdUserContext # /opt/dockethead/include/ar.h: 7074

ARMultiSchemaFieldIdStruct = struct_ARMultiSchemaFieldIdStruct # /opt/dockethead/include/ar.h: 7090

ARMultiSchemaFieldFuncStruct = struct_ARMultiSchemaFieldFuncStruct # /opt/dockethead/include/ar.h: 7105

ARMultiSchemaFieldIdList = struct_ARMultiSchemaFieldIdList # /opt/dockethead/include/ar.h: 7110

ARMultiSchemaFieldFuncList = struct_ARMultiSchemaFieldFuncList # /opt/dockethead/include/ar.h: 7115

ARMultiSchemaFuncCurrencyPartStruct = struct_ARMultiSchemaFuncCurrencyPartStruct # /opt/dockethead/include/ar.h: 7121

ARMultiSchemaStatHistoryValue = struct_ARMultiSchemaStatHistoryValue # /opt/dockethead/include/ar.h: 7127

ARMultiSchemaFuncStatHistoryValue = struct_ARMultiSchemaFuncStatHistoryValue # /opt/dockethead/include/ar.h: 7134

ARMultiSchemaArithOpStruct = struct_ARMultiSchemaArithOpStruct # /opt/dockethead/include/ar.h: 7186

ARMultiSchemaValueSetFuncQueryStruct = struct_ARMultiSchemaValueSetFuncQueryStruct # /opt/dockethead/include/ar.h: 7322

ARMultiSchemaFieldValueOrArithStruct = struct_ARMultiSchemaFieldValueOrArithStruct # /opt/dockethead/include/ar.h: 7154

ARMultiSchemaFuncArithOpStruct = struct_ARMultiSchemaFuncArithOpStruct # /opt/dockethead/include/ar.h: 7192

ARMultiSchemaFieldFuncValueOrArithStruct = struct_ARMultiSchemaFieldFuncValueOrArithStruct # /opt/dockethead/include/ar.h: 7171

ARMultiSchemaQualifierStruct = struct_ARMultiSchemaQualifierStruct # /opt/dockethead/include/ar.h: 7210

ARMultiSchemaAndOrStruct = struct_ARMultiSchemaAndOrStruct # /opt/dockethead/include/ar.h: 7178

ARMultiSchemaFuncQualifierStruct = struct_ARMultiSchemaFuncQualifierStruct # /opt/dockethead/include/ar.h: 7220

ARMultiSchemaFuncAndOrStruct = struct_ARMultiSchemaFuncAndOrStruct # /opt/dockethead/include/ar.h: 7184

ARMultiSchemaRelOpStruct = struct_ARMultiSchemaRelOpStruct # /opt/dockethead/include/ar.h: 7202

ARMultiSchemaFuncRelOpStruct = struct_ARMultiSchemaFuncRelOpStruct # /opt/dockethead/include/ar.h: 7208

ARMultiSchemaNestedQueryStruct = struct_ARMultiSchemaNestedQueryStruct # /opt/dockethead/include/ar.h: 7302

ARMultiSchemaRecursiveQueryStruct = struct_ARMultiSchemaRecursiveQueryStruct # /opt/dockethead/include/ar.h: 7282

ARMultiSchemaQueryFromStruct = struct_ARMultiSchemaQueryFromStruct # /opt/dockethead/include/ar.h: 7251

ARMultiSchemaNestedFuncQueryStruct = struct_ARMultiSchemaNestedFuncQueryStruct # /opt/dockethead/include/ar.h: 7308

ARMultiSchemaRecursiveFuncQueryStruct = struct_ARMultiSchemaRecursiveFuncQueryStruct # /opt/dockethead/include/ar.h: 7291

ARMultiSchemaFuncQueryFromStruct = struct_ARMultiSchemaFuncQueryFromStruct # /opt/dockethead/include/ar.h: 7264

ARMultiSchemaQueryFromList = struct_ARMultiSchemaQueryFromList # /opt/dockethead/include/ar.h: 7269

ARMultiSchemaFuncQueryFromList = struct_ARMultiSchemaFuncQueryFromList # /opt/dockethead/include/ar.h: 7274

ARMultiSchemaValueSetQueryStruct = struct_ARMultiSchemaValueSetQueryStruct # /opt/dockethead/include/ar.h: 7320

ARMultiSchemaSortStruct = struct_ARMultiSchemaSortStruct # /opt/dockethead/include/ar.h: 7333

ARMultiSchemaSortList = struct_ARMultiSchemaSortList # /opt/dockethead/include/ar.h: 7338

ARMultiSchemaFieldValueStruct = struct_ARMultiSchemaFieldValueStruct # /opt/dockethead/include/ar.h: 7343

ARMultiSchemaFieldValueList = struct_ARMultiSchemaFieldValueList # /opt/dockethead/include/ar.h: 7350

ARMultiSchemaFieldValueListList = struct_ARMultiSchemaFieldValueListList # /opt/dockethead/include/ar.h: 7355

ARMultiSchemaFieldFuncValueStruct = struct_ARMultiSchemaFieldFuncValueStruct # /opt/dockethead/include/ar.h: 7360

ARMultiSchemaFieldFuncValueList = struct_ARMultiSchemaFieldFuncValueList # /opt/dockethead/include/ar.h: 7365

ARMultiSchemaFieldFuncValueListList = struct_ARMultiSchemaFieldFuncValueListList # /opt/dockethead/include/ar.h: 7370

ARTaskCheckpointObj = struct_ARTaskCheckpointObj # /opt/dockethead/include/ar.h: 7395

ARTaskCheckpointObjList = struct_ARTaskCheckpointObjList # /opt/dockethead/include/ar.h: 7401

ARTaskCheckpoint = struct_ARTaskCheckpoint # /opt/dockethead/include/ar.h: 7411

ARTaskCheckpointList = struct_ARTaskCheckpointList # /opt/dockethead/include/ar.h: 7417

ARTask = struct_ARTask # /opt/dockethead/include/ar.h: 7430

ARTaskList = struct_ARTaskList # /opt/dockethead/include/ar.h: 7436

ARVercntlObject = struct_ARVercntlObject # /opt/dockethead/include/ar.h: 7442

ARVercntlObjectList = struct_ARVercntlObjectList # /opt/dockethead/include/ar.h: 7449

ARTaskInfo = struct_ARTaskInfo # /opt/dockethead/include/ar.h: 7460

ARTaskInfoList = struct_ARTaskInfoList # /opt/dockethead/include/ar.h: 7467

# No inserted files

