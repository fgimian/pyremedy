from ctypes import (
    c_char_p, c_char, c_int, c_uint, c_ubyte, c_void_p, c_double, c_size_t,
    Structure, Union, POINTER
)

# Data types (artypes.h).

ARLong32 = c_int
ARULong32 = c_uint
ARUIntPtr = c_size_t

# General limits (ar.h line 67).

# max actions for 1 filter/active link
AR_MAX_ACTIONS = 25
# max size of an active link message
AR_MAX_AL_MESSAGE_SIZE = 4095
# max size of auth string
AR_MAX_AUTH_SIZE = 2047
# max size of an auto item string
AR_MAX_AUTOMATION_SIZE = 2000
# max size of a temporary buffer
AR_MAX_BUFFER_SIZE = 352
# max size of a character menu value
AR_MAX_CMENU_SIZE = 255
# max size of a user command string
AR_MAX_COMMAND_SIZE = 255
# max size of a user commandLong string
AR_MAX_COMMAND_SIZE_LONG = 4096
# max size of a custom date time format
AR_MAX_FORMAT_SIZE = 32
# max size of a dde item string
AR_MAX_DDE_ITEM = 32767
# max size of a dde service/topic name
AR_MAX_DDE_NAME = 64
# max size of a COM name
AR_MAX_COM_NAME = 1024
# max size of a method string
AR_MAX_COM_METHOD_NAME = 128
# max size of a COM clsId/methodIId
AR_MAX_COM_ID_SIZE = 128
# max size of a character type default
AR_MAX_DEFAULT_SIZE = 255
# max size of a notify email address
AR_MAX_EMAIL_ADDR = 255
# max size of an entry id in the system
AR_MAX_ENTRYID_SIZE = 15
# max size of goto label string
AR_MAX_GOTOGUIDE_LABEL_SIZE = 128
# max size of the group list field
AR_MAX_GROUPLIST_SIZE = 255
# max size for a GUID string
AR_MAX_GUID_SIZE = 30
# max size for a GUID prefix
AR_MAX_GUID_PREFIX_SIZE = 2
# max bytes in ALL columns in an index
AR_MAX_INDEX_BYTES = 255
# max fields in an index
AR_MAX_INDEX_FIELDS = 16
# max size of a language name
AR_MAX_LANG_SIZE = 15
# max size of a license name
AR_MAX_LICENSE_NAME_SIZE = 50
# max size of a license key
AR_MAX_LICENSE_KEY_SIZE = 30
# max size of a locale
AR_MAX_LOCALE_SIZE = 64
# max size of a macro value
AR_MAX_MACRO_VALUE = 255
# max menu items in any single menu for char field default sets
AR_MAX_MENU_ITEMS = 199
# max menu levels for char field default sets
AR_MAX_MENU_LEVELS = 15
# max levels for Dynamic Query and SQL menu
AR_MAX_LEVELS_DYNAMIC_MENU = 5
# max size of a status message
AR_MAX_MESSAGE_SIZE = 255
# max entries that can be handled by a multiple entries call
AR_MAX_MULT_ENTRIES = 100
# max size of a name in the system
AR_MAX_NAME_SIZE = 254
# max size of an user name type (user,group)
AR_MAX_ACCESS_NAME_SIZE = 254
# max size of an access name type
AR_MAX_ACCESS_NAME_SIZE_63 = 30
# max size of a password type
AR_MAX_PASSWORD_SIZE = 30
# max size of hashed string
AR_MAX_HASH_SIZE = 28
# max size of an encrypted password type
AR_MAX_ENCRYPTED_PASSWORD_SIZE = 120
# max number of chars in an object name
AR_MAX_NAME_CHARACTERS = 80
# max size of a notify user line
AR_MAX_NOTIFY_USER = 255
# max size of a character limit pattern
AR_MAX_PATTERN_SIZE = 255
# max size of related to field
AR_MAX_RELATED_SIZE = 128
# max size schemaid in flat file schema cache
AR_MAX_SCHEMAID_SIZE = 5
# max size of a server name
AR_MAX_SERVER_SIZE = 64
# max size of a server name
AR_MAX_LINE_LENGTH = 2048
# max size of a short description
AR_MAX_SDESC_SIZE = 254
# max size of a notify subject line
AR_MAX_SUBJECT_SIZE = 255
# max size of a host id
AR_MAX_HOSTID_SIZE = 100
# max size of targetLocation string in activeLink OpenDlg struct
AR_MAX_TARGET_STRING_SIZE = 255
# max size of user identifier
AR_MAX_USER_GUID_SIZE = 128
# max size of wait continue label
AR_MAX_WAIT_CONT_TITLE_SIZE = 64

