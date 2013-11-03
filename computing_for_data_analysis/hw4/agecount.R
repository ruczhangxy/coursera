agecount <- function(age=NULL) {
#	if (age == NULL) {
#		stop('invalid age')
#	}

	data <- readLines('homicides.txt')
	num <- 0
	for (line in data) {
		line <- tolower(line)
		current_age <- sub('.* (\\d+) years old.*', '\\1', line, perl=TRUE)
		if (line == current_age) {
			#print(current_age)
			next
		}
		if (as.numeric(current_age) == age) {
			num <- num + 1
		}
	}

	return(num)
}
