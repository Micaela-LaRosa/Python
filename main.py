from paquete1.client import Client
from paquete1.primera_entrega import *

client1 = Client("Juan", "Hansen", "Jujuy 1571", 3412334322)
client2 = Client("Marizza", "Peña", "Marcos Paz 234bis", 3412339987)
print(client1)
print(client1.buy("Laptop", "Marketplace"))
print(client2.ask_for("Mouse", 5, "3413987653"))
