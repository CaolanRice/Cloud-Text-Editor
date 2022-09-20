package main

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"
)

func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}

func handler(w http.ResponseWriter, r *http.Request) {
	enableCors(&w)

	keys, ok := r.URL.Query()["text"]

	if !ok || len(keys[0]) < 1 {

		jsonResponse := Response{
			Count:  0,
			Status: 400,
			String: "Url Param 'text' is missing",
		}

		json.NewEncoder(w).Encode(jsonResponse)
		return
	}

	// Query()["key"] will return an array of items,
	// we only want the single item.
	key := keys[0]

	count := commaCount(key)

	jsonResponse := Response{
		Count:  count,
		Status: 200,
		String: "Contains " + strconv.Itoa(count) + " commas",
	}

	json.NewEncoder(w).Encode(jsonResponse)

}

type Response struct {
	Status int
	Count  int
	String string
}

func commaCount(text string) int {
	return strings.Count(text, ",")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":5002", nil)
}
