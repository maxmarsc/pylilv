from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import urllib.request
from pathlib import Path

VERSION = "v0.24.6"
URL = 'https://raw.githubusercontent.com/lv2/lilv/{}/bindings/python/lilv.py'.format(VERSION)
BASE_DIR = Path(__file__).parent

def download_livl_py(url):
    try:
        # Download and write the file
        with urllib.request.urlopen(url) as response:
            content = response.read().decode(response.headers.get_content_charset())

        # If the request succeeded, write the file
        with open(BASE_DIR/'lilv/lilv.py', 'w') as f:
            f.write(content)

        print("lilv.py downloaded successfully")

    except urllib.error.URLError as e:
        print(f"Failed to download lilv.py: {e}")
        raise SystemExit(e)

class PreDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        download_livl_py(URL)
        develop.run(self)

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        download_livl_py(URL)
        install.run(self)


setup(
    name='pylilv',
    version=VERSION,
    description='A simple setup.py for the lilv python bindings',
    author='maxmarsc',
    author_email='maxime.coutant@protonmail.com',
    packages=['lilv'],  # The name of the directory that contains your python module
    cmdclass={
        'develop': PreDevelopCommand,
        'install': PreInstallCommand,
    },
)