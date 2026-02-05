# Project Chimera - Development Environment Dockerfile
# Encapsulates Python, uv, and pytest for consistent testing across environments

# Stage 1: Copy uv binary from official image
FROM ghcr.io/astral-sh/uv:latest AS uv

# Stage 2: Python runtime with uv
FROM python:3.12-slim

# Copy uv binary from stage 1
COPY --from=uv /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Install system dependencies (minimal, for uv)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock .python-version ./

# Install Python dependencies using uv
# This creates a virtual environment and installs all dependencies including dev
RUN uv sync --extra dev --frozen

# Copy project structure (specs, skills, tests)
# Note: We do NOT copy application code - this is intentional for TDD
COPY specs/ ./specs/
COPY skills/ ./skills/
COPY tests/ ./tests/

# Set environment variables for uv
ENV PATH="/app/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/.venv"

# Default command runs pytest (can be overridden)
CMD ["pytest", "tests/", "-v"]
