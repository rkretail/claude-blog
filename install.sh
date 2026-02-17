#!/usr/bin/env bash
set -euo pipefail

# claude-blog installer
# Installs the blog skill ecosystem to ~/.claude/skills/ and ~/.claude/agents/

main() {
    local SKILL_DIR="${HOME}/.claude/skills"
    local AGENT_DIR="${HOME}/.claude/agents"
    local SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    echo "=== claude-blog Installer ==="
    echo ""

    # Check prerequisites
    if ! command -v python3 &>/dev/null; then
        echo "WARNING: python3 not found. The analyze_blog.py script requires Python 3."
        echo "Install with: sudo apt install python3"
    fi

    # Create directories
    echo "Creating directories..."
    mkdir -p "${SKILL_DIR}/blog/references"
    mkdir -p "${SKILL_DIR}/blog/scripts"
    mkdir -p "${SKILL_DIR}/blog-write"
    mkdir -p "${SKILL_DIR}/blog-rewrite"
    mkdir -p "${SKILL_DIR}/blog-analyze"
    mkdir -p "${SKILL_DIR}/blog-brief"
    mkdir -p "${SKILL_DIR}/blog-calendar"
    mkdir -p "${SKILL_DIR}/blog-strategy"
    mkdir -p "${AGENT_DIR}"

    # Copy main skill
    echo "Installing main skill: blog..."
    cp "${SCRIPT_DIR}/blog/SKILL.md" "${SKILL_DIR}/blog/SKILL.md"

    # Copy references
    echo "Installing reference files..."
    cp "${SCRIPT_DIR}/blog/references/"*.md "${SKILL_DIR}/blog/references/"

    # Copy sub-skills
    echo "Installing sub-skills..."
    for skill_dir in "${SCRIPT_DIR}/skills/"*/; do
        skill_name="$(basename "${skill_dir}")"
        cp "${skill_dir}SKILL.md" "${SKILL_DIR}/${skill_name}/SKILL.md"
        echo "  - ${skill_name}"
    done

    # Copy agents
    echo "Installing agents..."
    for agent_file in "${SCRIPT_DIR}/agents/"*.md; do
        agent_name="$(basename "${agent_file}")"
        cp "${agent_file}" "${AGENT_DIR}/${agent_name}"
        echo "  - ${agent_name}"
    done

    # Copy scripts
    echo "Installing scripts..."
    cp "${SCRIPT_DIR}/scripts/analyze_blog.py" "${SKILL_DIR}/blog/scripts/analyze_blog.py"
    chmod +x "${SKILL_DIR}/blog/scripts/analyze_blog.py"

    echo ""
    echo "=== Installation Complete ==="
    echo ""
    echo "Installed:"
    echo "  Main skill:  ${SKILL_DIR}/blog/SKILL.md"
    echo "  Sub-skills:  6 (write, rewrite, analyze, brief, calendar, strategy)"
    echo "  References:  5 (seo-2026, geo, content-rules, visual-media, quality-scoring)"
    echo "  Agents:      2 (blog-researcher, blog-writer)"
    echo "  Scripts:     1 (analyze_blog.py)"
    echo ""
    echo "Commands available:"
    echo "  /blog write <topic>        Write a new blog post"
    echo "  /blog rewrite <file>       Optimize an existing blog post"
    echo "  /blog analyze <file>       Audit blog quality (0-100 score)"
    echo "  /blog brief <topic>        Generate a content brief"
    echo "  /blog calendar             Generate an editorial calendar"
    echo "  /blog strategy <niche>     Blog strategy and topic ideation"
    echo ""
    echo "Restart Claude Code to activate the new skill."
}

main "$@"
