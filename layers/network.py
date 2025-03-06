class NetworkLayer:
    def __init__(self):
        self.ip_address = "192.168.1.1"

    def send(self, data):
        return f"{self.ip_address}:{data}"  # Attach IP address
    
    def receive(self, data):
        return data.split(":", 1)[1]  # Remove IP address
