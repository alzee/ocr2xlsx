### 下载 ocr2xlsx.py
[zip](https://github.com/alzee/ocr2xlsx/archive/refs/heads/main.zip), [tar.gz](https://github.com/alzee/ocr2xlsx/archive/main.tar.gz)

### 安装`python 3.11`
* **请勿使用`python 3.12`**，依赖库[`aiohttp`暂不支持`python 3.12`](https://github.com/aio-libs/aiohttp/issues/7739) 
* [python 3.11.7 64-bit 下载](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe), [python 3.11.7 32-bit 下载](https://www.python.org/ftp/python/3.11.7/python-3.11.7.exe)。
* 安装时请注意勾选“将`python`加入`PATH`“

### 安装依赖
运行`pip_install.cmd`安装依赖。

### 使用
复制`ocr2xlsx.py`和`main.cmd`至图片目录，运行`main.cmd`。脚本将识别目录中所有图片，并将数据导出为目录下的`output.xlsx`。表格式参看本目录下`output.xlsx`。

### Note
* 目前仅支持`jpg`和`png`格式的图片。
* 通过阿里云`OCR`接口获取图片数据。请确保网络畅通。
