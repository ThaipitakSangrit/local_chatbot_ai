from setuptools import setup, find_packages

setup(
    name='ollama_streamlit_demos',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here, for example:
        'streamlit',
        'numpy',
        'pandas',
    ],
)
