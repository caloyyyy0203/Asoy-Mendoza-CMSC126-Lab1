from layers.physical import PhysicalLayer 
from layers.datalink import DataLinkLayer
from layers.network import NetworkLayer
from layers.transport import TransportLayer
from layers.session import SessionLayer
from layers.presentation import PresentationLayer
from layers.application import ApplicationLayer

# Initialize Layers
phys_layer = PhysicalLayer()
datalink_layer = DataLinkLayer()
net_layer = NetworkLayer()
trans_layer = TransportLayer()
sess_layer = SessionLayer()
pres_layer = PresentationLayer()
app_layer = ApplicationLayer()

# Prompt user for message input
data = input("Enter the message to send: ")
print(f"Original Message: {data}\n")

# Sending Process (Top to Bottom)
print("=== SENDING PROCESS ===")
data = app_layer.send(data)
print(f"Application Layer (send): {data}")

data = pres_layer.send(data)
print(f"Presentation Layer (send): {data}")

data = sess_layer.send(data)
print(f"Session Layer (send): {data}")

data = trans_layer.send(data)
print(f"Transport Layer (send): {data}")

data = net_layer.send(data)
print(f"Network Layer (send): {data}")

data = datalink_layer.send(data)
print(f"Data Link Layer (send): {data}")

data = phys_layer.send(data)
print(f"Physical Layer (send): {data}\n")

print("Data Sent Successfully!\n")

# Receiving Process (Bottom to Top)
print("=== RECEIVING PROCESS ===")
data = phys_layer.receive(data)
print(f"Physical Layer (receive): {data}")

data = datalink_layer.receive(data)
print(f"Data Link Layer (receive): {data}")

data = net_layer.receive(data)
print(f"Network Layer (receive): {data}")

data = trans_layer.receive(data)
print(f"Transport Layer (receive): {data}")

data = sess_layer.receive(data)
print(f"Session Layer (receive): {data}")

data = pres_layer.receive(data)
print(f"Presentation Layer (receive): {data}")

data = app_layer.receive(data)
print(f"Application Layer (receive): {data}\n")

print("Data Received Successfully!")
