[tool.pytest.ini_options]
pythonpath = ["test_helpers"]
testpaths = ["tests"]
addopts = [
    "--import-mode=importlib",
]
