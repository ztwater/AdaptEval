dictionary1 = {
    "level1": {
        "level2": {"levelA": 0, "levelB": 1}
    }
}

dictionary1.update({
    "level1": {
        "level2": {
            **dictionary1["level1"]["level2"],
            "levelB": 10
        }
    }
})
