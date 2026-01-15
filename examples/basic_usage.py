"""
Basic usage examples for unattend-applier library
"""

from unattend_applier import UnattendConfig


def example_1_apply_all():
    """Example 1: Apply all settings from XML file"""
    print("Example 1: Apply all settings")
    print("-" * 50)
    
    config = UnattendConfig('autounattend.xml')
    config.apply_all()


def example_2_selective_application():
    """Example 2: Apply only specific settings"""
    print("\nExample 2: Selective application")
    print("-" * 50)
    
    config = UnattendConfig('autounattend.xml')
    
    # Apply only what you want
    config.remove_packages()
    config.apply_registry_scripts(config.extract_embedded_files())
    # Skip PowerShell scripts if desired


def example_3_preview_before_apply():
    """Example 3: Preview what will be applied"""
    print("\nExample 3: Preview before applying")
    print("-" * 50)
    
    config = UnattendConfig('autounattend.xml')
    
    # Get information about what will be applied
    info = config.get_info()
    
    print(f"Packages to remove: {len(info['packages'])}")
    print(f"Capabilities to remove: {len(info['capabilities'])}")
    print(f"Features to remove: {len(info['features'])}")
    print(f"PowerShell scripts: {len(info['scripts'])}")
    print(f"Registry files: {len(info['registry_files'])}")
    
    print("\nPackages:")
    for pkg in info['packages'][:5]:  # Show first 5
        print(f"  - {pkg}")


def example_4_silent_mode():
    """Example 4: Apply settings silently (no output)"""
    print("\nExample 4: Silent mode")
    print("-" * 50)
    
    config = UnattendConfig('autounattend.xml')
    success = config.apply_all(verbose=False)
    
    if success:
        print("✓ Settings applied successfully")
    else:
        print("✗ Failed to apply settings")


if __name__ == '__main__':
    print("=" * 50)
    print("UNATTEND APPLIER - USAGE EXAMPLES")
    print("=" * 50)
    
    # Uncomment the example you want to run:
    # example_1_apply_all()
    # example_2_selective_application()
    example_3_preview_before_apply()
    # example_4_silent_mode()