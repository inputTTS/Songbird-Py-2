# Songbird-Py
Songbird bindings for python

# Note
This repo is very WIP so do not try to use it.

Its public so I can share it easier.

# Contributing
Pyo3 asyncio is used with tokio.

## Dependencies
[Maturin](https://github.com/PyO3/maturin) should be installed though pip. This is used to build the Rust code to a python lib.
Run command `maturin develop` when changes are made to the Rust src.

[pyo3](https://github.com/PyO3/pyo3)

[pyo3 docs](https://pyo3.rs/v0.15.1/)

[pyo3 asyncio](https://github.com/awestlake87/pyo3-asyncio)

[pyo3 asyncio docs](https://docs.rs/pyo3-asyncio/0.13.4/pyo3_asyncio/) You can also look at the async secion of the pyo3 docs.

### Songbird
[Link](https://github.com/serenity-rs/songbird)

[docs](https://serenity-rs.github.io/songbird/current/songbird/index.html)

Its a good idea to install all the dependencies.

### Fixing pincer limitation (Hopefully temporary)
Go to pincer installed in venv

Add to `Dispatcher` class in `pincer/core/gateway.py)`
```python
async def send(self, payload):
  await self.__socket.send(payload)
```

## Goal of the project
Create API for songbird [driver](https://serenity-rs.github.io/songbird/current/songbird/driver/struct.Driver.html) and everything that is needed with it it.
