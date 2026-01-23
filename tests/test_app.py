from biocomp.app import biocomp_version


def test_biocomp_version():
    result = biocomp_version()
    assert result["version"] == "26.1"
