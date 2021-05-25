from setuptools import setup

setup(
    name='hamming',
    version='0.1',
    license='MIT',
    description='Simulation code de Hamming',
    author='Jérémie BASSO',
    author_email='jeremie.basso@hotmail.fr',
    py_modules=['hamming'],
    install_requires=[
        'Click',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'hamming = hamming:main',
        ],
    },
)
