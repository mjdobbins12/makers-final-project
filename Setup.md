In CMD:
**Install Python**
brew install python

**Install PYtest**
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
pip install pytest
pip3 install slackclient

**Running PYtest**
In Project root dir, as with rspec, just type `pytest`
