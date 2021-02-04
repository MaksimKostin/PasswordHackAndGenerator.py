import random

def generate_good_password(length):
  # 1.задать алфавит
  alphabet ='abcdefghijklmnopqrstuvwxyz'\
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
            '0123456789{}:;/?.'
  # 2.выбрать случайный символ из алфавита
  # 3.повторить length раз
  # 4. Склеить символы в строку
  password = ''
  for i in range(length):
    password += random.choice(alphabet)

  return password

print(generate_good_password(10))
print(generate_good_password(10))
print(generate_good_password(10))
