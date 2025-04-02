import rclpy 
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts       #Ejemplo tipo de servicio

class BasicService(Node):
    def __init__(self):
        super().__init__('basic_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback )
        #create_service(tipo de servicio == salidas y entradas, nombre, funcion llamada)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b       #Atributos definidos en el tipo de servicio
        self.get_logger().info('Suma realizada, devolviendo resultado...')

        return response

if __name__ == '__main__':
    clpy.init()

    basic_service = BasicService()

    rclpy.spin(basic_service)

    rclpy.shutdown()


