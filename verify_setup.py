#!/usr/bin/env python3
"""
Setup Verification Script - Python Crash Course Companion

This script verifies that all required packages are installed
and the environment is ready for offline use.
"""

import sys

def check_python_version():
    """Check if Python version is 3.7 or higher."""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 7:
        print("  ✅ Python version is compatible")
        return True
    else:
        print("  ❌ Python 3.7 or higher required")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed."""
    if import_name is None:
        import_name = package_name
    
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"  ✅ {package_name} (version: {version})")
        return True
    except ImportError:
        print(f"  ❌ {package_name} is not installed")
        return False

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("Python Crash Course - Environment Verification")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check Python version
    print("1. Checking Python Version...")
    all_good = check_python_version() and all_good
    print()
    
    # Check required packages
    print("2. Checking Required Packages...")
    packages = [
        ('pygame', 'pygame'),
        ('matplotlib', 'matplotlib'),
        ('plotly', 'plotly'),
        ('django', 'django'),
        ('requests', 'requests'),
        ('beautifulsoup4', 'bs4'),
        ('pytest', 'pytest'),
    ]
    
    for package_name, import_name in packages:
        check_package(package_name, import_name)
    
    print()
    
    # Check directory structure
    print("3. Checking Directory Structure...")
    import os
    directories = [
        'my_work/part_1_basics',
        'my_work/part_2_projects',
        'exercises',
        'quick_reference',
        'book_resources',
        'venv',
    ]
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"  ✅ {directory}/")
        else:
            print(f"  ❌ {directory}/ not found")
            all_good = False
    
    print()
    print("=" * 60)
    
    if all_good:
        print("✅ ALL CHECKS PASSED - You're ready to learn offline!")
    else:
        print("⚠️  Some issues detected - see above for details")
    
    print("=" * 60)
    print()
    print("Quick Start:")
    print("  1. Activate environment: source activate_env.sh")
    print("  2. Start learning: open exercises/CHAPTERS_OVERVIEW.md")
    print("  3. Work in: my_work/part_1_basics/chapters/chapter_XX/")
    print()

if __name__ == "__main__":
    main()
