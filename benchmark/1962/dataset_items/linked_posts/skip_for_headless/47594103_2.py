class Machine():
   def __init__(self, state):
      self.state = state

@pytest.fixture
def myfixture(request):
   return Machine("running")

@pytest.mark.skipif_call('myfixture.state != "running"')
def test_my_fixture_running_success(myfixture):
   print(myfixture.state)
   myfixture.state = "stopped"
   assert True

@pytest.mark.skipif_call('myfixture.state != "running"')
def test_my_fixture_running_fail(myfixture):
   print(myfixture.state)
   assert False

@pytest.mark.skipif_call('myfixture.state != "stopped"')
def test_my_fixture_stopped_success(myfixture):
   print(myfixture.state)
   myfixture.state = "running"

@pytest.mark.skipif_call('myfixture.state != "stopped"')
def test_my_fixture_stopped_fail(myfixture):
   print(myfixture.state)
   assert False
