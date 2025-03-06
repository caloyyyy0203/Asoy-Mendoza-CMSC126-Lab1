class TransportLayer:
    def send(self, data):
        return f"SEQ=1|{data}"  # Attach sequence number
    
    def receive(self, data):
        return data.split("|", 1)[1]  # Remove sequence number
