import re


class ValidationError(Exception):

  def __init__(self, errors):
    self.errors = errors
    super().__init__(self.errors)


def validate_user(data: dict):
  errors = []

  name = data.get("name")
  age = data.get("age")
  email = data.get("email")

  if not isinstance(name, str) or not name.strip():
    errors.append("tên không được trống, phải là chuỗi hợp lệ")

  if not isinstance(age, int) or isinstance(age, bool) or not (1 <= age <= 120):
    errors.append("tuổi là số nguyên từ 1 đến 120")

  email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
  if not isinstance(email, str) or not re.match(email_regex, email):
    errors.append("email không đúng")

  if errors:
    raise ValidationError(errors)

  return True


try:
  validate_user({"name": "Kim Ngân", "age": 19, "email": "emngancute@gmail.com"})
  assert True
except ValidationError:
  assert False

try:
  validate_user({"name": "", "age": 19, "email": "emngancute@gmail.com"})
  assert False
except ValidationError as e:
  assert "tên không được trống, phải là chuỗi hợp lệ." in e.errors

try:
  validate_user({"name": "Kim Ngân", "age": 0, "email": "emngancute@gmail.com"})
  assert False
except ValidationError as e:
  assert "tuổi là số nguyên từ 1 đến 120." in e.errors

try:
  validate_user(
      {"name": "Kim Ngân", "age": 999, "email": "emngancute@gmail.com"}
  )
  assert False
except ValidationError as e:
  assert "tuổi là số nguyên từ 1 đến 120." in e.errors

try:
  validate_user(
      {"name": "Kim Ngân", "age": "19", "email": "emngancute@gmail.com"}
  )
  assert False
except ValidationError as e:
  assert "tuổi là số nguyên từ 1 đến 120." in e.errors

try:
  validate_user(
      {"name": "Kim Ngân", "age": 19, "email": "emngancutegmail.com"}
  )
  assert False
except ValidationError as e:
  assert "email không đúng" in e.errors

try:
  validate_user({"name": "   ", "age": 369, "email": "mail"})
  assert False
except ValidationError as e:
  assert len(e.errors) == 3

try:
  validate_user({})
  assert False
except ValidationError as e:
  assert len(e.errors) == 3