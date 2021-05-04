import re

def handler(content, dt):
    deviceInfo, _, path, detail= content.split(":")
    deviceName, processName, processId = deviceInfo.split()
    processId = re.split(r'[.)]', processId)[-2]
    path = path.split()[2]
    # print(path)
    desc = "{}: {}".format(detail,path)
    desc = desc.strip()
    return {
        "deviceName": deviceName,
        "processId": processId,
        "processName": processName,
        "description": desc,
        "timeWindow": dt,
        }

if __name__ == "__main__":
    msg = "BBAOMACBOOKAIR2 com.apple.xpc.launchd[1] (com.apple.xpc.launchd.domain.pid.mdmclient.53157):       Failed to bootstrap path: path = /usr/libexec/mdmclient, error = 108: Invalid path"
    print(handler(msg, "0000"))