package routes

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func CheckErr(err error) {
	if err != nil {
		panic(err)
	}
}

func IndexHandler(w http.ResponseWriter, r *http.Request) error {
	page := PublicPageData{
		Page:        "index.html",
		Title:       "Higginbotham Paint",
		Content:     "Sample Content",
		Endpoints:   ENDPOINTS,
		StaticURL:   STATIC_URL,
		CompanyName: "Higginbotham Paint",
		EstimateJS:  "/static/js/requestEstimate.js",
	}
	page.RenderHTML(w, r)

	return nil
}

func ServicesHandler(w http.ResponseWriter, r *http.Request) error {
	page := PublicPageData{
		Page:      "services.html",
		Title:     "Higginbotham Paint",
		Content:   "Sample Content",
		Endpoints: ENDPOINTS,
		StaticURL: STATIC_URL,
	}
	page.RenderHTML(w, r)

	return nil
}

func AboutHandler(w http.ResponseWriter, r *http.Request) error {
	page := PublicPageData{
		Page:      "about.html",
		Title:     "Higginbotham Paint",
		Content:   "Sample Content",
		Endpoints: ENDPOINTS,
		StaticURL: STATIC_URL,
	}
	page.RenderHTML(w, r)

	return nil
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * form processing * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
type FormData struct {
	Name        string `json:"name"`
	Phone       string `json:"telephone"`
	Email       string `json:"email"`
	Description string `json:"description"`
}

func RequestEstimateHandler(w http.ResponseWriter, r *http.Request) error {
	var data FormData
	decoder := json.NewDecoder(r.Body)
	if err := decoder.Decode(&data); err != nil {
		fmt.Println(err)
		http.Error(w, err.Error(), http.StatusBadRequest)
		return err
	}
	// pasrse form
	fmt.Printf("\nName: %s\tPhone: %s\tEmail: %s\nDescription: %s\n\n", data.Name, data.Phone, data.Email, data.Description)

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
