In CMD:
**Install Python**
brew install python

**Install pip, PYtest, pytest-cov and slackclient**
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
python3 -m pip install pytest
python3 -m pip install pytest-cov
python3 -m pip install slackclient
python3 -m pip install --user pillow
python3 -m pip install python-chess (need to run python3 -m pytest to allow chess to be imported!)
python3 -m pip install cairosvg


**Running PYtest**
In Project root dir, as with rspec, just type `python3 -m pytest`
Coverage report pytest --cov ./
