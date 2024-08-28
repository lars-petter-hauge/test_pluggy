import pluggy


hookimpl = pluggy.HookimplMarker("main_pkg")
"""Marker to be imported and used in plugins (and for own implementations)"""
