# pylilv
A simple setup.py file that download and install `livl.py` from the [official lilv repository](https://github.com/lv2/lilv/blob/master/bindings/python/lilv.py)

__Note:__ The setup.py below only works when installing a source distribution zip or tarball, 
or installing in editable mode from a source tree. It will not work when installing
from a binary wheel (.whl)

## Install
```bash
git clone -b $VERSION git@github.com:maxmarsc/pylilv.git 
pip install -e pylilv
```