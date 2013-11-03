source('complete.R')

corr <- function(directory, threshold = 0) {
	## 'directory' is a character vector of length 1 indicating
	## the location of the CSV files

	## 'threshold' is a numeric vector of length 1 indicating the
	## number of completely observed observations (on all
	## variables) required to compute the correlation between
	## nitrate and sulfate; the default is 0

	## Return a numeric vector of correlations
	id <- 1:332
	id_strs <- sprintf("%03d",id)
	fnames <- paste(directory, '/', id_strs, '.csv', sep='')
	nobs <- count_cases(fnames)
	good_fnames <- fnames[nobs > threshold]
	cors <- vector()
	for (fname in good_fnames) {
		data <- read.csv(fname, header=TRUE)
		cors <- c(cors, cor(data$sulfate, data$nitrate, use="complete.obs"))
	}
	return(cors)
}
