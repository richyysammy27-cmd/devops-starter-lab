#!/bin/bash
echo "=== Starting DevOps Environment Check ==="
echo "Current User: $(whoami)"
echo "Current Directory: $(pwd)"
echo "OS Version: $(uname -a)"
echo "Disk Usage:"
df -h | grep '^/dev/'
echo "=== Check Passed Successfully ==="
