best <- function(state, outcome) {
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
	state_data <- state_data[order(state_data[,1]),]
	hospital_name <- state_data[which.min(state_data[,2]),'Hospital.Name']
	return(hospital_name)
}
