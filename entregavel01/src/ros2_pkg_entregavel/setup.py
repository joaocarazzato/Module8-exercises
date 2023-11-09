import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros2_pkg_entregavel'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch/*', '*launch.py')))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joao',
    maintainer_email='joao.carazzato@sou.inteli.edu.br',
    description='Entregavel modulo 8 eng comp',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "teste = ros2_pkg_entregavel.teste:main"

        ],
    },
)
