#!/usr/bin/python3

import os
import sys
import json
import filetype

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

                # print(i)
                print(i.name)
                print(kind)
                # continue

                client = Sample.create_client('LTAI5tBmKAjcNE7mpFiSW7n4', 'qOp2XtV5PQZjPh5O28YctTRb0x8B0n')
                body_stream = StreamClient.read_from_file_path(i)
                recognize_general_request = ocr_api_20210707_models.RecognizeGeneralRequest(
                    body=body_stream
                )
                runtime = util_models.RuntimeOptions()
                try:
                    res = client.recognize_general_with_options(recognize_general_request, runtime)
                    data = json.loads(res.body.data)
                    content = data['content']
                    l = content.split()
                    print(l)
                except Exception as error:
                    print(error.message)
                    print(error.data.get("Recommend"))
                    UtilClient.assert_as_string(error.message)

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
