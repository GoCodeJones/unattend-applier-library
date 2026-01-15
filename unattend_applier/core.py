# ============================================================================
# unattend_applier/__init__.py - API PÚBLICA
# ============================================================================

"""
Unattend Applier - Apply Windows configurations from autounattend.xml files

Usage:
    >>> from unattend_applier import UnattendConfig
    >>> config = UnattendConfig('autounattend.xml')
    >>> config.apply_all()
"""

from .core import UnattendConfig

__version__ = '1.0.0'
__all__ = ['UnattendConfig']


# ============================================================================
# EXEMPLO DE USO - CASO 1: Simples (95% dos casos)
# ============================================================================

from unattend_applier import UnattendConfig

# Aplicar tudo
config = UnattendConfig('autounattend.xml')
config.apply_all()


# ============================================================================
# EXEMPLO DE USO - CASO 2: Seletivo
# ============================================================================

from unattend_applier import UnattendConfig

config = UnattendConfig('autounattend.xml')

# Aplicar só o que quiser
config.remove_packages()
config.apply_registry_tweaks()
# Pular PowerShell se quiser


# ============================================================================
# EXEMPLO DE USO - CASO 3: Preview (ver antes de aplicar)
# ============================================================================

from unattend_applier import UnattendConfig

config = UnattendConfig('autounattend.xml')

# Ver o que seria feito
info = config.get_info()
print(f"Packages: {len(info['packages'])}")
print(f"Scripts: {len(info['scripts'])}")
print(f"Registry files: {len(info['registry_files'])}")


# ============================================================================
# EXEMPLO DE USO - CASO 4: Como CLI (mantém compatibilidade)
# ============================================================================

# python -m unattend_applier autounattend.xml

# Ou após pip install:
# unattend-apply autounattend.xml


# ============================================================================
# setup.py MINIMALISTA
# ============================================================================

"""
from setuptools import setup, find_packages

setup(
    name='unattend-applier',
    version='1.0.0',
    description='Apply Windows debloat configurations from autounattend.xml',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    url='https://github.com/yourusername/unattend-applier',
    packages=find_packages(),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'unattend-apply=unattend_applier.core:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
    ],
)
"""


# ============================================================================
# pyproject.toml MINIMALISTA (alternativa moderna ao setup.py)
# ============================================================================

"""
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "unattend-applier"
version = "1.0.0"
description = "Apply Windows debloat configurations from autounattend.xml"
readme = "README.md"
requires-python = ">=3.7"
license = {text = "MIT"}

[project.scripts]
unattend-apply = "unattend_applier.core:main"
"""


# ============================================================================
# unattend_applier/core.py - CÓDIGO PRINCIPAL (mesmo que já temos)
# ============================================================================

# Apenas pequenas modificações no código existente:

class UnattendConfig:
    """Main class for applying unattend.xml configurations"""
    
    def __init__(self, xml_path):
        """Initialize with path to XML file
        
        Args:
            xml_path: Path to autounattend.xml file
        """
        self.xml_path = xml_path
        # ... resto do código que já temos
    
    def get_info(self):
        """Get information about what will be applied
        
        Returns:
            dict: Information about packages, scripts, etc
        """
        files = self.extract_embedded_files()
        return {
            'packages': self.get_packages_to_remove(),
            'capabilities': self.get_capabilities_to_remove(),
            'features': self.get_features_to_remove(),
            'scripts': [f for f in files if f.endswith('.ps1')],
            'registry_files': [f for f in files if f.endswith('.reg')]
        }
    
    def apply_all(self, verbose=True):
        """Apply all configurations
        
        Args:
            verbose: Show progress messages
            
        Returns:
            bool: True if successful
        """
        # ... código que já temos


# Para manter CLI funcionando:
def main():
    """CLI entry point"""
    import sys
    if len(sys.argv) < 2:
        print("Usage: unattend-apply <file.xml>")
        sys.exit(1)
    
    config = UnattendConfig(sys.argv[1])
    success = config.apply_all()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()


# ============================================================================
# INSTALAÇÃO E USO
# ============================================================================

"""
# Para desenvolver localmente:
pip install -e .

# Para publicar no PyPI:
python -m build
python -m twine upload dist/*

# Para usuários instalarem:
pip install unattend-applier

# Usar como lib:
from unattend_applier import UnattendConfig
config = UnattendConfig('my.xml')
config.apply_all()

# Usar como CLI:
unattend-apply my.xml
"""