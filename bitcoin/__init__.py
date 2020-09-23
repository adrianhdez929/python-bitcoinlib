# Copyright (C) 2012-2018 The python-bitcoinlib developers
# Copyright (C) 2020 The python-crownlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.11.1dev'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xb8\xeb\xb3\xdf'
    DEFAULT_PORT = 9340
    RPC_PORT = 9341
    DNS_SEEDS = (('crowncoin.org', 'dnseed1.crowncoin.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':(0x01, 0x75, 0x07),
                       'SCRIPT_ADDR':(0x01, 0x75, 0xF1),
                       'SECRET_KEY' :128}
    BECH32_HRP = 'bc'

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0f\x18\x0e\x06'
    DEFAULT_PORT = 19340
    RPC_PORT = 19341
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':(0x01, 0x7A, 0xCD, 0x67),
                       'SCRIPT_ADDR':(0x01, 0x7A, 0xCD, 0x51),
                       'SECRET_KEY' :239}
    BECH32_HRP = 'tb'

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfb\xae\xc6\xdf'
    DEFAULT_PORT = 19445
    RPC_PORT = 19444
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':(0x01, 0x7A, 0xCD, 0x67),
                       'SCRIPT_ADDR':(0x01, 0x7A, 0xCD, 0x51),
                       'SECRET_KEY' :239}
    BECH32_HRP = 'bcrt'

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
