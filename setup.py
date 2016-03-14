from distutils.core import setup
setup(
    name="irc-autobot",
    packages=["autobot"],
    version="1.0.2",
    description="Context Manager for ease of creating IRC bots",
    author="Wayne Simmerson",
    author_email="wsimmerson@gmail.com",
    url="https://github.com/wsimmerson/autobot",
    download_url="https://github.com/wsimmerson/autobot/tarball/1.0.2",
    keywords=["irc", "bot"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ],
    long_description="""
        Autobot
        -------

        Context Manger for ease of creating IRC Bots
    """
)
