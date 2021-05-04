#!/usr/bin/env python3
# Author: yanshunjun
# Email: sharkyunops@126.com

import json
from pathlib import Path
from src.Plugins import plugin_handler
from settings import file_path


if __name__ == "__main__":
    # 测试代码
    p = Path(file_path)
    if not p.is_file():
        exit("文件不存在或者已损坏")
    error_hour_summary = plugin_handler(file_path)

    for k, v in error_hour_summary.items():
        print(k, json.dumps(v, indent=2))                