# Filename Limits (ar.h line 126). These are restrictive so the names will be
# legal on any target system and these limits are smallest.

AR_MAX_FILENAME_SIZE = 12
AR_MAX_FILENAME_BASE = 8
AR_MAX_FULL_FILENAME = 255

# Table and column field size limits (ar.h line 180).

# max data size displayed in a column
AR_MAX_COLFLD_COLLENGTH = 255
# max len of details in svr event form
AR_MAX_SVR_EVENT_DETAILS = 255
# max len of a server event list string
AR_MAX_SVR_EVENT_LIST = 255
# maximum external table name size
AR_MAX_TABLENAME_SIZE = 2047
# max columns in a table field
AR_MAX_TBLFLD_NUMCOLS = 255
# max rows returned in a refresh
AR_MAX_TBLFLD_RETROWS = 9999

# Decimal and currency limits (ar.h line 235).

AR_MAX_DECIMAL_SIZE = 64
AR_MAX_CURRENCY_CODE_SIZE = 3
AR_MAX_CURRENCY_RATIO_SIZE = 64
AR_CURRENT_CURRENCY_RATIOS = 0

# Name for the system constants relating to the ARBoolean type (ar.h line 249).

FALSE = 0
TRUE = 1

# Codes for return values from API routines (ar.h line 264).

# successful; status may contain notes
AR_RETURN_OK = 0
# successful?; status contains details
AR_RETURN_WARNING = 1
# failure; status contains details
AR_RETURN_ERROR = 2
# failure; status may or may not contain any details
AR_RETURN_FATAL = 3
# status structure is invalid
AR_RETURN_BAD_STATUS = 4
# status for the active link action
AR_RETURN_PROMPT = 5
# status message for client accessibility
AR_RETURN_ACCESSIBLE = 6
# message type for ToolTips message action
AR_RETURN_TOOLTIP = 7

# Remedy data types (ar.h line 534).

# code for a NULL value
AR_DATA_TYPE_NULL = 0
# code indicating a keyword setting
AR_DATA_TYPE_KEYWORD = 1
# codes for the data type of a value
AR_DATA_TYPE_INTEGER = 2
AR_DATA_TYPE_REAL = 3
AR_DATA_TYPE_CHAR = 4
AR_DATA_TYPE_DIARY = 5
AR_DATA_TYPE_ENUM = 6
AR_DATA_TYPE_TIME = 7
AR_DATA_TYPE_BITMASK = 8
AR_DATA_TYPE_BYTES = 9
AR_DATA_TYPE_DECIMAL = 10
AR_DATA_TYPE_ATTACH = 11
AR_DATA_TYPE_CURRENCY = 12
AR_DATA_TYPE_DATE = 13
AR_DATA_TYPE_TIME_OF_DAY = 14

# Field data types (ar.h line 568).

# per record stored data field type
AR_FIELD_TYPE_DATA = 1
# visual trim field type
AR_FIELD_TYPE_TRIM = 2
# GUI control field type
AR_FIELD_TYPE_CONTROL = 4
# page field type
AR_FIELD_TYPE_PAGE = 8
# page holder field type
AR_FIELD_TYPE_PAGE_HOLDER = 16
# table field type
AR_FIELD_TYPE_TABLE = 32
# column field type
AR_FIELD_TYPE_COLUMN = 64
# attachment field type
AR_FIELD_TYPE_ATTACH = 128
# attachment pool type
AR_FIELD_TYPE_ATTACH_POOL = 256

