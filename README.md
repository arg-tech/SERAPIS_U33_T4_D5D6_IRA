# SERAPIS_U33_T4_D5D6_IRA
 
To run the service locally run command:

docker-compose up

## Run the tool

The service can also be called from code via calls to the url:

http://127.0.0.1:3000/move

with a post method, the data of which is the message (question/answer) expressed in the amulet
format and returns json data that includes the responding locutions (if there are any) from daas.
