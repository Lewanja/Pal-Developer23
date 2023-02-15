### PREREQUISITES
1. Docker
2. Docker compose

### HOW TO RUN
1. Clone the repo `git clone .....`
2. Cd into the directory
3. Run `docker compose up --build`. You can run without the `-d` to view the logs from the server and clients combined but this will be a bit mixed up.Preferrably run with the `-d` flag then follow instructions in watching output below.
4. Observe the terminal output


#### Client exited and ranks re-ordered
1. Gracefully stop a container. First get the container id by running `docker ps` and stop it by running `docker stop {container_id}`
2. Observe the output

#### Client joined and ranks re ordered
*** provide run commands to add a docker container within the network

### Watching output
Run `docker ps` and get the ids of the containers
In separate terminals run `docker logs -f {container id}`
let the logs stream

![Assigning Ranks](images/Assign%20rank%20request.JPG)

![Send Command](images/Send%20command.JPG)

![Unassigning Ranks](images/Unassign%20rank%20request.JPG)


### HOW IT WORKS
![Flow of system](images/Distributed%20system%20diagram.jpg)

#### RANKS
The ranks are stored in cache by the server. Clients do not hold any information about ranks by themselves. The data structure used is a JSON list of strings made of ip and port of the client.

To assign a rank an entry is added at the end of the cache. However before adding we check if the ip port is in the list and if present do not take any action.

To unassign a rank the entry is deleted. The indexes are then re ordered. In this case python programming language is used so this is done by the interpreter automatically.

#### SERVER
The server is a single docker container which exposes the following endpoints:
1. Get rank endpoint. This is used by the clients to request for a rank. When called the client is assigned a rank and the new rankings printed to console.
2. Send command endpoint. Clients send commands to this endpoint which will then be sent to other clients of lower rank. The server will print to console the number of clients the command will be sent to. The clients will print to console when they receive the command from the server.
3. Unassign rank endpoint. Clients call this server endpoint when they are about to exit. The server will update the ranking and then print the new ones to console.


#### CLIENT
The client are multiple docker containers resuing the same imgae(same code) but with different environment variables for PORT to simulate different clients.
They each exposes one endpoint, the `receive-command` endpoint. The server uses this endpoint to send commands to the individual client.

Clients also have the following functionality, in the form of http calls to the server:
1. Request rank. This call is made only once during startup. When a rank is received the client will print to console but does not hold it in its state.
2. Un-assign rank. This call is made when the app is exiting gracefully.
3. Send command. This gets a random command (list defined in `file client.py line 23`) and sends it to the server to be forwarded to other clients. This is done at random intervals (minimum and maximum defined in `file client.py line 29&30`). This is done in a separate thread so as not the block the main thread used by flask to server the endpoints. 


#### NETWORKING
The application is run using Docker containers. These containers are then communicate with each other using a docker network. 
This allows us to have a simple method to have applications isolated and each given its own ip address

The server container is assigned it hostname `http://server` by the docker compose network . [Reference here](https://docs.docker.com/compose/networking/). 
This allows us to be able to call it from the client containers without knowing its IP beforehand. 
This value is stored in an environment variable to allow the application to be as flexible as possible.

### LIMITATIONS
1. Clients only notify the server of exit when the container is stopped gracefully i.e. using `docker stop {container id}`

### POSSIBLE IMPROVEMENTS
1. Use better caching mechanism. Currently used is in memory cache. ideal would be such as Redis or Memcache.
2. Provide Graphical UI
3. Make the process of replication more intuitive.