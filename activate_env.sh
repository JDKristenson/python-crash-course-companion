#!/bin/bash
# Activation Helper for Python Crash Course Companion
# This script activates the virtual environment

echo "=================================================="
echo "Python Crash Course - Environment Activator"
echo "=================================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "   Please run: python3 -m venv venv"
    exit 1
fi

# Activate the virtual environment
source venv/bin/activate

echo "✅ Virtual environment activated!"
echo ""
echo "📚 Quick Commands:"
echo "   - Run tests: python quick_test.py"
echo "   - Start Python: python"
echo "   - Deactivate: deactivate"
echo ""
echo "📂 Your workspace: my_work/"
echo "📖 Exercise guides: exercises/"
echo "🔍 Quick reference: quick_reference/"
echo "📦 Book resources: book_resources/"
echo ""
echo "=================================================="
