import re


def handler(content, dt):
    """
    1. 设备名称: (deviceName)
    2. 错误的进程号码: (processId)
    3. 进程/服务名称: (processName)
    4. 错误的原因（描述）(description)
    5. 发生的时间（小时级），例如 0100-0200，0300-0400, (timeWindow)
    6. 在小时级别内发生的次数 (numberOfOccurrence)
    """
    deviceInfo, desc, *_ = content.split(":")
    deviceName, processName, processId = deviceInfo.split()
    processId = re.split(r'[][]', processId)[1]
    return {
        "deviceName": deviceName,
        "processId": processId,
        "processName": processName,
        "description": desc,
        "timeWindow": dt,
        }

if __name__ == "__main__":
    msg = "BBAOMACBOOKAIR2 com.apple.xpc.launchd[1] (com.apple.mdworker.bundles[52682]): Could not find uid associated with service: 0: Undefined error: 0 501"

    print(handler(msg, "0000"))