# Entry retrieval limits (ar.h line 841).

# code to indicate should retrieve from result set starting with first entry
AR_START_WITH_FIRST_ENTRY = 0
# code to indicate no maximum limit for number of entries retrieved in list
AR_NO_MAX_LIST_RETRIEVE = 0
# retrieve all entries even if there is a limit on the number of entries that
# the server will return
AR_RETRIEVE_ALL_ENTRIES = 999999999

# Enum styles (ar.h line 3845).

# list auto-indexed starting at 0
AR_ENUM_STYLE_REGULAR = 1
# list indexed manually, gaps in numbers OK
AR_ENUM_STYLE_CUSTOM = 2
# search performed to find name/number pairs
AR_ENUM_STYLE_QUERY = 3

# Schema types (ar.h line 5525).

# get list of all schemas
AR_LIST_SCHEMA_ALL = 0
# get list of all regular schemas
AR_LIST_SCHEMA_REGULAR = 1
# get list of all join schemas
AR_LIST_SCHEMA_JOIN = 2
# get list of all view schemas
AR_LIST_SCHEMA_VIEW = 3
# get list of all schemas depending on given schema
AR_LIST_SCHEMA_UPLINK = 4
# get list of all schemas the given schema bases on
AR_LIST_SCHEMA_DOWNLINK = 5
# get list of all dialog schemas
AR_LIST_SCHEMA_DIALOG = 6
# get list of all schemas with database fields
AR_LIST_SCHEMA_ALL_WITH_DATA = 7
# get list of all vendor schemas
AR_LIST_SCHEMA_VENDOR = 8
# get list of all schemas allowed in multi-form searches
AR_LIST_SCHEMA_ALLOWED_IN_MFSEARCH = 9

# SetEntry options (ar.h line 5555).

# don't enforce join referential integrity
AR_JOIN_SETOPTION_NONE = 0
# enforce join referential integrity For internal API workflow
AR_JOIN_SETOPTION_REF = 1

# DeleteEntry options (ar.h line 5566).

# individual entries will be deleted only when the entry can be retrieved
# through the join schema
AR_JOIN_DELOPTION_NONE = 0
# delete individual entries even when the entry cannot be retrieved from the
# join schema. Error will be ignored for those entry pieces that are no longer
# existing.
AR_JOIN_DELOPTION_FORCE = 1

# Type definitions (ar.h line 275).

# boolean flag set to TRUE or FALSE
ARBoolean = c_ubyte
# structure to hold an entry id value
AREntryIdType = c_char * (AR_MAX_ENTRYID_SIZE + 1)
# structure to hold an internal id
ARInternalId = ARULong32
# structure to hold an object name
ARNameType = c_char * (AR_MAX_NAME_SIZE + 1)
# structure to hold password
ARPasswordType = c_char * (AR_MAX_PASSWORD_SIZE + 1)
# structure to hold an auth string
ARAuthType = c_char * (AR_MAX_AUTH_SIZE + 1)
# structure to hold a file name
ARFileNameType = c_char * (AR_MAX_FULL_FILENAME + 1)
# structure to hold an access name
ARAccessNameType = c_char * (AR_MAX_ACCESS_NAME_SIZE + 1)
# structure to hold an encrypted password
AREncryptedPasswordType = c_char * (AR_MAX_ENCRYPTED_PASSWORD_SIZE + 1)
# structure to hold a server name
ARServerNameType = c_char * (AR_MAX_SERVER_SIZE + 1)
# timestamp; Unix style timestamp (seconds since Jan. 1, 1970)
ARTimestamp = ARLong32
# structure to hold a license name
ARLicenseNameType = c_char * (AR_MAX_LICENSE_NAME_SIZE + 1)
# structure to hold a license key
ARLicenseKeyType = c_char * (AR_MAX_LICENSE_KEY_SIZE + 1)
# used to hold host id string
ARHostIDType = c_char * (AR_MAX_HOSTID_SIZE + 1)
# structure to hold a locale string
ARLocaleType = c_char * (AR_MAX_LOCALE_SIZE + 1)
# structure to hold a menu entry
ARCMenuType = c_char * (AR_MAX_CMENU_SIZE + 1)
# structure to hold a table name
ARTableNameType = c_char * (AR_MAX_TABLENAME_SIZE + 1)
# (seconds since midnight 00.00.00)
ARTime = ARLong32
ARCurrencyCodeType = c_char * (AR_MAX_CURRENCY_CODE_SIZE + 1)


