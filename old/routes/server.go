package routes

import (
  "fmt"
  
  "github.com/gin-gonic/gin"
  
  "gorm.io/gorm"
  "gorm.io/driver/sqlite"
)

type Server struct {
	Router *gin.Engine
	DB     *gorm.DB
  Portal *gin.RouterGroup
}

func (s *Server) ConfigureRouter() {
	s.Router = gin.Default()
	s.Router.LoadHTMLGlob("templates/**/*")
	s.Router.Static("/static", "./static")
}

func (s *Server) ConnectDatabase(databaseFile string) {
    var err error
    if s.DB, err = gorm.Open(sqlite.Open(fmt.Sprintf("instance/%s", databaseFile)), &gorm.Config{}); err != nil {
        panic(err)
    }
}

func (s Server) RegisterRoutes() {
	// handler functions can be found in public.go
	s.Router.GET("/", s.IndexHandler)
	s.Router.GET("/about", s.AboutHandler)

	// portal login
	s.Router.GET("/secret-portal", s.LoginHandler)
}


