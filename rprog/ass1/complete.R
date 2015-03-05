complete <- function(directory, id_vec = 1:332) {
	total_data <- data.frame()
	for (id in id_vec) {
		fname <- paste(directory, '/', str_pad(id, 3, pad='0'), '.csv', sep='')
		tmp_data <- read.csv(fname)
		row <- c(id, sum(complete.cases(tmp_data)))
		total_data <- rbind(total_data, row)
	}
	colnames(total_data) <- c('id', 'nobs')
	total_data
}
