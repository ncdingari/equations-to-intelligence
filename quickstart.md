# Quickstart: From Equations to Intelligence Presentation

This presentation uses the lightweight and powerful Reveal.js framework. It has no build steps, relies on pure front-end web technologies, and is ready out-of-the-box.

## How to run locally

Since this project consists of just static files (HTML, CSS, Markdown), you can serve it easily via any local web server. 

The easiest method (if you have Python installed) is to run the following command directly from this directory:

```bash
python3 -m http.server 8080
```

Then, open your browser and navigate to:
**[http://localhost:8080](http://localhost:8080)**

---

## How it works

- **`index.html`**: The main rendering engine. This contains all custom styling, the Reveal.js initialization scripts, your custom CSS variables (fonts/colors), your SciEncephalon AI global logo, and custom animations.
- **`slides.md`**: Your actual presentation separated by `---` (horizontal sections) lines. If you need to edit the copy or change speaker notes, you do it directly here using standard Markdown syntax!

## How to navigate

- **Next / Previous Slide:** `Space bar` or `Arrow Keys` (←, →, ↑, ↓)
- **Speaker Notes Window:** Press `S` on your keyboard. This opens the second screen specifically made for you while projecting. 
- **Slide Overview View:** Press `Esc` or `O` on your keyboard to instantly zoom out and see every slide at once. 
