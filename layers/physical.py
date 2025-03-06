class PhysicalLayer:
    def send(self, data):
        return ''.join(format(ord(i), '08b') for i in data)  # Convert to binary
    
    def receive(self, data):
        return ''.join(chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8))  # Convert back to text