class ARNameList(Structure):
    """List of 0 or more object names (ar.h line 354)."""
    _fields_ = [
        ('numItems', c_uint),
        ('nameList', POINTER(ARNameType))
    ]


class ARInternalIdList(Structure):
    """List of 0 or more internal ids (ar.h line 330)."""
    _fields_ = [
        ('numItems', c_uint),
        ('internalIdList', POINTER(ARInternalId))
    ]


class AREntryIdList(Structure):
    """List of 0 or more entry ids (ar.h line 322)."""
    _fields_ = [
        ('numItems', c_uint),
        ('entryIdList', POINTER(AREntryIdType))
    ]


class ARByteList(Structure):
    """Byte stream (ar.h line 447)."""
    _fields_ = [
        # type of list
        ('type', ARULong32),
        ('noval_', ARULong32),
        # length of bytes
        ('numItems', c_uint),
        # not NULL terminated
        ('bytes', POINTER(c_ubyte))
    ]


class ARLocalizationInfo(Structure):
    """Localisation information (ar.h line 456)."""
    _fields_ = [
        ('locale', c_char * (AR_MAX_LOCALE_SIZE + 1)),
        ('charSet', c_char * (AR_MAX_LANG_SIZE + 1)),
        ('timeZone', c_char * (AR_MAX_LOCALE_SIZE + 1)),
        ('customDateFormat', c_char * (AR_MAX_FORMAT_SIZE + 1)),
        ('customTimeFormat', c_char * (AR_MAX_FORMAT_SIZE + 1)),
        ('separators', c_char * (AR_MAX_LANG_SIZE + 1))
    ]


class ARControlStruct(Structure):
    """Control record containing information about the user and the
    environment (ar.h line 467).  An instance of this structure will be the
    first parameter of all the calls supported by the AR system.

    .. note:: Server is listed last in the structure below as it is not passed
       in the RPC call.  It is not needed on the server (who already knows
       who he is).  By placing it last, there can still be a "clean" mapping
       of the first part of the record with the RPC structure.
    """

    _fields_ = [
        # id assigned and used by the system for efficient cache access
        ('cacheId', ARLong32),
        # time at which the operation was performed
        ('operationTime', ARTimestamp),
        # username and password for access control
        ('user', ARAccessNameType),
        ('password', ARPasswordType),
        # locale information
        ('localeInfo', ARLocalizationInfo),
        # API session identifier
        ('sessionId', ARUIntPtr),
        # Windows domain
        ('authString', ARAuthType),
        # server to access
        ('server', c_char * (AR_MAX_SERVER_SIZE + 1))
    ]


class ARStatusStruct(Structure):
    """Type of error (ar.h line 498)."""
    _fields_ = [
        ('messageType', c_uint),
        ('messageNum', ARLong32),
        ('messageText', c_char_p),
        ('appendedText', c_char_p)
    ]


class ARStatusList(Structure):
    """List of 0 or more status messages (ar.h line 508)."""
    _fields_ = [
        ('numItems', c_uint),
        ('statusList', POINTER(ARStatusStruct))
    ]


class ARCoordStruct(Structure):
    """Coordinates in typographic points (i.e. pixels) (ar.h line 694)."""
    _fields_ = [
        ('x', ARLong32),
        ('y', ARLong32)
    ]


class ARCoordList(Structure):
    """Ordered list of 0 or more coordinates (ar.h line 701)."""
    _fields_ = [
        ('numItems', c_uint),
        ('coords', POINTER(ARCoordStruct))
    ]


