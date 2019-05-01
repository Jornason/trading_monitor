import json
import urllib
import os
import io
import time
import datetime
import math
import string

from flask import Response


def json_response(status=200, obj={}, sort=True):
    # wrap a response
    r = {"_system": "geekree api system", "result": obj}
    return Response(
        response=json.dumps(r, ensure_ascii=False, sort_keys=sort, indent=2),
        status=200,
        mimetype="application/json")


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


def url_decode(str):
    return urllib.parse.unquote(str)


def tail(file_name, line_count=10, encoding='utf-8'):
    # print('tail',file_name)
    """
    读取某文本文件最末的行
    :param file_name: 文件名
    :param line_count: 读多少行
    :param encoding: 文件编码
    :return: 数组格式的行列表
    """
    f = open(file_name, mode='rb')
    f.seek(0, io.SEEK_END)
    file_size = f.tell()
    if file_size == 0 or line_count <= 0:
        return []
    lines = []
    prev_char = None
    curr_line = bytearray()
    chars_read = 0
    f.seek(-1, io.SEEK_END)
    while True:
        curr_char = f.read(1)
        chars_read += 1
        # 以下三个步骤：增加字符、增加行、跳出循环，如果文件已经读完，则都要做
        if curr_char not in (b'\n', b'\r') or chars_read == file_size:
            curr_line.extend(curr_char)
        if curr_char == b'\n' or (curr_char == b'\r' and not prev_char == b'\n'
                                  ) or chars_read == file_size:
            curr_line.reverse()
            lines.append(bytes(curr_line).decode(encoding))
            curr_line.clear()
        if len(lines) == line_count or chars_read == file_size:
            break
        # 前退一个字节，此处可以测试一下性能
        f.seek(-2, io.SEEK_CUR)
        prev_char = curr_char
    lines.reverse()
    return lines

if __name__=='__main__':
    pass
