from setuptools import setup, find_packages

from django_mail_tester import __version__


CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python',
    'Topic :: Communications :: Email',
    'Topic :: Communications',
    'Topic :: Software Development :: Testing',
    'Topic :: Utilities',
]

setup(
    name='django-mail-tester',
    version=__version__,
    description='Django management command to send email',
    author='Anton Egorov',
    author_email='anton.egoroff@gmail.com',
    url='https://github.com/satyrius/django-mail-tester',
    license='MIT',
    long_description=open('README.rst').read(),
    classifiers=CLASSIFIERS,
    platforms=['OS Independent'],
    packages=find_packages(),
    zip_safe=False,
)
