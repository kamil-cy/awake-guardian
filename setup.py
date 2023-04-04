from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    author="Kamil Cyganowski",
    author_email="kamil.cyganowski@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    description="AwakeGuardia is a program that helps you keep awake and not to fall asleep in front of a computer. "
    "The program frequently alerts you when detects your inactivity by reminding or later by nagging you using sound. "
    "Moreover to save your money your computer can be suspended or powered off.",
    entry_points={"gui_scripts": ["AwakeGuardian = awake_guardian:main"]},
    install_requires=[
        "appdirs",
        "pynput",
        "PySide6",
        "pyyaml",
        "playsound",
        "pyalsaaudio;platform_system=='Linux'",
        "pycaw;platform_system=='Windows'",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="awake-guardian",
    package_data={"": ["audio/*.mp3", "images/*.png"]},
    packages=["awake_guardian"],
    python_requires=">=3.6",
    scripts=["bin/AwakeGuardian"],
    url="https://github.com/kamil-cy/awake-guardian",
    version="1.3.1",
)
