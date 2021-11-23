#!/usr/bin/env python3
# coding:utf-8
import base64
import zlib
import json


def b64_decode(s):
    pad = b'=' * (-len(s) % 4)
    return base64.urlsafe_b64decode(s + pad)


def decode_session_data(data):
    data = data.split(".")[-1]
    data = data.split(":")[0]
    data = data.encode('ascii')
    data = b64_decode(data)
    data = zlib.decompress(data)
    data = json.loads(data)
    return data


if __name__ == "__main__":
    data = '.eJxVjMsOwiAQRf-FtSHA8NKl-34DAWaQqoGktCvjv2uTLnR7zzn3xULc1hq2QUuYkV2YYqffLcX8oLYDvMd26zz3ti5z4rvCDzr41JGe18P9O6hx1G9tvfUqOmeMhqQ9apvJZKSUBRSAWIokKqYkkRR5h0KenfRFOQQkEI69P-plOD8:1kFbqF:bM3BvLXVTe96vRHdd87BREnScekvtNNK5lwg2lgOrQQ'
    data2 = '.eJxVjDsOwjAQBe_iGln-7TqmpOcM1nptkwBypDipEHeHSCmgfTPzXiLSto5x62WJUxZnobURp981ET9K21G-U7vNkue2LlOSuyIP2uV1zuV5Ody_g5H6-K1NHZIzQIYVYgDAAXwA9HUomkgpx4WNRUesU3W2sLUEqKCiZ6ODFu8PC_U3cQ:1kFocw:hlVneTWYXXOeVBEMKcq5YbsFEOLVSa-3ACZhcZEokb0'
    data = decode_session_data(data)
    print(data)
    data2 = decode_session_data(data2)
    print(data2)
