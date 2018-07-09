from setuptools import setup, find_packages

setup(
    name='avs_client',
    version='0.6.0',
    packages=find_packages(exclude=["tests.*", "tests"]),
    url='https://github.com/Yud07/alexa-voice-service-client',
    license='MIT',
    author='Richard Tier',
    author_email='rikatee@gmail.com',
    description='Python Client for Alexa Voice Service (AVS)',
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=['hyper==0.7.0', 'requests-toolbelt==0.8.0', 'requests==2.18.3'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
