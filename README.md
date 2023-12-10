通过阿里云`OCR`接口获取图片数据。请确保网络畅通。

安装`python 3.11`。**请勿使用`python 3.12`**，依赖库`aiohttp`暂不支持`python 3.12`。  
[python 3.11.7 64-bit](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe), [python 3.11.7 32-bit](https://www.python.org/ftp/python/3.11.7/python-3.11.7.exe)。

安装依赖：
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install filetype
pip install XlsxWriter
pip install alibabacloud_darabonba_stream
pip install alibabacloud_ocr_api20210707==2.0.1
```

复制`main.py`和`main.cmd`至图片文件夹，运行`main.cmd`。脚本将读取文件夹中所有文件信息，并将数据导出为文件夹下的`output.xlsx`，表格式参看本文件夹下`output.xlsx`。
