import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16MultiArray


class nodo1(Node):

    def __init__(self):
        super().__init__('minodo1')
        self.publisher_ = self.create_publisher(Int16MultiArray, 'nod1_2', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int16MultiArray()
        prim=[]
        for n in range(2, 51):
            es_primo = True
            if n < 2:
                es_primo = False
            else:
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        es_primo = False
                        break
            
            if es_primo:
                prim.append(n)
                if len(prim) == 12:  # Detener cuando tengamos 8 primos
                    break

        msg.data = prim
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % list(msg.data))
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minodo1 = nodo1()

    rclpy.spin(minodo1)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minodo1.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()