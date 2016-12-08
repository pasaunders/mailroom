"""Setup file for mailroom automation assignment."""


from setuptools import setup


setup(
    name="mailroom",
    description="A project to automate drafting thankyou letters.",
    version=0.1,
    author="Patrick & Rachael",
    author_email="patrick.a.n.saunders@gmail.com",
    license="MIT",
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=['faker'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        'console scripts': [
            "mailroom = mailroom:main"
        ]
    }
)
