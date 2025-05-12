class Course:
    def __init__(self, course_id, title, description, price, teacher_id, students):
        self.id = course_id
        self.title = title
        self.description = description
        self.price = price
        self.teacher_id = teacher_id
        self.students = students

    @classmethod
    def from_dict(cls, data):
        return cls(
            course_id=data['id'],
            title=data['title'],
            description=data['description'],
            price=data['price'],
            teacher_id=data['teacher_id'],
            students=data.get('students', [])
        )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'teacher_id': self.teacher_id,
            'students': self.students
        }
