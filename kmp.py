def sub_string(s):
	s_len = len(s)
	if s_len < 2:
		s_array = 0
	else:
		j = 0
		i = 1
		s_array = [0]*s_len
	while i < s_len:
		if j == 0 and s[j] != s[i]:
			s_array[i] = 0
			i = i+1
			print "if"
		elif s[i] == s[j]:
			s_array[i] = j+1
			i = i+1
			j = j+1
			print "elif"
		else:
			while j > 0 and s[i] != s[j]:
				j = s_array[j-1]
				print s_array
			#i = i+1
		        print "else"	
	print s_array

#def kpm(text, pattern):
	
sub_string('a')
