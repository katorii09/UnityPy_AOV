from setuptools import setup, find_packages

setup(
    name='UnityPy_AOV',
    packages=find_packages(),
    package_data={"UnityPy_AOV": ["resources/uncompressed.tpk"]},
    install_requires=open('requirements.txt').read().splitlines(),
    python_requires='>=3.7',
)
