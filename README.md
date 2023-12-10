通过阿里云`OCR`接口获取图片数据。请确保网络畅通。

安装`python`。

安装依赖：
```
pip install filetype
pip install XlsxWriter
pip install alibabacloud_darabonba_stream
pip install alibabacloud_ocr_api20210707==2.0.1
```

复制`main.py`至图片文件夹并运行。脚本将读取文件夹中所有文件信息，并将数据导出为文件夹下的`output.xlsx`。
