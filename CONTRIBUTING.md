# Contributing

Thanks for improving Social Content Engine!

- Keep the core skill generic: no private company information, real users' writing samples, X tokens, session cookies, private data exports or auto-publishing features.
- Preserve the distinction between *X discussion signals*, *verified news*, and *author opinion*.
- Prefer tests that use synthetic fixtures and mock network calls. Never make CI depend on a live X account or X API key.
- Update both English and Chinese instructions when the workflow changes.
- Run `python3 -m unittest discover -s tests -v` before proposing changes.
- Discuss new API costs, authentication and recurring jobs before adding them; never silently activate tasks.

Issues and pull requests are welcome. Follow the repository's MIT License.
