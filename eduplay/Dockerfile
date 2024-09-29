name: Deploy App to Code Engine

on:
  push:
    branches:
      - main

jobs:
  app:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v3

      - name: Build Docker Image
        run: |
          docker build -t my-docker-image ./eduplay  # Ajusta la ruta según sea necesario

      - name: Deploy Application to Code Engine
        uses: ibm/code-engine-github-action@v1
        with:
          api-key: '1D4vtuwENvuxvHRvYlOK22towUf8WOT0YLCjKQ92ThnE'  # Usa un secreto para la API Key
          resource-group: 'EDUPLAY'
          region: 'us-south'
          project: 'ce-project-APPEDUPLAY'
          component: 'app'
          name: 'eduplayv2'
          build-source: './eduplay'