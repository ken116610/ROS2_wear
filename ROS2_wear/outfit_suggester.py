#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Yuken Ro
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

from .outfit_rules import suggest_outfit

TOPIC_TEMP = "/temp_c"
TOPIC_ADVICE = "/outfit_advice"


class OutfitSuggester(Node):
    def __init__(self) -> None:
        super().__init__("outfit_suggester")
        self.create_subscription(Float32, TOPIC_TEMP, self.cb, 10)
        self.pub = self.create_publisher(String, TOPIC_ADVICE, 10)
        self.get_logger().info(f"Waiting: {TOPIC_TEMP}")

    def cb(self, msg: Float32) -> None:
        temp = float(msg.data)
        advice = suggest_outfit(temp)
        out = String()
        out.data = f"{temp:.1f}°C -> {advice}"
        self.pub.publish(out)
        self.get_logger().info(f"Publish: {TOPIC_ADVICE} : {out.data}")


def main() -> None:
    rclpy.init()
    node = OutfitSuggester()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

