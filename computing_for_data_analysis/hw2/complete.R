count_cases <- function(fnames) {
	nobs <- vector()
	for (fname in fnames) {
		data <- read.csv(fname, header=TRUE)
		n <- length(which(complete.cases(data)))
		nobs <- c(nobs, n)
	}
	return(nobs)
}
complete <- function(directory, id = 1:332) {
	## 'directory' is a character vector of length 1 indicating
	## the location of the CSV files

	## 'id' is an integer vector indicating the monitor ID numbers
	## to be used
	
	## Return a data frame of the form:
	## id nobs
	## 1  117
	## 2  1041
	## ...
	## where 'id' is the monitor ID number and 'nobs' is the
	## number of complete cases
	id_strs <- sprintf("%03d",id)
	fnames <- paste(directory, '/', id_strs, '.csv', sep='')
	nobs <- count_cases(fnames)
	return(data.frame(cbind(id, nobs)))
}
