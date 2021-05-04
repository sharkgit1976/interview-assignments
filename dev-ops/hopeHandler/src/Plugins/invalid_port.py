def handler(content, dt):
    deviceInfo, detail= content.rsplit(":", maxsplit=1)
    deviceName, processName, _, _, processId = deviceInfo.split()
    detail = detail.split(')')[-1]
    return {
        "deviceName": deviceName,
        "processId": processId.strip("tid:"),
        "processName": processName.strip(":"),
        "description": detail.strip(),
        "timeWindow": dt,
        }

if __name__ == "__main__":
    msg = "BBAOMACBOOKAIR2 xpcproxy[55327]:              libcoreservices: _dirhelper_userdir: 557: bootstrap_look_up returned (ipc/send) invalid destination port"

    print(handler(msg, "0000"))