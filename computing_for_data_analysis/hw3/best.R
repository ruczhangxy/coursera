best <- function(state, outcome) {
	# Read in data.
	data <- read.csv('outcome-of-care-measures.csv', header=TRUE)
	outcome_set <- c('heart attack', 'heart failure', 'pneumonia')
	hosp_name_var <- 'Hospital.Name'

	# Params check.
	if (!(outcome %in% outcome_set)) {
		stop('invalid outcome')
	}
	if (!(state %in% data[,c('State')])) {
		stop('invalid state')
	}

	index_map <- c(11, 17, 23)
	measure_index <- index_map[match(outcome, outcome_set)]

	data <- data[data['State'] == state & data[measure_index] != 'Not Available',]

	min_value <- min(as.numeric(as.character(data[,measure_index])), na.rm=TRUE)
	candidates <- data[as.numeric(as.character(data[,measure_index])) == min_value, 'Hospital.Name']

	return(min(as.character(candidates), na.rm=TRUE))
}
