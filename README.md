### 安装`python 3.11`
**请勿使用`python 3.12`**，依赖库`aiohttp`暂不支持`python 3.12`。  
[python 3.11.7 64-bit 下载](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe), [python 3.11.7 32-bit 下载](https://www.python.org/ftp/python/3.11.7/python-3.11.7.exe)。

### 安装依赖
运行`pip_install.cmd`安装依赖。

### 使用
复制`ocr2xlsx.py`和`main.cmd`至图片文件夹，运行`main.cmd`。脚本将读取文件夹中所有文件信息，并将数据导出为文件夹下的`output.xlsx`，表格式参看本文件夹下`output.xlsx`。

### Note
* 目前仅支持`jpg`和`png`格式的图片。
* 通过阿里云`OCR`接口获取图片数据。请确保网络畅通。