class ARBufStruct(Structure):
    """A generic buffer (ar.h line 714)."""
    _fields_ = [
        ('bufSize', ARULong32),
        ('buffer', POINTER(c_ubyte)),
    ]


class ARLocUnion(Union):
    """Union relating to locating an attachment (ar.h line 722)."""
    _fields_ = [
        # filename to open
        ('filename', c_char_p),
        # memory buffer
        ('buf', ARBufStruct)
    ]


class ARLocStruct(Structure):
    """Structure relating to locating an attachment (ar.h line 722)."""
    _fields_ = [
        # AR_LOC_FILENAME | AR_LOC_BUFFER
        ('locType', ARULong32),
        ('u', ARLocUnion)
    ]


class ARAttachStruct(Structure):
    """An attachment (ar.h line 734)."""
    _fields_ = [
        # name of attachment
        ('name', c_char_p),
        # pre-compression number of bytes
        ('origSize', ARLong32),
        # post-compression number of bytes
        ('compSize', ARLong32),
        # how to locate attachment content
        ('loc', ARLocStruct)
    ]


class ARFuncCurrencyStruct(Structure):
    """(ar.h line 744)"""
    _fields_ = [
        # numeric currency value
        ('value', c_char_p),
        # ISO currency code
        ('currencyCode', ARCurrencyCodeType)
    ]


class ARFuncCurrencyList(Structure):
    """(ar.h line 752)"""
    _fields_ = [
        ('numItems', c_uint),
        ('funcCurrencyList', POINTER(ARFuncCurrencyStruct))
    ]


class ARCurrencyStruct(Structure):
    """(ar.h line 760)"""
    _fields_ = [
        # numeric value of currency
        ('value', c_char_p),
        # ISO currency code
        ('currencyCode', ARCurrencyCodeType),
        # timestamp of conversion
        ('conversionDate', ARTimestamp),
        # list of functional currencies
        ('funcList', ARFuncCurrencyList)
    ]


class ARValueUnion(Union):
    """Union used to hold a value (ar.h line 777)."""
    _fields_ = [
        # noval_ is big enough to initialize both integer and pointer
        # union members in declarations like ARValueStruct val = { 0, {0}}
        ('noval_', c_size_t),
        ('keyNum', c_uint),
        ('intVal', ARLong32),
        ('realVal', c_double),
        ('charVal', c_char_p),
        ('diaryVal', c_char_p),
        ('enumVal', ARULong32),
        ('timeVal', ARTimestamp),
        ('maskVal', ARULong32),
        ('timeOfDayVal', ARTime),
        ('byteListVal', POINTER(ARByteList)),
        ('decimalVal', c_char_p),
        ('attachVal', POINTER(ARAttachStruct)),
        ('ulongVal', ARULong32),
        ('coordListVal', POINTER(ARCoordList)),
        ('dateVal', c_int),
        ('currencyVal', POINTER(ARCurrencyStruct)),

        # Placeholder for passing pointers through this data structure.
        # Can only be used locally - you can't XDR a pointer unless
        # you know the type of object being referenced.
        ('ptrVal', c_void_p)
    ]


class ARValueStruct(Structure):
    """Structure used to hold a value (ar.h line 777).  There is one branch
    for each datatype/property that is supported by the system.
    """

    _fields_ = [
        # AR_DATA_TYPE_xxx
        ('dataType', c_uint),
        ('u', ARValueUnion)
    ]


class ARValueList(Structure):
    """List of values (ar.h line 817)."""
    _fields_ = [
        ('numItems', c_uint),
        ('valueList', POINTER(ARValueStruct))
    ]


class AREntryListFieldStruct(Structure):
    """Definition for a field in the entry list (ar.h line 850)."""
    _fields_ = [
        ('fieldId', ARInternalId),
        ('columnWidth', c_uint),
        ('separator', c_char * 10)
    ]


