package admin

import (
    "net/http"
    "context"
    "github.com/go-chi/chi/v5"
)

type appError struct {
    Err error
    Message string
    Code int
}

type authHandler func(w http.ResponseWriter, r *http.Request, c context.Context) *appError 

func (ah authHandler) serveHTTP(w http.ResponseWriter, r *http.Request) {
    // setup auth here
    uid := 1 // example id
    userIDKey := "dfajkelkajflkdjalkf" // example key

    // setup context
    parent := context.TODO()
    ctx := context.WithValue(parent, userIDKey, uid)
    if err := ah(w, r, ctx); err != nil { // err is *appError, not os.Error
        http.Error(w, err.Message, err.Code)
    }
}

type AdministrativePermssion struct {}

func (ap *AdministrativePermssion) IsAdmin() bool {return true}

func AdminOnly(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        ctx := r.Context()
        perm, ok := ctx.Value("acl.permission").(AdministrativePermssion)
        if !ok || !perm.IsAdmin() {
            http.Error(w, http.StatusText(403), 403)
            return
        }
        next.ServeHTTP(w, r)
    })
} 

func AdminRoutesConfig() http.Handler {
    r := chi.NewRouter()


}
