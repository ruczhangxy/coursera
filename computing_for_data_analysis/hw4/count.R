count <- function(cause=NULL) {
	cause_v <- c('asphyxiation', 'blunt force', 'other', 'shooting', 'stabbing', 'unknown')
	cause <- tolower(cause)
	if (!(cause %in% cause_v)) {
		stop('invalid cause')
	}

	data <- readLines('homicides.txt')
	num <- 0
	for (line in data) {
		line <- tolower(line)
		current_cause <- sub('.*<dd>cause: (.+?)</dd>.*', '\\1', line, perl=TRUE)
		if (line == current_cause) {
			next
		}
		if (tolower(current_cause) == cause) {
			num <- num + 1
		}
	}

	return(num)
}
