from setuptools import setup


setup(
    name='softbutterfly-wagtail-materialize',
    version='1.0.0',
    description='A drop-in module to build material design sites using wagtail and materializecss.',
    author='SoftButterfly',
    author_email='dev@softbutterfly.io',
    license='BSD',
    url='https://github.com/softbutterfly/softbutterfly-wagtail-materialize',
    download_url='https://github.com/softbutterfly/softbutterfly-wagtail-materialize/tarball/1.0.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    keywords=['softbutterfly', 'django', 'wagtail', 'materializecss'],
    packages=[
        'softbutterfly.wagtail.materialize',
    ],
    include_package_data=True,
    install_requires=[
        'django',
        'wagtail',
        'django-compressor'
        'django-settings-export'
    ],
)
