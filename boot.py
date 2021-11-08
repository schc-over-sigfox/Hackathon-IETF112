from network import WLAN

# Connect to WiFi
# SSID is your WiFi connection name and PASSWORD your WiFi password
wlan = WLAN(mode=WLAN.STA)
wlan.connect("SSID", auth=(WLAN.WPA2, "PASSWORD"), timeout=5000)