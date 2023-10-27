package data

// this file will handle database connections
import (
	"database/sql"
	_ "github.com/lib/pq"
)

const (
	host 		= "localhost"
	port 		= 5432
	user 		= "postgres"
	password 	= "1lP(=F=<HHwD]v"
	dbname		= "hpaintTest"
)

var DB *sql.DB

func InitConn() {
	psqlconn := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlconn)
	utils.CheckErr(err)

	defer db.Close()

	err = db.Ping()
	utils.CheckErr(err)

	fmt.Println("\tDatabase connection successful!\r\n\n")

}


func AddTable(db *sql.DB, tableName, sqlStatement string) error {

	_, err := db.Exec(sqlStatement)
	if err != nil {
		return err
	}
	fmt.Printf("\t*    Table '%s' created successfully\r\n", tableName)
	return err
}



