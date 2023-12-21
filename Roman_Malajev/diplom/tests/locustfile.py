from locust import HttpUser, task


class User(HttpUser):
    @task
    def mainPage(self):
        self.client.get('/')

    @task
    def postMethod(self):
        self.client.post('/?act=connect_authorize', json={
        'username': 'romanmalajev@gmail.com',
        'password': 'VK59724150987'
        })