from importlib.metadata import distributions
from pluggy import HookimplMarker, PluginManager, HookImpl, HookspecMarker


hookspec = HookspecMarker("main_pkg")
hookimpl = HookimplMarker("main_pkg")


class PluginClass:
    """add_hookspecs takes either a module or class. We put The
    specification within a class this time as to avoid another file"""

    @hookspec
    def test_func(self, parameters: list):
        """The hook specification names a function that others can create
        an implementation of. Several implementations of this test_func can
        be added to the plugin manager.
        """


class Plugin_1:
    """A hook implementation namespace."""

    @hookimpl
    def test_func(self, parameters: list):
        # If this function is second in line then the parameters are already
        # modified from the first function
        print("inside Plugin_1")
        return parameters


def main():
    pm = PluginManager("main_pkg")
    pm.add_hookspecs(PluginClass)
    pm.register(Plugin_1())

    # The following is done inside the load entrypoints function
    # import importlib.metadata
    # dists = list(importlib.metadata.distributions())
    # entry_points = [
    #     ep for dist in dists for ep in dist.entry_points if ep.group == "main_pkg"
    # ]
    # for ep in entry_points:
    #   plugin = ep.load()
    #   pm.register(plugin)

    pm.load_setuptools_entrypoints("main_pkg")
    result = pm.hook.test_func(parameters=[1, 2, 3])
    # The result is a list, but it only contains a single variable regardless
    # of how many hook implementations there are.. Looks like the functions
    # are chained together, output of one is input to the next.
    print(result)


if __name__ == "__main__":
    main()
