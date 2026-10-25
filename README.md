# Voxel Valley

A procedurally generated isometric voxel diorama rendered with Three.js: a mauve
rock plateau with perched pools and dead trees, a band of leafy forest and
lavender stone spires, a shallow turquoise lake with terraced sand shallows,
a snowy spruce corner and a dark conifer forest.

Open `index.html` in a browser (it loads Three.js from a CDN), or serve the
folder with any static server, e.g. `npx serve .`.

- Drag to rotate, right-drag to pan, scroll to zoom.
- **New world** generates a fresh seed, **Orbit** slowly spins the camera,
  **Tilt-shift** toggles the miniature-style depth-of-field blur.

How it works: a seeded simplex-noise heightfield is blended from four
landscape masks (plateau, lowland/lake, snow, forest), filled into a
256 × 176 × 64 voxel grid, decorated with trees and spires, then meshed into
exposed faces only with per-vertex ambient occlusion baked into the vertex
colours. Water is a separate translucent shader surface whose colour and
opacity follow the depth below it. Shadows come from a single directional
sun; a two-pass tilt-shift blur and a light colour grade finish the frame.

# Penguin Donut Shop

`donut-shop.html` is a hand-drawn style 2D scene on a canvas: a muted shopfront
with a pastry display case, a COFFEE / TEA / MILK sign, hanging bulbs, a mauve
door, and two animated penguins. On an 18-second loop the penguin by the wall machine
reaches up, pulls out a donut, turns to face you and eats it in four bites
(crumbs, "nom"s, a happy heart), then the machine slides a fresh donut into place.
The camera pushes in for the snack; the "Close-ups" button keeps the full frame. Lines are drawn with a seeded "sketchy" stroke so
they wobble, overshoot and break like ink; character lines re-jitter on a
three-frame cycle like hand-drawn animation, and a paper grain sits on top.
Open the file in a browser; it fits any screen at 16:9.
