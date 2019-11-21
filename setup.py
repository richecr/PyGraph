from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyGraphT',
    version='0.1.0',
    author='Rich Elton',
    author_email='richelton14@gmail.com',
    description='Biblioteca com intuito de implementar os grafos e seus \
        algoritmos de Teoria dos Grafos.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(),
    url="https://github.com/Rickecr/PyGraph",
    project_urls={
        'Código fonte': 'https://github.com/Rickecr/PyGraph',
    },
    keywords='graph theory algorithms',
    license='MIT'
)