class AREntryListFieldList(Structure):
    """List of 0 or more fields in entrylist (ar.h line 858)."""
    _fields_ = [
        ('numItems', c_uint),
        ('fieldsList', POINTER(AREntryListFieldStruct))
    ]


class ARFieldValueStruct(Structure):
    """An id and value for a single field (ar.h line 917)."""
    _fields_ = [
        ('fieldId', ARInternalId),
        ('value', ARValueStruct)
    ]


class ARFieldValueList(Structure):
    """List of 0 or more field/value pairs (ar.h line 925)."""
    _fields_ = [
        ('numItems', c_uint),
        ('fieldValueList', POINTER(ARFieldValueStruct))
    ]


class AREntryListFieldValueStruct(Structure):
    """Parallel entry list structures which are used to return entryList as a
    list of entryId and entry as field/value pairs (ar.h line 933).
    """

    _fields_ = [
        ('entryId', AREntryIdList),
        ('entryValues', POINTER(ARFieldValueList))
    ]


class AREntryListFieldValueList(Structure):
    """List of 0 or more entries (ar.h line 944)."""
    _fields_ = [
        ('numItems', c_uint),
        ('entryList', POINTER(AREntryListFieldValueStruct))
    ]


class ARBooleanList(Structure):
    """List of 0 or more ARBoolean (ar.h line 982)."""
    _fields_ = [
        ('numItems', c_uint),
        ('booleanList', POINTER(ARBoolean))
    ]


class ARStatHistoryValue(Structure):
    """Special selection field that stores user and time stamp information for
    each of the defined status values (ar.h line 1036).
    """

    _fields_ = [
        ('enumVal', ARULong32),
        ('userOrTime', c_uint)
    ]


class ARCurrencyPartStruct(Structure):
    """Part of a currency field that combine to represent a complete currency
    value (ar.h line 1067).
    """

    _fields_ = [
        ('fieldId', ARInternalId),
        ('partTag', c_uint),
        ('currencyCode', ARCurrencyCodeType)
    ]


class ARQualifierStruct(Structure):
    """Structure used to hold a qualification which entries to retrieve when
    creating a query result list (ARGetListEntry) or computing entry statistics
    (ARGetEntryStatistics) (ar.h line 1029 and 1189).
    """

    pass


class ARQueryValueStruct(Structure):
    """(ar.h line 1049)"""
    _fields_ = [
        ('schema', ARNameType),
        ('server', c_char * (AR_MAX_SERVER_SIZE + 1)),
        ('qualifier', POINTER(ARQualifierStruct)),
        ('valueField', ARInternalId),
        ('multiMatchCode', c_uint)
    ]


class ARArithOpStruct(Structure):
    """(ar.h line 1146)"""
    pass


class ARFieldValueOrArithUnion(Union):
    """Union used to hold values to compare in a relational qualification
    operation (ar.h line 1116).
    """

    _fields_ = [
        # noval_ is big enough to initialize both integer and pointer
        # union members in declarations like
        # ARFieldValueOrArithStruct val = { 0, {0}};
        ('noval_', c_size_t),
        ('fieldId', ARInternalId),
        ('value', ARValueStruct),
        ('arithOp', POINTER(ARArithOpStruct)),
        ('statHistory', ARStatHistoryValue),
        ('valueSet', ARValueList),
        ('variable', c_uint),
        ('queryValue', POINTER(ARQueryValueStruct)),
        ('currencyField', POINTER(ARCurrencyPartStruct))
    ]


class ARFieldValueOrArithStruct(Structure):
    """Structure used to hold values to compare in a relational qualification
    operation (ar.h line 1116).
    """

    _fields_ = [
        ('tag', c_uint),
        ('u', ARFieldValueOrArithUnion)
    ]


ARArithOpStruct._fields_ = [
    ('operation', c_uint),
    ('operandLeft', ARFieldValueOrArithStruct),
    ('operandRight', ARFieldValueOrArithStruct)
]


class ARRelOpStruct(Structure):
    """Relational qualification operator (ar.h line 1164)."""
    _fields_ = [
        ('operation', c_uint),
        ('operandLeft', ARFieldValueOrArithStruct),
        ('operandRight', ARFieldValueOrArithStruct),
    ]


