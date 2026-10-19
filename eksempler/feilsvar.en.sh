# Without a key: 401 with a link to the registration page
curl -s -w "\nHTTP %{http_code}\n" "https://api.nasjonalmuseet.no/api/v1/objects/NG.M.00939"
