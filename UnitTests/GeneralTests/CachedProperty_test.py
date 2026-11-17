from otlmow_model.OtlmowModel.BaseClasses.CachedProperty import cached_property


def test_cached_property():
    class Foo:
        @cached_property
        def bar(self):
            return 42

    f = Foo()
    assert f.bar == 42
    assert f.bar == 42
    assert f.__dict__['bar'] == 42
    assert Foo.bar.__get__(None, Foo) is Foo.bar
