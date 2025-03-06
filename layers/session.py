class SessionLayer:
    def send(self, data):
        return f"SESSION:START|{data}|SESSION:END"  # Add session markers
    
    def receive(self, data):
        return data.split("|", 1)[1].rsplit("|", 1)[0]  # Remove session markers
