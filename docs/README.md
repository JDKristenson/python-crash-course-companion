# Learning map

- [Editable Excalidraw scene](learning-map.excalidraw): open/import this file in an Excalidraw-compatible editor. Text and rectangles are separate editable elements, not a flattened image.
- [SVG preview](learning-map.svg): a deterministic, simplified rendering of the same scene, embedded in the main README. It uses standard fonts rather than Excalidraw's hand-drawn renderer.
- [Preview renderer](render_learning_map.py): Python standard library only; no package installation or application build needed.

After editing text or rectangles in the scene, regenerate and check the preview from the repository root:

```bash
python3 docs/render_learning_map.py
python3 docs/render_learning_map.py --check
```

The renderer deliberately supports only the current plain-text/rectangle subset. If you introduce other element types, update the renderer or export and verify a matching SVG in the editor instead. Inspect the final preview visually; byte parity alone cannot prove readability or successful editor import.

The map separates existing material, unresolved upstream resources and future student work. It does not describe an application architecture. Book attribution, recorded human/Warp credits and Reason AI assistance are shown without assigning ownership or licensing rights. No private paths, account values, external images or student data are embedded. See [provenance and license status](../README.md#provenance-credits-and-license-status) for the limits of those statements.
