import SCOPP_tester;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()
def test_hello():
    expectedIO.print("Hello World")
    assert SCOPP_tester.test(testIO=testIO , expectedIO=expectedIO)
    # assert SCOPP_tester.test(arg1, agr 2, testIO=testIO , expectedIO=expectedIO) arg1 and arg2 will be passed to runner function
    print("Passed")
