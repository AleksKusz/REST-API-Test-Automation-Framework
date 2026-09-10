class usersapi:
    def __init__(self, base_url, api_session):
        self.base_url = base_url
        self.api_session = api_session

    def get_user(self, user_id):
        return self.api_session.get(f"{self.base_url}/users/{user_id}")

    def post_user(self, user_data):
        return self.api_session.post(f"{self.base_url}/users", json=user_data)
    
    def put_user(self, user_id, user_data):
        return self.api_session.put(f"{self.base_url}/users/{user_id}", json=user_data)
      
    def delete_user(self, user_id):
        return self.api_session.delete(f"{self.base_url}/users/{user_id}")