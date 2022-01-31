# SERAPIS_U33_T4_D5D6_IRA
 
To run the service locally run command:

docker-compose up

## Run the tool

The service can be called from code via calls to the url:

http://127.0.0.1:3000/move

with a POST method, the data of which is the message (question/answer) expressed in the amulet
format. This returns json data that includes the responding locutions (if there are any) from DaaS.
