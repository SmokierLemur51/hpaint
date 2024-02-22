package routes

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

var TITLE = "Hpaint"
var DevCompany = "LoganLee.space"

func IndexHandler(c *gin.Context) {
	c.HTML(http.StatusOK, "public/index.html", gin.H{
		"title":   TITLE,
		"devTeam": DevCompany,
	})
}

func AboutHandler(c *gin.Context) {
	c.HTML(http.StatusOK, "public/about.html", gin.H{
		"title":   TITLE,
		"devTeam": DevCompany,
	})
}

func LoginHandler(c *gin.Context) {
	c.HTML(http.StatusOK, "public/login.html", gin.H{
		"title":   TITLE,
		"devTeam": DevCompany,
	})
}
