from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(0.1, 2)

    @task(1)
    def generate_weather(self):
        self.client.get("/generate", name="/generate")
