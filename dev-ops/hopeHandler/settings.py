#!/usr/bin/env python3
# Author: yanshunjun
# Email: sharkyunops@126.com
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

file_path = "test/DevOps_interview_data_set"

PLUGINS_TEMPLATE = {
    "error_eq": {"keyword": "error =", "module": "src.Plugins.error_eq"},
    "error_501": {"keyword": "error: 0 501", "module": "src.Plugins.error_501"},
    "invalid_port": {"keyword": "destination port", "module": "src.Plugins.invalid_port"},
    "invalid_ecid": {"keyword": "with invalid ecid","module": "src.Plugins.invalid_ecid"}
}
