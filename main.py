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
print(f"Message: {data}")

# Sending Process (Top to Bottom)
data = app_layer.send(data)
data = pres_layer.send(data)
data = sess_layer.send(data)
data = trans_layer.send(data)
data = net_layer.send(data)
data = datalink_layer.send(data)
data = phys_layer.send(data)

print("Data Sent:", data)

# Receiving Process (Bottom to Top)
data = phys_layer.receive(data)
data = datalink_layer.receive(data)
data = net_layer.receive(data)
data = trans_layer.receive(data)
data = sess_layer.receive(data)
data = pres_layer.receive(data)
data = app_layer.receive(data)

print("Data Received:", data)
