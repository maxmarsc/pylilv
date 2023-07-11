# pylilv
A simple setup.py file that download and install `livl.py` from the [official lilv repository](https://github.com/lv2/lilv/blob/master/bindings/python/lilv.py)

This python package is only a module wrapper around the C library, you will need to have
the `liblilv` installed on your system.

If you need both the library and the python module I suggest checking [moddevices/lilvlib](https://github.com/moddevices/lilvlib)

__Note:__ The setup.py below only works when installing a source distribution zip or tarball, 
or installing in editable mode from a source tree. It will not work when installing
from a binary wheel (.whl)

## Install
```bash
git clone -b $VERSION git@github.com:maxmarsc/pylilv.git 
pip install -e pylilv
```

or 

```bash
pip install https://github.com/maxmarsc/pylilv/archive/refs/tags/$VERSION.zip
```