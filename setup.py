from distutils.core import setup

packages=['ngrams']
template_patterns = [
    'templates/*.html',
    'templates/*/*.html',
    'templates/*/*/*.html',
    ]

setup(
    name='django-ngrams',
    version='0.1.2',
    author='Michael McAuliffe',
    author_email='michael.e.mcauliffe@gmail.com',
    url='http://pypi.python.org/pypi/django-ngrams/',
    license='LICENSE.txt',
    description='',
    long_description=open('README.md').read(),
    install_requires=['django'],
    packages = packages,
    package_data=dict( (package_name, template_patterns)
                   for package_name in packages )
)
