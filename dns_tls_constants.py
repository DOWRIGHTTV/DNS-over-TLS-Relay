#!/usr/bin/env python3

import time as _time

from struct import Struct as _Struct
from enum import IntEnum as _IntEnum
from collections import namedtuple as _namedtuple

from advanced_tools import ByteContainer as _ByteContainer

fast_time = _time.time
fast_sleep = _time.sleep

KEEPALIVES_ENABLED = False

# general settings
MINIMUM_TTL = 300
DEFAULT_TTL = 3600
MAX_A_RECORD_COUNT = 3
HEARTBEAT_FAIL_LIMIT = 3
TOP_DOMAIN_COUNT = 20
KEEP_ALIVE_DOMAIN = 'duckduckgo.com'

NOT_VALID = -1
NULL_ADDR = (None, None)

# times
NO_DELAY = 0
MSEC = .001
FIVE_SEC = 5
TEN_SEC = 10
THIRTY_SEC = 30
THREE_MIN = 180
FIVE_MIN = 300

KEEPALIVE_INTERVAL = 8

# namedtuples
RELAY_CONN = _namedtuple('relay_conn', 'remote_ip sock')
DNS_CACHE  = _namedtuple('dns_cache', 'ttl records')
DNS_SERVERS = _namedtuple('dns_server', 'primary secondary')
CACHED_RECORD = _namedtuple('cached_record', 'expire ttl records')

# byte container
RESOURCE_RECORD = _ByteContainer('resource_record', 'name qtype qclass ttl data')

# COMPILED STRUCTS
dns_header_unpack = _Struct('!6H').unpack
dns_header_pack   = _Struct('!6H').pack

resource_record_pack = _Struct('!3HLH4s').pack

short_unpackf = _Struct('!H').unpack_from

byte_pack = _Struct('!B').pack
short_unpack = _Struct('!H').unpack
short_pack   = _Struct('!H').pack
long_pack    = _Struct('!L').pack
long_unpack  = _Struct('!L').unpack

double_short_unpack = _Struct('!2H').unpack_from
double_short_pack   = _Struct('!2H').pack


# enums
class PROTO(_IntEnum):
    NOT_SET = 0
    TCP = 6
    DNS = 53
    DNS_TLS = 853


class DNS(_IntEnum):
    ROOT = 0
    AR = 1
    NS = 2
    OPT = 41

    QUERY = 0
    KEEPALIVE = 69
    RESPONSE = 128
