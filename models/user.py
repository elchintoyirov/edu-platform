class User:
    def __init__(self, user_id, name, email, password, is_teacher):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.is_teacher = is_teacher

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data['id'],
            name=data['name'],
            email=data['email'],
            password=data['password'],
            is_teacher=data['is_teacher']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'is_teacher': self.is_teacher
        }
