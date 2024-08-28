import main_pkg


@main_pkg.hookimpl
def test_func(parameters):
    print("inside pluggy_pkg")
    return parameters.reverse()
