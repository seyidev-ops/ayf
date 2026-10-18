# October 18, 2026: GitHub Pages project-path repair

The initial pages referenced root-relative `/assets/*` and `/programs/*` links. These do not resolve on the GitHub project URL `https://seyidev-ops.github.io/ayf/` because that website is under `/ayf/`, resulting in a bare unstyled document. All internal file references are now relative to the current page directory. This works from both the project URL and the custom apex domain `https://adamuyolafoundation.org/`.

Changed only href/src/action/poster local paths and restored missing binary asset files. Do not switch local file references back to absolute `/` paths. Canonical SEO URLs intentionally remain on the custom foundation domain.