#!/bin/sh

# Installer les packages python3 et pip3
apk add --no-cache python3 py3-pip

# Installer Flask
pip3 install Flask

# Creation du fichier requirements.txt
pip3 freeze | grep Flask >> requirements.txt
