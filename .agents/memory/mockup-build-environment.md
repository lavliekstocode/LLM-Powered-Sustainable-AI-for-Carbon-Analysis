---
name: Mockup build environment
description: Environment variables required when validating the mockup sandbox production build
---

The mockup sandbox Vite configuration requires both `PORT` and `BASE_PATH` during production builds; the preview workflow supplies these at runtime.

**Why:** A plain `npm run build` fails before compilation when either variable is absent, which can look like a repository or dependency problem.

**How to apply:** Use `PORT=<preview-port> BASE_PATH=/__mockup/ npm run build` from the mockup sandbox directory when validating the tracked artifact.