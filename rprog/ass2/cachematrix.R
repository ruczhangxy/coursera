## Put comments here that give an overall description of what your
## functions do

## Write a short comment describing this function

# This function construct a special object that supports various operations
# related to getting and computing the inverse.
makeCacheMatrix <- function(x = matrix()) {
	inv <- NULL

	# Define utility functions of the special object.
	set <- function(y) {
		x <<- y
		inv <<- NULL
	}
	get <- function() x
	setInverse <- function(inv) inv <<- inv
	getInverse <- function() inv

	# Encapsulate utility functions to form the special object.
	list(set=set, get=get, setInverse=setInverse, getInverse=getInverse)
}


## Write a short comment describing this function

# This function takes a special matrix object and 
# return the inverse of the matrix.
# If the inverse of the matrix has already been computed,
# the value is returned. Else the inverse is computed
# and returned, while at the same time cached for future use.

cacheSolve <- function(x, ...) {
	## Return a matrix that is the inverse of 'x'

	# First check if the inverse has been already been computed.
	# If so, return the computed inverse.
	inv <- x$getInverse()
	if (!is.null(inv)) {
		message('getting cache data')
		return(inv)
	}

	# If the inverse has not been computed, get data and compute it.
	data <- x$get()
	inv <- solve(x)
	# Then save the computed inverse.
	x$setInverse(inv)

	return(inv)
}
