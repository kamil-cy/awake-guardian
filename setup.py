from platform import system
from setuptools import setup
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if system() == "Linux":
    executable = "bin/AwakeGuardian"
else:
    executable = "bin/AwakeGuardian.py"


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        if system() == "Windows":
            from os import environ

            desktop_path = f"{environ['USERPROFILE']}\\Desktop\\AwakeGuardian.bat"
            with open(desktop_path, "w") as f:
                f.write(
                    "@echo off\n"
                    """FOR /F "delims=" %%i IN ('where AwakeGuardian.py') DO set aw=%%i"""  # don't change %%, """, ", '
                    "\nstart pythonw %aw%\n"
                )


setup(
    name="awake-guardian",
    version="1.0.1",
    author="Kamil Cyganowski",
    author_email="kamil.cyganowski@gmail.com",
    packages=["awake_guardian"],
    package_data={"": ["audio/*.wav", "images/*.png"]},
    scripts=[executable],
    install_requires=[
        "appdirs",
        "configparser",
        "pynput",
        "PySide2",
        "simpleaudio;platform_system=='Linux'",
        "pyalsaaudio;platform_system=='Linux'",
        "pycaw;platform_system=='Windows'",
        "playsound==1.2.2;platform_system=='Windows'",
        # FIXED to 1.2.2, because playsound 1.3.0 error: The specified device is not open or is not recognized by MCI
    ],
    cmdclass={
        "install": PostInstallCommand,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    description="AwakeGuardia is a program that helps you keep awake and not to fall asleep in front of a computer. "
    "The program frequently alerts you when detects your inactivity by reminding or later by nagging you using sound.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamil-cy/awake-guardian",
)
