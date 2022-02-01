#!/bin/env bash

set -e

echo -e "\nStart black\n" && black . --exclude=venv
echo -e "\nStart isort\n\n" isort . --skip venv
