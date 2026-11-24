# shop (sample repo)

A tiny made-up project that JARVIS's tools can read, test and branch without touching
real work. `scripts/make_sample_repo.py` copies it to `data/sandbox/shop` and turns the
copy into a Git repository.

- `services/cart`: a shopping cart. One test fails on purpose (see ticket 3).
- `services/checkout`: order totals. All tests pass.
