import json

class PresentationLayer:
    def send(self, data):
        return json.dumps({"message": data})  # Convert to JSON
    
    def receive(self, data):
        return json.loads(data)["message"]  # Extract message from JSON
