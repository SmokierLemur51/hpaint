package data
// this file will define models for the project


// import ()

type Address struct {
    Id      int
    Street1 string
    Street2 string
    City    string
    State   string
    Zip     string
}

type ContactInfo struct {
    Id int
    Name string
    Phone string
    Email string
}

type QuoteRequest struct {
    Id      int
    Contact ContactInfo
    Address Address
    Description string
}


type QuoteAutoEmail struct {
    Id int
    QuoteRequest QuoteRequest
    Subject string
    Messge  string
}

func (q *QuoteAutoEmail) SendReceiveConfirmationEmail() error {
    // this sends the confirmation email saying we recieved but not that
    // we are saying yes or no to the bid
    return nil
}


type UserRole struct {
    Id int
    Role string
    Description string
    AccessLevel int
}

func (u *UserRole) CreateRole() error {return nil}


type User struct {
    Id int
    Username string
    // no password here
    Name string
    Role UserRole
}

func (u *User) CreateUser() error {return nil}

func (u *User) ChangePassword() error {return nil}

func (u *User) ChangeUserRole() error {return nil}

func (u *User) ListUsersByRole() error { return nil }


