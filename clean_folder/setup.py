from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Clean folder by Python',
    url='https://github.com/egorshanin21/Module7.git',
    author='Egor Shanin',
    author_email='egorshanin21@gmail.com',
    license='MIT',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:run']}
)