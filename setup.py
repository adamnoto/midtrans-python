from setuptools import setup, find_packages
import re
import ast

pkg_req = [
    'requests>=2.3.0'
]
test_req = pkg_req + [
    'pytest>=3.0.6'
]

with open('midtrans/__init__.py', 'rb') as f:
    _version_re = re.compile(r'__version__\s+=\s+(.*)')
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')
    ).group(1)))

setup(name='midtrans',
      version=version,
      url='https://github.com/saveav/midtrans-python',
      license='MIT',
      author='Adam Pahlevi',
      author_email='adam.pahlevi@midtrans.com',
      description='Official Midtrans library',
      long_description='Official Midtrans library',
      packages=find_packages(),
      keywords='midtrans veritrans',
      include_package_data=True,
      platform='any',
      install_requires=pkg_req,
      tests_requires=test_req)
