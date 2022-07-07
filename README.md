### This is a demo for a python package creation
mypackage-name
### build
```bash
python setup.py  bdist_wheel
python setup.py sdist bdist_wheel --universal
```

### install
```bash
pip install [-e] .
pip install dist/... --force-reinstall
```
