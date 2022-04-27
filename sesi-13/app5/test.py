import unittest
from app import connex_app 


class TestAPI(unittest.TestCase):

    def test_all_directors(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/directors")
        self.assertEqual(response.status_code, 200)
        # get all data director

    def test_all_movies(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/movies")
        self.assertEqual(response.status_code, 200)
        # get all data movie

    def test_best_movie(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/best_movies")
        self.assertEqual(response.status_code, 200)
        # vote_average

          


if __name__ == '__main__':
    unittest.main()