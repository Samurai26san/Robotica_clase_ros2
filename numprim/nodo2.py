import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16MultiArray,Float32MultiArray

class nodo2pro(Node):
    def __init__(self):
        super().__init__('minodo2')
        self._subscription = self.create_subscription(
            Int16MultiArray,
            'nod1_2',
            self.listener_callback,
            10)
        
        self.publisher_=self.create_publisher(Float32MultiArray, 'nod2_3',10)

        self.get_logger().info('Nodo 2- opercion en ')
    
    def listener_callback(self,msg):
        nod1_2 = list(msg.data)
        self.get_logger().info(f'Nodo 2 recibe:{nod1_2}')
        vectorpro = [x/2 for x in nod1_2] 
        
        msg_mand=Float32MultiArray()
        msg_mand.data = vectorpro

        self.publisher_.publish(msg_mand)
        self.get_logger().warning(f'nodo2 manda a nodo 3: {vectorpro}')


def main(args=None):
    rclpy.init(args=args)
    mi_nodo2 = nodo2pro()
    rclpy.spin(mi_nodo2)
    mi_nodo2.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()