class ARAndOrStruct(Structure):
    """Logical qualification operator (ar.h line 1179)."""
    _fields_ = [
        ('operandLeft', POINTER(ARQualifierStruct)),
        ('operandRight', POINTER(ARQualifierStruct))
    ]


class ARQualifierUnion(Union):
    """Union used to hold a qualification (ar.h line 1189)."""
    _fields_ = [
        ('andor', ARAndOrStruct),
        ('notQual', POINTER(ARQualifierStruct)),
        ('relOp', POINTER(ARRelOpStruct)),
        ('fieldId', ARInternalId)
    ]


ARQualifierStruct._fields_ = [
    ('operation', c_uint),
    ('u', ARQualifierUnion)
]


class ARIntegerLimitsStruct(Structure):
    """Integer limits (ar.h line 3780)."""
    _fields_ = [
        ('rangeLow', ARLong32),
        ('rangeHigh', ARLong32)
    ]


class ARRealLimitsStruct(Structure):
    """Real number limits (ar.h line 3789)."""
    _fields_ = [
        ('rangeLow', c_double),
        ('rangeHigh', c_double),
        ('precision', c_int)
    ]


class ARCharLimitsStruct(Structure):
    """Character limits (ar.h line 3820)."""
    _fields_ = [
        ('maxLength', c_uint),
        # append or overwrite with new menu selections
        ('menuStyle', c_uint),
        # operation to use from QBE type operation
        ('qbeMatchOperation', c_uint),
        # name of character menu associated to field
        ('charMenu', ARNameType),
        # pattern, incl wildcards, value must match
        ('pattern', c_char_p),
        # Full Text options
        ('fullTextOptions', c_uint),
        # 0 for in-byte, 1 for in-char
        ('lengthUnits', c_uint),
        # 0 for Default, 1 for In-Row and 2 for Out-of-Row
        ('storageOptionForCLOB', c_uint)
    ]


class ARDiaryLimitsStruct(Structure):
    """Diary limits (ar.h line 3839)."""
    _fields_ = [
        ('fullTextOptions', c_uint)
    ]


class AREnumItemStruct(Structure):
    """Custom enum item (ar.h line 3849)."""
    _fields_ = [
        ('itemName', ARNameType),
        ('itemNumber', ARULong32)
    ]


class AREnumItemList(Structure):
    """Custom enum limits (ar.h line 3856)."""
    _fields_ = [
        ('numItems', c_uint),
        ('enumItemList', POINTER(AREnumItemStruct))
    ]


class AREnumQueryStruct(Structure):
    """Query definition for query enum limits (ar.h line 3863)."""
    _fields_ = [
        ('schema', ARNameType),
        ('server', c_char * (AR_MAX_SERVER_SIZE + 1)),
        ('qualifier', ARQualifierStruct),
        ('nameField', ARInternalId),
        ('numberField', ARInternalId)
    ]


class AREnumLimitsUnion(Union):
    """Union used to hold enum limits (ar.h line 3873)."""
    _fields_ = [
        ('regularList', ARNameList),
        ('customList', AREnumItemList),
        ('queryList', AREnumQueryStruct)
    ]


class AREnumLimitsStruct(Structure):
    """Structure used to hold enum limits (ar.h line 3873)."""
    _fields_ = [
        ('listStyle', c_uint),
        ('u', AREnumLimitsUnion)
    ]


class ARAttachLimitsStruct(Structure):
    """Attachment limits (ar.h line 3888)."""
    _fields_ = [
        # 0 means unlimited
        ('maxSize', ARULong32),
        ('attachType', c_uint),
        ('fullTextOptions', c_uint)
    ]


