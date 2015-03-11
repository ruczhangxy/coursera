rankhospital <- function(state, outcome, num='best') {
	if (num == 'best') {
		num <- 1
	} else if (num == 'worst') {
		num <- -1
	}

	outcome_index <- 0
	if (outcome == 'heart attack') {
		outcome_index <- 11
	} else if (outcome == 'heart failure') {
		outcome_index <- 17
	} else if (outcome == 'pneumonia') {
		outcome_index <- 23
	} else {
		stop('invalid outcome')
	}

	fname <- 'outcome-of-care-measures.csv'
	data <- read.csv(fname, header=TRUE, na.strings='Not Available', stringsAsFactors=FALSE)
	state_data <- data[data$State==state&!is.na(data[,outcome_index]),c(2, outcome_index)]
	if (nrow(state_data) == 0) {
		stop('invalid state')
	}
	state_data <- state_data[order(state_data[,2], state_data[,1]),]
	if (num > nrow(state_data)) {
		return(NA)
	}
	if (num == -1) {
		num <- nrow(state_data)
	}
	return(state_data[num,1])
}
