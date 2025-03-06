class DataLinkLayer:
    def __init__(self):
        self.mac_address = "AA:BB:CC:DD:EE:FF"

    def send(self, data):
        return f"{self.mac_address}:{data}"  # Attach MAC address
    
    def receive(self, data):
        return data.split(":", 1)[1]  # Remove MAC address
