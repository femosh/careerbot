#!/bin/bash

# Quick start script for CareerBot Microservice
# This script initializes the database and starts both the API and dashboard

echo "========================================="
echo "CareerBot Microservice Quick Start"
echo "========================================="
echo ""

# Check if database exists
if [ ! -f "careerbot.db" ]; then
    echo "Database not found. Initializing..."
    python3 init_db.py <<EOF
yes
EOF
    if [ $? -ne 0 ]; then
        echo "Error: Failed to initialize database"
        exit 1
    fi
    echo ""
fi

# Generate API documentation
echo "Generating API documentation..."
python3 generate_api_docs.py
echo ""

# Start FastAPI backend
echo "Starting FastAPI backend on http://localhost:8000..."
python3 main.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

# Check if backend is running
if curl -s http://localhost:8000/ > /dev/null; then
    echo "✓ Backend is running successfully"
    echo ""
    echo "API Documentation available at:"
    echo "  - Swagger UI: http://localhost:8000/docs"
    echo "  - ReDoc: http://localhost:8000/redoc"
    echo ""
else
    echo "✗ Failed to start backend"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

# Start Dashboard
echo "Starting Plotly Dash dashboard on http://localhost:8050..."
echo ""
echo "========================================="
echo "Services are starting..."
echo "========================================="
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Run dashboard in foreground
python3 dashboard.py

# Cleanup on exit
kill $BACKEND_PID 2>/dev/null
echo ""
echo "All services stopped."
