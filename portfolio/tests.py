import pytest
import pytest_django

from portfolio import views


class PortfolioTest:
    def test_knows_my_skills():
        pass

    def test_about_me():
        pass

    def test_all_my_project():
        pass

    def test_look_details_project():
        pass

    def test_go_on_my_project():
        pass


def test_skills():
    pass


def test_projects():
    # assert type(Project.title) == str
    # assert type(Project.description) == str
    # assert Project.technology is str
    # assert Project.image is str
    # assert Project.realization_date is date
    pass


# @pytest.mark.urls("portfolio.test_urls")
def test_context_of_home_page_exist(rf):
    request = rf.get("/")
    response = views.home_page(request)
    print("RESPONSE ====> ", response)
    assert response.status_code == 200
