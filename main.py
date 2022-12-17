from factory import MyPostgresFactory

useCase = MyPostgresFactory.create()

response = useCase.do_something(True)


print(response)