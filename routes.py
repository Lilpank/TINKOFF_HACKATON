class Routes():
    def __init__(self, base_path, session_id, bot_url, bot_id) -> None:
        self.base_path = base_path
        self.session_id = session_id
        self.bot_url = bot_url
        self.bot_id = bot_id

    def registration(self) -> str:
        return f"http:/{self.base_path}/sessions/{self.session_id}/registration"
    