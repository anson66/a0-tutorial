import os

def get_all_test_names():
    # get all test names from test_cases folder
    test_names = []
    for root, dirs, files in os.walk("test_cases"):
        for file in files:
            if file.endswith(".test"):
                test_names.append(os.path.join(root, file[:-5]))
    return test_names

def pytest_generate_tests(metafunc):
    if "testname" in metafunc.fixturenames:
        test_names = get_all_test_names()
        metafunc.parametrize("testname", test_names)

if __name__ == "__main__":
    print(get_all_test_names())