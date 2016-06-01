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
