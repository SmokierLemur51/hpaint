package main

import (
	"log"
	"net/http"

	"github.com/SmokierLemur51/hpaint/routes"

	"github.com/go-chi/chi/v5"
    "github.com/go-chi/chi/v5/middleware"
)

type ServerConfig struct {
	PORT string
}

func main() {
	var config ServerConfig = ServerConfig{PORT: ":5000"}
	r := chi.NewRouter()
    r.Use(middleware.RequestID)
    r.Use(middleware.RealIP)
    r.Use(middleware.Logger)
    r.Use(middleware.Recoverer)
    
    r.Handle("/static/*", http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))

	routes.ConfigureRoutes(r)

	log.Println("Starting server on port ", config.PORT)
	http.ListenAndServe(config.PORT, r)
}
