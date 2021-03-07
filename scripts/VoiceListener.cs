using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using System.Threading;
using System;
public class VoiceListener : MonoBehaviour{

 Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;
    string running = "false";


    public void startStopListening()
    {
        if (running.Equals("true")) {
        running = "false";
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

    void GetInfo(){
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(IPAddress.Any, connectionPort);
        listener.Start();
        Debug.Log("Start listener");
        client = listener.AcceptTcpClient();
        running = "true";
        while (running.Equals("true")){
            SendAndReceiveData();
        }
    }

    void SendAndReceiveData(){ 
        NetworkStream nwStream = client.GetStream();
        //---receiving Data from the Host----
        byte[] buffer = new byte[client.ReceiveBufferSize];
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string
        Avatar avatar = new Avatar();

        if (dataReceived != null){
           //---Using received data---
        int x = 0;   
        string[] signs_id_list = dataReceived.Split(',');

        foreach(string sign_id in signs_id_list){
            if(!sign_id.Equals(" "))
             avatar.setSignId(Int32.Parse(sign_id));
             print("Fast"+sign_id);
        }
            
        }

    }

    }