class ARTableLimitsStruct(Structure):
    """Table limits (ar.h line 3896)."""
    _fields_ = [
        # number of columns in table field
        ('numColumns', c_uint),
        # qualification for table field
        ('qualifier', ARQualifierStruct),
        # max rows to retrieve
        ('maxRetrieve', c_uint),
        # data fields belong to this schema
        ('schema', ARNameType),
        # that schema is in this server
        ('server', ARServerNameType),
        ('sampleSchema', ARNameType),
        ('sampleServer', ARServerNameType)
    ]


class ARColumnLimitsStruct(Structure):
    """Column limits (ar.h line 3921)."""
    _fields_ = [
        # parent field column field belongs to
        ('parent', ARInternalId),
        # remote fieldId form which data comes
        ('dataField', ARInternalId),
        # data source for the above dataField
        ('dataSource', c_uint),
        # column length to display - char fields
        ('colLength', c_uint)
    ]


class ARDecimalLimitsStruct(Structure):
    """Decimal limits (ar.h line 3933)."""
    _fields_ = [
        ('rangeLow', c_char_p),
        ('rangeHigh', c_char_p),
        # number of places to right of dec point
        ('precision', c_int),
    ]


class ARViewLimits(Structure):
    """View limits (ar.h line 3941)."""
    _fields_ = [
        # 0 means unlimited length
        ('maxLength', c_uint)
    ]


class ARDisplayLimits(Structure):
    """Display limits (ar.h line 3947)."""
    _fields_ = [
        # 0 means unlimited length
        ('maxLength', c_uint),
        # 0 for in-byte, 1 for in-char
        ('lengthUnits', c_uint),
    ]


class ARDateLimitsStruct(Structure):
    """Date limits (ar.h line 3953)."""
    _fields_ = [
        # minimum date value, in julian days
        ('minDate', c_int),
        # maximum date value, in julian days
        ('maxDate', c_int)
    ]


class ARCurrencyDetailStruct(Structure):
    """Details of a currency limit (ar.h line 3963)."""
    _fields_ = [
        # currency type
        ('currencyCode', ARCurrencyCodeType),
        # number of places to right of dec point
        ('precision', c_int)
    ]


class ARCurrencyDetailList(Structure):
    """List of currency limit details (ar.h line 3971)."""
    _fields_ = [
        ('numItems', c_uint),
        ('currencyDetailList', POINTER(ARCurrencyDetailStruct))
    ]


class ARCurrencyLimitsStruct(Structure):
    """Currency limits (ar.h line 3978)."""
    _fields_ = [
        ('rangeLow', c_char_p),
        ('rangeHigh', c_char_p),
        # number of places to right of dec point
        ('precision', c_int),
        ('functionalCurrencies', ARCurrencyDetailList),
        ('allowableCurrencies', ARCurrencyDetailList),
    ]


class ARFieldLimitUnion(Union):
    """Union used to hold field limits (ar.h line 3991)."""
    _fields_ = [
        ('intLimits', ARIntegerLimitsStruct),
        ('realLimits', ARRealLimitsStruct),
        ('charLimits', ARCharLimitsStruct),
        ('diaryLimits', ARDiaryLimitsStruct),
        ('enumLimits', AREnumLimitsStruct),
        # time has no external limits
        ('maskLimits', AREnumLimitsStruct),
        # bytes has no external limits
        ('attachLimits', ARAttachLimitsStruct),
        ('tableLimits', ARTableLimitsStruct),
        ('columnLimits', ARColumnLimitsStruct),
        ('decimalLimits', ARDecimalLimitsStruct),
        ('viewLimits', ARViewLimits),
        ('displayLimits', ARDisplayLimits),
        ('dateLimits', ARDateLimitsStruct),
        ('currencyLimits', ARCurrencyLimitsStruct)
    ]


class ARFieldLimitStruct(Structure):
    """Structure used to hold field limits (ar.h line 3991)."""
    _fields_ = [
        ('dataType', c_uint),
        ('u', ARFieldLimitUnion)
    ]


class ARFieldLimitList(Structure):
    """List of 0 or more FieldLimitStructs (ar.h line 4015)."""
    _fields_ = [
        ('numItems', c_uint),
        ('fieldLimitList', POINTER(ARFieldLimitStruct))
    ]
