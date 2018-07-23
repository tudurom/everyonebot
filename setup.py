from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="everyonebot",
    version="0.0.1",
    author="Tudor Roman",
    author_email="tudurom@gmail.com",
    description="Telegram bot that implements Discord's @everyone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tudurom/everyonebot",
    packages=find_packages(),
    install_requires=['Pyrogram', 'TgCrypto'],
    scripts=['everyonebot/everyonebot'],
    classifiers=[
        'License :: OSI Approved :: ISC License (ISCL)'
    ]
)
