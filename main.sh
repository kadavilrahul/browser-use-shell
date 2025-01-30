#!/bin/bash

# Function to detect the package manager and Linux distribution
detect_package_manager() {
    if command -v apt &> /dev/null; then
        echo "debian"
    elif command -v pacman &> /dev/null; then
        echo "arch"
    else
        echo "unsupported"
    fi
}

# Get the distribution type
DISTRO_TYPE=$(detect_package_manager)

# Execute the appropriate setup script based on the distribution
case "$DISTRO_TYPE" in
    "debian")
        echo "Detected Debian-based system. Running Debian setup..."
        bash ./setup-debian.sh
        ;;
    "arch")
        echo "Detected Arch-based system. Running Arch setup..."
        bash ./setup-arch.sh
        ;;
    *)
        echo "Error: Unsupported Linux distribution or package manager."
        echo "This script currently supports Debian-based (apt) and Arch-based (pacman) systems."
        exit 1
        ;;
esac
