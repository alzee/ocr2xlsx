@echo off

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install filetype
pip install XlsxWriter
pip install alibabacloud_darabonba_stream
pip install alibabacloud_ocr_api20210707==2.0.1

echo Press any key to exit...
pause > nul
