# h2
Doing science &amp; still alive

# Installation

```sh
# Create virtual env
$ virtualenv2 .env
$ . .env/bin/activate

# Install requirements
$ make init_linux

# Run the app
$ ./app.py
```

# Deploying Linux binary

```sh
# Build into ./build dir
make build_linux
```

# Cross-platform build for Windows using Wine

```sh
# Build into ./build dir
$ make init_wine
$ make build_wine
```

# Credits

Lonely me.
