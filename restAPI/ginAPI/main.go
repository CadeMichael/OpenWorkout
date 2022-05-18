package main

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	// example url of /max?reps=x&weight=y
	router.GET("/max", func(ctx *gin.Context) {
		reps, _ := strconv.Atoi(ctx.Query("reps"))
		weight, _ := strconv.Atoi(ctx.Query("weight"))
		orm := reps + weight
		ctx.String(http.StatusOK, "One rep max of %d", orm)
	})
	router.Run(":8080")
}
