import SCOPP_tester;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()
def test_hello():
    expectedIO.print("Hello World")
    assert SCOPP_tester.test(testIO=testIO , expectedIO=expectedIO)
    print("Passed")