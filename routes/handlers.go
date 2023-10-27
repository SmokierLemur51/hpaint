package routes

import (
	"encoding/json"
	"fmt"
	"html/template"
	"net/http"
    
	// "github.com/SmokierLemur51/hpaint/data"
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
}

// declarations
var ENDPOINTS = PublicEndpoints{Index: "/", About: "/about", Services: "/services"}

var STATIC_URL string = "/static/css/testing.css"

func RenderTemplate(w http.ResponseWriter, data PublicPageData) error {
    tmpl, err := template.ParseFiles("templates/" + data.Page)
    if err != nil {
        return err
    }
    err = tmpl.Execute(w, data)
    if err != nil {
        return err
    }
    return nil
}

// yet to be created 
func RenderTemplateFromBase(w http.ResponseWriter, r *http.Request, data PublicPageData) error {return nil}

func CheckErr(err error) {
    if err != nil {
        panic(err)
    }
}

func IndexHandler(w http.ResponseWriter, r *http.Request) error {
    page := PublicPageData{
        Page: "index.html",
        Title: "Higginbotham Paint",
        Content: "Sample Content",
        Endpoints: ENDPOINTS,
        StaticURL: STATIC_URL,
    }
    // this prevents the superflous hanlder err 
    w.Header().Set("Content-Type", "text/html; charset=utf-8")

    err := RenderTemplate(w, page)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return err
    }
    return nil
}


func ServicesHandler(w http.ResponseWriter, r *http.Request) error {
    page := PublicPageData{
        Page: "services.html",
        Title: "Higginbotham Paint",
        Content: "Sample Content",
        Endpoints: ENDPOINTS,
        StaticURL: STATIC_URL,
    }

    w.Header().Set("Content-Type", "text/html; charset=utf-8")

    err := RenderTemplate(w, page)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return err
    }
    return nil
}

func AboutHandler(w http.ResponseWriter, r *http.Request) error {
    page := PublicPageData{
        Page: "about.html",
        Title: "Higginbotham Paint",
        Content: "Sample Content",
        Endpoints: ENDPOINTS,
        StaticURL: STATIC_URL,
    }
    
    w.Header().Set("Content-Type", "text/html; charset=utf-8")
    
    err := RenderTemplate(w, page)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return err
    }
    return nil
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * form processing * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
type FormData struct {
    Phone string `json:"telephone"`
    Email string `json:"email"`
    Description string `json:"description"`
}

func RequestEstimateHandler(w http.ResponseWriter, r *http.Request) error {
    var data FormData
    decoder := json.NewDecoder(r.Body)
    if err := decoder.Decode(&data); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return err
    }
    // pasrse form
    fmt.Printf("\nPhone: %s\tEmail: %s\nDescription: %s\n\n", data.Phone, data.Email, data.Description)
    
    responseData := "Request recieved successfully"

    jsonResponse, err := json.Marshal(responseData)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return err
    }
    // set response header
    w.Header().Set("Content-Type", "application/json")
    // write json response <3 to response writer
    w.WriteHeader(http.StatusOK)
    w.Write(jsonResponse)
    
    return nil
}


// func ProcessLogin(w http.ResponseWriter, r *http.Request) error {
//     var login data.LoginForm 
//     decoder := json.NewDecoder(r.Body)
//     if err := decoder.Decode(&login); err != nil {
//         http.Error(w, err.Error(), http.StatusBadRequest)
//         return err
//     }

//     // if login.Username != 
// }