# PyRemedy #

*A simple remedy for remedy*

## Introduction ##

PyRemedy is a simple library for interacting with Remedy ARS in Python.  It
primarily focuses on CRUD operations.

I intend for this library to stay simple and minimal, therefore I kindly ask
that any additional major features are not submitted.  You're welcome to fork
this project if you wish to extend it and build a more complete interface for
Remedy ARS similar to PyARS.

This library was heavily influenced by the following:

* [PyARS](http://pyars.sourceforge.net/): The reference for Remedy
  implementations in Python.  I'd like to sincerely thank Axel for spending
  the time to write it.  It has served as a great reference.
* [Remedy::ARSTools](http://search.cpan.org/~ahicox/Remedy-ARSTools-1/ARSTools.pod):
  This library has accomplished in Perl something similar to what I need in
  Python.  The API design for PyRemedy takes a lot of inspiration from it.
* [BMC Remedy Documentation](https://docs.bmc.com/docs/display/public/ars81/Developing%20an%20API%20program):
  The documentation provided by BMC is absolutely awesome and has been the main
  reference used during the development of PyRemedy.

## Installation ##

1. Download the **linux** 8.x API package from
   [RRR](https://rrr.se/cgi/index?pg=arapi) (8.11 version recommended.)
2. Extract the API to a suitable location (e.g. /opt/remedy)

   ``` bash
   sudo mkdir /opt/remedy
   sudo tar xvfz api811linux.tar.gz  -C /opt/remedy --strip 1
   ```

3. Add the shared libraries to your library path using **ldconfig** as follows

   ``` bash
   sudo bash -c "echo '# Remedy ARS support' > /etc/ld.so.conf.d/remedy.conf"
   sudo bash -c "echo /opt/remedy/lib >> /etc/ld.so.conf.d/remedy.conf"
   sudo bash -c "echo /opt/remedy/bin >> /etc/ld.so.conf.d/remedy.conf"
   sudo ldconfig
   ```

4. Now install PyRemedy using **pip** as per usual

   ``` bash
   pip install pyremedy
   ```

## Quick Start ##

``` python
from __future__ import print_function

from pyremedy import ARS, ARSError

try:
    # Initialise a connection to the Remedy ARS server
    ars = ARS(
        server='myserver.domain.com', port=1234,
        user='fots', password='password123'
    )

    # Run a query to retrieve several entries from a schema
    entries = ars.query(
        schema='HPD:Help Desk',
        qualifier="""'Status*' = "Assigned"
                     AND ('Assigned Group*+' = "My Team"
                          OR 'Owner Group+' = "My Team")""",
        fields=['Incident Number', 'Submit Date', 'Status', 'Description']
    )

    # Display each of the entries
    for entry_id, entry_values in entries:
        print('Entry ID: {}'.format(entry_id))
        print('-' * 80)
        for field, value in entry_values.items():
            print('{}: {}'.format(field, value))
        print()
except ARSError as e:
    print('ERROR: {}'.format(e))
    for message_number, message_text, appended_text in ars.errors:
        if appended_text:
            print(
                'Message {}: {} ({})'.format(
                    message_number, message_text, appended_text
                )
            )
        else:
            print('Message {}: {}'.format(message_number, message_text))
finally:
    ars.terminate()
```

## Development Notes ##

### Generating arh.py (ctypes version of ar.h) for reference ###

I now maintain my own hand-written version of ar.h converted to ctypes to ensure minimal bloat and maximum transparency.  However, it is useful to have a generated copy alongside for reference when adding any structs to this file.

To generate this file, please follow the steps below:

1. Install ctypesgen

   ``` bash
   pip install ctypesgen
   ```

2. Generate arhgen.py using the ar.h C header file

   ``` bash
   ctypesgen.py /opt/remedy/include/ar.h -o arhgen.py
   ```

## Compatibility ##

### Remedy API ###

PyRemedy has specifically been designed to work with 8.x of the Remedy API.  It
is not compatible with any Remedy API prior to this version.  However, the 8.x
API is backwards compatible with older server versions.  Our organisation is
running 7.5 which PyRemedy has no trouble with at all using the 8.1.1 API.

### Operating System Support ###

I'm proud to say that PyRemedy fully supports 64-bit Python running on Linux
systems along with 32-bit Python.  Windows is not currently supported although
support is planned.

### Python ###

Currently, only Python 2.7.x is supported by this library.  Python 3.x is not
currently supported although support is planned.
