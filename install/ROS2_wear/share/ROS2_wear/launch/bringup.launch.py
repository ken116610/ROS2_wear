#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Yuken Ro
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch_ros.actions

def generate_launch_description():
    outfit_suggester = launch_ros.actions.Node(
            package="ROS2_wear",
            executable="outfit_suggester",
            output="screen",
    )

    return launch.LaunchDescription([outfit_suggester])
