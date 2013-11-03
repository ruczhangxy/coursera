rankhospital <- function(state, outcome, num='best') {
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
	# Return hospital name in that state with the given rank 30-day death rate
	if (num == 'best') {
		num = 1
	} else if(num == 'worst') {
		num = nrow(data)
	}

	if (num > nrow(data)) {
		return(NA)
	}
	
	order_v <- order(as.numeric(as.character(data[,measure_index])), data['Hospital.Name'])
	data <- data[order_v,]
	return(as.character(data[num,'Hospital.Name']))
}
