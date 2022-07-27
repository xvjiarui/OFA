from setuptools import find_packages, setup

setup(
    name="ofa",
    py_modules=["ofa"],
    version="1.0",
    description="",
    author="OFA",
    packages=find_packages(),
    install_requires = [
  'fairseq @ git+ssh://git@github.com/xvjiarui/OFA-fairseq@main#egg=fairseq',
],
    include_package_data=True,
)