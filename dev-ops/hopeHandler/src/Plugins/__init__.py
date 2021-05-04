#!/usr/bin/env python3
# Author: yanshunjun
# Email: sharkyunops@126.com

import importlib
from pathlib import Path

from settings import PLUGINS_TEMPLATE

def plugin_handler(file_path):
    p = Path(file_path)
    if not p.is_file():
        exit("文件不存在或者已损坏")
    error_hour_summary = {}
    up_hour = ''
    with open(file_path) as f:
        for line in f:
            for k, item in PLUGINS_TEMPLATE.items():
                if item["keyword"] in line:
                    _, _, dt, *msg = line.split()
                    msg_source = " ".join(msg)
                    hour = dt[:2] + "00"
                    if up_hour != hour:
                        error_kw_summary = {}
                    up_hour = hour
                    plugins_path = item["module"]
                    plugins_obj = importlib.import_module(plugins_path)
                    handler = getattr(plugins_obj, "handler")
                    error_item = handler(msg_source, hour)
                    error_kw_item = error_kw_summary.setdefault(k, {"numberOfOccurrence": 0, "errors": []})
                    error_kw_item["numberOfOccurrence"] += 1
                    error_kw_item["errors"].append(error_item)
                    
                    error_sum_item = error_hour_summary.setdefault(hour, {"numberOfOccurrence": 0, "errors_kw_summary" : error_kw_summary})
                    error_sum_item["numberOfOccurrence"] += 1

    return error_hour_summary