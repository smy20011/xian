# Dumpling Filling Seasoning Calculator

This project contains two ways to run the meat filling seasoning calculator:

1. **CLI** (original):
   ```bash
   uv run main.py
   ```
   Follow the prompts to enter ingredient weights.
2. **Static website (Vue-powered)**: open `index.html` in any modern browser (double-click it or serve the repo with your favorite static file server). Vue 3 (loaded via CDN) drives the reactive ingredient lists—add beef、虾仁、蔬菜等项目，调整可选调味量，配比会实时刷新。

Both versions share the same computation logic: water is 40% of the meat, oil is 2% of the combined mixture, and the seasonings are derived from the overall salt ratio.
