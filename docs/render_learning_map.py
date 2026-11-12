"""Render the deliberately simple Excalidraw learning map without dependencies.

Run from the repository root: python3 docs/render_learning_map.py [--check]
Only rectangles and plain text are supported; this is a documentation preview,
not Excalidraw's hand-drawn renderer. No repository application is executed.
"""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def render():
    scene = json.loads((ROOT / "learning-map.excalidraw").read_text())
    assert scene["type"] == "excalidraw" and scene["version"] == 2
    assert not scene.get("files"), "Do not embed external or personal assets"
    elements = scene["elements"]
    assert len({e["id"] for e in elements}) == len(elements)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="700" viewBox="0 0 1000 700" role="img" aria-labelledby="title desc">',
        '<title id="title">Python Crash Course companion learning map</title>',
        '<desc id="desc">Present learning material is separate from unresolved book resources and future personal exercises. This is not application architecture.</desc>',
        '<rect width="1000" height="700" fill="white"/>',
    ]
    for e in elements:
        assert e["type"] in ("rectangle", "text") and not e["isDeleted"]
        assert e["link"] is None and 0 <= e["x"] < 1000 and 0 <= e["y"] < 700
        x, y = e["x"], e["y"]
        if e["type"] == "rectangle":
            dash = ' stroke-dasharray="8 6"' if e["strokeStyle"] == "dashed" else ""
            parts.append(f'<rect x="{x}" y="{y}" width="{e["width"]}" height="{e["height"]}" fill="{e["backgroundColor"]}" stroke="{e["strokeColor"]}" stroke-width="2"{dash}/>')
        else:
            size = e["fontSize"]
            parts.append(f'<text x="{x}" y="{y + size}" fill="{e["strokeColor"]}" font-family="Arial, Helvetica, sans-serif" font-size="{size}">')
            for i, line in enumerate(e["text"].splitlines()):
                parts.append(f'<tspan x="{x}" dy="{0 if i == 0 else size * e["lineHeight"]}">{html.escape(line)}</tspan>')
            parts.append('</text>')
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check source/preview parity without writing")
    args = parser.parse_args()
    output = ROOT / "learning-map.svg"
    svg = render()
    if args.check:
        assert output.read_text() == svg, "Preview is stale; rerun renderer"
        print("PASS: editable scene and SVG preview match")
    else:
        output.write_text(svg)
        print("Rendered docs/learning-map.svg")
