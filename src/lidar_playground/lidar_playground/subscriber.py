import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2, Imu


class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscription_to_cloud = self.create_subscription(
            PointCloud2,
            'unilidar/cloud',
            self.cloud_listener_callback,
            10
        )

        self.subscription_to_imu = self.create_subscription(
            Imu,
            'unilidar/imu',
            self.imu_listener_callback,
            10
        )

        # prevent unused variable warning
        self.subscription_to_cloud
        self.subscription_to_imu

    def cloud_listener_callback(self, msg):
        self.get_logger().info('Cloud: I heard: "%s"' % msg.data)

    def imu_listener_callback(self, msg):
        self.get_logger().info('IMU: I heard: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
