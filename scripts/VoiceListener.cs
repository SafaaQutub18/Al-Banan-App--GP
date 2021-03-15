using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using UnityEngine.UI;
using System.Threading;
using System;


public class VoiceListener : MonoBehaviour{

    public Sprite enableListen;
    public Sprite disableListen;
    public Button button;
    Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;
    

    // varible to control the activation 
    string running = "false";

    //function activated by the user to start or stop the translation
    public void startStopListening()
    {
        //check if the translation is activated to stop it.
        if(running.Equals("true")) {
        running = "false";
        listener.Stop();
        Debug.Log("Stop listener");
        button.image.sprite = disableListen;
       // VideoCaptureCtrl.Instance.StopCapture();
        } 
        // if the translation is not activated, start it
        else {
        //VideoCaptureCtrl.Instance.StartCapture();
        button.image.sprite = enableListen;
        ThreadStart ts = new ThreadStart(GetInfo);
        mThread = new Thread(ts);
        mThread.Start();
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
        
        // initialize avatar object 
        Avatar avatar = new Avatar();

        if (dataReceived != null){
        string[] signs_id_list = dataReceived.Split(','); // split the id by comma 
        // looping throug the signs_id_list
        foreach(string sign_id in signs_id_list){
            if(!sign_id.Equals(" ")) // to prevent sign id from concatenation
            
            // convert the id from string to integer
             avatar.setSignId(Int32.Parse(sign_id));
             
        }
            
        }

    }

    }
