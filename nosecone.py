
import argparse
import numpy as np

def main(args):
    print(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Makes nosecone shape')
    parser.add_argument('--shape',
                        type=str,
                        help='nose cone shape',
                        choices = ['conic'],
                        required=True)
    parser.add_argument('--radius',
                        type=float,
                        help='radius at base',
                        required=True)
    parser.add_argument('--length',
                        type=float,
                        help='length from base to apex',
                        required=True)
    args = parser.parse_args()
    main(args)
