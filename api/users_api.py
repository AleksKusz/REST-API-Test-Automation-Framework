class UsersApi:
    def __init__(self, base_url, api_session, timeout=10):
        self.base_url = base_url
        self.api_session = api_session
        self.timeout = timeout

    def get_user(self, user_id):
        return self.api_session.get(
            f"{self.base_url}users/{user_id}", timeout=self.timeout
        )

    def get_users(self, params=None):
        return self.api_session.get(
            f"{self.base_url}users/", params=params, timeout=self.timeout
        )  # also able to filter out

    def post_user(self, user_data):
        return self.api_session.post(
            f"{self.base_url}users", json=user_data, timeout=self.timeout
        )
    
    def put_user(self, user_id, user_data):
        return self.api_session.put(
            f"{self.base_url}users/{user_id}",
            json=user_data,
            timeout=self.timeout,
        )
      
    def delete_user(self, user_id):
        return self.api_session.delete(
            f"{self.base_url}users/{user_id}", timeout=self.timeout
        )