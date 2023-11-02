package routes

import (
    "net/http"
    "html/template"
    "log"
)

type PublicEndpoints struct {
    Index string
    About string
    Services string
}

type PublicPageData struct {
    Page string
    Title string
    Content string
    Endpoints PublicEndpoints
    StaticURL string
    EstimateJS string
    CompanyName string
}

func (p PublicPageData) RenderHTML(w http.ResponseWriter, r *http.Request) {
    tmpl, err := template.ParseFiles("templates/" + p.Page)
    if err != nil {
        log.Println("Err: ", err)
        return
    }
    err = tmpl.Execute(w, p)
    if err != nil {
        log.Println("Err: ", err)
        return
    }
    w.Header().Set("Content-Type", "text/html; charset=utf-8")
}    

// declarations
var ENDPOINTS = PublicEndpoints{Index: "/", About: "/about", Services: "/services"}

var STATIC_URL string = "/static/css/testing.css"
