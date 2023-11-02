package routes

import (
    "net/http"
    "github.com/go-chi/chi/v5"
) 

type Handler func(w http.ResponseWriter, r *http.Request) error

func (h Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    if err := h(w, r); err != nil {
        // handle returned err here
        w.WriteHeader(503)
        w.Write([]byte("Bad"))
    }
}

// note for later
// router.Method("GET", "/", Handler(IndexHandler))
//    >> you can use this to define multiple methods for the same endpoint
// router.Get("/", IndexHandler)
//     >> specific method only (its GET if you couldnt tell)
// 


func ConfigureRoutes(router *chi.Mux) {
    router.Method(http.MethodGet, "/", Handler(IndexHandler))
    router.Method(http.MethodGet, "/about", Handler(AboutHandler))
    router.Method(http.MethodGet, "/services", Handler(ServicesHandler))

    // post routes
    router.Method(http.MethodPost, "/request-estimate", Handler(RequestEstimateHandler))

    // router.Method(http.MethodPost, "/process-login", Handler(ProcessLogin))


    // https://go-chi.io/#/pages/routing
}



