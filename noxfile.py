import nox


@nox.session(python=["3.11", "3.12"])
def test(session):
    """
    nox -s test
    :param session: nox session
    :return:
    """
    session.install("poetry")
    session.run("poetry", "install")
    session.run("pytest")
