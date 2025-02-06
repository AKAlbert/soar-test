from locust import HttpUser, task, between
from faker import Faker
import random

fake = Faker()

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        # Store some generated users for login testing
        self.test_users = []

    @task(2)
    def register_user(self):
        user_data = {
            'fullName': fake.name(),
            'userName': fake.user_name(),
            'email': fake.email(),
            'password': fake.password(),
            'phone': fake.phone_number()
        }
        # Store user for login testing
        self.test_users.append({
            'userName': user_data['userName'],
            'email': user_data['email'],
            'password': user_data['password']
        })
        
        response = self.client.post("/client_registeration", data=user_data)
        
    @task(3)
    def login_user(self):
        if not self.test_users:
            # If no test users available, use default admin
            login_data = {
                'userName': 'Admin',
                'email': 'admin@test.com',
                'password': 'admin@1234'
            }
        else:
            # Use random previously registered user
            login_data = random.choice(self.test_users)
            
        response = self.client.post("/client_login", data=login_data) 