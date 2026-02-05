#!/bin/bash
# spec-check.sh - Lightweight validation that code structure aligns with specs
# Exit code: 0 if all checks pass, 1 if any check fails

set -e

ERRORS=0
WARNINGS=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check_file() {
    local file=$1
    local description=$2
    
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ Missing: $file${NC} ($description)"
        ((ERRORS++))
        return 1
    else
        echo -e "${GREEN}✓${NC} Found: $file"
        return 0
    fi
}

check_directory() {
    local dir=$1
    local description=$2
    
    if [ ! -d "$dir" ]; then
        echo -e "${RED}❌ Missing directory: $dir${NC} ($description)"
        ((ERRORS++))
        return 1
    else
        echo -e "${GREEN}✓${NC} Found directory: $dir"
        return 0
    fi
}

check_contains() {
    local file=$1
    local pattern=$2
    local description=$3
    
    if grep -q "$pattern" "$file" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $description"
        return 0
    else
        echo -e "${RED}❌ $description${NC} (pattern not found: $pattern)"
        ((ERRORS++))
        return 1
    fi
}

echo "=========================================="
echo "Project Chimera - Spec Structure Check"
echo "=========================================="
echo ""

# Check required spec files
echo "📋 Checking spec files..."
check_file "specs/technical.md" "Technical specifications"
check_file "specs/functional.md" "Functional specifications"
check_file "specs/_meta.md" "Spec metadata"
check_file "specs/openclaw_integration.md" "OpenClaw integration specs"

# Check skills documentation
echo ""
echo "🛠️  Checking skills structure..."
check_directory "skills" "Skills directory"
check_file "skills/README.md" "Skills README"

# Validate skills README contains required skill definitions
if [ -f "skills/README.md" ]; then
    echo ""
    echo "   Validating skill contracts in skills/README.md..."
    check_contains "skills/README.md" "skill_fetch_trends" "skill_fetch_trends contract defined"
    check_contains "skills/README.md" "skill_generate_script" "skill_generate_script contract defined"
    check_contains "skills/README.md" "skill_generate_video" "skill_generate_video contract defined"
    check_contains "skills/README.md" "skill_publish_video" "skill_publish_video contract defined"
fi

# Check test files
echo ""
echo "🧪 Checking test files..."
check_directory "tests" "Tests directory"
check_file "tests/__init__.py" "Tests package init"
check_file "tests/test_trend_fetcher.py" "Trend fetcher tests"
check_file "tests/test_skills_interface.py" "Skills interface tests"

# Validate tests reference correct contracts
if [ -f "tests/test_trend_fetcher.py" ]; then
    echo ""
    echo "   Validating test_trend_fetcher.py references..."
    check_contains "tests/test_trend_fetcher.py" "skills.trend_fetcher" "Test imports trend_fetcher module"
    check_contains "tests/test_trend_fetcher.py" "fetch_trends" "Test references fetch_trends function"
fi

if [ -f "tests/test_skills_interface.py" ]; then
    echo ""
    echo "   Validating test_skills_interface.py references..."
    check_contains "tests/test_skills_interface.py" "skill_fetch_trends" "Test references skill_fetch_trends"
    check_contains "tests/test_skills_interface.py" "skill_generate_script" "Test references skill_generate_script"
    check_contains "tests/test_skills_interface.py" "skill_generate_video" "Test references skill_generate_video"
    check_contains "tests/test_skills_interface.py" "skill_publish_video" "Test references skill_publish_video"
fi

# Check pytest configuration
echo ""
echo "⚙️  Checking pytest configuration..."
check_file "pyproject.toml" "Project configuration"

if [ -f "pyproject.toml" ]; then
    check_contains "pyproject.toml" "pytest" "pytest in dependencies"
    check_contains "pyproject.toml" "\\[tool.pytest.ini_options\\]" "pytest configuration section"
fi

# Summary
echo ""
echo "=========================================="
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ All checks passed!${NC}"
    echo "   Code structure aligns with specifications."
    exit 0
else
    echo -e "${RED}❌ Validation failed with $ERRORS error(s)${NC}"
    echo "   Please fix the issues above."
    exit 1
fi
