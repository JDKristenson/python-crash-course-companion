#!/usr/bin/env python3
"""
Quick Test Runner - Python Crash Course Companion

A simple script to quickly test Python code snippets.
Perfect for trying out exercises and examples from the book.

Usage:
    python quick_test.py

This will run whatever code you put in the test_code() function below.
"""

def test_code():
    """
    Put your test code here!
    This is your sandbox for quick experiments.
    """
    # Example: Uncomment and modify the code below
    # print("Hello, Python!")
    
    # Try your own code here:
    pass


if __name__ == "__main__":
    print("=" * 50)
    print("Python Crash Course - Quick Test Runner")
    print("=" * 50)
    print()
    
    try:
        test_code()
    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"   {e}")
        import traceback
        print("\nFull traceback:")
        traceback.print_exc()
    else:
        print("\n✅ Code executed successfully!")
    
    print()
    print("=" * 50)
