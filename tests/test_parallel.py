import time

# pip install pytest-xdist
# then
# pytest tests\test_parallel.py -s -v -n8
# or
# pytest tests\test_parallel.py -s -v -nauto


def test_parallel_1():
    time.sleep(5)
    print("Result 1 has completed!")


def test_parallel_2():
    time.sleep(5)
    print("Result 2 has completed!")


def test_parallel_3():
    time.sleep(5)
    print("Result 3 has completed!")


def test_parallel_4():
    time.sleep(5)
    print("Result 4 has completed!")


def test_parallel_5():
    time.sleep(5)
    print("Result 5 has completed!")


def test_parallel_6():
    time.sleep(5)
    print("Result 6 has completed!")


def test_parallel_7():
    time.sleep(5)
    print("Result 7 has completed!")


def test_parallel_8():
    time.sleep(5)
    print("Result 8 has completed!")


