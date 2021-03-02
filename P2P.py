from socket import *
import _thread

<<<<<<< HEAD
nodePort = "17000"
=======
nodePort = "16001"
>>>>>>> b62b0fac3f5dab9465f1249e9efbfec96322a5e8

latestSender = ""

ports = {
    "17000":["149.130.230.118","17000",["15001","16000"],{}],
    "17001":["149.130.230.118","17001",["16000","16001"],{}],
    "16000":["149.130.227.40","16000",["17000","17001","15000"],{}],
    "16001":["149.130.227.40","16001",["17001", "15001"],{}],
    "15000":["149.130.185.217","15000",["16000","16001"],{}],
    "15001":["149.130.185.217","15001",["17000"],{}]
}

dataWithPorts = {
    "17000":["cat.txt","dog.txt","turtle.txt"],
    "17001":["penguin.txt","squid.txt","dog.txt"],
    "16000":["dolpin.txt","cat.txt","bird.txt"],
    "16001":["tortiose.txt","penguin.txt","dolpin.txt"],
    "15000":["tiger.txt","lion.txt","squid.txt"],
    "15001":["fish.txt","shark.txt","turtle.txt"]
}


#TODO: how to loop through edges and create connections while still being able to reference sockets later
def threadNeighbor():
    #Set up TCP connections with all neighbors
    myEdges = ports[nodePort][2]
    print("at the start of threadNeighbor")
    for e in myEdges:
        print("in the forloop")
        edge = ports[e]
        serverName = edge[0]
        serverPort = int(edge[1])
<<<<<<< HEAD
        print("serverPort")
=======
>>>>>>> b62b0fac3f5dab9465f1249e9efbfec96322a5e8
        clientSocket = socket(AF_INET,SOCK_STREAM)
        print(serverPort)
        clientSocket.connect((serverName,serverPort))
        print(serverPort)
        ports[nodePort][3][serverPort] = clientSocket

    print("out of the forloop")
<<<<<<< HEAD

=======
    #add the start of a for loop here?
>>>>>>> b62b0fac3f5dab9465f1249e9efbfec96322a5e8
    request = input("Please type the name of the file you are requesting.\n>")

    if request in dataWithPorts[nodePort]:
         #if you already have requested file
  	     print("You already have " + request)
    else:
        self = ports[nodePort]
        for neighbor in self[2]:
            neighborInfo = ports[neighbor]
            query = "Query " + self[0] + ":" + self[1] + " " + self[0] + ":"
<<<<<<< HEAD
            +str(self[1]) + " " +  str(neighborInfo[0]) + ":"
=======
            +self[1] + " " +  neighborInfo[0] + ":"
>>>>>>> b62b0fac3f5dab9465f1249e9efbfec96322a5e8
            + neighborInfo[1] + " " + request + " 4"
            self[3][neighborInfo[1]].send(query)

def listen(s):
    print("at the listen function")
    while True:
        print("I am listening")
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        # print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(receivedMessage(c), ())
    s.close()

def receivedMessage(c):
    message = c.recvfrom(nodePort)
    messageInfo = message.split()

    type = messageInfo[0]

    origSenderInfo = messageInfo[1].split(":")
    origSenderIP = origSenderInfo[0]
    origSenderPort = origSenderInfo[1]

    senderInfo = messageInfo[2].split(":")
    senderIP = senderInfo[0]
    senderPort = senderInfo[1]

    receiverInfo = messageInfo[3].split(":")
    receiverIP = receiverInfo[0]
    receiverInfo = receiverInfo[1]

    requesting = messageInfo[4]

    ttl = messageInfo[5]
    newttl = 4 - int(ttl)
    self = ports[nodePort]

    if type == "Query":
        latestSender = senderPort
        response = "Response " + origSenderInfo + " "+ receiverInfo
        + " " + senderInfo + " " + requesting + " "
        + newttl + " " + message

        if message in dataWithPorts[nodePort].values():
            response += "Found item"
            ports[nodePort][3][latestSender].send(response)
        elif message not in dataWithPorts[nodePort].values() and ttl>0:
            #SEND TO EVERYONE BUT WHO SENT IT TO YOU
            for neighbor in self[2]:
                neighborInfo = ports[neighbor]
                if neighborInfo[0] == senderIP:
                    skip
                else:
                    query = "Query " + origSenderInfo + " " + self[0]
                    + ":" + self[1] + " " +  neighborInfo[0]
                    + ":" + neighborInfo[1] + " " + request

                    self[3][neighbor].send(query)
        		#SEND QUERY
    elif type == "Response":
        destinationIP = origSenderIP
        destinationPort = origSenderPort
        responseData = messageInfo[6]

        if nodePort == destinationPort:
            dataWithPorts[nodePort].append(responseData)
            print("Message Received: "+ message)
        else:
            if ttl > 0:
                #recreate response datagram with new ttl/sender/receiver and forward
                response = "Response " + origSenderInfo + " "+ receiverInfo
                + " " + senderInfo + " " + requesting + " "
                + newttl + " " + message

                ports[nodePort][3][latestSender].send(response)




def Main():
    serverPort = int(nodePort)
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print("Ready to receive")

    input("Are you ready? Please type \'go\' when ready... ")
<<<<<<< HEAD
    _thread.start_new_thread(threadNeighbor(), ())
    _thread.start_new_thread(listen(serverSocket), ())

    print("after start new thread for listen")

=======

    _thread.start_new_thread(threadNeighbor(), ())
    print("after start new thread for listen")
    _thread.start_new_thread(listen(serverSocket), ())
>>>>>>> b62b0fac3f5dab9465f1249e9efbfec96322a5e8



if __name__ == "__main__":
    Main()
