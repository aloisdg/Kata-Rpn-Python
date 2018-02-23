#! /bin/bash

while true; do git reset --hard -q; git clean -f -q; sleep 340; echo "20s left"; sleep 20; echo "erased"; done
