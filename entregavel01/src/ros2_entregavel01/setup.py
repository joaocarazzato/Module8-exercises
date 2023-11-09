import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros2_entregavel01'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joao',
    maintainer_email='joao.carazzato@sou.inteli.edu.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "teste = ros2_entregavel01.ola:main",
            "go_to_pose = ros2_entregavel01.nav2_go_to_pose:main",
            "set_initial_pose = ros2_entregavel01.set_initial_pose_nav2:main"
        ],
    },
)
