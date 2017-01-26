from setuptools import setup
import midtrans

pkg_req = [
    'requests>=2.3.0'
]
test_req = pkg_req + [
    'pytest>=3.0.6'
]

setup(name='midtrans',
      version=midtrans.__version__,
      url='https://github.com/saveav/midtrans-py',
      license='MIT',
      author='Adam Pahlevi',
      author_email='adam.pahlevi@midtrans.com',
      description='Official Midtrans library',
      long_description='Official Midtrans library',
      packages=['midtrans'],
      keywords='midtrans veritrans',
      include_package_data=True,
      platform='any',
      install_requires=pkg_req,
      tests_requires=test_req)
