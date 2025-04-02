import rclpy 
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class BasicClientA(Node):
    def __init__(self):
        super().__init__('basic_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        future = self.client.call_async(self.req)
        future.add_done_callback(self.response_callback)    #Añadir callback para no estar esperando al servicio
        return future
    
    def response_callback(self, future):
        response = future.result()
        self.get_logger().info(f"Resultado recibido: {response.sum}")
    
    
if __name__=='__main__':
    rclpy.init()

    basic_client = BasicClientA()
    future_obj = basic_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    #Como asíncrono no se devuelve inmediatamente sino que es un 'objeto futuro'(python nativo usado por ros internamente)
    #Verificar si ha llegado la respuesta : future.done()
    rclpy.spin_until_future_complete(basic_client, future_obj)
    response = future_obj.result()



