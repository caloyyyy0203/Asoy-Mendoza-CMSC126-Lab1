class ApplicationLayer:
    def send(self, data):
        return f"HTTP/1.1 200 OK\\n\\n{data}"  # Add HTTP header
    
    def receive(self, data):
        return data.split("\\n\\n", 1)[1]  # Extract message
