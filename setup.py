from setuptools import setup

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Physics',
    version='0.1.0',
    description="Description tamplate",
    long_description=readme + '\n\n' + history,
    author="Sablin Sergey",
    author_email='serewkasablin@outlook.com',
    packages=[
        'Physics',
    ],
    package_dir={'Physics':
                 'Physics'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='Physics',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
