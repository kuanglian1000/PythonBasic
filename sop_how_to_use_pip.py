
# PIP是 Python套件管理工具
# Python 3.4以上,PIP預設已安裝

# Check if PIP is installed
# (全域)Python3.x\Scripts\路徑下 , script: pip --version , 即可查看PIP版本
# (虛擬)VENV_DV\Scripts\路徑下 , script: pip --version , 即可查看PIP版本
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

# Download a Package
# script : pip install <package_name>
# ex. pip install camelcase

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

# Remove a Package
# script : pip uninstall camelcase

# List Package
# script : pip list
