def handler(content, dt):
    deviceInfo, detail= content.split("-")
    deviceName, processName, processId = deviceInfo.split()
 
    return {
        "deviceName": deviceName,
        "processId": processId.strip("tid:"),
        "processName": processName.strip(":"),
        "description": detail.strip(),
        "timeWindow": dt,
        }

if __name__ == "__main__":
    msg = "BBAOMACBOOKAIR2 AMPDeviceDiscoveryAgent[976]: tid:8813 - Can t handle disconnect with invalid ecid"
    print(handler(msg, "0000"))