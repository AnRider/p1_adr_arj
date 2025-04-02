import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class BasicSubscriber(Node):
    def __init__(self):
        super().__init__('basic_subscriber')
        self.subcription = self.create_subcription(String, 'topic', self.listener_callback, 10)

    def listener_callback(self,msg):
        self.get_logger().info(f'Mensaje: {msg.data}')

if __name__=='__main__':
    rclpy.init()

    basic_subscriber = BasicSubscriber()

    rclpy.spin(basic_subscriber)

    basic_subscriber.destroy_node()
    rclpy.shutdown()

