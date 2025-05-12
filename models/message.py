class Message:
    def __init__(self, msg_id, from_id, from_name, to_id, to_name, content, timestamp):
        self.id = msg_id
        self.from_id = from_id
        self.from_name = from_name
        self.to_id = to_id
        self.to_name = to_name
        self.content = content
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, data):
        return cls(
            msg_id=data['id'],
            from_id=data['from_id'],
            from_name=data['from_name'],
            to_id=data['to_id'],
            to_name=data['to_name'],
            content=data['content'],
            timestamp=data['timestamp']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'from_id': self.from_id,
            'from_name': self.from_name,
            'to_id': self.to_id,
            'to_name': self.to_name,
            'content': self.content,
            'timestamp': self.timestamp
        }
