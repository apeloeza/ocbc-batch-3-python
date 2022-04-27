import unittest
from app import connex_app 


class TestAPI(unittest.TestCase):

    def test_all_directors(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/directors")
        self.assertEqual(response.status_code, 200)

    def test_all_movies(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/movies")
        self.assertEqual(response.status_code, 200)

    def test_best_movie(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/best_movies")
        self.assertEqual(response.status_code, 200)

    def test_flop_movie(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/flop_movies")
        self.assertEqual(response.status_code, 200)

    def test_least_budget(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/budget/least")
        self.assertEqual(response.status_code, 200)
        
    def test_most_budget(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/budget/most")
        self.assertEqual(response.status_code, 200)
        

    def test_least_vote(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/vote/least")
        self.assertEqual(response.status_code, 200)
        
    def test_most_vote(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/vote/most")
        self.assertEqual(response.status_code, 200)
        

    def test_least_revenue(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/revenue/least")
        self.assertEqual(response.status_code, 200)
        
    def test_most_revenue(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/revenue/most")
        self.assertEqual(response.status_code, 200)
        

    def test_least_popular(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/popular/not")
        self.assertEqual(response.status_code, 200)
        
    def test_most_popular(self):
        connex_app.app.testing=True
        data = connex_app.app.test_client(self)
        response = data.get("/api/popular/most")
        self.assertEqual(response.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()