package main

import (
	"database/sql"
	"fmt"

	"github.com/SmokierLemur51/hpaint/routes"

	"github.com/gin-gonic/gin"
	_ "github.com/mattn/go-sqlite3"
)

type Server struct {
	Router *gin.Engine
	DB     *sql.DB
}

func (s *Server) configureRouter() {
	s.Router = gin.Default()
	s.Router.LoadHTMLGlob("templates/**/*")
	s.Router.Static("/static", "./static")
}

func (s *Server) connectDatabase(databaseFile string) {
	var err error
	s.DB, err = sql.Open("sqlite3", fmt.Sprintf("instance/%s", databaseFile))
	if err != nil {
		panic(err)
	}
}

func (s Server) registerRoutes() {
	// handler functions can be found in public.go
	s.Router.GET("/", routes.IndexHandler)
	s.Router.GET("/about", routes.AboutHandler)

	// portal login
	s.Router.GET("/secret-portal", routes.LoginHandler)
}

func main() {
	var s Server

	s.configureRouter()
	s.connectDatabase("test_1.db")
	s.registerRoutes()

	s.Router.Run(":5000") // defaults to port 8080
}
