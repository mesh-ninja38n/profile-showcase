import argparse
import sys
import yaml
from pathlib import Path
from renderers import render_markdown

def load_config(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Config not found: {path}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Invalid YAML: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate a privacy-first profile showcase in Markdown.")
    parser.add_argument("--config", required=True, help="Path to config.yml")
    parser.add_argument("--output", default="OUTPUT.md", help="Path to write rendered Markdown")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    md = render_markdown(cfg)

    out_path = Path(args.output)
    out_path.write_text(md, encoding="utf-8")
    print(f"Written: {out_path}")

if __name__ == "__main__":
    main()
