import versioneer
from setuptools import setup, find_packages

setup(name='test_proj',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='BSD',
      author='n-wbrown',
      packages=find_packages(),
      description='abcdefghijklmnop',
      )
