# python-crownlib

This Python3 library provides an easy interface to the Crown data
structures and protocol. The approach is low-level and "ground up", with a
focus on providing tools to manipulate the internals of how Crown works.


## Requirements

    sudo apt-get install libssl-dev

The RPC interface, `crown.rpc`, is designed to work with Crown Core v0.16.0.
Older versions may work but there do exist some incompatibilities.


## Structure

Everything consensus critical is found in the modules under crown.core. This
rule is followed pretty strictly, for instance chain parameters are split into
consensus critical and non-consensus-critical.

    crown.core            - Basic core definitions, datastructures, and
                              (context-independent) validation
    crown.core.key        - ECC pubkeys
    crown.core.script     - Scripts and opcodes
    crown.core.scripteval - Script evaluation/verification
    crown.core.serialize  - Serialization

In the future the crown.core may use the Satoshi sourcecode directly as a
library. Non-consensus critical modules include the following:

    crown          - Chain selection
    crown.base58   - Base58 encoding
    crown.bloom    - Bloom filters (incomplete)
    crown.net      - Network communication (in flux)
    crown.messages - Network messages (in flux)
    crown.rpc      - Bitcoin Core RPC interface support
    crown.wallet   - Wallet-related code, currently Bitcoin address and
                       private key support

Effort has been made to follow the Satoshi source relatively closely, for
instance Python code and classes that duplicate the functionality of
corresponding Satoshi C++ code uses the same naming conventions: CTransaction,
CBlockHeader, nValue etc. Otherwise Python naming conventions are followed.


## Mutable vs. Immutable objects

Like the Crown Core codebase CTransaction is immutable and
CMutableTransaction is mutable; unlike the Crown Core codebase this
distinction also applies to COutPoint, CTxIn, CTxOut, and CBlock.


## Endianness Gotchas

Rather confusingly Crown Core shows transaction and block hashes as
little-endian hex rather than the big-endian the rest of the world uses for
SHA256. python-crownlib provides the convenience functions x() and lx() in
crown.core to convert from big-endian and little-endian hex to raw bytes to
accomodate this. In addition see b2x() and b2lx() for conversion from bytes to
big/little-endian hex.


## Module import style

While not always good style, it's often convenient for quick scripts if
`import *` can be used. To support that all the modules have `__all__` defined
appropriately.


# Example Code

See `examples/` directory. For instance this example creates a transaction
spending a pay-to-script-hash transaction output:

    $ PYTHONPATH=. examples/spend-pay-to-script-hash-txout.py
    <hex-encoded transaction>


## Selecting the chain to use

Do the following:

    import crown
    crown.SelectParams(NAME)

Where NAME is one of 'testnet', 'mainnet', or 'regtest'. The chain currently
selected is a global variable that changes behavior everywhere, just like in
the Satoshi codebase.


## Unit tests

Under crown/tests using test data from Crown Core. To run them:

    python3 -m unittest discover

Alternately, if Tox (see https://tox.readthedocs.org/) is available on your
system, you can run unit tests for multiple Python versions:

    ./runtests.sh

HTML coverage reports can then be found in the htmlcov/ subdirectory.

## Documentation

Sphinx documentation is in the "doc" subdirectory. Run "make help" from there
to see how to build. You will need the Python "sphinx" package installed.

Currently this is just API documentation generated from the code and
docstrings. Higher level written docs would be useful, perhaps starting with
much of this README. Pages are written in reStructuredText and linked from
index.rst.
