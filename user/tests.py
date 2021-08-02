import pytest

from user.models import User

# import pytest_django


# user = User.objects.create(
#     about_us="more than 300 characters so it s impossible to save him normaly because it's record like that and that's all"
# )


# @pytest.fixture
# def user_about_us():
#     return User.objects.create(
#         first_name="Yoan",
#         last_name="Fornari",
#         about_us="more than 300 characters so it s impossible to save him normaly because it's record like that and that's all",
#     )


# @pytest.mark.django_db
# def test_limit_char_of_about_us_field():
#     """Test than the about us section can't do more than 300 char"""
#     user = User(
#         about_us="more than 300 characters so it s impossible to save him normaly because it's record like that and that's all hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
#     )
#     print("error ===> ", user.save())
# assert user.save()
# response = user.save()
# print("response => ", response)
# print("user => ", user)
# assert 1 + 1 == 2
# assert user.save()
