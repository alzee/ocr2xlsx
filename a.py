#!/usr/bin/python3

import os
import sys
import json
import filetype
import xlsxwriter

from typing import List

from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> ocr_api20210707Client:
        """
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            access_key_id = access_key_id,
            access_key_secret = access_key_secret
        )
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # files = os.listdir()
        files = os.scandir()
        for i in files:
            if i.is_file():
                kind = filetype.guess(i.name)
                # if kind is not None and (kind.extension == 'jpg' or kind.extension == 'png'):
                if kind is None:
                    continue
                if kind.extension != 'jpg' and kind.extension != 'png':
                    continue

                # print(i)
                # print(i.name)
                # print(kind)
                # continue

                client = Sample.create_client('LTAI5tBmKAjcNE7mpFiSW7n4', 'qOp2XtV5PQZjPh5O28YctTRb0x8B0n')
                body_stream = StreamClient.read_from_file_path(i)
                recognize_general_request = ocr_api_20210707_models.RecognizeGeneralRequest(
                    body=body_stream
                )
                runtime = util_models.RuntimeOptions()

                workbook = xlsxwriter.Workbook('demo.xlsx')
                worksheet = workbook.add_worksheet()

                try:
                    # res = client.recognize_general_with_options(recognize_general_request, runtime)
                    # data = json.loads(res.body.data)
                    # content = data['content']
                    content = '目 待机 (00 DI ? 08/12/2023 00：40 样品状态 状态 详细信息 实时显示 分析仪状态 所有 快速 IS E 视图模式 静态 样本号 E001 血清 样品ID 6001 TP 49.6 ALB 34.6 ALT 64.8 AST 50.3 GGT 47.9 TB IL 19.3 DB IL 13.5 CHE 5929 ALP 121.9 UA 326.7 83.6 BUN 6.72 GLU 5.51 TG 1.48 2.70 CK 153.8 LDH 161.3 HB DH 171.1 AMY 83.9 LPS 44.3 样本号 E002 血清 样品ID 6002 TP 80.1 ALB 44.0 @ ALT 148.4 AST 149.6 GGT 199.4 TB IL 71.0 DB IL 34.8 CHE 9599 ALP 307.8 UA 662.2 517.3 BUN 20.16 GLU 13.16 TG 2.69 4.55 CK 277.1 LDH 300.2 HB DH 331.8 AMY 214.3 LPS 101.7 样本号 E003 血清 样品ID 6003 PA 196 APO A 0.91 APOB 0.44 RBP 27.3 A SO 105.11 样本号 E004 血清 样品ID 6004 PA 315 APO A 1.53 APOB 0.66 RBP 41.3 A SO 177.91 样本号 E005 血清 样品ID 6005 HDL 1.10 LDL 2.15 样本号 E006 血清 样品ID 6006 HDL 1.77 LDL 3.46 样本号 E007 血清 样品ID 6007 CK MB 51.5 样本号 E008 血清 样品ID 6008 CK MB 116.0 样本号 E009 血清 样品ID 6009 5NT 69.2 样本号 E010 血清 样品ID 6010 5NT 89.3 二 转换至 反应 搜索 静态视图 样品管理器 监控器 IS E保养 六 凤'
                    l = content.split()
                    print(l)
                except Exception as error:
                    print(error.message)
                    print(error.data.get("Recommend"))
                    UtilClient.assert_as_string(error.message)

        worksheet.write(1, 1, 123.12)
        workbook.close()

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
