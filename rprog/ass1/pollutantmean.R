library(stringr)
pollutantmean <- function(directory, pollutant, id_vec=1:332) {
	total_data <- data.frame()
	for (id in id_vec) {
		fname <- paste(directory, '/', str_pad(id, 3, pad='0'), '.csv', sep='')
		tmp_data <- read.csv(fname)
		total_data <- rbind(total_data, tmp_data)
	}
	mean(total_data[[pollutant]], na.rm=TRUE)
}
