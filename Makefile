# Project Chimera - Standardized Build and Test Automation
# Ensures "works on my machine" is never an issue

.PHONY: help setup test spec-check clean

# Docker image name
IMAGE_NAME := project-chimera
CONTAINER_NAME := project-chimera-test

# Default target
help:
	@echo "Project Chimera - Available Commands:"
	@echo ""
	@echo "  make setup      - Build Docker image and install dependencies"
	@echo "  make test       - Run pytest inside Docker (tests should fail at TDD stage)"
	@echo "  make spec-check - Validate code structure aligns with specs"
	@echo "  make clean      - Remove Docker image and containers"
	@echo ""

# Build Docker image (installs dependencies via uv)
setup:
	@echo "🔨 Building Docker image with dependencies..."
	docker build -t $(IMAGE_NAME) .
	@echo "✅ Setup complete. Image '$(IMAGE_NAME)' is ready."

# Run pytest inside Docker container
# Tests MUST fail at this stage (TDD - no implementations exist)
test:
	@echo "🧪 Running tests in Docker container..."
	@echo "   (Expected: All tests will fail - this is correct for TDD stage)"
	docker run --rm \
		--name $(CONTAINER_NAME) \
		-v $$(pwd)/specs:/app/specs:ro \
		-v $$(pwd)/skills:/app/skills:ro \
		-v $$(pwd)/tests:/app/tests:ro \
		$(IMAGE_NAME) \
		pytest tests/ -v --tb=short
	@echo ""
	@echo "ℹ️  Note: Test failures are expected until implementations are added."

# Validate code structure aligns with specifications
spec-check:
	@echo "🔍 Validating code structure against specs..."
	@./scripts/spec-check.sh

# Clean up Docker resources
clean:
	@echo "🧹 Cleaning up Docker resources..."
	-docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	-docker rmi $(IMAGE_NAME) 2>/dev/null || true
	@echo "✅ Cleanup complete."
