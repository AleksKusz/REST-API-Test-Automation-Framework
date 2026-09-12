class PostApi:
    def __init__(self, base_url, api_session, timeout=10):
        self.base_url = base_url
        self.api_session = api_session
        self.timeout = timeout

    def get_post(self, post_id):
        return self.api_session.get(
            f"{self.base_url}posts/{post_id}", timeout=self.timeout
        )

    def get_posts(self, params=None):
        return self.api_session.get(
            f"{self.base_url}posts/", params=params, timeout=self.timeout
        )  # also able to filter out

    def post_post(self, post_data):
        return self.api_session.post(
            f"{self.base_url}posts", json=post_data, timeout=self.timeout
        )
    
    def put_post(self, post_id, post_data):
        return self.api_session.put(
            f"{self.base_url}posts/{post_id}",
            json=post_data,
            timeout=self.timeout,
        )
      
    def delete_post(self, post_id):
        return self.api_session.delete(
            f"{self.base_url}posts/{post_id}", timeout=self.timeout
        )