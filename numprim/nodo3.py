import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class nodo3fin(Node):

    def __init__(self):
        super().__init__('nodo3_subcriptor')

        self.subscription = self.create_subscription(
            Float32MultiArray,
            'nod2_3',
            self.listener_callback,
            10)
        self.get_logger().info('Nodo3 iniciado')


    def listener_callback(self, msg):
        vectfin = list(msg.data)
        self.get_logger().warning(f'Resultado final {vectfin}')


def main(args=None):
    rclpy.init(args=args)
    nodo3 = nodo3fin()

    rclpy.spin(nodo3)

    nodo3.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()