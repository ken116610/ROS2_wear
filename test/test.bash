#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Yuken Ro
# SPDX-License-Identifier: BSD-3-Clause

source /opt/ros/humble/setup.bash
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=1
set -eu

cd "$(dirname "$0")"

rm -rf build install log
colcon build --packages-select ROS2_wear
set +u
source install/setup.bash
set -u

LOG=/tmp/ros2_wear.log
rm -f "$LOG"

timeout 20 ros2 launch ROS2_wear bringup.launch.py > "$LOG" 2>&1 &
LPID=$!

sleep 2

timeout 10 ros2 topic pub -1 /temp_c std_msgs/msg/Float32 "{data: 4.0}"  > /dev/null
sleep 1
timeout 10 ros2 topic pub -1 /temp_c std_msgs/msg/Float32 "{data: 28.0}" > /dev/null
sleep 1

if grep -q "/outfit_advice" "$LOG"; then
	grep -Eq "4\.0.*(厚手|コート)" "$LOG" || { cat "$LOG"; echo "1"; exit 1; }
	grep -Eq "28\.0.*半袖" "$LOG" || { cat "$LOG"; echo "1"; exit 1; }

	echo "0"
	exit 0
else
	cat "$LOG"
	echo "1"
	exit 1
fi
