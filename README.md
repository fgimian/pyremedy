# PyRemedy

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/fgimian/pyremedy/blob/master/LICENSE)

![PyRemedy Logo](https://raw.githubusercontent.com/fgimian/pyremedy/master/images/pyremedy-logo.png)

Artwork courtesy of
[Open Clip Art Library](http://openclipart.org/detail/192888/tux-nurse-1-by-merlin2525-192888)

## Introduction

PyRemedy is a simple library for interacting with Remedy ARS in Python.  It
primarily focuses on CRUD operations.

I intend for this library to stay simple and minimal, therefore I kindly ask
that any additional major features are not submitted.  You're welcome to fork
this project if you wish to extend it and build a more complete interface for
Remedy ARS similar to PyARS.

## Quick Start

Please follow the
[installation instructions](http://pyremedy.readthedocs.io/en/latest/#installation)
in the [documentation](http://pyremedy.readthedocs.io/) to install PyRemedy.

A sample of a PyRemedy script which retrieves a list of entries can be found
below:

```python
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

## Documentation

Please check out the
[PyRemedy documentation at Read the Docs](http://pyremedy.readthedocs.org/).

You may generate the documentation as follows:

```python
pip install sphinx
cd docs
make html
```

Documentation will then be available under **docs/_build/html/index.html**.

## License

PyRemedy is released under the **MIT** license. Please see the
[LICENSE](https://github.com/fgimian/pyremedy/blob/master/LICENSE)
file for more details.

## TODO

- **Ensure that date timezone conversion is correct**: I'm currently simply
  using datetime.fromtimestamp to convert epoch timestamps returned from
  Remedy but this assumes that Remedy's timezone is the same as the server
  running the script.
- **Support attachment fields**: It would be ideal to support downloading and
  uploading attachments using Remedy attachment fields.
- **Determine if we can test authentication against the user**: The
  ARVerifyUser function never seems to return errors when used with the
  8.x version of the Remedy API.  At present, it's only possible to know if
  your account is invalid when you run a method such as query or create.
- **Write unit tests for the library**: This is technically difficult to do
  due to lack of test Remedy server.  A real live server test would really be
  the best way to test this library and that currently isn't plausible.
- **Deal with the currency data type if possible**: A few schemas we deal with
  contain a few fields of type AR_DATA_TYPE_CURRENCY which is not currently
  handled.  Here's some useful code I wrote to grab details of the currency
  for when this feature is looked at...

    ```
    currency_struct = value_struct.u.currencyVal.contents
    <class 'pyremedy.arh.String'> (e.g. .00)
    print('value:', currency_struct.value)
    <type 'str'> (e.g. AUD)
    print('currencyCode:', currency_struct.currencyCode)
    <type 'int'> (epoch timestamp)
    print('conversionDate:', currency_struct.conversionDate)
    <class 'pyremedy.arh.struct_ARFuncCurrencyList'>
    print('funcList:', currency_struct.funcList)
    ```

- **Implement multiple caching backends**: I'm currently using a few dicts to
  store schemas, field mappings and enum mappings to ensure that we don't
  unnecessarily hit the Remedy server.  It would be ideal to support a custom
  caching mechanism so users could use redis or memcache and the results could
  potentially last a restart (in the case of redis).
- **Implement query enums if possible**: The third type of enum (query) is not
  currently supported primarily due to the fact I can't find an example of its
  use to test and develop against.

    Here's some useful code I wrote to grab details of the query enum...

    ```
    query_list = field_enum_limits_list.u.queryList
    print("schema: %s" % query_list.schema)
    print("server: %s" % query_list.server)
    qualifier: query_list.qualifier
    print("nameField: %d" % query_list.nameField)
    print("numberField: %d" % query_list.numberField)
    ```

- **Support for Windows**: I haven't really invested any time in attempting to
  support Windows systems as I don't foresee a big interest in such
  compatibility.
- **Support for 32-bit Linux systems**: Due to the fact that 32-bit Remedy C
  code is heavily affected by the -malign-double option, this is rather tricky
  to implement.  Firstly, the ctypes _pack_ directive would be required for
  many of the structs defined, but for these to work, a custom build of Python
  [repaired a ctypes bug](http://ufpr.dl.sourceforge.net/project/pyars/python-patch/pyars-python272-patch)
  is also needed.  Further to this, the ARByteList struct will need to be
  modified to exclude the noval_ attribute in 32-bit systems as is done in
  the original source code by Remedy.
