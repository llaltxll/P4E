class PartyAnimal:
	x = 0
	name = ''
	def __init__(self, nam=''):
		self.name = nam
		print(self.name,"constructed")

	def party(self):
		self.x = self.x +1
		print(self.name,"Party count", self.x)


	def __del__(self):
		print(self.name,"destructed", self.x)

# only run example code if this is the main func, peventing the examples from runing when we import the class above to another program
if __name__ == "__main__":
	# an = PartyAnimal()
	# an.party()
	# an.party()
	# an.party()
	# # Same thing different syntax
	# PartyAnimal.party(an)

	# an = 42
	# print('an contains', an)

	s = PartyAnimal('Sally')
	j = PartyAnimal('Jim')

	s.party()
	j.party()
	s.party()
	j.party()

	# print("Type", type(an))
	# print("Dir ", dir(an))
	# print("Type", type(an.x))
	# print("Dir ", type(an.party))


	# print("Type", type(PartyAnimal))
	# print("Dir ", dir(PartyAnimal))