#!/bin/bash

# Batch script to generate API documentation artifacts for frontend developers

echo "========================================="
echo "CareerBot API Documentation Generator"
echo "========================================="
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

echo "Generating API documentation artifacts..."
echo ""

# Run the documentation generator
python3 generate_api_docs.py

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "Documentation generated successfully!"
    echo "========================================="
    echo ""
    echo "Generated files:"
    ls -lh api_endpoints.json API_DOCUMENTATION.md 2>/dev/null
    echo ""
    echo "These artifacts are ready for frontend developers to use."
else
    echo ""
    echo "Error: Failed to generate documentation"
    exit 1
fi
