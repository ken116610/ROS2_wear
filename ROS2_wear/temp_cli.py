#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Yuken Ro
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

TOPIC_TEMP = "/temp_c"

class TempCli(Node):
    def __init__(self) -> None:
        super().__init__("temp_cli")
        self.pub = self.create_publisher(Float32, TOPIC_TEMP, 10)
        self.get_logger().info("Type temperature in Celsius (e.g., 23.5). Ctrl+C to quit.")

    def publish_temp(self, temp: float) -> None:
        msg = Float32()
        msg.data = float(temp)
        self.pub.publish(msg)
        self.get_logger().info(f"Published: {msg.data:.1f} °C -> {TOPIC_TEMP}")

def main() -> None:
    rclpy.init()
    try:
        while rclpy.ok():
            s = input("Temp[°C]> ").strip()
            if not s:
                continue
            node.publish_temp(float(s))
            rclpy.spin_once(node, timeout_sec=0.1)
        except (KeyboardInterrupt, EOFError):
            pass
        except ValueError:
            node.get_logger().error("Invalid number. Example: 18 or 23.5")
        finally:
            node.destroy_node()
            rclpy.shutdown()

if __name__ == "__main__":
    main()
