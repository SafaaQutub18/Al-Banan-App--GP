using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using System.Threading;

public class listenVideoVoice : MonoBehaviour
{
 Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;
    string running = "false";

    public void Open()
    {
        if (running.Equals("true")) {
        running = "false";
        SendAndReceiveData();
        listener.Stop();
        Debug.Log("Stop listener");
        
        
        
        } 
        else {
        ThreadStart ts = new ThreadStart(GetInfo);
        mThread = new Thread(ts);
        mThread.Start();
        Debug.Log("Start thread");
        } 
    }

    void GetInfo()
    {
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(IPAddress.Any, connectionPort);
        listener.Start();
        Debug.Log("Start listener");

        client = listener.AcceptTcpClient();

        running = "true";
        while (running.Equals("true"))
        {
            SendAndReceiveData();
        }
    }

    void SendAndReceiveData()
    {
        
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];
        //print("tototototototototototototototototo");
        byte[] myWriteBuffer = Encoding.ASCII.GetBytes(running); //Converting string to byte data
            nwStream.Write(myWriteBuffer, 0, myWriteBuffer.Length); //Sending the data in Bytes to Python

        //---receiving Data from the Host----
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string
        
        if (dataReceived != null)
        { 
           //---Using received data---
            print(dataReceived);
           // print("helloooooooooooooooooo");
        }

    }
    }
