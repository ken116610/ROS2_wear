#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Yuken Ro
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import find_packages, setup

import os
from glob import glob

package_name = 'ROS2_wear'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yuken Ro',
    maintainer_email='yuken.lu3@gmail.com',
    description='a package for task',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'temp_cli = ROS2_wear.temp_cli:main',
            'outfit_suggester = ROS2_wear.outfit_suggester:main',
        ],
    },
)
