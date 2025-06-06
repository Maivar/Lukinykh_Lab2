# MLOps Labs – Lukinykh

This repository contains completed lab assignments 1–5 for the ML Operations course. Each lab is implemented in a separate folder and includes configuration files, training scripts, tracking tools, and automation components.

## Lab Overview

### Lab 1 – Training Pipeline
- PyTorch model using MNIST dataset.
- Includes model training, evaluation, and metrics like accuracy, precision, recall, and F1-score.

### Lab 2 – Dataset Extension
- Dynamically creates training/validation/test splits using a configuration file.
- Demonstrates how different splits affect model performance.

### Lab 3 – DVC Pipeline
- DVC pipeline with stages: prepare, train, evaluate.
- Tracks parameters and dependencies via dvc.yaml and params.yaml.

### Lab 4 – MLflow Tracking
- Tracks experiment parameters, metrics, and model artifact.
- View experiments through MLflow UI.

### Lab 5 – Weights & Biases
- Tracks multiple runs with parameters and accuracy metrics using wandb.

## Project Structure

Each lab has its own directory with scripts and configs. To run any lab:
```bash
cd labX_directory
python script.py
