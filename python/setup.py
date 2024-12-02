from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel
import platform
import subprocess
import os

def get_version():
    """Get version number"""
    with open('version.txt', 'r') as f:
        return f.read().strip()

def get_wheel_platform_tag():
    """Get wheel package platform tag"""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    arch_mapping = {
        'x86_64': {
            'windows': 'win_amd64',
            'linux': 'manylinux2014_x86_64',
            'darwin': 'macosx_12_0_x86_64'
        },
        'amd64': {
            'windows': 'win_amd64',
            'linux': 'manylinux2014_x86_64',
            'darwin': 'macosx_12_0_x86_64'
        },
        'arm64': {
            'windows': 'win_arm64',
            'linux': 'manylinux2014_aarch64',
            'darwin': 'macosx_11_0_arm64'
        },
        'aarch64': {
            'windows': 'win_arm64',
            'linux': 'manylinux2014_aarch64',
            'darwin': 'macosx_11_0_arm64'
        }
    }
    
    platform_arch = arch_mapping.get(machine, {}).get(system)
    if not platform_arch:
        raise RuntimeError(f"Unsupported platform: {system} {machine}")
    
    return platform_arch

def get_lib_path_info():
    """Get library file path information"""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == 'windows':
        arch = 'x64' if machine in ['amd64', 'x86_64'] else 'arm64'
    elif system == 'linux':
        arch = 'x64' if machine == 'x86_64' else 'arm64'
    elif system == 'darwin':
        if machine == 'x86_64':
            try:
                is_rosetta = bool(int(subprocess.check_output(
                    ['sysctl', '-n', 'sysctl.proc_translated']).decode().strip()))
                arch = 'arm64' if is_rosetta else 'x64'
            except:
                arch = 'x64'
        else:
            arch = 'arm64'
    else:
        raise RuntimeError(f"Unsupported system: {system}")
    
    return system, arch

class BinaryDistWheel(bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        # Mark this is not a pure Python package
        self.root_is_pure = False
        # Set platform tag
        self.plat_name = get_wheel_platform_tag()

# Get current platform information
system, arch = get_lib_path_info()

# Build library file path relative to package
lib_path = os.path.join('modules', 'core', 'libs', system, arch, '*')

setup(
    name='inspireface',
    version=get_version,
    packages=find_packages(),
    # package_data path should be relative to package directory
    package_data={
        'inspireface': [lib_path]
    },
    author='Jingyu Yan',
    author_email='tunmxy@163.com',
    description='InspireFace Python SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HyperInspire/InspireFace',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
    ],
    python_requires='>=3.7',
    cmdclass={
        'bdist_wheel': BinaryDistWheel
    }
)