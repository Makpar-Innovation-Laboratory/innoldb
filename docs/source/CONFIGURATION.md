# Configuration

## Log Level

The log level can be set through the environment variable **LOG_LEVEL** to the values: `NOTSET`, `INFO`, `DEBUG` and `ERROR`,

```shell
export LOG_LEVEL='INFO'
qldb-orm --table table-name --all
```

```python
import os

os.environ['LOG_LEVEL'] = 'DEBUG'

from qldb-orm.qldb import Query

Query('table-name').get_all()
```

.. note::
  The environment must be set before the `qldb-orm` import. During the import, `qldb-orm` will scan the environment and use the value it finds on its initial load. 

## Build From Source

The `qldb-orm` library can be built from source with the following script,

```shell
git clone https://github.com/Makpar-Innovation-Laboratory/qldb-orm
cd qldb-orm
python -m build
VERSION=$(cat version.txt)
cd dist
pip install qldb-orm-${VERSION}-py3-none-any.whl
```

Or use the pre-packaged helper script,

```shell
git clone https://github.com/Makpar-Innovation-Laboratory/qldb-orm
./qldb-orm/scripts/install
```