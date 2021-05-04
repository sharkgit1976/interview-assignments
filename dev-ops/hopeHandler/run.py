#!/usr/bin/env python3
# Author: yanshunjun
# Email: sharkyunops@126.com

import requests

from src.Plugins import plugin_handler
from settings import file_path

if __name__ == "__main__":
    error_hour_summary = plugin_handler(file_path)
    url = "https://foo.com/bar"
    response = requests.post(url=url, json=error_hour_summary)
    print('response', response.text)

