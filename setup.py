from setuptools import setup

setup(
    name="my_app",
    packages=["my_app"],
    include_package_data=True,
    install_requires=[
        "flask",
        "flake8",
        "isort",
        "mypy",
        "pre-commit",
        "pytest"
    ],
)
