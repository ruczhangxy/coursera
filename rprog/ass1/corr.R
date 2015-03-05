corr <- function(directory, threshold = 0) {
	corr_vec <- vector()
	for (fname in list.files(directory)) {
		fname <- paste(directory, '/', fname, sep='')
		data <- read.csv(fname, header=TRUE)
		data <- data[complete.cases(data),]
		if (nrow(data) > threshold) {
			tmp <- cor(data$sulfate, data$nitrate)
			corr_vec <- c(corr_vec,tmp)
		}
	}
	corr_vec
}
