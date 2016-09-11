import subprocess
from setuptools import setup
from setuptools.command.install import install as _install


class install(_install):
    def run(self):
        _install.run(self)
        subprocess.call(["bash", "post_install"])


setup(
    name="chronos",
    version="0.3.6",
    description="Boiling/cooling water system.",
    url="https://bitbucket.org/quarck/chronos/",
    author="Dmitry Misharov",
    author_email="quarckster@gmail.com",
    packages=[
        "chronos",
        "chronos.lib",
        "chronos.bin",
        "chronos.utils"],
    install_requires=[
        "apscheduler",
        "sqlalchemy",
        "Flask",
        "pymodbus",
        "websocket-client",
        "SimpleWebSocketServer"],
    dependency_links=[
        ("git+https://github.com/dpallot/simple-websocket-server.git"
         "#egg=SimpleWebSocketServer-0.1")
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "chronosd = chronos.bin.chronosd:main",
            "chronos_debug = chronos.utils.chronos_hardware_debug:main"]},
    data_files=[
        ("/etc", ["data_files/chronos_config.json"]),
        ("/etc/init.d", ["data_files/chronos"]),
        ("/etc/apache2/sites-enabled", ["data_files/chronos.conf"]),
        ("/var/www", ["data_files/chronos.wsgi"])],
    cmdclass={
        "install": install},
    classifiers=[
        "Private :: Do Not Upload"]
)
