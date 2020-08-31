from profanity_check import predict


def contains_offensive_word(string_array):
	"""
	:param string_array:
	:return boolean:
	"""
	# predict() takes an array and returns a 1 for each string if it is offensive, else 0.
	checker = predict(string_array)
	if max(checker) > 0:
		return True
	return False
