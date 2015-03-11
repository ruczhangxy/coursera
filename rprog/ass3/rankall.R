rankall <- function(outcome, num='best'){ 
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
	state_index <- 7
	hospital_name_index <- 2
	fname <- 'outcome-of-care-measures.csv'
	data <- read.csv(fname, header=TRUE, na.strings='Not Available', stringsAsFactors=FALSE)
	data <- data[!is.na(data[,outcome_index]), c(hospital_name_index, outcome_index, state_index)]
	all_rank <- sapply(split(data, data[,3]), best_in_state, num=num)
	all_rank <- cbind(all_rank, names(all_rank))
	colnames(all_rank) <- c('hospital', 'state')
	all_rank <- as.data.frame(all_rank)
	return(all_rank[order(all_rank$state),])
}

best_in_state <- function(state_data, num) {
	state_data <- state_data[order(state_data[,2]),]
	if (num > nrow(state_data)) {
		return(NA)
	}
	if (num == -1) {
		num <- nrow(state_data)
	}
	return(state_data[num,1])
}
