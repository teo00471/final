
def do_connect():
    import network
    ssid = 'GLORIA'
    password = 'Gloria111'

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    try:
        wlan.connect(ssid, password)
        print(f'Connecting to: {ssid}')
        print('Connected to Wi-Fi')
    except Exception as e:
        print("Error connection wi-fi: ",e)

    while not wlan.isconnected():
        pass
    
    
do_connect()
