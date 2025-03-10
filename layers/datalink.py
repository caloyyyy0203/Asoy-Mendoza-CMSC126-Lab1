class DataLinkLayer:
    def __init__(self):
        self.mac_address = "AA:BB:CC:DD:EE:FF"

    def send(self, data):
        return f"{self.mac_address}:{data}"  # Attach MAC address
    
    def receive(self, data):
        # Remove only the MAC address part
        return data[len(self.mac_address) + 1:]  # +1 accounts for the colon (":")
