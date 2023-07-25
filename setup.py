from setuptools import setup, find_packages

setup(
    name='gptyoutube',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'youtube_dl',
        'openai',
        'SpeechRecognition',
    ],
    entry_points={
        'console_scripts': [
            'gptyoutube=gptyoutube.__main__:main',
        ],
    },
)
