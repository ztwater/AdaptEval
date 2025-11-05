@pytest.fixture(params=[(None, 'myStr', 'UPDATED'),
                        ('level1', 'myInt', 'UPDATED'),
                        ('level2', 'myBool', 'UPDATED'),
                        ('level3', 'myList', 'UPDATED'),
                        ('level4', 'myInt', 'UPDATED'),
                        ('level5', 'myBool', 'UPDATED')])
def sample_data(request):
    return request.param
