from setuptools import setup, find_packages

setup(
    name='evestidor_event_stream',
    version='0.1',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=[
        'pika',
    ],
)
