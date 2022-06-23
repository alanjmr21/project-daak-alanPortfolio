#!sh/bin

#test the 'GET' API
echo "This is the 'GET' API test"
curl http://192.168.1.73:5000/api/timeline_post

#test the 'POST' API
echo "This is the 'POST' API test"
echo "Enter a name: "
read NAME

echo "Enter an email: "
read MAIL

echo "Enter a message: "
read CONTENT

curl --request POST http://localhost:5000/api/timeline_post -d "name=$NAME&email=$MAIL&content=$CONTENT"

#test the 'DELETE' API
echo "This is the 'POST' API test"
echo "Enter the id of the post to delete: "
read ID
curl --request DELETE http://localhost:5000/api/timeline_post -d "id=${ID}"