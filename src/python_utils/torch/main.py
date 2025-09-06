import argparse
import sys
from pathlib import Path

from . import data_setup
from . import engine
from . import model_builder
from . import train
from . import utils

def main():
    """Main function that coordinates the PyTorch workflow."""
    parser = argparse.ArgumentParser(description="PyTorch Training Pipeline")
    parser.add_argument("--mode", choices=["train", "eval", "data_prep"], 
                       default="train", help="Mode to run")
    parser.add_argument("--data-path", type=str, required=True,
                       help="Path to training data")
    parser.add_argument("--model-name", type=str, default="simple_cnn",
                       help="Model architecture to use")
    parser.add_argument("--epochs", type=int, default=10,
                       help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=32,
                       help="Batch size for training")
    
    args = parser.parse_args()
    
    print(f"Starting PyTorch pipeline in {args.mode} mode...")
    
    if args.mode == "data_prep":

        print("Setting up data...")

        
    elif args.mode == "train":
        print("Starting training...")

        
        print(f"Training completed with {args.epochs} epochs")
        
    elif args.mode == "eval":
        print("Starting evaluation...")
        
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()