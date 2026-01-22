#!/usr/bin/env bash

# === CONFIG ===
APP_NAME="matplotlib"
ENTRYPOINT="src/projects/pyside6/main.py"
DIST_DIR="dist"
BUILD_DIR="build"

# Clean previous builds
rm -rf "$DIST_DIR" "$BUILD_DIR" "${APP_NAME}.spec"

# Build one-file executable
pyinstaller \
  --name "$APP_NAME" \
  --onefile \
  --windowed \
  --clean \
  --noconfirm \
  --distpath "$DIST_DIR" \
  --workpath "$BUILD_DIR" \
  "$ENTRYPOINT"

echo
echo "=== Done. Output: ${DIST_DIR}/${APP_NAME} ==="
