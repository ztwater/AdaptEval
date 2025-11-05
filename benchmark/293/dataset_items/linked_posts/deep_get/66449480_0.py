from deepextract import deepextract
# Demo: deepextract.extract_key(obj, key)
deeply_nested_dict = {
    "items": {
        "item": {
            "id": {
                "type": {
                    "donut": {
                        "name": {
                            "batters": {
                                "my_target_key": "my_target_value"
                            }
                        }
                    }
                }
            }
        }
    }
}
print(deepextract.extract_key(deeply_nested_dict, "my_target_key") == "my_target_value")
