#!/usr/bin/env python3
"""
verbot - A CLI tool for generating verbal content (for testing/research purposes only)
"""
import argparse
import sys
from insult_engine import InsultEngine

def setup_parser():
    parser = argparse.ArgumentParser(
        description="Generate verbal content for testing/research purposes",
        epilog="Note: This tool is for testing and research purposes only."
    )
    parser.add_argument(
        "--target",
        help="Target name to customize the output",
        default=""
    )
    parser.add_argument(
        "--category",
        choices=["appearance", "intelligence", "personality"],
        help="Category of content to generate",
        default="personality"
    )
    parser.add_argument(
        "--intensity",
        choices=["light", "medium", "brutal"],
        help="Intensity level of the content",
        default="light"
    )
    parser.add_argument(
        "--count",
        type=int,
        help="Number of lines to generate",
        default=1
    )
    parser.add_argument(
        "--save",
        help="Save output to specified file",
        metavar="FILE"
    )
    return parser

def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    engine = InsultEngine()
    engine.set_intensity_level(args.intensity)
    
    outputs = []
    for _ in range(args.count):
        if args.target:
            output = engine.generate_keyword_insult(args.target, args.category)
        else:
            output = engine.generate_random_insult(args.category)
        outputs.append(output)
        print(f"🗯️ {output}")
    
    if args.save:
        with open(args.save, "w") as f:
            f.write("\n".join(outputs))
            print(f"\nOutput saved to {args.save}")

if __name__ == "__main__":
    main()
