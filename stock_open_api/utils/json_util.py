# -*- coding: utf-8 -*-
"""
@File    : json_util.py
@Date    : 2023-07-18
"""
import json


def encode_json(data):
    return json.dumps(data, indent=2, ensure_ascii=False)
