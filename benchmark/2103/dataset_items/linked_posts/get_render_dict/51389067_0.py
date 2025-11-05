@pytest.fixture
def compare_test_vs_actual():
    def a_function(test, actual):
        print(test, actual)
    return a_function
