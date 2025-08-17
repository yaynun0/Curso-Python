from setuptools import setup

setup(
    name='Mensajes',
    version='1.0',
    description='Un paquete para saludar y despedir',
    author='Gerardo Nuñez',
    author_email='hola@yo.com',
    url='https://www.google.com',
    packages=['mensajes','mensajes.hola','mensajes.adios'],
    scripts=['test.py']
)

