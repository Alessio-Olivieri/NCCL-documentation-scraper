# NCCL Documentation Scraper

This simple Python script extracts the current developer guide for NCCL (Nvidia Collective Communication Library).

## What is this for?

As LLM context windows are starting to get bigger, we can feed them entire documentations and ask them directly. This Python script addresses the need for an easily LLM-readable documentation for NCCL.

## How to run

1. **Set up the environment:**
   Ensure you have `nix` installed on your system. If not, you can install it from [NixOS](https://nixos.org/download.html).

2. **Enter the development environment:**
   Run the following command to enter the development environment:
   ```sh
   nix develop
   ```

3. **Execute the script:**
   Once you are in the development environment, run the script using:
   ```sh
   python main.py
   ```

This will execute the script and extract the NCCL developer guide, making it ready for further processing or direct querying by an LLM.
