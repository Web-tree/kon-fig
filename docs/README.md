# Documentation source

The docs/ directory is the canonical website content. Start at [index](index.md). All content pages use YAML front matter and ordinary Markdown. navigation.json is the ordered sidebar manifest; paths are relative to docs/. A future site generator can consume it or translate it to its own sidebar format. Links to repository schemas and fixtures should be served as static assets or rewritten to immutable release URLs. Publish versioned snapshots when releases exist. No generator or deployment is configured yet.
