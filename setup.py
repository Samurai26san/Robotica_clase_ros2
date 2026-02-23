from setuptools import find_packages, setup

package_name = 'numprim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='samuel',
    maintainer_email='dsamuelguzman@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'nodo1 = numprim.nodo1:main',
            'nodo2 = numprim.nodo2:main',
            'nodo3 = numprim.nodo3:main'
        ],
    },
)
